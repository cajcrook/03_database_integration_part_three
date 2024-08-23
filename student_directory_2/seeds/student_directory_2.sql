DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq CASCADE;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date text
);

DROP TABLE IF EXISTS students CASCADE;
DROP SEQUENCE IF EXISTS students_id_seq CASCADE;

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 1', '01/01/2023');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 2', '01/06/2023');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 3', '01/01/2024');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 4', '01/06/2024');

INSERT INTO students (name, cohort_id) VALUES ('Chris', 1);
INSERT INTO students (name, cohort_id) VALUES ('Chris_2', 1);
INSERT INTO students (name, cohort_id) VALUES ('Chris_3', 1);
INSERT INTO students (name, cohort_id) VALUES ('Irina', 2);
INSERT INTO students (name, cohort_id) VALUES ('Christopher', 3);
INSERT INTO students (name, cohort_id) VALUES ('Reen', 4);
