import requests
import bs4
import pandas as pd
import datetime
import os 
from prefect.deployments import Deployment
from prefect import flow,task
from google.cloud import storage
from dotenv import load_dotenv
from prefect.server.schemas.schedules import CronSchedule

basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env'))
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("Google_Cred_path")

@task(name='Get Web Content Category',log_prints=True)
def get_web_data():
    page = requests.get('https://fred.stlouisfed.org/categories/')
    beatiful = bs4.BeautifulSoup(page.content, 'html.parser')
    category_page =beatiful.find_all("div",{"class":"fred-categories-group"})        
    return category_page

@task(name='Get sub page Category',log_prints=True)
def get_subpage(id):        
    sub_url =f'https://fred.stlouisfed.org/categories/{id}'
    subpage =requests.get(sub_url)
    beatiful = bs4.BeautifulSoup(subpage.content, 'html.parser')
    category_page_col =beatiful.find_all("div",{"class":"col-12 panel-menu"})
    category_page_subcol =beatiful.find_all("div",{"class":"col-12 subcats"})  
    return category_page_col,category_page_subcol

@flow(name='test_flow')
def main():
    # category_page = get_web_data()
    # category = []
    # for i in category_page:
    #     line_ref = i.find("a")
    #     pa_name = line_ref.text # Money, Banking, & Finance 
    #     pa_id = line_ref['href'][line_ref['href'].rfind('/')+1:] # 32991
    #     category.append((pa_name,pa_id,None,None)) # [('Money, Banking, & Finance', '32991', None, None)]
    #     for a in i:
    #         for o in a:
    #             _temp = o.find('a')
    #             if _temp != -1 and _temp !=None:
    #                 name= _temp.text # Interest Rates
    #                 id  =_temp['href'][_temp['href'].rfind('/')+1:] # 22
    #                 category.append((name,id,pa_name,pa_id))

    # print(category)
    category_page_col, category_page_subcol = get_subpage(32991)
    print(category_page_col)
    # print(category_page_subcol)

if __name__ == '__main__':
    main() 