### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
A type of relational database, using sql syntax and queries

- What is the difference between SQL and PostgreSQL?
SQL refers to the query language itself, where postgres is an implemention of a database server 
using that language but adding many features and addition syntax as well.

- In `psql`, how do you connect to a database?
psql# \c "database of choice"

- What is the difference between `HAVING` and `WHERE`?
  HAVING is used to filter tables by a specific condition, WHERE is used with group by where it filters the group using the condition of HAVING

- What is the difference between an `INNER` and `OUTER` join?
INNER Joins with have all of the entries of two joined tables where the data intersects using the primary keys of the joined tables. Outer joins can contain entries that are present in one but not the other table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
LEFT OUTER join will contain all the matching entries from the joined table as well as non matching entries on the "left" table, RIGHT join is the same but will have the non matching entries come from the table being joined to the original.

- What is an ORM? What do they do?
A framework for working with databases like postgres, that simplify the syntax and querying and allow creating models for relationship objects, as well as working with high level programming languages to achieve this, instead of pure sql

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
When making requests on server side you can avoid CORS issues that might come up while trying to pass your server side results through a client side http request. 

- What is CSRF? What is the purpose of the CSRF token?
type of validation to make sure people dont abuse the fact that you can submit forms to other end points than intended. its a unique token generated for form validation to assure the data is going to and coming from the correct place/server/end point.

- What is the purpose of `form.hidden_tag()`?
it hides the CSRF token in html form tag, but is still there when submitted for validating the form.