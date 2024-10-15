## 1. Extract nouns from the user stories or specification

```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.
User > Account > email

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.
User > Account > user_name

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.
User > Posts > account_id

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.
User > Posts > title
User > Posts > content

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.
User > Posts > views

```

```
Nouns:

Accounts, email, user_name, Posts, title, content, views, account_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                  | Properties                        |
| ---------------------   | ------------------                |
| Accounts                | email, user_name                  |
| Posts                   | title, content, views, account_id |


1. Name of the first table (always plural): `Accounts` 

    Column names: `email`, `user_name`

2. Name of the second table (always plural): `Posts` 

    Column names: `title`, `content`, `views`, `account_id`

## 3. Decide the column types
```
# EXAMPLE:

Table: Accounts
id: SERIAL
email: varchar(250)
user_name: varchar(250)

Table: Posts
id: SERIAL
title: varchar(250)
content: text
views: int
account_id: int
```

## 4. Decide on The Tables Relationship

You'll then be able to say that:

1. **[Accounts] has many [Posts]**
2. And on the other side, **[Posts] belongs to [Accounts]**
3. In that case, the foreign key is in the table [Posts]


```
# EXAMPLE

1. Can one Account have many Posts? YES
2. Can one Post have many Accounts? NO

-> Therefore,
-> An Account HAS MANY Posts
-> A Post BELONGS TO an Account

-> Therefore, the foreign key is on the Posts table.
```
## 5. Write the SQL

```sql
-- EXAMPLE
-- file: students_table.sql

-- Create the table without the foreign key first.
CREATE TABLE accounts (
  id SERIAL PRIMARY KEY,
  email VARCHAR(250),
  user_name VARCHAR(250)
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(250),
  content TEXT,
  views INT,
-- The foreign key name is always {other_table_singular}_id
  account_id int,
  constraint fk_account_id foreign key(account_id)
    references accounts(id)
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 social_network < ssocial_network.sql
```