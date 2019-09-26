from flask import render_template, jsonify
from server import app
from server.models import Patient


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/api')
def api():
    patient = Patient.query.filter_by(pid='19921030-0412').first()
    return jsonify(patient.serialize())


@app.route('/api/<string:patient_pid>')
def get_patient(patient_pid):
    patient = Patient.query.filter_by(pid=patient_pid).first()
    return jsonify(patient.serialize())

@app.route('/api/patient_list')
def patient_list():
    patients = Patient.query.all()
    patients = [p.short_form() for p in patients]
    return jsonify(patients)
