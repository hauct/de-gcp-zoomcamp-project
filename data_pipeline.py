import pandas as pd
from google.cloud import storage
import os

path_to_private_key = 'D:\de-gcp-zoomcamp-project\credentials\de-data-422410-3863bd49070c.json'


# Define constants
PROJECT_ID = "de-data-422410"
GCS_BUCKET = "hauct_nyc_project"


def fetch(dataset_url: str) -> str:
    # Download the file using wget
    os.system(f"wget {dataset_url}")
    return dataset_url.split("/")[-1]

def clean(file_path: str) -> pd.DataFrame:
    """
    Cleans the DataFrame by setting correct data types for each column.
    """
    # Extract date value from file path
    raw_date_value = file_path.split("_")[-1].split(".")[0]

    # Read CSV file
    df = pd.read_csv(file_path)

    # Rename columns
    df = df.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'rate_code_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    })

    # Convert data types
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['passenger_count'] = df['passenger_count'].astype(str)
    df['trip_distance'] = df['trip_distance'].astype(float)
    df['rate_code_id'] = df['rate_code_id'].astype(str)
    df['pu_location_id'] = df['pu_location_id'].astype(str)
    df['do_location_id'] = df['do_location_id'].astype(str)
    df['payment_type'] = df['payment_type'].astype(str)
    df['fare_amount'] = df['fare_amount'].astype(float)
    df['extra'] = df['extra'].astype(float)
    df['mta_tax'] = df['mta_tax'].astype(float)
    df['tip_amount'] = df['tip_amount'].astype(float)
    df['tolls_amount'] = df['tolls_amount'].astype(float)
    df['improvement_surcharge'] = df['improvement_surcharge'].astype(float)
    df['total_amount'] = df['total_amount'].astype(float)
    df['congestion_surcharge'] = df['congestion_surcharge'].astype(float)

    # Add new column
    df['raw_month'] = raw_date_value

    return df

def write_local(df: pd.DataFrame, dataset_file: str):
    """
    Writes the DataFrame locally as a gzip-compressed parquet file.
    
    Args:
    - df: DataFrame to be written to disk.
    - year: Year of the dataset.
    - dataset_file: Name of the dataset.
    
    Returns:
    - Path where the file was saved.
    """
    file_name = f"{dataset_file}.parquet"
    df.to_parquet(file_name, compression='gzip')
    return file_name

def write_to_gcs(path_to_private_key, file_name, dest_file) -> None:
    """
    Writes a DataFrame to a Google Cloud Storage (GCS) bucket.
    """
    client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)
    
    bucket = client.bucket('hauct_nyc_project')
    # The name assigned to the CSV file on GCS
    blob = bucket.blob(dest_file)

    blob.upload_from_filename(file_name)

def remove_file(local_path):
    """
    Removes a local file.
    
    Args:
    - local_path: Path of the file to be removed.
    """
    if os.path.isfile(local_path):
        os.remove(local_path)
    else:
        print(f"Error: {local_path} file not found")


def etl_web_to_gcs(year: int, month: int) -> None:
    """
    Main ETL function that orchestrates the entire data processing pipeline, from fetching the data
    to writing it to GCS and BigQuery.
    """
    dataset_file = f"yellow_tripdata_{year}-{month:02}"

    # Construct the dataset URL and fetch the data
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/{dataset_file}.csv.gz"
    file_path = fetch(dataset_url)

    # Clean the data
    df = clean(file_path)
    
    file_name = write_local(df, dataset_file)
    
    # Write the cleaned data to GCS and BigQuery
    write_to_gcs(path_to_private_key, file_name, file_name)

    remove_file(file_name)
    
if __name__ == '__main__':
    # Define the years and months for which to run the ETL
    years = [2019, 2020, 2021]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Run the ETL for the defined years and months
    for year in years:
        if year == 2021:
            months = [1, 2, 3, 4, 5, 6, 7]
        for month in months:
            etl_web_to_gcs(year, month)
