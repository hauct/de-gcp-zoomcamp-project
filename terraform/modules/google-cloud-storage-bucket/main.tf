
# Create Cloud Storage Bucket for Data WareHouse
resource "google_storage_bucket" "data_warehouse_bucket" {
  name     = "${var.project}_data-warehouse"
  location = var.region

  public_access_prevention = "enforced"
}

# Create bucket to store source code for Cloud Function
resource "google_storage_bucket" "cloud_function_bucket" {
  name     = "${var.project}_${var.region}_gcf-source"
  location = var.region

  public_access_prevention = "enforced"
}

# Create bucket to store source code for Dataproc
resource "google_storage_bucket" "pyspark_repo_bucket" {
  name     = "${var.project}_dataproc-source"
  location = var.region
  public_access_prevention = "enforced"
}