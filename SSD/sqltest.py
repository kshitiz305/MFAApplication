# sqltest.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sql5495299:hz7bDRYNPh@sql5.freesqldatabase.com:3306/sql5495299"

db.init_app(app)

@app.route('/')
def index():

    sql_cmd = """
        select *
        from sql5495299.testusers;
        """

    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    return 'ok'


if __name__ == "__main__":
    app.run()