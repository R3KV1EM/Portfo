from flask import Flask, render_template, request, url_for, redirect
import csv
from csv import writer
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect("/thank.html")
        except:
            return "Didn't save to database"
    else:
        return "NE YSPEH"





# flask --app /home/archy/PycharmProjects/pythonProject/venv/webserver/server run
#  export FLASK_APP=/home/archy/PycharmProjects/Gamma/venv/server.py
#  flask run --debug
