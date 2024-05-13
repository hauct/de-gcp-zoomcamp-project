provider "google" {
    project = var.project_id
    credentials = file("../cred/credential.json")
    region = var.region
    zone = var.zone  
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}

data "google_client_openid_userinfo" "me" {}

resource "google_compute_instance" "fred-productionapi" {
  boot_disk {
    auto_delete = true
    device_name = "fred-productionapi"

    initialize_params {
      image = "projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230302"
      size  = 30
      type  = "pd-balanced"
    }
    mode = "READ_WRITE"
  }

  zone = var.zone  
  machine_type = "e2-standard-2"
  name = "fred-productionapi"
  tags = [ "ssh" ]

  allow_stopping_for_update = true
  network_interface {
    network = google_compute_network.vpc_network.name
    access_config {
    }
    }
  service_account {
    email  = data.google_client_openid_userinfo.me.email
    scopes = ["cloud-platform"]
  }

 
  metadata = {
    ssh-keys = "${var.email}:${tls_private_key.ssh.public_key_openssh}"
  }
}

resource "google_compute_firewall" "ssh-rule" {
  name = "sshrule"
  network = google_compute_network.vpc_network.name
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
  target_tags = ["ssh"]
  source_ranges = ["0.0.0.0/0"]
}