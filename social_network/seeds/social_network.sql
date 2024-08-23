DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq CASCADE;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq CASCADE;

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
  user_id int,
  constraint fk_user foreign key(user_id) references users(id) on delete cascade
);

INSERT INTO users (email_address, username) VALUES ('test@test.com', 'test');
INSERT INTO users (email_address, username) VALUES ('trial@trial.com', 'trial');
INSERT INTO users (email_address, username) VALUES ('tony_hawks@skate.com', 'sk8');
INSERT INTO users (email_address, username) VALUES ('matt_hoffman@bmx.com', 'bmx');

INSERT INTO posts (title, content, views, user_id) VALUES ('Blog_1', 'My first blog', 63, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Blog_2', 'My sk8 blog', 77, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('BmxBlog', 'I bmx blog', 99, 4);
INSERT INTO posts (title, content, views, user_id) VALUES ('Blog_trial', 'Blog trial', 20, 2);
