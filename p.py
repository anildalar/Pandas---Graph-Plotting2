import sqlite3

con = sqlite3.connect('./db.sqlite3')


cur = con.cursor()

for row in cur.execute('SELECT * FROM populations'):
    print(row)

for x in range(3):
    cn = input('Enter the country name ')
    yr = input('Enter the year ')
    pibillion =input('Enter the population in billions ')

    cur.execute("INSERT INTO populations VALUES (NULL,'{}','{}','{}')".format(cn, yr,pibillion ))
    # Save (commit) the changes
    con.commit()
#cur.execute("CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)")




