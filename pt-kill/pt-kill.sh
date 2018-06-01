#!/bin/bash

ps -ef |grep pt-kill|awk '{print "kill -9 " $2}'|sh & /root/mysqlquery_autokill.pl
