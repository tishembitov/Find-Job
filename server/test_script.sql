create table source_files (
	id integer PRIMARY KEY autoincrement, 
	filename varchar(255) NOT NULL, 
	processed datetime
);
create table user (
	id integer PRIMARY KEY autoincrement, 
	email varchar(255) NOT NULL, 
	password varchar(255) NOT NULL,
	role varchar(255) NOT NULL
);

create table mydocuments (
	id integer PRIMARY KEY autoincrement, 
	user_id integer NOT NULL,
	CONSTRAINT fk_user 
	FOREIGN KEY (user_id) 
	REFERENCES user (id)
	ON DELETE CASCADE
);

create table resume (
	id integer PRIMARY KEY autoincrement,
	title varchar(255) NOT NULL,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL,
	middle_name varchar(255) NOT NULL,
	age integer NOT NULL,
	gender varchar(255) NOT NULL,
	area varchar(255) NOT NULL,
	education_level varchar(255) NOT NULL,
	experience integer NOT NULL,
	salary varchar(255) NOT NULL,
	skills varchar(255) NOT NULL
);

create table vacancy (
	id integer PRIMARY KEY autoincrement,
	name varchar(255) NOT NULL,
	employer varchar(255) NOT NULL,
	status varchar(255) NOT NULL,
	shedule varchar(255) NOT NULL,
	experience integer NOT NULL,
	salary varchar(255) NOT NULL,
	skills varchar(255) NOT NULL,
	city varchar(255) NOT NULL,
	street varchar(255) NOT NULL,
	building varchar(255) NOT NULL,
	logo varchar(255) NOT NULL
);

create table myresumes (
	id integer PRIMARY KEY autoincrement, 
	mydocuments_id integer NOT NULL,
	resume_id integer NOT NULL,
	CONSTRAINT fk_mydocuments
	FOREIGN KEY (mydocuments_id) 
	REFERENCES mydocuments (id)
	ON DELETE CASCADE,
	CONSTRAINT fk_resume
	FOREIGN KEY (resume_id) 
	REFERENCES resume (id)
	ON DELETE CASCADE
);

create table myvacancies (
	id integer PRIMARY KEY autoincrement, 
	mydocuments_id integer NOT NULL,
	vacancy_id integer NOT NULL,
	CONSTRAINT fk_mydocuments
	FOREIGN KEY (mydocuments_id) 
	REFERENCES mydocuments (id)
	ON DELETE CASCADE,
	CONSTRAINT fk_vacancy
	FOREIGN KEY (vacancy_id) 
	REFERENCES vacancy (id)
	ON DELETE CASCADE
);
