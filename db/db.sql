DROP SCHEMA `pollyDB`;

CREATE SCHEMA `pollyDB`;

USE `pollyDB`;



CREATE TABLE person (
	id TINYINT UNSIGNED NOT NULL,
	title varchar(3), -- e.g., 2sf (2nd person singular female)
	PRIMARY KEY(id)
);


-- counting mood
CREATE TABLE tense (
	id TINYINT UNSIGNED NOT NULL,
	title varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE verb (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title varchar(25),
	freq SMALLINT UNSIGNED,
	PRIMARY KEY(id)
); 

CREATE TABLE vconj (
	id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
	person_id TINYINT UNSIGNED,
	tense_id TINYINT UNSIGNED,
	verb_id SMALLINT UNSIGNED,
	conj_verb varchar(40),
	PRIMARY KEY (id),
	FOREIGN KEY (person_id) REFERENCES person(id),
	FOREIGN KEY (tense_id) REFERENCES tense(id),
	FOREIGN KEY (verb_id) REFERENCES verb(id),
	UNIQUE (person_id, tense_id, verb_id)
);

CREATE TABLE sentence (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title varchar(255),
	PRIMARY KEY(id)
);

