#import library to connect to postgresql
import psycopg2


#connect to dvdrental db
conn = psycopg2.connect(
    host="127.0.0.1", #localhost
    port="5432",
    dbname="dvdrental",
    user="postgres",
    password="postgres")

print("Opened database successfully")

#create cursor object
cur = conn.cursor()

# Menghitung jumlah film dengan tema astronout
cur.execute('''
SELECT COUNT(*) 
FROM film
WHERE description LIKE "_stronaut%";''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

# Menghitung jumlah film yang ratingnya 'R' dan replacement costnya antara 5-15
cur.execute('''
SELECT COUNT(*) 
FROM film
WHERE rating = 'R'
AND replacement_cost
BETWEEN 5 AND 15;''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

# Menghitung jumlah film yang ratingnya 'R' dan replacement costnya antara 5-15
cur.execute('''
SELECT COUNT(*) 
FROM film
WHERE rating = 'R'
AND replacement_cost
BETWEEN 5 AND 15;''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

# Melihat jumlah transaksi dan total nilai transaksi yang ditangani oleh tiap staff
cur.execute('''
SELECT staff_id, COUNT(payment_id), SUM(amount)
FROM payment
GROUP BY staff_id;''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

# Menghitung rata-rata replacement cost film berdasarkan ratingnya
cur.execute('''
SELECT rating, AVG(replacement_cost) AS avg_replacement_cost
FROM film
GROUP BY rating;''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

# Melihat nama, email, dan total nilai transaksi 5 customer teratas
cur.execute('''
SELECT first_name, last_name, email, SUM(amount) AS spend_amount
FROM customer AS c
INNER JOIN payment AS p
ON c.customer_id = p.customer_id
GROUP BY first_name,last_name,email
ORDER BY spend_amount DESC
LIMIT 5;''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

# Menghitung jumlah inventory film di setiap store
cur.execute('''
SELECT film_id, store_id, COUNT(inventory_id) AS movie_amount
FROM inventory
GROUP BY film_id, store_id
ORDER BY film_id ASC;''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

# Menghitung jumlah inventory film di setiap store
cur.execute('''
SELECT film_id, store_id, COUNT(inventory_id) AS movie_amount
FROM inventory
GROUP BY film_id, store_id
ORDER BY film_id ASC;''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

# Melihat nama dan email dari customer yang telah melakukan minimal 40 kali transaksi 
cur.execute('''
SELECT first_name, last_name, email
FROM customer AS c
INNER JOIN payment AS p
ON c.customer_id = p.customer_id
GROUP BY first_name,last_name,email
HAVING COUNT(amount) >= 40;''')
rows = cur.fetchall()
for row in rows:
   print("date = ", row[0])
   print("sale = ", row[1],"\n")

print("Operation done successfully")

#close connection
conn.close()


