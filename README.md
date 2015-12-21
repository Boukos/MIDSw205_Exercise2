# MIDS w205: Exercise 2
This is the code for Exercise 2. Here are the directions on how to run the code. This codebase assumes that ucbw205_complete_plus_postgres_PY2.7 AMI is being run, with all the proper postgres, python2.7 (with all the libraries, ie tweepy and psycopg2), and streamparse setup, done via the EasyButton instructions and the Lab 9 setup instructions. First things first, clone repo into root directory:

```
git clone https://github.com/kyungguyeo/exercise2.git
```

## Setting up the DB
Follow these commands to create the tcount database, connect to it, then create the tweetwordcount table; enter them line by line:
```
su - postgres
psql
CREATE DATABASE Tcount;
\connect tcount;
CREATE TABLE Tweetwordcount (word varchar(255) NOT NULL PRIMARY KEY, count integer);
```
Press ctrl+D twice to go back to the root directory.

## Running the Twitter Word Count Stream
To run the streamparse, from the root directory:
```
cd exercise2
cd EX2Tweetwordcount
sparse run
```
You should see logs of words being counted - every time it's counted, the count is being entered into the db.

## Getting Some Data
To get a list of words and their counts, go into EX2Tweetwordcount, then:
```
python finalresults.py
```
This list of words is alphabetized in ascending order in the ASCII way: http://support.ecisolutions.com/doc-ddms/help/reportsmenu/ascii_sort_order_chart.htm

If you want to see counts of specific word instead of the whole schlop of words, then simply add those words as arguments after calling the script:
```
python finalresults.py hello goodbye 
```

If you want to specify the list of words you see to a list of counts, then:
```
python histogram k1 k2
```
This will give you a list of words with a count of at least k1 and less than k2. 

## Analysis

Plot.R provides the R code that queries the Psql database to create the visualization, which is saved in Plot.png.

The data for the plot is from a 20 minute stream, administered at 11:42 AM on 12/12/15.