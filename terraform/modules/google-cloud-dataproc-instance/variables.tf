
variable pyspark_repo_bucket_name { }

variable "region" {
  default = "asia-southeast1"
}

variable "machine_type" {
  default = "n2-standard-2"
}

variable "boot_disk_size_gb" {
  default = 32
}

variable "image_version" {
  default = "2.2-ubuntu22"
}