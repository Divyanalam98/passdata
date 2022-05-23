import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    _id = request.form['_id']
    employee_name = request.form['employee_name']
    department = request.form['department']
    working_from_office = request.form['working_from_office']
    role = request.form['role']
    shared = [_id, employee_name, department, working_from_office, role]
    fp = open("/Users/pbchandra1/Documents/passdata/venv/shared.pkl", "wb")
    pickle.dump(shared, fp)
    return render_template('pass.html', _id=_id, employee_name=employee_name, department=department,
                           working_from_office=working_from_office, role=role)

if __name__ == '__main__':

    app.run(debug=True)

