# AWS에서 키 페어 생성 후 키 페어 다운로드
# 키 페어 파일 이름: keyPair-for-jenkins.pem
# 키 페어 파일 위치: /Users/jaehwan/Desktop/goormthon/team-mission/iaas-cloud-operate-automation/jenkins/keyPair-for-jenkins.pem

# 키 페어 파일 권한 설정
chmod 400 /Users/jaehwan/Desktop/goormthon/team-mission/iaas-cloud-operate-automation/jenkins/keyPair-for-jenkins.pem

# SSH 접속
ssh -i /Users/jaehwan/Desktop/goormthon/team-mission/iaas-cloud-operate-automation/jenkins/keyPair-for-jenkins.pem ubuntu@$PUBLIC_IP