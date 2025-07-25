Drop database IF EXISTS RealStateDB;

CREATE DATABASE RealStateDB;

USE RealStateDB;

CREATE TABLE realstate
(
   houseID int AUTO_INCREMENT primary key,
   address1 varchar(25) NOT NULL,
   address2 varchar(25) NULL,
   city varchar(15) NOT NULL,
   state varchar(2),
   postalcode varchar(5),
   country varchar(25),
   photo varchar(255),
   house_size float,
   registerDate date
);

-- Insert or create a new house
INSERT INTO RealStateDB.realstate (houseID, address1, address2, city, state, postalcode, country, photo, house_size, registerDate) 
     VALUES (null, '567 calle Quito', 'suite 439', 'San Juan', 'PR', '00921', 'USA', 'myhome.jpg', 100, '2000-10-31');

-- Select all houses from DB
SELECT * FROM RealStateDB.realstate;	

-- Select an specific house 
SELECT * FROM RealStateDB.realstate WHERE houseID = 1;

-- Update a product
UPDATE RealStateDB.realstate SET house_size = 125 WHERE houseID = 1;

	 
