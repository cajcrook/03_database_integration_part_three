# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

```

```
Nouns:

cohorts name, start dates
student names, cohorts name
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| cohort                | names, start_date
| names                 | cohort

1. Name of the first table (always plural): `cohorts` 

    Column names: 'names', 'start_date'

2. Name of the second table (always plural): `names` 

    Column names: `cohort`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
Table: cohorts
id: SERIAL
name: text
start_date: text

Table: names
id: SERIAL
name: text
cohort: text
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
1. Can one cohort have many students? YES
2. Can one student have many cohorts? NO

Therefore cohorts HAS MANY students
A student belongs to a a cohort

Therefore the foreign key must be on the Students table
```

## 5. Write the SQL

```sql

file: cohorts_table.sql
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  start_date text,
);

CREATE TABLE students(
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
-- below dictates that a cohorts id is the id from the cohorts table but it also says to delete all entries within a cohort when a cohort is removed.
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 student_directory_2 < student_directory_2.sql
```

