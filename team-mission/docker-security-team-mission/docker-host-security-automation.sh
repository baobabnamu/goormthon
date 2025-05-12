#!/bin/bash

# 1. Docker 업데이트
apt -y update
apt install --only-upgrade docker.io -y

# 2. Docker 관련 감사 설정
apt -y install auditd
cat <<EOF >> /etc/audit/rules.d/audit.rules
-w /usr/bin/docker
-w /var/lib/docker -k docker
-w /etc/docker -k docker
-w /lib/systemd/system/docker.service -k docker
-w /lib/systemd/system/docker.socket -k docker
-w /etc/default/docker -k docker
EOF
systemctl restart auditd