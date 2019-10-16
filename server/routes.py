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


@app.route('/api/ehr/<string:patient_ehr>')
def get_patient_ehr(patient_ehr):
    patient = Patient.query.filter_by(ehrId=patient_ehr).first()
    return jsonify(patient.serialize())


@app.route('/api/pid/<string:patient_pid>')
def get_patient_pid(patient_pid):
    patient = Patient.query.filter_by(Personnummer=patient_pid).first()
    return jsonify(patient.serialize())


@app.route('/api/patient_list')
def patient_list():
    patients = Patient.query.all()
    patients = [p.short_form() for p in patients]
    return jsonify(patients)
