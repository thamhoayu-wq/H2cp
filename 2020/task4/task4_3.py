import flask
import csv

app = Flask(__name__)

@app.route('/')

def index():
    record = []

    with open("people.txt",'r') as file:

        reader = csv.reader(file)

        for line in reader:

            full_name = line[0]
            date_of_birth = line[1]
            identity = line[2]

            name = full_name.replace(" ", "")

            month = date_of_birth[5:7]
            date = date_of_birth[8:10]

            screen_name = name + month + date

            if identity == "Staff":
                screen_name += "Staff"

            record.append([full_name, screen_name, identity])
    file.close()

    return render_template("index.html", record=record)

def __name__ == "__main__":
    app.run(debug=True)
