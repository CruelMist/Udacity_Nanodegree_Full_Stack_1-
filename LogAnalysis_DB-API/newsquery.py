#!/usr/bin/env python3
import psycopg2
DBNAME = "news"

ques1 = "What are the most popular three articles of all time?"

ans1 = """
        SELECT articles.title,count(*) AS shows
        FROM articles, log
        WHERE log.path='/article/'||articles.slug
        GROUP BY articles.title
        ORDER BY shows DESC
        LIMIT 3;
      """

ques2 = "Who are the most popular article authors of all time?"

ans2 = """
        SELECT authors.name, count(*) as auth_views
        FROM articles, authors, log
        WHERE articles.author=authors.id AND
        log.path='/article/'||articles.slug
        GROUP BY authors.name
        ORDER BY auth_views DESC;
     """

ques3 = "On which days did more than 1% of requests lead to errors?"

ans3 = """
        WITH day_req AS (
        SELECT time::date as day, count(*)
        FROM log
        GROUP BY day
        ORDER BY day ),
        day_err AS (
        SELECT time::date AS day, count(*)
        FROM log
        WHERE status <> '200 OK'
        GROUP BY day
        ORDER BY day ),
        err_rate AS (
        SELECT day_req.day, day_err.count::float / day_req.count::float * 100
        AS err_fin
        FROM day_req, day_err
        WHERE day_req.day = day_err.day )
        SELECT * FROM err_rate WHERE err_fin > 1;
    """

print("Results:"+"\n")


def query1(statement):
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print ("Unable to connect to the database")
    c = db.cursor()
    c.execute(statement)
    var1 = c.fetchall()
    db.close()
    return var1

print(ques1)
result1 = query1(ans1)
count = 0
for i in result1:
    count += 1
    title = i[0]
    views = '" -- ' + str(i[1]) + " views"
    print(str(count) + '. ' + '"' + title + views)
print("\n")


def query2(statement):
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print ("Unable to connect to the database")
    c = db.cursor()
    c.execute(statement)
    var2 = c.fetchall()
    db.close()
    return var2

print(ques2)
result2 = query2(ans2)
count = 0
for i in result2:
    count += 1
    author = i[0]
    views = '" -- ' + str(i[1]) + " views"
    print(str(count) + ". " + '"' + author + views)
print("\n")


def query3(statement):
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print ("Unable to connect to the database")
    c = db.cursor()
    c.execute(statement)
    var3 = c.fetchall()
    db.close()
    return var3


print(ques3)
result3 = query3(ans3)
for i in result3:
    date = i[0].strftime('%B %d, %Y')
    err = str(round(i[1], 2))
    print(date + ' -- ' + err + "%" + " errors")
