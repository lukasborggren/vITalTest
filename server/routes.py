from flask import render_template, jsonify
from server import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    return jsonify({
        'personal information': {
            'name' : 'john doe',
            'sex' : 'male',
            'PID' : '19921030-0412'
        },
        'vitals' : {
            'pulse': 100,
            'blood pressure': 120,
            'oxygen saturation': 98
        }
    })