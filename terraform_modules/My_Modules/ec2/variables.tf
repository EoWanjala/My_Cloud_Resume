variable "instance_size" {
    description = "instance size"
    type = string
    default = "t2.micro"
  
}

variable "server_name" {
    description = "instance name"
    type = string
  
}

variable "security_group_ids" {
    description = "ec2 sg ids"
    type = list(string)
  
}

variable "subnet_id" {
    description = "ec2 subnet id"
    type = string
  
}