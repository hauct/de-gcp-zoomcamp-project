from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation
from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import CronSchedule
import argparse

@flow(name='DBT function prod')
def dbt_runjob_prod() :
    result = DbtCoreOperation(
        commands=[f"dbt seed --target prod",f"dbt run --target prod"],
        project_dir="DBT",
        profiles_dir="."
    ).run()
    return result

@flow(name='DBT function dev')
def dbt_runjob_dev():
    result = DbtCoreOperation(
        commands=[f"dbt seed --target dev",f"dbt run --target dev"],
        project_dir="DBT",
        profiles_dir="."
    ).run()
    return result

def deploy(params):
    target = params.target
    schedule=  params.schedule
    if target =='prod':
        flow_torun = dbt_runjob_prod
    elif target =='dev':
        flow_torun = dbt_runjob_dev
    else:
        print('Pass in wrong paramter. Accept para prod,dev')
        return None
    if schedule =='y':
        deployment = Deployment.build_from_flow(
            flow=flow_torun,
            name=f"DBT-transform-{target}",
            schedule=(CronSchedule(cron="0 7 5 * *"))
        )
    else:
        deployment = Deployment.build_from_flow(
            flow=flow_torun,
            name=f"DBT-transform-{target}"
        )
    deployment.apply()
    return None

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Script to setup dbt deployment.')
    parser.add_argument('--target',required=True,help='Target database to deploy from DBT',default='dev')
    parser.add_argument('--schedule',required=True,help='Deploy with schedule or not',default='n')
    args = parser.parse_args()
    deploy(args)