#!/usr/bin/env  bash
cd output &&
for i in `ls`
do rm -rf  $i
done
