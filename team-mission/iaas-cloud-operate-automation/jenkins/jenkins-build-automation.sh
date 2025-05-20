#!/bin/bash

ssh -i "$EC2_KEY" -o StrictHostKeyChecking=no $EC2_USER@$EC2_HOST << EOF
  cd $APP_DIR
  git pull origin team-mission/iaas
  docker compose pull
  docker compose up -d --build
EOF