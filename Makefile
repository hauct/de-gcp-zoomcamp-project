update-yml-window:
	python flows/Updateyml.py

update-yml-linix:
	python3 flows/Updateyml.py

infra-setup:
	terraform -chdir=./infra init
	terraform -chdir=./infra plan

infra-create:
	terraform -chdir=./infra apply -auto-approve

infra-down:
	terraform -chdir=./infra destroy -auto-approve

vm-connect:
	ssh -i .ssh/fredkey ${Email}@${vm_Externalip}

vm-copycred:
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" .env ${Email}@fred-productionapi:"./Final_Project_FredETE/"
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" cred/credential.json ${Email}@fred-productionapi:"./Final_Project_FredETE/cred/"

