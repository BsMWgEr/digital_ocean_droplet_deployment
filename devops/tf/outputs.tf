
output "instances" {
  value = [for host in digitalocean_droplet.app_vm.*: "${host.name}: ${host.ipv4_address}"]
}