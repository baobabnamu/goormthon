# main.tf
resource "aws_vpc" "goorm_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "Goorm-VPC"
  }
}

resource "aws_subnet" "public_subnet" {
  vpc_id            = aws_vpc.goorm_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "ap-northeast-2a"
  tags = {
    Name = "Goorm-PublicSubnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.goorm_vpc.id
  tags = {
    Name = "Goorm-IGW"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.goorm_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "Goorm-PublicRouteTable"
  }
}

resource "aws_route_table_association" "public_rt_association" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_security_group" "goorm_sg" {
  name        = "Goorm-SG"
  description = "Allow SSH and HTTP"
  vpc_id      = aws_vpc.goorm_vpc.id

  ingress { # SSH
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress { # HTTP
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress { # Django Apps
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress { # Jenkins
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Goorm-SG"
  }
}

# Generate private key
resource "tls_private_key" "goorm_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

# Create AWS key pair using the generated public key
resource "aws_key_pair" "goorm_key" {
  key_name   = "goorm-key"
  public_key = tls_private_key.goorm_key.public_key_openssh
}

resource "aws_instance" "goorm_ec2" {
  ami           = "ami-0c9c942bd7bf113a2"  # Ubuntu 22.04 LTS
  instance_type = "t2.micro"
  key_name      = aws_key_pair.goorm_key.key_name
  subnet_id     = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.goorm_sg.id]

  tags = {
    Name = "Goorm-EC2"
  }
}

resource "aws_eip" "goorm_eip" {
  instance = aws_instance.goorm_ec2.id
}

output "public_ip" {
  value = aws_instance.goorm_ec2.public_ip
}

output "eip" {
  value = aws_eip.goorm_eip.public_ip
}
