
echo "Redis master clients"
redis-cli -h 10.9.94.237 info clients | grep connected_clients
echo "Redis slave clients"
redis-cli -h 10.9.189.174 info clients | grep connected_clients 

echo "Mysql data connections"
mysql -h10.9.162.240 -uyw_operate -pyw_operate_2017 -e"show processlist" | wc -l
echo "Mysql xs connections"
mysql -h10.9.114.204 -uyw_read -pyw_read_2017 -e"show processlist" | wc -l


