#!/bin/bash

# 1. 컨테이너 SELinux 보안 옵션 설정 (활성화)
systemctl stop dockerd docker.socket docker.service
sed -i 's|DOCKER_OPTS="--icc=false"|DOCKER_OPTS="--selinux-enabled --icc=false"|' /etc/default/docker
systemctl daemon-reload && systemctl restart dockerd docker.socket docker.service

# 2. 컨테이너에서 ssh 사용 금지
# 대부분 백업, 로그 확인, 프로세스 재시작, 설정 변경과 같은 작업을 위해 SSH를 사용한다. 
# 하지만 Docker 컨테이너에서의 이러한 작업은 SSH가 없어도 가능하다. 
# SSH 접속을 위해 사용하는 키와 패스워드는 이미지와 같이 만들거나 불륨에 넣는다. 
# 키와 패스워드를 갱신해야 할 때, 이미지 안에 넣는 경우, 이미지를 다시 만들어 배포한 후 컨테이너를 재시작해야 한다. 
# 인증정보를 볼륨에 넣어두고 관리하는 경우에는 컨테이너가 인증정보를 파손시킬 수 있으므로 컨테이너에 쓰기 권한을 부여해서는 안 된다.

# 3. 컨테이너에 privileged 포트 매핑 금지
# TCP/IP 포트 중 1024 미만의 포트는 권한이 있는 포트로 특정한 목적을 위해서 IANA에서 할당한 포트 번호이다. Docker를 사용하면 컨테이너 포트를 privileged 포트에 매핑할 수 있는데, 이때 일반 사용자와 프로세스는 다양한 보안상의 이유로 privileged 포트를 사용하지 않는 것이 좋다. 
# 따라서 privileged 포트 이외의 별도 포트를 지정하여 매핑하도록 한다.

# 4. PIDs cgroup 제한
# 공격자는 컨테이너 내부에서 포크 폭탄을 실행할 수 있다. 
# 이 포크 폭탄으로 인해 전체 시스템이 손상될 수 있으므로 컨테이너 내부에서 발생할 수 있는 포크의 수를 제한함으로써 이러한 공격을 방지하여야 한다. 
# docker run 시 --pids-limit int 옵션을 사용하면 된다.

# 5. 도커의 default bridge docker() 사용 제한
# Docker는 브리지 모드에서 생성된 가상 인터페이스를 docker0라는 공통 브리지에 연결한다. 
# 이 네트워크 모델은 필터링이 적용되지 않기 때문에 ARP Spoofing 및 MAC Flooding 등의 공격에 취약하다.

# 6. Host의 user namespaces 공유 제한
# user namespaces는 컨테이너 내부의 루트 프로세스가 컨테이너 외부의 루트가 아닌 프로세스에 매핑되도록 한다. 
# 따라서 호스트의 user namespaces을 컨테이너와 공유하면 호스트의 사용자와 컨테이너의 사용자가 분리되지 않는다.