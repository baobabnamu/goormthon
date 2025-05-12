#!/bin/bash
for i in {1..10}
do
  username="user$i"

  if id "$username" &>/dev/null; then
    userdel -r "$username"
  else
    echo "User $username does not exist, skipping!"
  fi
done