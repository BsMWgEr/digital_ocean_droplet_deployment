terraform {
    required_version = ">= 0.15"
    required_providers {
#        linode = {
#            source = "linode/linode"
#            version = "1.22.0"
#        }
        digitalocean = {
          source = "digitalocean/digitalocean"
          version = "~> 2.0"
        }
    }
    backend "s3" {
        skip_credentials_validation = true
        skip_region_validation = true
    }
}

provider "digitalocean" {
    token = var.do_pa_token
}