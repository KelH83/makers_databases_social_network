DROP TABLE IF EXISTS students;

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  full_name varchar(100),
  cohort varchar(250)
);

INSERT INTO students (full_name, cohort) VALUES ('Kelly Howes', 'Sept 2024 foundations ra');
INSERT INTO students (full_name, cohort) VALUES ('Kimiko Dogue', 'Walkies');
INSERT INTO students (full_name, cohort) VALUES ('Twyla Kitty', 'Purrfect');
INSERT INTO students (full_name, cohort) VALUES ('Yuki Snake', 'Cornucopia');
