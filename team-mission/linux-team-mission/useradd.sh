#!/bin/bash
for i in {1..10}
do
  username="user$i"

  if id "$username" &>/dev/null; then
    echo "User $username already exists, skipping!"
  else
    if (($i % 10 == 0)); then
      useradd -m "$username" -u "10$i" -g 1000
    else
      useradd -m "$username" -u "100$i" -g 1000
    fi
      echo "User $username created."
  fi
done          