# 실습 내용
- VPC 구성
  - Subnet 구성
    - Private, Public Subnet
    - Routing Table
      - Private Subnet : 0.0.0.0/0 - NAT GW 추가
      - Public Subnet : 0.0.0.0/0 - IGW 추가
  - Gateway 구성
    - NAT GW
    - IGW

- EC2 구성
  - Bastion Host (Public Subnet)
  - Client (Private Subnet)

- S3 구성
  - 정적 웹 사이트 구성 (test.html)