resource "digitalocean_droplet" "app_vm" {
  count = var.app_instance_vm_count
  name = "app-vm"
  image = var.do_image
  region = "nyc3"
  size = "s-1vcpu-1gb"
  ssh_keys = [ var.authorized_key ]
#  root_pass = var.root_user_pw
  tags = ["app", "app-node"]
}


resource "local_file" "ansible_inventory" {
  content = templatefile("${local.templates_dir}/ansible-inventory.tpl", {
    webapps = [for host in digitalocean_droplet.app_vm.*: "${host.ipv4_address}"]
  })
  filename = "${local.ansible_dir}/inventory.ini"
}