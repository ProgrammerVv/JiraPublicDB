from clickhouse_driver import connect, Client

def db_connect(host):

    client = Client(
        host=host,
        #port='8123',
        #secure=False,
        #verify=False
        #user='python_automation',
        #password='joij1310jVCnskz39414'
        settings={'use_numpy': True}
    )
    return client
   #print(client.execute('SHOW DATABASES'))


#Отключить учетную запись default в бд после тестов и выкатки на настоящмие данные
#Не забыть добавить функцию disconnect() для закрытия соединения после работы с бд
# вытащить из функции дб-коннект параметры подключения - логин.пароль