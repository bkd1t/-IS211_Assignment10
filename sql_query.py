CREATE TABLE person(
	id INT NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	age INT
);

CREATE TABLE person( person_id INT AUTO_INCREMENT primary key NOT NULL, first_name VARCHAR(50), last_name VARCHAR(50), age INT );

CREATE TABLE pet( pet_id INT AUTO_INCREMENT primary key NOT NULL, name VARCHAR(50), breed VARCHAR(50), age INT , dead INT );

CREATE TABLE person_pet( person_id int, pet_id int, FOREIGN KEY (person_id) REFERENCES person(person_id), FOREIGN KEY (pet_id) REFERENCES pet(pet_id) );

INSERT INTO person VALUE("rajendra", "badgujar", 26);

DESCRIBE person_pet;

DROP TABLE pet;

USE person




 