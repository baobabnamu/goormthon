#!/bin/bash

# 전역 변수
BACKUP_DIR="/backup"
LOG_DIR="/var/log"
USER_LIST="user_list.txt"
DATE=$(date '+%Y%m%d_%H%M%S')

# 함수: 디스크 사용량 모니터링
check_disk_usage() {
    echo "[INFO] 디스크 사용량 확인 중..."
    USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    if [ "$USAGE" -ge 80 ]; then
        echo "[WARN] 디스크 사용량이 80%를 초과했습니다. ($USAGE%)"
    else
        echo "[INFO] 디스크 사용량이 정상입니다. ($USAGE%)"
    fi
}

# 함수: 로그 파일 백업
backup_logs() {
    echo "[INFO] 로그 파일 백업 시작..."
    mkdir -p "$BACKUP_DIR/logs_$DATE"
    cp -r "$LOG_DIR"/* "$BACKUP_DIR/logs_$DATE/"
    echo "[INFO] 로그 파일이 $BACKUP_DIR/logs_$DATE 에 백업되었습니다."
}

# 함수: 최근 7일간 수정된 로그 파일 분석
analyze_recent_logs() {
    echo "[INFO] 최근 7일 내 수정된 로그 파일 분석 중..."
    find "$LOG_DIR" -type f -mtime -7 -exec grep -i "error" {} + > "$BACKUP_DIR/logs_$DATE/error_summary.txt"
    echo "[INFO] 에러 로그 요약 파일이 생성되었습니다: $BACKUP_DIR/logs_$DATE/error_summary.txt"
}

# 함수: 사용자 추가
add_users() {
    if [ ! -f "$USER_LIST" ]; then
        echo "[ERROR] 사용자 리스트 파일($USER_LIST)이 존재하지 않습니다."
        return 1
    fi

    echo "[INFO] 사용자 추가 시작..."
    while read -r user; do
        if id "$user" &>/dev/null; then
            echo "[INFO] 사용자 $user 는 이미 존재합니다."
        else
            useradd "$user"
            echo "[INFO] 사용자 $user 추가 완료."
        fi
    done < "$USER_LIST"
}

# 메인 메뉴
main_menu() {
    while true; do
        echo ""
        echo "===== 시스템 관리 툴 ====="
        echo "1. 디스크 사용량 확인"
        echo "2. 로그 파일 백업"
        echo "3. 최근 7일간 에러 로그 분석"
        echo "4. 사용자 추가"
        echo "5. 종료"
        read -p "원하는 작업 번호를 입력하세요: " choice

        case $choice in
            1)
                check_disk_usage
                ;;
            2)
                backup_logs
                ;;
            3)
                analyze_recent_logs
                ;;
            4)
                add_users
                ;;
            5)
                echo "[INFO] 프로그램을 종료합니다."
                exit 0
                ;;
            *)
                echo "[ERROR] 올바른 번호를 입력하세요."
                ;;
        esac
    done
}

# 스크립트 실행
main_menu
