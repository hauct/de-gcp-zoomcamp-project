terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

module "google_cloud_storage_bucket" {
  source  = "./modules/google-cloud-storage-bucket"
  project = var.project
  region  = var.region
}

module "google_cloud_dataproc_instance" {
  source                     = "./modules/google-cloud-dataproc-instance"
  pyspark_repo_bucket_name = module.google_cloud_storage_bucket.pyspark_repo_bucket_name
}