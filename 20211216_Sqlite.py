 
import sqlite3

# (1) Connection object that represents our database

conn = sqlite3.connect('employee.db')

# (2) Create cursor variable that allows us to execute SQL commands

c = conn.cursor()

# (3) Create table that holds an employees' records (1) firstname (2) lastName (3) Pay
# command created in triple quote """ <docstring>

##c.execute("""CREATE TABLE employees(
##            first TEXT,
##            last TEXT,
##            pay INTEGER
##    )""")


# ***** remember >> comment out code that has been executed or you get an error


# (4) Insert data into the table employees
# c.execute("INSERT INTO employees VALUES ('Diya', 'Nair', 99999)")

# (5) Edit table entries
c.execute ("SELECT * FROM employees WHERE last='Mathur'")

# (6) Execute commands for DBase - Call in the selected data
c.fetchone()

# Print the selected data
print(c.fetchone())


# (7) Close the connection
conn.commit()

conn.close()



# -------------------------------
# For adding many records at once

# Create a set of tuples

many_customers = [
                    ('', '', ''),
                    ('', '', ''),
                    ('', '', '')
                  ]
c.executemany("INSERT INTO employees VALUES (?,?,?)", many_customers) # here <?> are SQL placeholders

# -------------------------------
# Retreive the results

c.execute("SELECT * FROM employees")
c.fetchone()                         # gets last one record - can specify add numer c.fetchone() [3]
c.fetchmany()                        # gets many records at once
c.fetchall ()                        # gets all records

print (c.fetchall())


# -------------------------------
# Present / print results

print("NAME" + "\t\t EMAIL")         # list data separated by tabs </t>
item = c.fetchall()
for item in items:
    print (item[0] + "| " + item[1] + "\t " + item [2])

# -------------------------------
# Primary key id -- unique id for each record

c.execute("SELECT rowid, * FROM employees")      # rowid brings out the unique id SQL puts for each row


# -------------------------------
# Fetching specific records using WHERE / LIKE

c.execute("SELECT rowid, * FROM employees WHERE last_name = 'Elder'")

c.execute("SELECT rowid, * FROM employees WHERE age > 32)

c.execute("SELECT rowid, * FROM employees WHERE name LIKE 'Br%'")   # name starts with "Br"


# -------------------------------
# Update records -- use doc string """ """

c.execute("""UPDATE employees SET first_name = 'Bob'
            WHERE last_name = 'Elder'

        """)
conn.commit()

# or to target specific records

c.execute("""UPDATE employees SET first_name = 'Bob'
            WHERE rowid = 1

        """)
conn.commit()


# -------------------------------
# Delete records

c.execute("DELETE from employees WHERE rowid = 6")   # deletes specific record


# -------------------------------
# Ordering results -- ORDER BY

c.execute ("SELECT FROM employees ORDER BY rowid DESC")   #order by DESCending / last_name


          
# -------------------------------
# And / or -- allows us to add more conditions

c.execute("SELECT rowid, * FROM employees WHERE last_name LIKE 'Br%' AND rowid = 3")

c.execute("SELECT rowid, * FROM employees WHERE last_name LIKE 'Br%' OR rowid = 3")



# -------------------------------
# Limiting Results

c.execute("SELECT rowid, * FROM employees LIMIT 2"  # -- gives just 2 from results


# -------------------------------
# Deleting a Table

c.execute("DROP TABLE employees")
conn.commit


# ===============================
## Creating an App

import sqlite3

# Function - query the database and return all records
def show_all():

    # connect to database
    conn = sqlite3.connect('employees.db')

    # create a cursor
    c = conn.cursor()

    # query the database
    c.execute("SELECT rowid, * FROM employees")
    items = c.fetchall()
    for item in items:
        print(item)

    # commit the commands - wrap it up
    conn.commit()
    
    # close the connection
    conn.close()
    
## -- this function cab be called from within the database created

import database
database.show_all()

## call it from the terminal line

python our_app.py


# ===============================
## Function to Add a record function to our app

# add a new record to the table
def add_one(first, last, email):

    # connect to database
    conn = sqlite3.connect('employees.db')

    # create a cursor
    c = conn.cursor()

    # add a record to the database
    c.execute("INSERT INTO employees VALUES (?,?,?)", (first, last,email))

    # commit and close the connection
    conn.commit()
    conn.close()

## execute the function
import database
database.add_one("Diya", "Nair", "dnair@gmail.com"))
databae.show_all()

    
# ===============================
## Function to Delete a record from our database

def del_one(id):

    # connect to database and create a cursor
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    # delete a record from the database
    c.execute("DELETE FROM employees WHERE rowid= (?)", id)

    # commit and close the connection
    conn.commit()
    conn.close()

## delete record by using the rowid as a _strin_ !
database.del_one('6')



# ===============================
## Function to add multiple records

def add_many(list):

    # connect to database and create a cursor
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    # add multiple records to the database
    c.executemany ("INSERT INTO employees VALUES(?,?,?)", (list) )

    # commit and close the connection
    conn.commit()
    conn.close ()

## call in the function using -
## add many records

stuff = [
    ("Ram","Sundaram","rs@gmail.com")
    ("Shyam","Ponnappa","shyampo@wierd.com")
    ("Amar","Ujala","aujala@party.com")
    ]

database.add_many(stuff)

database.show_all()


# ===============================
## Where clause

def email_lookup(email):

    # connect to the databse an create a cursor
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    # look up a given email id -- remember that a tuple is added with a comma
    c.execute("SELECT rowid * FROM employees WHERE email = (?)", (email,))

    for item in items:
        print(item)

    # commit and close the connection
    conn.commit()
    conn.close()

# database email lookup
database.email_lookup("aujala@party.com")








