include .env.config

update-yml-window:
	python flows/update_yml.py

update-yml-linix:
	python3 flows/update_yml.py

infra-setup:
	terraform -chdir=./infra init
	terraform -chdir=./infra plan

infra-create:
	terraform -chdir=./infra apply -auto-approve

infra-down:
	terraform -chdir=./infra destroy -auto-approve

vm-connect:
	ssh -i .ssh/fredkey ${Email}@${vm_Externalip}

vm-setup:
	sudo apt install docker.io -y
	sudo chmod 666 /var/run/docker.sock
	sleep 1

vm-setupdocker:
	sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
	docker-compose --version

vm-copycred:
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" .env.config ${Email}@${vm_Externalip}:"./de-gcp-zoomcamp-project/"
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" cred/credential.json ${Email}@${vm_Externalip}:"./de-gcp-zoomcamp-project/cred/"

docker-build:
	docker build --build-arg Prefect_Workspace=${Prefect_Workspace} --build-arg Prefect_API_KEY=${Prefect_API_KEY} -f dockerfile -t python_prefect_dbt .

docker-up:
	docker-compose --profile agent up --detach

deployment-create:
	docker-compose run job flows/fred_series.py
	docker-compose run job flows/fred_map_api.py
	docker-compose run job flows/fred_category_scrape.py

deployment-dbtprod:
	docker-compose run job flows/dbt_job.py --target prod --schedule y
