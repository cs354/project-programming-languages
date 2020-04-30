#!/bin/bash

# This is the exact script that will grade your work.
# It uses the exact same grader as ../runtest. If you get 100%
# in your container. You'll get 100% on the server.


FILE=/tmp/submission/submission.tar.gz
if ! test -f "$FILE"; then
  # Student entering container, not grading
  /bin/bash
  exit
fi

# Grading

if ! tar -xf /tmp/submission/submission.tar.gz -C /tmp/submission 2> /dev/null; then
  echo "FAIL_UNTAR"
  exit
fi

while ! mysqladmin ping -h"$MYSQLD_HOST" --silent > /dev/null ; do
    sleep 1
done
sleep 2

mv /tmp/submission/mysql/* /grading/mysql
mv /tmp/submission/ruby/* /grading/ruby
mv /tmp/submission/shell/* /grading/shell
mv /tmp/submission/c/* /grading/c


python3 /grading/util/grader.py