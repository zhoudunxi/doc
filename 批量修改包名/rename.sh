#!/bin/sh

for file in `ls`
do
mv $file `echo $file | sed 's/xiaoniu/wawa/g'`
done

