terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "5.57.0" #not dependent on the main version module,so one can specify the one needed
    }
  }
}

# resource "aws_instance" "server_1"{

# }

resource "aws_instance" "this_server" {
  ami                     = "ami-0249211c9916306f8"
  instance_type           = var.instance_size
  #host_resource_group_arn = "arn:aws:resource-groups:us-west-2:012345678901:group/win-testhost"
  #tenancy                 = "host"
  monitoring = false
  vpc_security_group_ids = var.security_group_ids
  subnet_id = var.subnet_id

  root_block_device {
    delete_on_termination = false
    encrypted = true
    volume_size = 20
    volume_type = "standard"

  }
  tags = {
    name="${var.server_name}-production"

  }
}