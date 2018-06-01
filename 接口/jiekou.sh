#!/bin/bash
function sscurl {
while read line;do
    {   
    echo $line| grep '^#' >>/dev/null && continue
    Rcode=`curl -o  /dev/null --connect-timeout 1 -m 2 -s -d "{}" -w %{http_code} $line`
    if (($Rcode==200));then
        tagg=1
    elif [[ $Rcode =~ [2][0-9]+$ ]];then
        tagg=1
    elif (($Rcode==000));then
        echo "$line 有问题 返回值为 $Rcode 域名不能解析"
        echo "1" >>`dirname $0`/tag.txt
    else
        echo "$line 有问题 返回值为 $Rcode"
        echo "1" >>`dirname $0`/tag.txt
    fi  
    } & 
done  < `dirname $0`/jiekou.txt
}
>`dirname $0`/tag.txt
sscurl
wait
if [ ! -s `dirname $0`/tag.txt ];then
    echo "okokok"
fi

