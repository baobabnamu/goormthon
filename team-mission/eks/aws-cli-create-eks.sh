#! /bin/bash
# for using AWS CLI to create EKS cluster

# 1. 권한 확인
aws sts get-caller-identity

# 2. CloudFormation 스택 생성
aws cloudformation create-stack \
  --region ap-northeast-2 \
  --stack-name goorm-eks-vpc-stack \
  --template-url https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2020-10-29/amazon-eks-vpc-private-subnets.yaml

# 3. iam 역할 생성
aws iam create-role \
  --role-name goorm-eks-cluster-role \
  --assume-role-policy-document file://"eks-cluster-role-trust-policy.json"

# 4. 역할 확인
aws iam list-roles | jq '.Roles[] | select(.RoleName == "goorm-eks-cluster-role")'

# 5. 역할 정책 추가
aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy \
  --role-name goorm-eks-cluster-role

# 6. 역할 정책 확인
aws iam list-attached-role-policies \
  --role-name goorm-eks-cluster-role

# 7. 클러스터 생성
aws eks create-cluster \
  --region ap-northeast-2 \
  --name goorm-eks-cluster \
  --kubernetes-version 1.32 \
  --role-arn arn:aws:iam::593793025731:role/goorm-eks-cluster-role \
  --resources-vpc-config subnetIds=your-private-subnet-id1,your-private-subnet-id2

# 8. 클러스터 확인
aws eks list-clusters

# 9. 클러스터 설명 확인
aws eks describe-cluster \
  --name goorm-eks-cluster

# 10. kubeconfig 업데이트
aws eks update-kubeconfig --region ap-northeast-2 --name goorm-eks-cluster

# 11. 클러스터 접속 확인
kubectl get svc
