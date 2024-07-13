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