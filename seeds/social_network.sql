DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts (
  id SERIAL PRIMARY KEY,
  email VARCHAR(250),
  user_name VARCHAR(250)
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(250),
  content TEXT,
  views INT,
  account_id int,
  constraint fk_account_id foreign key(account_id)
    references accounts(id)
    on delete cascade
);

INSERT INTO accounts (email, user_name) VALUES ('Kelly@madeupemail.com', 'Kelly H');
INSERT INTO accounts (email, user_name) VALUES ('Kimi@adogue.com','Kimiko Dogue');
INSERT INTO accounts (email, user_name) VALUES ('KittyKatty@whiskas.com','Twyla Kitty');
INSERT INTO accounts (email, user_name) VALUES ('slytherinhouse@hp.com','Yuki Snake');

INSERT INTO posts (title, content, views, account_id) VALUES ('Day 1', 'Learned Python fundamentals', 1, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Day 2','Went on an awesome walk', 3, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Day 3','tuna is the best flavour ever!', 0, 3);
INSERT INTO posts (title, content, views, account_id) VALUES ('Day 4','I am very hungry, might eat a mouse later', 2, 4);