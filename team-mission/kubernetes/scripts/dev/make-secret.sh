#!/bin/bash
# Secret 에서 값을 저장해서 사용하기 위해서는 base64 인코딩이 필요함
# 예시
echo -n "mysql-django" | base64
# 혹은 secret 파일의 data: 필드를 stringData: 필드로 변경하면 자동으로 base64 인코딩 됨