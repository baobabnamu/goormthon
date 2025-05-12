filePath="file:///Users/jaehwan/Desktop/goormthon/team-mission/cloud-computing-team-mission/cloudformation"

# 템플릿 유효성 검사
aws cloudformation validate-template --template-body $filePath/networking/VPC.yaml
aws cloudformation validate-template --template-body $filePath/networking/VPC-subnets.yaml
aws cloudformation validate-template --template-body $filePath/networking/sg-web.yaml
aws cloudformation validate-template --template-body $filePath/compute/EC2.yaml

# 템플릿을 활용해 stack 생성
aws cloudformation create-stack \
    --stack-name cfn-goorm-vpc \
    --template-body $filePath/networking/VPC.yaml \
    --region ap-northeast-2

aws cloudformation create-stack \
  --stack-name cfn-goorm-vpc-subnets \
  --template-body $filePath/networking/vpc-subnets.yaml \
  --parameters $filePath/parameters/parameter.yaml \
  --capabilities CAPABILITY_IAM

aws cloudformation create-stack \
  --stack-name cfn-goorm-sg-web \
  --template-body $filePath/networking/sg-web.yaml \
  --parameters $filePath/parameters/parameter.yaml \
  --capabilities CAPABILITY_IAM

aws cloudformation create-stack \
    --stack-name cfn-goorm \
    --template-body $filePath/compute/EC2.yaml \
    --region ap-northeast-2

# 오류 발생 시 stack 삭제 후 재생성해야 함.
# stack 삭제
aws cloudformation delete-stack \
    --stack-name cfn-goorm

# stack 업데이트
aws cloudformation update-stack \
    --stack-name cfn-goorm \
    --template-body $filePath/compute/EC2.yaml \
    --region ap-northeast-2
