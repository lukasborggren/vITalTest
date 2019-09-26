from server import db
from server.models import Patient


def addPatient(pid, name, sex, bp, pulse, o2):
    db.session.add(Patient(pid=pid, name=name, sex=sex, bp=bp, pulse=pulse, o2=o2))


db.reflect()
db.drop_all()
db.create_all()

addPatient('19921030-0412', 'John Doe', 'male', 90, 80, 98)
addPatient('19870108-0766', 'Jane Doe', 'female', 105, 70, 100)
addPatient('19600721-8418', 'John Doe sr.', 'male', 140, 130, 91)

db.session.commit()


