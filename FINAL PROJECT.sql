create database banks_portal;
use banks_portal;

create table accounts 
(
	accountId int not null unique auto_increment primary key,
	ownerName varchar(45) Not Null,
	owner_ssn int not null,
	balance decimal (10,2) default 0.00,
	account_status varchar(45)
);
 

create table transactions 
(
	transactionId int not null unique auto_increment primary key,
    accountID int not null,
    transactionType varchar(45) not null,
    transactionAmount decimal (10,2) not null
    
);

insert into accounts
values ("Maria Jozef", 123456789, 10000.00, "active"), ("Linda Jones", 987654321, 2600.00, "inactive"), 
	  ("John McGrail", 222222222, 100.50, "active"), ("Patty Luna", 111111111, 509.75, "inactive");
      
 insert into transactions 
 values (1, deposit, 650.98), 
		(3, withdraw, 899.87), 
        (3, deposit, 350.00);

Delimiter //

Create procedure accountTransactions(IN accountID INT)
BEGIN
    SELECT * FROM Transactions
    WHERE accountID = accountID;
END //
Delimiter;

Delimiter //
 
 Create procedure deposit(
 IN accountID int, in amount decimal(10,2))
 Begin
 insert into transacions (accountId, transactionType, transacttionAmount)
 Values (accountId, "deposit", amount);
 update accounts set balance = balance + amount where accountId = accountID;
 end //
 delimiter //

