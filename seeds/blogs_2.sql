CREATE TABLE blogs (
  id SERIAL PRIMARY KEY,
  name text,
  blog_title text,
  blog_content text
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comment_content text,
  comment_author text,
  blog_id int,
  constraint fk_blog foreign key(blog_id)
    references blogs(id)
    on delete cascade
);
