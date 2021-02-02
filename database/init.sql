CREATE TABLE setup (
	complete			CHAR(1)		NOT NULL
);

CREATE TABLE tickets (
	id 					INTEGER 	PRIMARY KEY AUTOINCREMENT,
	ticket_id			TEXT
);

CREATE TABLE description (
	id 					INTEGER 	PRIMARY KEY AUTOINCREMENT,
	parent				INTEGER 	NOT NULL,
	description			TEXT,
	FOREIGN KEY 		(parent)	REFERENCES tickets(id)
);

CREATE TABLE short_description (
	id 					INTEGER 	PRIMARY KEY AUTOINCREMENT,
	parent				INTEGER 	NOT NULL,
	short_description	TEXT,
	FOREIGN KEY 		(parent)	REFERENCES tickets(id)
);

CREATE TABLE work_notes (
	id 					INTEGER 	PRIMARY KEY AUTOINCREMENT,
	parent				INTEGER 	NOT NULL,
	work_note			TEXT,
	FOREIGN KEY 		(parent)	REFERENCES tickets(id)
);

CREATE TABLE users (
	id 					INTEGER 	PRIMARY KEY AUTOINCREMENT,
	name				TEXT 		NOT NULL,
	username			TEXT		NOT NULL,
	email				TEXT,
	roles				TEXT
);

CREATE TABLE password (
	id					INTEGER		PRIMARY KEY AUTOINCREMENT,
	user				INTEGER		NOT NULL UNIQUE,
	password			CHAR(64)	NOT NULL,
	FOREIGN KEY			(user)		REFERENCES users(id)
);
