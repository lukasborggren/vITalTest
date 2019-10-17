from server import db


class Patient(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    firstNames = db.Column(db.String(40))
    lastNames = db.Column(db.String(40))
    gender = db.Column(db.String(8))
    dateOfBirth = db.Column(db.String(20))

    ehrId = db.Column(db.String(20))
    Personnummer = db.Column(db.String(13))

    pulse = db.Column(db.Integer)
    oxSaturation = db.Column(db.Integer)
    sysBloodPressure = db.Column(db.Integer)
    diaBloodPressure = db.Column(db.Integer)

    breathingFreq = db.Column(db.Integer)
    alertness = db.Column(db.String(10))
    bodyTemp = db.Column(db.Float)

    def serialize(self):
        return {
            'demographics': {
                'id': self.id,
                'firstNames': self.firstNames,
                'lastNames': self.lastNames,
                'gender': self.gender,
                'dateOfBirth': self.dateOfBirth,
                'additionalInfo': {
                    'ehrId': self.ehrId,
                    'Personnummer': self.Personnummer
                }
            },
            'vital_signs': {
                'body_temperature': [
                    {
                        'any_event': [
                            {
                                'temperature': [
                                    {
                                        '|magnitude': self.bodyTemp,
                                        '|unit': '°C'
                                    }
                                ]
                            }
                        ]
                    }
                ],
                'blood_pressure': [
                    {
                        'any_event': [
                            {
                                'systolic': [
                                    {
                                        '|unit': 'mm[Hg]',
                                        '|magnitude': self.sysBloodPressure
                                    }
                                ],
                                'diastolic': [
                                    {
                                        '|unit': 'mm[Hg]',
                                        '|magnitude': self.diaBloodPressure
                                    }
                                ],
                                'position': [
                                    {
                                        '|code': 'at1001',
                                        '|value': 'Sitting'
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            'pulse': self.pulse,
            'oxygen_saturation': self.oxSaturation,
            'breathing_frequency': self.breathingFreq,
            'alertness': self.alertness
        }

    def short_form(self):
        return {
            'firstNames': self.firstNames,
            'lastNames': self.lastNames,
            'pid': self.Personnummer,
            'ehrId': self.ehrId
        }


class Staff(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20))
    firstNames = db.Column(db.String(40))
    lastNames = db.Column(db.String(40))
    position = db.Column(db.String(20))

    def serialize(self):
        return {
            'firstNames': self.firstNames,
            'lastNames': self.lastNames,
            'position': self.position
        }
