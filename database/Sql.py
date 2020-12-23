import mysql.connector

class Sql:
    # Param object
    def __init__(self):
        self.mydb = mysql.connector.connect(host = self.host, user = self.user,password = self.password, database = self.database)
        
    # Select where
    def select(self, element, table, where = {}):
        mycursor = self.mydb.cursor()
        sql = "SELECT "+element+" FROM "+table
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
        
    # Insert data
    def insert(self, table, value):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO {} VALUES(%s)".format(table);
        val = value
        mycursor.execute(sql, val)
        self.mydb.commit()
        return mycursor.rowcount
    
    # Delete data
    def delete(self, table, value):
        mycursor = self.mydb.cursor()
        sql = "DELETE INTO {} VALUES(%s)".format(table);
        val = value
        mycursor.execute(sql, val)
        self.mydb.commit()
        return mycursor.rowcount
    
    # update data
    def update(self,where,table, values, value):
        mycursor = self.mydb.cursor()
        sql = "UPDATE {} SET %s WHERE {}".format(table, where);
        val = value
        mycursor.execute(sql, val)
        self.mydb.commit()
        return mycursor.rowcount

    def disconnect(self):
        self.mydb.close()
