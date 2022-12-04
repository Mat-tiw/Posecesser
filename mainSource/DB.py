import base64
from threading import local
import mysql.connector
import random
class posecessorDBs():
    def __init__(self):
        self.localDB = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password='',
            database='posecessordb'
        )
        print('database connected')
    
    def add_user(self, username, password):
        mycurser = self.localDB.cursor()
        exeLine = "INSERT INTO users (Usernames, passwords) values(%s,%s)"
        value = (username, password)
        mycurser.execute(exeLine, value)
        self.localDB.commit()
        return print('commit successful')
    def commiting(self):
        self.localDB.commit()
        return print('closed')
    
    def show(self):
        mycurser = self.localDB.cursor()
        exeLine = "SELECT * FROM users"
        mycurser.execute(exeLine)
        mys = mycurser.fetchall()
        listmy = []
        for i in mys:
            listmy.append(DBMethod(i[0],i[1],i[2]))
        self.localDB.close
        return listmy
    
    def updating(self,userName,id):
        mycurser = self.localDB.cursor()
        exeLine = "UPDATE `users` SET `userName` = %s WHERE `id`= %s"
        value = (userName,id)
        return mycurser.execute(exeLine,value)
    
    def deleting(self,ids):
        mycurser = self.localDB.cursor()
        exeLine = "DELETE FROM `users` WHERE `id`= %s"
        value = (ids, )
        return mycurser.execute(exeLine,value)
    
    def loginFunc(self,Usernames,password):
        if(Usernames == 'admin' and password == '123'):
            return "admin"
            
        mycursor = self.localDB.cursor()

        sql ="""SELECT Usernames,passwords
                FROM users
                WHERE Usernames = %s and passwords = %s
                LIMIT 1;
                """
        val = (Usernames,password)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        if len(myresult) == 1:
            return 'login done'
        else:
            return "Login failed"
    def pullImage(self):
        mycurser = self.localDB.cursor()
        sql = "Select images from imagestorage where Im_id = %s "
        randResult = (random.randrange(1,self.getMaxImage()), )
        print(randResult)
        mycurser.execute(sql,randResult)
        images = mycurser.fetchall()
        images = base64.b64encode(images[0][0]).decode('ascii')
        return images
    def getMaxImage(self):
        mycurser = self.localDB.cursor()
        sql = "select count(Im_id) from imagestorage"
        mycurser.execute(sql)
        result = mycurser.fetchall()
        print(result)
        print(type(result))
        return result[0][0]
    
    def updating(self,userName,id):
        mycurser = self.localDB.cursor()
        exeLine = "UPDATE `users` SET `Usernames` = %s WHERE `id`= %s"
        value = (userName,id)
        mycurser.execute(exeLine,value)
        self.localDB.commit()
        return print('Done')
    
    def deleting(self,ids):
        mycurser = self.localDB.cursor()
        exeLine = "DELETE FROM `users` WHERE `id`= %s"
        value = (ids, )
        mycurser.execute(exeLine,value)
        self.localDB.commit()
        return print('done')
    
class DBMethod():
    def __init__(self,Id,name,password):
        self.Id = Id
        self.name = name
        self.password = password