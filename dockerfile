FROM  prefecthq/prefect:2.8.7-python3.11

COPY ./requirements.txt .

ARG Prefect_API_KEY
ARG Prefect_Workspace

RUN pip install -r  requirements.txt
RUN prefect cloud login --key $Prefect_API_KEY --workspace $Prefect_Workspace