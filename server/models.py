from server import db


class Patient(db.Model):
    pid = db.Column(db.String(13), primary_key=True)
    name = db.Column(db.String(40))
    sex = db.Column(db.String(40))
    bp = db.Column(db.Integer)
    pulse = db.Column(db.Integer)
    o2 = db.Column(db.Integer)

    def serialize(self):
        return {
            'personal information': {
                'PID': self.pid,
                'name': self.name,
                'sex': self.sex
            },
            'vitals': {
                'blood pressure': self.bp,
                'oxygen saturation' : self.o2,
                'pulse': self.pulse
            }
        }

    def short_form(self):
        return {
            'PID': self.pid,
            'name': self.name
        }
