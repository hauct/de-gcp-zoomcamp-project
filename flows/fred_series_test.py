import API_helper.url_module as hp
import pandas_gbq as pd
import datetime
import time
import os
from prefect import flow,task
from google.cloud import storage
from config import query_bq,clean_df
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from dotenv import load_dotenv

basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env'))

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("Google_Cred_path")

@task(name='Get_BQ_SQL_Series',log_prints=True)
def get_bq_data(query):     
    df_bq = pd.read_gbq(query=query,
    project_id=os.getenv("Gcp_Project_id")

    )
    return df_bq

query = query_bq.query_getseriesPara
print(query)
