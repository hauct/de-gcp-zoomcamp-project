from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation
import argparse
@flow(name='DBT ingest')
def main(arg) :
    target = arg.target
    result = DbtCoreOperation(
        commands=[f"dbt seed --target {target}"],
        project_dir="DBT",
        profiles_dir="."
    ).run()
    return result

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Script to ingest seed data.')
    parser.add_argument('--target',required=True,help='Target database to deploy start ingest',default='dev')
    args = parser.parse_args()
    main(args)