import API_helper.url_module as hp
import pandas_gbq as pd
import datetime
import time
import os
from prefect import flow,task
from google.cloud import storage
from config import query_bq,clean_df
from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import CronSchedule
from dotenv import load_dotenv

basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env.config'))

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("Google_Cred_path")

@task(name='Get_BQ_SQL_Series',log_prints=True)
def get_bq_data(query):     
    df_bq = pd.read_gbq(query=query,
    project_id=os.getenv("Gcp_Project_id")

    )
    return df_bq

@task(name='Get_API_Series',log_prints=True)
def get_series_id(id):
    offset = 0
    item = 1
    all_list = []
    while  offset<item:
        result = hp.category.series_category(category_id=id,limit=1000,offset=offset)

        if result is None:
            print('Result return with Noting skipping current call.')
            offset+= 1000

        elif result.ok:
            json = result.json()
            item =json['count']
            offset+= 1000
            all_list.extend(json['seriess'])
            
        else:
            print(f"Issue while calling API {result.status_code}")
            print(result.content)
            time.sleep(5)
    count_data = len(all_list)
    print(f'Done for ID {id} get total of {count_data}')
    time.sleep(1)
    return all_list,count_data

@task(name='Move_archive_Series',log_prints=True)
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

@task(name='Clean_data_Series',log_prints=True)
def clean_series_df(data,id):
    df = pd.json_normalize(data)
    df_col = clean_df.series_col
    str_col  = clean_df.series_str_col
    int_col  = clean_df.series_int_col
    date_col = clean_df.series_date_col
    df_net = df[df_col]
    df_net[str_col] = df_net[str_col].astype('string')
    df_net[int_col] = df_net[int_col].astype('int')
    df_net['last_updated'] = df_net['last_updated'].str[:10]
    for col in date_col:
        df_net[col] = pd.to_datetime(df_net[col])

    id_listarray = []
    for key,item in id.items():
        _templistid =[key] * item
        id_listarray = id_listarray + _templistid
    df_net['category_id'] = id_listarray

    df_net = df_net.drop_duplicates()
    return df_net

@flow(name='Function call Series',log_prints=True)
def main():
    # Get series id base on cat id
    client = storage.Client()
    bucket = client.get_bucket(os.getenv("Gcs_Bucket_name"))
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
    query = query_bq.query_getseriesPara
    result_query = get_bq_data(query)
    all_list = []
    id_data = {}
    print('Moving file to archive folder')
    move_archive(bucket,'series')
    for id in result_query.values.tolist():
        result_id,count_data = get_series_id(id[0])
        all_list.extend(result_id)
        id_data[id[0]] = count_data

    df_series = clean_series_df(all_list,id_data)
    uppload_path =f'stagging/series/{time_stamp}/SeriesData_{time_stamp}.parquet'
    print(f'Uploading file to cloud for {time_stamp} series data.')

    # Upload to bucket
    bucket.blob(uppload_path).upload_from_string(df_series.to_parquet(), 'text/parquet')
    return True

