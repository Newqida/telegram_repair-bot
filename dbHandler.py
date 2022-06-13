import sqlite3

        
connection = sqlite3.connect('botDB.db', check_same_thread=False)
cursor = connection.cursor()

def user_exists(user_id): 
    """проверяем есть ли юзер в bd"""
    result = cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
    return bool(len(result.fetchall()))

def get_user_id(user_id):
    """Добавляем id юзера в бд по его user_id  в телеграме"""
    result = cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?",(user_id,))
    return result.fetchone()[0]

def add_user(user_id):
    """добавляем юзера в бд"""
    cursor.execute("INSERT INTO `users` (`user_id`) VALUES(?)",(user_id,))
    return connection.commit()

def get_pricesPL():
    cursor.execute("SELECT * FROM priceListPL")
    outputString = ''
    for data in cursor.fetchall():
        outputString += str(data[0]) + ' ' + str(data[1]) + 'zł\n'
    return outputString

def get_pricesRU():
    cursor.execute("SELECT * FROM priceListRU")
    outputString = ''
    for data in cursor.fetchall():
        outputString += str(data[0]) + ' ' + str(data[1]) + 'zł\n'
    return outputString

def write_records(user_id,value):
    cursor.execute("INSERT INTO `records` (user_id,value) VALUES(?,?)",
    (get_user_id(user_id),
    value))    
    return connection.commit()

def close():
    connection.close()