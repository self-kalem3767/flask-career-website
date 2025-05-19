from flask import Flask, render_template
from flask import jsonify


# Web Development with Python Flask
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Lahore, Pakistan',
        'salary': 'Rs.10,000, 00',
        'job-type': 'onsite'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Islamabad, Pakistan',
        'salary': 'Rs. 15,000, 00',
        'job-type': 'onsite'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Faslabad, Pakistan',
        'job-type': 'Remote'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$12000',
        'job-type': 'Remote'
    }
]

@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS, company_name='Devsinc')

@app.route('/api/jobs')
def job_list():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(debug=True)



