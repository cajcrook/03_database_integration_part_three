# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.

```

```
Nouns:
blog, titles, content
comments, comment content, author

```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| blog                  | blog_title, blog_content
| comment               | comment_content, comment_author

1. Name of the first table (always plural): `blogs` 

    Column names: `blog_title`, `blog_content`

2. Name of the second table (always plural): `comments` 

    Column names: `comment_content`, `comment_author`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
Table: blogs
id: SERIAL
blog_title: text
blog_content: text

Table: comments
id: SERIAL
comment_content: text
comment_author: text
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

```
1. Can one blog have many comments? YES
2. Can one comments have many blogs? NO

-> Therefore,
-> An blog  HAS MANY comments
-> An comment BELONGS TO a blog

-> Therefore, the foreign key is on the comments table.
```

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE blogs (
  id SERIAL PRIMARY KEY,
  name text,
  blog_title text,
  blog_content text,
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comment_content text,
  comment_author text,
-- The foreign key name is always {other_table_singular}_id
-- below dictates that a artists_id is the id from the albums table but it also says to delete all entries within a artitst when a artist is removed.
  blog_id int,
  constraint fk_blog foreign key(blog_id)
    references blogs(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 blogs_2 < blog_2.sql
```

INSERT INTO posts (title) VALUES ('SQL basics');
INSERT INTO tags (name) VALUES ('sql');

INSERT INTO posts_tags (post_id, tag_id) VALUES (9, 6);

SELECT tags.id, tags.name
  FROM tags 
    JOIN posts_tags ON posts_tags.tag_id = tags.id
    JOIN posts ON posts_tags.post_id = posts.id
    WHERE posts.id = 9;


SELECT posts.id, posts.title
  FROM posts
  JOIN posts_tags ON posts_tags.post_id = posts.id
  JOIN tags ON posts_tags.tag_id = tags.id
  WHERE tags.id = 2;