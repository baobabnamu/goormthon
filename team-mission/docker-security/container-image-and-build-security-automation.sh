#!/bin/bash

# 1. root가 아닌 user로 컨테이너 실행
# 기본적으로 컨테이너의 user namespace는 호스트의 namespace와 동일하다. 
# 즉, 컨테이너 내부의 root 사용자는 호스트 시스템의 root 사용자이므로 root로 실행되는 컨테이너 프로세스의 손상으로 Docker 호스트 또한 손상될 수 있다. 
# 일반적으로 컨테이너에는 root 권한이 필요하지 않으므로 컨테이너에 있는 애플리케이션은 root 권한으로 실행하지 않아야 한다.
# 아래 내용을 Dockerfile 에 추가하면 된다.
# RUN useradd –d /home/username –m s /bin/bash username
# USER username

# 2. 도커를 위한 컨텐츠 신뢰성 활성화
# Content Trust 설정은 원격 Docker 레지스트리와 주고받는 데이터에 디지털 서명을 허용할 수 있는 기능을 제공한다. 
# 이미지 서명은 데이터 전송 도중에 발생할 수 있는 컨테이너 조작을 방지할 수 있으므로 콘텐츠 신뢰성 설정을 적용해야 한다.
cat <<EOF >> /etc/bash.bashrc 
export DOCKER_CONTENT_TRUST=1
EOF