import sqlite3
import os
import ui.db as db

class Tools():



    @staticmethod
    def getData():

        cur,conn  = db.getLink()
        cur.execute('select input.id,parentId,path,imgName,groupId,parm1,segName,comment from input inner join output o on input.id = o.parentId')
        data = cur.fetchall()

        conn.close()
        return data

        # 新增的数据库操作

    @staticmethod
    def getNoCompleteData():
        cur, conn = db.getLink()
        cur.execute(
            'select input.id,parentId,path,imgName,groupId,parm1,segName,comment from input left join output o on input.id = o.parentId where  parentId is null' )
        data = cur.fetchall()

        conn.close()
        return data

        # 新增的数据库操作

    @staticmethod
    def addData(username, passwd,email,role,remark):

        cur,connect = db.getLink()
        sql = "insert  into user (userName,passWord,email,role ,remark)  values (%s,%s,%s,%s,%s)"
        parm=(username,passwd,email,role,remark)
        cur.execute(sql,parm)
        connect.commit()
        connect.close()

    @staticmethod
    def editData(id,username, passwd,email,role,remark):

        cur,connect = db.getLink()
        command = "update user set userName='%s',passWord='%s',email='%s',role ='%s',remark='%s' where id=%s" % (
        username, passwd,email,role,remark, id)
        cur.execute(command)
        connect.commit()
        connect.close()

    @staticmethod
    def delData(id):
        print(33333)
        cur,conn = db.getLink()
        # connect = sqlite3.connect('mydata.db')
        # c = connect.cursor()
        # print(1)
        command = "delete from user where id = %s" % id
        print(command)
        cur.execute(command)
        conn.commit()
        conn.close()
