#!/bin/zsh
# pyenv 설치
brew install pyenv

# pyenv 설정
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

source ~/.zshrc

pyenv install 3.13.0
pyenv global 3.13.0

# 파이썬 버전 확인
python --version

# 가상환경 생성
python -m venv django-tutorial-env
source django-tutorial-env/bin/activate

# django 설치
pip install django

# django 버전 확인
python -m django --version

# django 디렉터리 생성
mkdir django-tutorial

# django 프로젝트 생성
django-admin startproject mysite django-tutorial

# 서버 실행
python manage.py runserver 0.0.0.0:8000


