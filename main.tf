provider "aws" {
  region     = "us-west-2"
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  cpu_core_count = 1
  cpu_threads_per_core = 1
  hibernation = true

  tags = {
    Name = "HelloNetology"
  }
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}