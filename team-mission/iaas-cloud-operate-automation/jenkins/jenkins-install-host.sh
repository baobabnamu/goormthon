# Jenkins LTS 버전 설치
brew install jenkins-lts

# Jenkins 서비스 시작
brew services start jenkins-lts

# Jenkins 서비스 동작 확인
brew services list | grep jenkins-lts
brew services info jenkins-lts

# Jenkins 웹 인터페이스 접속
open http://localhost:8080

# Jenkins 초기 설정
jenkins-lts # 결과로 나오는 토큰 값을 이용하여 초기 설정 진행
cat /var/lib/jenkins/secrets/initialAdminPassword # 토큰 값 위치

