import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="3600",
                 database="banks_portal",
                 user='root',
                 password='Jordan28'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)


    def getAllAccounts(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            query = "select * from accounts"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllTransactions(self):
        ''' Complete the method to execute
                query to get all transactions'''

        query = "SELECT * FROM transactions"
        cursor = connection.cursor()

    try:
        cursor.execute(query)
        transactions = cursor.fetchall()
    return transactions

    except Exception as e:
        print(f"Error retrieving transactions: {e}")
        # Handle the exception as per your requirement

    cursor.close()
       
       
    def deposit(self, accountID, amount):
        if self.connection is connected():
            self.cursor= self.connection.cursor();
            query = "select * from transactions where transactionType = 'deposit'"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records


    def withdraw(self, accountID, amount):
        if self.connection is connected():
            self.cursor= self.connection.cursor();
            query = "select * from transactions where transactionType = 'withdraw'"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
    
        
    def addAccount(self, ownerName, owner_ssn, balance, status):
        if self.connection is connected():
            self.cursor= self.connection.cursor();
            query = "insert into accounts (ownerName, owner_ssn, balance, status) values VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, values)
            records = self.cursor.fetchall()
            return records
  
    def accountTransactions(self, accountID):
        if self.connection is connected():
            self.cursor= self.connection.cursor();
            query = ""
            self.cursor.execute(query,ownerName, owner_ssn, balance,status)
            records = self.cursor.fetchall()
            return records
  
    def deleteAccount(self, AccountID):
        if self.connection is connected():
            self.cursor= self.connection.cursor();
            query = "Delete from accouns where accountID = %s"
            self.cursor.execute(query, values)
            records = self.cursor.fetchall()
            return records
        
        
        
    
    
