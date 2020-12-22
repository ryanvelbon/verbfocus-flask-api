DROP SCHEMA `es`;

CREATE SCHEMA `es` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_ci;


USE `es`;



CREATE TABLE person (
	id TINYINT UNSIGNED NOT NULL,
	title varchar(3), -- e.g., 2sf (2nd person singular female)
	PRIMARY KEY(id),
	UNIQUE (title)
);


-- counting mood
CREATE TABLE tense (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title varchar(30), -- for tr.tense varchar(60)
	PRIMARY KEY(id),
	UNIQUE (title)
);

-- grammar topics
CREATE TABLE grammar (
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

-- grammar-focused sentences
-- e.g. 
-- Yesterday I {went} to the beach and {swam}. {go}{swim}
-- The man is {taller} than the woman. {tall}

CREATE TABLE gr_sentence (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title varchar(255),
	bracket_terms varchar(100),
	grammar_id TINYINT UNSIGNED,
	PRIMARY KEY(id),
	FOREIGN KEY (grammar_id) REFERENCES grammar(id),
	UNIQUE (title)
);


-- Language-Specific Tables

--FR - FRENCH -----------------------------------------------------------------
CREATE TABLE de.vppppa (
	verb_id SMALLINT UNSIGNED,
	present_participle varchar(25),
	past_participle varchar(25),
	auxiliary varchar(25),
	PRIMARY KEY (verb_id),
	FOREIGN KEY (verb_id) REFERENCES verb(id)
);


--EN - ENGLISH -----------------------------------------------------------------
CREATE TABLE en.vconj (
	verb_id SMALLINT UNSIGNED,
	past varchar(25),
	past_participle varchar(25),
	third_person_present varchar(25),
	gerund varchar(25),
	PRIMARY KEY (verb_id),
	FOREIGN KEY (verb_id) REFERENCES verb(id)
);

-- ES - SPANISH --------------------------------------------------------------
-- Verb Past Participles & Gerund
CREATE TABLE es.vppg (
	verb_id SMALLINT UNSIGNED,
	gerund varchar(25),
	ms varchar(25),
	fs varchar(25),
	mp varchar(25),
	fp varchar(25),
	PRIMARY KEY (verb_id),
	FOREIGN KEY (verb_id) REFERENCES verb(id)
);

--FR - FRENCH -----------------------------------------------------------------
CREATE TABLE fr.vppg (
	verb_id SMALLINT UNSIGNED,
	gerund varchar(25),
	past_participle varchar(25),
	PRIMARY KEY (verb_id),
	FOREIGN KEY (verb_id) REFERENCES verb(id)
);

--IT - ITALIAN ---------------------------------------------------------------
CREATE TABLE it.vppppga (
	verb_id SMALLINT UNSIGNED,
	auxiliary_is_essere BIT,
	gerund varchar(25),
	present_participle varchar(25),
	past_participle varchar(25),
	PRIMARY KEY (verb_id),
	FOREIGN KEY (verb_id) REFERENCES verb(id)
);

--PT - PORTUGUESE---------------------------------------------------------------
-- Verb Past Participles & Gerund
CREATE TABLE pt.vppg (
	verb_id SMALLINT UNSIGNED,
	gerund varchar(25),
	ms varchar(25),
	fs varchar(25),
	mp varchar(25),
	fp varchar(25),
	PRIMARY KEY (verb_id),
	FOREIGN KEY (verb_id) REFERENCES verb(id)
);


