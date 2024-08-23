# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

```

```
Nouns:
information, email_address, username
posts, title, content, views

```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| users                 | email_address, username
| posts                 | title, content, views

1. Name of the first table (always plural): `users` 

    Column names: `email_address`, `username`

2. Name of the second table (always plural): `posts` 

    Column names: `title`, `content`, `views`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
Table: users
id: SERIAL
email_address: text 
username: text

Table: posts
id: SERIAL
title: text
content: text
views: int
```

## 4. Decide on The Tables Relationship

1. Can one user have many posts? YES
2. Can one post have many users? NO

-> Therefore,
-> An user HAS MANY posts
-> An post BELONGS TO an user

-> Therefore, the foreign key is on the albums table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL
```
```sql
-- EXAMPLE
-- file: users_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text,
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
-- The foreign key name is always {other_table_singular}_id
-- below dictates that a artists_id is the id from the albums table but it also says to delete all entries within a artitst when a artist is removed.
  user_id int,
  constraint fk_user foreign key(user_id)
    references user(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 social_network < social_network.sql
```