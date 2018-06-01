curl -i -X POST 'https://oapi.dingtalk.com/robot/send?access_token=62399a3a4f8e4014cf4c7341613ce2992341b53933f17c14a9e245a27f74dae8' \
   -H 'Content-Type: application/json' \
   -d '
  {"msgtype": "text", 
    "text": {
        "content":"hg后台发券失败@all"
     },
   "at":{
	"atMobiles":[
		"18116208606",
                "18016013975"],
   "isAtAll":false
	}
  }'

mysql -h'rr-uf6636rv5e2v3o7bl.mysql.rds.aliyuncs.com' -u'mao' -p'bv4Tfm8Vy'


