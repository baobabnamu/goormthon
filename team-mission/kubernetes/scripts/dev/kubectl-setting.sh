#!/bin/bash

# 로컬 -> vagrant 클러스터에 원격 실행

# vagrant 환경 - K8s-master 접속 (vagrant ssh k8s-master)
sudo -i
# 아래 출력 내용 복사
cat ~/.kube/config

# localhost 환경
# 복사했던 내용 붙여넣기
vi ~/.kube/config