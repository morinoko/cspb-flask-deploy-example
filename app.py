from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Felice in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://cspb_example_db_user:BDrT7caz1cGMsEP0Kql2ofs0Dot7krOk@dpg-d7763kdm5p6s739fs2c0-a/cspb_example_db")
    conn.close()
    return 'Database connection successful!'

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://cspb_example_db_user:BDrT7caz1cGMsEP0Kql2ofs0Dot7krOk@dpg-d7763kdm5p6s739fs2c0-a/cspb_example_db")
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
