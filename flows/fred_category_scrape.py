import requests
import bs4
import pandas as pd
import datetime
import os 
from prefect.deployments import Deployment
from prefect import flow,task
from google.cloud import storage
from dotenv import load_dotenv
from prefect.orion.schemas.schedules import CronSchedule

basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env.config'))
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("Google_Cred_path")

@task(name='Get Web Content Category',log_prints=True)
def get_web_data():
    page =requests.get('https://fred.stlouisfed.org/categories/')
    beatiful = bs4.BeautifulSoup(page.content, 'html.parser')
    category_page =beatiful.find_all("div",{"class":"fred-categories-group"})        
    return category_page

@task(name='Move_archive_Category',log_prints=True)
def move_archive(bucket,typecheck):
    file_acrhive=  list(bucket.list_blobs())
    for file in file_acrhive:
        name = file.name
        pos = name.find('/')
        type = name[:pos]
        if type == 'staging':
            sub_pos = name.find('/',pos+1)
            sub_type = name[pos+1:sub_pos]
            if sub_type == typecheck:
                bucket.copy_blob(file,destination_bucket=bucket,new_name=name.replace('staging','archive'))
                bucket.delete_blob(name)    
    return True
@task(name='Get sub page Category',log_prints=True)
def get_subpage(id):        
    sub_url =f'https://fred.stlouisfed.org/categories/{id}'
    subpage =requests.get(sub_url)
    beatiful = bs4.BeautifulSoup(subpage.content, 'html.parser')
    category_page_col =beatiful.find_all("div",{"class":"col-12 panel-menu"})
    category_page_subcol =beatiful.find_all("div",{"class":"col-12 subcats"})  
    return category_page_col,category_page_subcol

@flow(name='Function Call Category',log_prints=True)
def main():
    category_page = get_web_data()
    category = []
    for i in category_page:    
        line_ref = i.find("a")
        pa_id = line_ref['href'][line_ref['href'].rfind('/')+1:]
        pa_name = line_ref.text
        category.append((pa_name,pa_id,None,None))
        for a in i:
            for o in a:
                _temp = o.find('a')
                if _temp != -1 and _temp !=None:
                    name= _temp.text
                    id  =_temp['href'][_temp['href'].rfind('/')+1:]
                    category.append((name,id,pa_name,pa_id))
                    category_page_col,category_page_subcol = get_subpage(id)                                      
                    if category_page_subcol:
                        for i in category_page_subcol:
                            sub_page = i.find_all('a',href=True)
                            for item in sub_page:
                                subname = item.text
                                subid   = item['href'][item['href'].rfind('/')+1:]
                                category.append((subname,subid,name,id)) 
                    elif category_page_col:
                        for i in category_page_col:
                            sub_page = i.find_all('a',href=True)
                            for item in sub_page:
                                subname = item.text
                                subid   = item['href'][item['href'].rfind('/')+1:]
                                category.append((subname,subid,name,id)) 
                    
    df_category = pd.DataFrame(category,columns=['name','id','parent_name','parent_id'])
    df_category[['name','parent_name']] = df_category[['name','parent_name']].astype('string')
    df_category[['id','parent_id']] = df_category[['id','parent_id']].fillna(0).astype('int')

    client = storage.Client()

    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
    bucket = client.get_bucket(os.getenv("Gcs_Bucket_name"))

    print('Moving file to archive folder')
    move_archive(bucket,'series')

    uppload_path =f'stagging/category/CategoryData_{time_stamp}.parquet'
    print(f'Uploading file to cloud.')
    bucket.blob(uppload_path).upload_from_string(df_category.to_parquet(), 'text/parquet')
    return True

def deploy():
    deployment = Deployment.build_from_flow(
        flow=main,
        name="Fred-Category",
        schedule=(CronSchedule(cron="0 5 5 * *"))
    )
    deployment.apply()

if __name__ =='__main__':
    deploy()