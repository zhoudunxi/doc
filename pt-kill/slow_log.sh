#!/bin/bash

uf651u415rq31702d="shandai主库"
#uf69iald573xi20h0="shandai从库"
uf69iald573xi20h0="none"
uf6c6w0hiv0hp9d60="none"
uf6rn4txomr76haj9="none"
uf6r8m3n0g7gh38r2="current闪贷风控主库"
uf60mf1q7e0772hqh="current闪贷风控从库"
uf6u25ene6b03rwib="current催收主库"
uf6r711ot90719yc9="current催收从库"
uf6u94lhoqqd1ez78="current惠花花app主库"
uf6uk14v1p8402kik="current惠花花app从库"
uf62q63345934b308="current惠花花risk主库"
uf6ts456pxxz22dbl="current惠花花risk从库"
uf6522mi7k3487a32="current电销主库"
uf6ho6939d7d5z229="current电销从库01"
uf6e13490y0p7rmd1="current电销从库02"
uf6xph47fy1lm90r2="current运营主库"
uf68se3i2yw6fiugk="current运营从库01"

 d=`date +"%Y-%m-%d"`
 h=`date +"%H"`
 h=`expr $h + 0`
 m=`date +"%M"`
 m=`expr $m + 0`

function tt_str {
  string=$1
  echo $string |grep -q "current"
  if [ ! $? -eq 0 ];then
    if [ $h -gt 8 ];then
       h=$(($h-8))
    elif [ $h -lt 8 ];then
       h=$(($h+24-8)) 
    elif [ $h -eq 8 ];then
       h="00"
    fi
 fi

 t_str="# ${d}T${h}"
 if [ $h -lt 10 ];then
    tim_str="# ${d}T0${h}"
 fi
 echo "$t_str"
}

logfile=`cd /tmp ;ls |grep -E "(^rr-|^rm-)"`
flag=0
for f in $logfile
do
  filename=`echo $f |awk -F "[.-]" '{print $2}'`
  eval alter_str="\$$filename"
  [ -z $alter_str ] && alter_str="数据库 $filename "
  if [[ $alter_str != "none" ]];then
     tim_str=`tt_str $alter_str`
     grep "$tim_str" /tmp/$f > /tmp/slow_log.txt
     num=`cat /tmp/slow_log.txt |wc -l`
     if [ ! -z $num ];then
        for x in `seq 1 $num`
        do
          line=`sed -n "${x}p" /tmp/slow_log.txt`
          echo "$line" |grep -q -i -E "(xxl_job|XXL_JOB)"
          if [ $? -eq 0 ];then
             continue    
          fi
          mm=`echo "$line" |awk -F ":" '{print $2}'` 
          mm=`expr $mm + 0`
          if [[ $mm -gt $m ]];then
             mm=`expr ${mm} - ${m} `
          else
             mm=`expr ${m} - ${mm} `
          fi
          if [[ $mm -lt 50 ]];then
             li=`echo "$line" | awk '{print $2}'`
             n=`grep -n "$li" /tmp/$f |awk -F ":" '{print $1}'`
             n=`echo $n |awk '{print $1}'`
             echo "${f}: ${alter_str}慢日志：$line"
             sed -n "${n},\$p" /tmp/$f 
             flag=1
             break
         fi 
       done
    fi
  fi     
done

[ $flag -eq 0 ] && echo "okokok!"
