brew tap hashicorp/tap # terraform 패키지 추가 (brew에서 추가되어 있지 않은 패키지를 추가하기 위해 필요)
brew install hashicorp/tap/terraform # terraform 설치

# terraform 버전 확인
terraform version

# terraform 초기화
terraform init

# terraform 플랜 생성
terraform plan -out=tfplan

# terraform 적용
terraform apply tfplan
