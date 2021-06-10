# configure the docker provider
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.12.2"
    }
  }
}

provider "docker" {}

#image to be used by container.
resource "docker_image" "terraform-centos" {
  name         = "centos:7"
  keep_locally = true
}

resource "docker_container" "centos" {
  image   = docker_image.terraform-centos.latest
  name    = "terraform-centos"
  start   = true
  command = ["/bin/sleep", "500"]
}

