terraform {
  required_providers {
    tls = {
      source  = "hashicorp/tls"
      version = "4.0.4"
    }
  }
}

provider "tls" {}

resource "tls_private_key" "ssh" {
  algorithm = "RSA"
  rsa_bits  = 4096
}
resource "local_file" "ssh_private_key_pem" {
  content         = tls_private_key.ssh.private_key_openssh
  filename        = "../.ssh/fredkey"
}