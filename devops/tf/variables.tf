variable "do_pa_token" {
  sensitive = true
}

variable "authorized_key" {
  sensitive = true
}

#variable "root_user_pw" {
#  sensitive = true
#}

variable "app_instance_vm_count" {
  default=0
}

variable "do_image" {
  sensitive = true
}