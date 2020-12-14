DROP SCHEMA `polly_es`;

CREATE SCHEMA `polly_es` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_ci;


USE `polly_es`;



CREATE TABLE person (
	id TINYINT UNSIGNED NOT NULL,
	title varchar(3), -- e.g., 2sf (2nd person singular female)
	PRIMARY KEY(id),
	UNIQUE (title)
);


-- counting mood
CREATE TABLE tense (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title varchar(30),
	PRIMARY KEY(id),
	UNIQUE (title)
);

CREATE TABLE verb (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title varchar(25),
	freq SMALLINT UNSIGNED,
	PRIMARY KEY(id),
	UNIQUE (title)
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
	PRIMARY KEY(id),
	UNIQUE (title)
);
