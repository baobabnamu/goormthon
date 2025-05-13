filePath="/Users/jaehwan/Desktop/goormthon/team-mission/cloud-computing-team-mission/cloudformation"

# 템플릿 유효성 검사
aws cloudformation validate-template --template-body file://$filePath/networking/VPC.yaml
aws cloudformation validate-template --template-body file://$filePath/networking/VPC-subnets.yaml
aws cloudformation validate-template --template-body file://$filePath/networking/sg-web.yaml
aws cloudformation validate-template --template-body file://$filePath/security/keypair.yaml
aws cloudformation validate-template --template-body file://$filePath/compute/EC2-web-servers.yaml
aws cloudformation validate-template --template-body file://$filePath/compute/TG-EC2-web-servers.yaml
aws cloudformation validate-template --template-body file://$filePath/compute/EC2.yaml

# 템플릿을 활용해 stack 생성
aws cloudformation create-stack \
    --stack-name cfn-goorm-vpc \
    --template-body file://$filePath/networking/VPC.yaml \
    --region ap-northeast-2

aws cloudformation create-stack \
  --stack-name cfn-goorm-vpc-subnets \
  --template-body file://$filePath/networking/vpc-subnets.yaml \
  --capabilities CAPABILITY_IAM

aws cloudformation create-stack \
  --stack-name cfn-goorm-keypair \
  --template-body file://$filePath/security/keypair.yaml \
  --capabilities CAPABILITY_IAM

aws cloudformation create-stack \
  --stack-name cfn-goorm-sg-web \
  --template-body file://$filePath/networking/sg-web.yaml \
  --capabilities CAPABILITY_IAM

aws cloudformation create-stack \
  --stack-name cfn-goorm-web-servers \
  --template-body file://$filePath/compute/EC2-web-servers.yaml \
  --capabilities CAPABILITY_IAM

aws cloudformation create-stack \
  --stack-name cfn-goorm-tg-web-servers \
  --template-body file://$filePath/compute/TG-EC2-web-servers.yaml \
  --capabilities CAPABILITY_IAM

aws cloudformation create-stack \
    --stack-name cfn-goorm \
    --template-body file://$filePath/compute/EC2.yaml \
    --region ap-northeast-2

# 오류 발생 시 stack 삭제 후 재생성해야 함.
# stack 삭제
aws cloudformation delete-stack --stack-name cfn-goorm
aws cloudformation delete-stack --stack-name cfn-goorm-keypair
aws cloudformation delete-stack --stack-name cfn-goorm-web-servers
aws cloudformation delete-stack --stack-name cfn-goorm-tg-web-servers

# stack 업데이트
aws cloudformation update-stack \
    --stack-name cfn-goorm \
    --template-body file://$filePath/compute/EC2.yaml \
    --region ap-northeast-2

# SSM Parameter 생성
aws ssm put-parameter --name "/cloudformation/networking/VpcId" --value "vpc-0a9cc247dbc0fcda2" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/networking/AvailabilityZone1" --value "ap-northeast-2a" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/networking/AvailabilityZone2" --value "ap-northeast-2b" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/networking/PublicSubnet1Cidr" --value "10.0.1.0/24" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/networking/PublicSubnet2Cidr" --value "10.0.2.0/24" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/networking/PrivateSubnet1Cidr" --value "10.0.3.0/24" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/networking/PrivateSubnet2Cidr" --value "10.0.4.0/24" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/networking/PrivateSubnet1Id" --value "subnet-02417533a3a113c28" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/networking/PrivateSubnet2Id" --value "subnet-00cb400073f50f7e1" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/compute/InstanceType" --value "t3.micro" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/compute/EC2InstanceAMI" --value "ami-061fdbe1769e05459" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/compute/ExistingSecurityGroupId" --value "sg-0e714341ed2c161fe" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/security/KeyPairName" --value "goormEC2WebServerKeyPair" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/compute/ExistingEC2Instance1Id" --value "i-0d021a97a3152a31c" --type String --overwrite
aws ssm put-parameter --name "/cloudformation/compute/ExistingEC2Instance2Id" --value "i-07e243e0403a8f957" --type String --overwrite