import sqlite3

db = sqlite3.connect('Registration')
rs = db.cursor()


#rs.execute('''create table Register(name varchar(50), email varchar(100), passwd varchar(10))''')
#db.commit()

rs.execute('''insert into register values('logan', '@gmail.com', 'logan1234#' )''')
db.commit()


rs.execute('select * from register')
for i in rs:
    print(i)