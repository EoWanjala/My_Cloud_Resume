terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.58.0"
    }
  }
}

provider "aws" {
  # Configuration options
}

resource "aws_vpc" "production" {
    cidr_block ="10.0.0.1/16"

}

resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.production
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-north-1"

  tags = {
    Name = "public_subnet"
  }


}

module "webserver" {
  source = "terraform_modules/My_Modules/ec2"
  server_name = "production_webserver"
  instance_size = "t2.micro"
  subnet_id = aws_subnet.public_subnet.id
  security_group_ids = [aws_vpc.production.vpc_security_group_ids]
  
}