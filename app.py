from flask import Flask
import psycopg2

DATABASE_URL = "postgresql://cspb_example_db_user:BDrT7caz1cGMsEP0Kql2ofs0Dot7krOk@dpg-d7763kdm5p6s739fs2c0-a/cspb_example_db"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Felice in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect(DATABASE_URL)
    conn.close()
    return 'Database connection successful!'

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return 'Table created successfully!'

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return 'Basketball Table Populated'

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    cur.close()
    conn.close()

    response_string = ''
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for attribute in player:
            response_string += f"<td>{attribute}</td>"
        response_string += "</tr>"
    response_string += "</table>"
    return response_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Basketball;')
    conn.commit()
    cur.close()
    conn.close()
    return 'Basketball Table Successfully Dropped'
