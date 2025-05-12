#!/bin/bash

# 1. default bridge 사용 비활성화 (컨테이너 간 네트워크 트래픽 제한) 
systemctl stop dockerd docker.socket docker.service
echo 'DOCKER_OPTS="--icc=false"' >> /etc/default/docker
sed -i '/^ExecStart=/iEnvironmentFile=/etc/default/docker' /lib/systemd/system/docker.service
sed -i 's|--containerd=/run/containerd/containerd.sock|$DOCKER_OPTS|' /lib/systemd/system/docker.service
systemctl daemon-reload && systemctl restart dockerd docker.socket docker.service

# 2. 도커 클라이언트 인증 설정
# OPA 플러그인 등을 활용하여 적절하게 설정
# Ref : https://iwantbaobab.tistory.com/674

# 3. legacy registry 비활성화
# Docker v17.12 이상이면 상관 없음

# 4. 추가 권한 획득으로부터 컨테이너 제한
# 컨테이너 Run 시 --security-opt=no-new-privileges 옵션을 사용한다.