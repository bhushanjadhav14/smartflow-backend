SmartFlow Database Setup Guide



1\. Create PostgreSQL Database



Create a database:

smart flow db





2\. Create Tables



Run the SQL commands from:

schema.sql



This creates:

\- traffic\_features table

\- traffic\_target table





3\. Import Dataset



Use the CSV files located in:

data/

\- delhi\_traffic\_features.csv

\- delhi\_traffic\_target.csv





Import traffic features:



COPY traffic\_features

FROM 'data/delhi\_traffic\_features.csv'

DELIMITER ','

CSV HEADER;





Import traffic target:



COPY traffic\_target

FROM 'data/delhi\_traffic\_target.csv'

DELIMITER ','

CSV HEADER;





4\. Verify Data



Run:

SELECT COUNT(\*) FROM traffic\_features;



Expected:

4000 rows





Run:

SELECT COUNT(\*) FROM traffic\_target;



Expected:

4000 rows





Database Tables



traffic\_features

\- Trip details

\- Distance

\- Average speed

\- Traffic density





traffic\_target

\- Travel time in minutes

