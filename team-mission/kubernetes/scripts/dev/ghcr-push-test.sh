#!/bin/bash
# 1. 도커 허브에 로그인
export CR_PAT=<PERSONAL_ACCESS_TOKEN>
echo $CR_PAT | docker login ghcr.io -u baobabnamu --password-stdin

# 2. 도커 이미지 빌드
docker build -t ghcr.io/baobabnamu/goormthon/team-mission-kubernetes-django-dev:latest .

# 3. 도커 이미지 푸시
# Format : docker push ghcr.io/<깃허브 사용자명 또는 조직>/<이미지명>:<태그>
docker push ghcr.io/baobabnamu/goormthon/team-mission-kubernetes-django-dev:latest

# 4. 도커 이미지 실행 (GHCR 테스트)
# 실행 전에 Github Packages 에서 공개 상태로 변경 필수
docker run -p 8000:8000 ghcr.io/baobabnamu/goormthon/team-mission-kubernetes-django-dev:latest