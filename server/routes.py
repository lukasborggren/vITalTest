from flask import render_template, jsonify, request
from server import app
from server import db
from server.models import Patient, Staff


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ehr/<string:patient_ehr>', methods=['GET'])
def get_patient_ehr(patient_ehr):
    patient = Patient.query.filter_by(ehrId=patient_ehr).first()
    return jsonify(patient.serialize())


@app.route('/api/pid/<string:patient_pid>', methods=['GET'])
def get_patient_pid(patient_pid):
    patient = Patient.query.filter_by(Personnummer=patient_pid).first()
    return jsonify(patient.serialize())


# Expected data format: { "pulse": 80, "oxygen_saturation": 40, "blood_pressure_systolic": 127,
# "blood_pressure_diastolic": 67, "breathing_frequency": 17, "alertness": "awake", "body_temperature": 37.3 }
@app.route('/api/update/<string:patient_ehr>', methods=['PUT'])
def update_patient(patient_ehr):
    patient = Patient.query.filter_by(ehrId=patient_ehr).first()

    patient.pulse = request.json['pulse']
    patient.oxSaturation = request.json['oxygen_saturation']
    patient.sysBloodPressure = request.json['blood_pressure_systolic']
    patient.diaBloodPressure = request.json['blood_pressure_diastolic']
    patient.breathingFreq = request.json['breathing_frequency']
    patient.alertness = request.json['alertness']
    patient.bodyTemp = request.json['body_temperature']

    db.session.commit()


# Expected data format: { "username": "useruser", "password": "passpass" }
@app.route('/api/authenticate', methods=['GET'])
def get_staff_authorization():
    staff = Staff.query.filter_by(username=request.json['username']).first()
    if staff.password == request.json['password']:
        return jsonify(staff.serialize())
    else:
        return '{}'


@app.route('/patient_list', methods=['GET'])
def patient_list():
    patients = Patient.query.all()
    patients = [p.short_form() for p in patients]
    return jsonify(patients)


@app.route('/staff_list', methods=['GET'])
def staff_list():
    staff = Staff.query.all()
    staff = [s.short_form() for s in staff]
    return jsonify(staff)
