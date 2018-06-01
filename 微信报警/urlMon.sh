#!/bin/bash

script_path=$(dirname $0)
urls=${script_path}/url.txt
t=$(wc -l $urls |awk '{print $1}')
tim=`date +"%Y-%m-%d %H:%M:%S"`
flag=0
> /tmp/urlmonitor.txt
for x in $(seq 1 $t)
   do  
        t1=$(awk "NR==$x"'{print $1}' $urls)
        t2=$(awk "NR==$x"'{print $2}' $urls)
        t3=$(awk "NR==$x"'{print $3}' $urls)
        if [ ! -z $t1 ] ;then
            echo $t1 |grep -q "#"
            [ $? -eq 0 ] && continue 
            if [ $t2 == "get" ];then
               re=$(python ${script_path}/get.py "$t1")
            elif [ $t2 == "post" ];then
               re=$(python ${script_path}/req.py "$t1" "data")
            fi 

            if [[ ! $re -eq 1 ]];then
                echo "$t3" >> /tmp/urlmonitor.txt
                flag=1
                sh /home/wls81/shell/rundeck/send-msg-to-wx.sh "$tim ${t3} "  2>&1 | > /dev/null
            fi  
        fi  
 done

[ $flag -eq 0 ] && echo "okokok!" > /tmp/urlmonitor.txt




