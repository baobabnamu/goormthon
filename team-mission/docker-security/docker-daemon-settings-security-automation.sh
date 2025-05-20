#!/bin/bash

# 1. docker.service 소유권 설정
chown root:root /lib/systemd/system/docker.service

# 2. docker.service 파일 접근 권한 설정
chmod 644 /lib/systemd/system/docker.service

# 3. docker.socket 소유권 설정
chown root:root /lib/systemd/system/docker.socket

# 4. docker.socket 파일 접근 권한 설정
chmod 644 /lib/systemd/system/docker.socket

# 5. /etc/docker 디렉터리 소유권 설정
chown root:root /etc/docker

# 6. /etc/docker 디렉터리 접근 권한 설정
chmod 755 /etc/docker

# 7. /var/run/docker.sock 파일 소유권 설정
chown root:docker /var/run/docker.sock 

# 8. /var/run/docker.sock 파일 접근 권한 설정
chmod 660 /var/run/docker.sock

# 9. daemon.json 파일 소유권 설정
chown root:root /etc/docker/daemon.json

# 10. daemon.json 파일 접근 권한 설정
chmod 644 /etc/docker/daemon.json

# 11. /etc/default/docker 파일 소유권 설정
chown root:root /etc/default/docker 

# 12. /etc/default/docker 파일 접근 권한 설정
chmod 644 /etc/default/docker 