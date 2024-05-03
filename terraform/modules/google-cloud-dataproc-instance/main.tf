# Upload pyspark file to run pyspark Job
resource "google_storage_bucket_object" "pyspark_repo_archive" {
  name   = "process_gh_archive_dataproc.py"
  bucket = var.pyspark_repo_bucket_name
  source = "../dataproc/process_gh_archive_dataproc.py"
}

# Create DataProc Cluster
resource "google_dataproc_cluster" "pyspark_cluster" {
  name   = "pyspark-cluster"
  region = var.region
  graceful_decommission_timeout = "120s"
  labels = {
    foo = "bar"
  }

    cluster_config {
    staging_bucket = var.pyspark_repo_bucket_name

    master_config {
      num_instances = 1
      machine_type  = var.machine_type
      disk_config {
        boot_disk_type    = "pd-ssd"
        boot_disk_size_gb = var.boot_disk_size_gb
      }
    }
      worker_config {
      num_instances    = 2
      machine_type     = var.machine_type
      min_cpu_platform = "Intel Cascade Lake"
      disk_config {
        boot_disk_size_gb = var.boot_disk_size_gb
        num_local_ssds    = 1
      }
    }
      software_config {
      image_version = var.image_version
      override_properties = {
        "dataproc:dataproc.allow.zero.workers" = "true"
      }
    }
  }
}