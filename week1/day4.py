# server_ip = ["192.162.0.1", "168.72.0.0"]

# server_conf = {
#     "host": "web01",
#     'ip': "128.01.0.0",
#     'status': "active"
# }
# i = 0
# print(f"Информация о сервераъ и доступных ip")
# for ip in server_ip:
#     i += 1
#     print(f"{i}. {ip}")
# print(f"Всего ip в списке {server_ip.__len__()}")

# for key,value in server_conf.items():
#     print(f"{key}: {value}")
    
server_info = [
    {
        "host":"web01",
        "ip":"192.168.0.0",
        "status": "active"
    },
    {
        "host":"db22",
        "ip":"192.169.0.0",
        "status": "offline"
     },
    {
        "host":"web07",
        "ip":"192.170.0.0",
        "status": "active"
     },
    {
        "host":"db01",
        "ip":"192.171.0.0",
        "status": "active"
     },
    {
        "host":"test",
        "ip":"192.172.0.0",
        "status": "offline"
     },
]
print(f"Всего серверов {server_info.__len__()}")
offline_server = 0
active_server = 0
for server in server_info:
    if server['status'] == "active":
        active_server += 1
    elif server["status"] == "offline":
        offline_server += 1
print(f"Активных {active_server}")
print(f"Неактивных {offline_server}")


search = input("Введите имя сервера: ")
for server in server_info:
    if server['host'] == search:
        print(f"Сервер {server['host']}\nIP {server['ip']}\nСтатус {server['status']}")

search_host = input("Введите хост: ")
up_status = input("Введите status(activate/offline): ")
for server in server_info:
    if server['host'] == search_host:
        server["status"] = up_status
        print(f"Статус сервера изменен на {up_status}\n{server['host']}\n{server['ip']}\n{server['status']}")