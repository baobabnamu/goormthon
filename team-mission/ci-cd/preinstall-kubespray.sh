#!/bin/bash

git clone https://github.com/kubernetes-sigs/kubespray.git

brew install kreuzwerker/taps/m1-terraform-provider-helper
m1-terraform-provider-helper activate
m1-terraform-provider-helper install hashicorp/template -v v2.2.0

cd kubespray/contrib/terraform/aws

terraform init

terraform plan -out=tfplan

terraform apply tfplan

# Kubespray 루트 폴더로 이동
cd /Users/jaehwan/Desktop/goormthon/team-mission/ci-cd/kubespray/

# Kubespray는 Ansible 버전 2.16.4 ~ 2.17.0만 지원되므로 최신 버전일 경우, 아래와 같이 버전 변경
# 버전 확인
ansible --version

# 버전 변경
brew uninstall ansible && pip install ansible-core==2.16.4

# Ansible 호환되는 Python 버전 설치
pyenv install 3.11.8 && pyenv global 3.11.8

pip install -r requirements.txt

# 컬렉션 설치
ansible-galaxy collection install kubernetes.core ansible.posix community.general ansible.utils

ansible-playbook -i inventory/hosts cluster.yml \
  -e ansible_user=ubuntu \
  -e ansible_ssh_private_key_file=~/.ssh/your-key.pem \
  -e "ansible_ssh_common_args='-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ProxyCommand=\"ssh -i ~/.ssh/goorm-kubespray.pem -W %h:%p ubuntu@your-bastion-ip\"'" \
  -e ansible_become=yes \
  -e ansible_become_method=sudo \
  -e ansible_become_user=root \
  --ask-become-pass \
  --flush-cache \
  -vvv # 디버깅 출력

# 테스트용 SSH 명령어
ssh -o StrictHostKeyChecking=no \
    -o UserKnownHostsFile=/dev/null \
    -i ~/.ssh/your-key.pem \
    -o ProxyCommand="ssh -i ~/.ssh/your-key.pem -W %h:%p ubuntu@your-bastion-ip" \
    ubuntu@your-k8s-node-ip 'echo "test"'

# SSH Connection closed by UNKNOWN port 65535 오류 발생 시
# terraform 폴더에서 사용한 키와 동일한 키가 존재해야 하고, 0400 권한이여야 함.
ls -l ~/.ssh/
chmod 400 ~/.ssh/your-key.pem