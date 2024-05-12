import os
from dotenv import load_dotenv

basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env'))


def main():
    replace_list = ["Gcp_Project_id","Gcp_Zone","Gcp_Region","Account_id","Email","Gcs_Bucket_name"]
    with open('profiles.yml','r') as e:
        content = e.read()
        content = content.replace("${Gcp_Project_id}",os.getenv("Gcp_Project_id"))
    with open('profiles.yml','w') as e:
        e.write(content)

    with open('DBT/models/stagging/schema.yml','r') as e:
        content = e.read()
        content = content.replace("${Gcp_Project_id}",os.getenv("Gcp_Project_id"))
    with open('DBT/models/stagging/schema.yml','w') as e:
        e.write(content)


    with open('infra/terraform.tfvars','r') as f:
        con = f.read()

    for i in replace_list:
        con= con.replace(i,os.getenv(i))

    with open('infra/terraform.tfvars','w') as f:
        f.write(con)
if __name__ == "__main__":
    main()