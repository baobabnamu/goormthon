#!/bin/bash
# 시스템 패키지 업데이트
yum update -y

# 웹 서버 (NGINX) 설치
amazon-linux-extras install -y nginx1

# 사용자 정의 웹 페이지 생성 (호스트명 표시)
HOSTNAME=$(hostname)
echo "<h1>Hello from ELB Test - $HOSTNAME</h1>" > /usr/share/nginx/html/index.html

# NGINX 서비스 활성화 및 시작
systemctl enable nginx
systemctl start nginx
