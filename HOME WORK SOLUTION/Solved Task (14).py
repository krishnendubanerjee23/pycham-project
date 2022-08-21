# 1 . Write a program to insert a record in sql table via api
# 2 .  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api
# 5 . All the above questions you have to answer for mongo db as well .

from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

@app.route('/abc',methods=['GET', 'POST'])
def test():
    if(request.method=='POST'):

        client = pymongo.MongoClient("mongodb+srv://krishnendubanerjee23:Kolkata1@cluster0.7ju5nnf.mongodb.net/?retryWrites=true&w=majority")
        db = client.MangoApi

        data = {
            "item": request.json['item1'],
            "qty": request.json['qty1'],
            "size": {"h": request.json['hight'], "w": request.json['Weight'], "uom": request.json['volum']},
            "status": request.json['status']
            }

        db1 = client['API']
        collections = db1['MangoApi']
        collections.insert_one(data)

        return jsonify((print(db)))

if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost", user='root', passwd="Jaijai1@11")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.tasktable  values(%s , %s)", (name, number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))


@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("update taskdb.tasktable set number = number + 500 where name = %s ", (get_name,))
        mydb.commit()
        return jsonify(str("updated successfully"))


@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from taskdb.tasktable where name = %s", (name_del,))
        mydb.commit()
        return jsonify(str("deleted successfully"))


@app.route("/fetch", methods=['POST', 'GET'])
def fetch_data():
    cursor.execute("select * from taskdb.tasktable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))


if __name__ == '__main__':
    app.run()

    {
        "name": "nizam",
        "number": 6867
    }

from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("")
database = client['taskdb']
collection = database['taskcollection']


@app.route("/insert/mongo", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("succefully inserted "))


if __name__ == '__main__':
    app.run()

from flask import Flask, request

app = Flask(__name__)


@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get('mail_id')

    return "this is my first function for get {} {} {}".format(get_name, mobile_number, mail_id)


@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="Jaijai1@11", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5002)