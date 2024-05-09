
# Create Cloud Storage Bucket for Data WareHouse
resource "google_storage_bucket" "data_warehouse_bucket" {
  name     = "hauct_${var.project}_data-warehouse"
  location = var.region

  public_access_prevention = "enforced"
}

# Create bucket to store source code for Dataproc
resource "google_storage_bucket" "pyspark_repo_bucket" {
  name     = "hauct_${var.project}_dataproc-source"
  location = var.region
  public_access_prevention = "enforced"
}