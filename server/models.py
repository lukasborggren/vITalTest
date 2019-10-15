from server import db


class Patient(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    firstNames = db.Column(db.String(40))
    lastNames = db.Column(db.String(40))
    gender = db.Columns(db.String(8))
    dateOfBirth = db.Column(db.String(20))

    ehrId = db.Column(db.String(20))
    Personnummer = db.Column(db.String(13))

    pulse = db.Column(db.Integer)
    oxSaturation = db.Column(db.Integer)
    sysBloodPressure = db.Column(db.Integer)  # 45
    diaBloodPressure = db.Column(db.Integer)  # 3

    breathingFreq = db.column(db.Integer)
    alertness = db.column(db.Integer)
    bodyTemp = db.Column(db.Integer)

    #$scope.sendCompositionParams.compositionDataJSON = '{ "ctx/language": "en", "ctx/territory": "US", "ctx/composer_name": "' + $scope.username +'", "ctx/id_namespace": "HOSPITAL-NS", "ctx/id_scheme": "HOSPITAL-NS", "ctx/participation_name": "Dr. Marcus Johnson", "ctx/participation_function": "requester", "ctx/participation_mode": "face-to-face communication", "ctx/participation_id": "199", "ctx/participation_name:1": "Lara Markham", "ctx/participation_function:1": "performer", "ctx/participation_id:1": "198", "ctx/health_care_facility|name": "Hospital", "ctx/health_care_facility|id": "9091", "vital_signs": { "context": [ { "context_detail": [ { "tags": [ "Tags 61" ] } ] } ], "body_temperature": [ { "any_event": [ { "temperature": [ { "|magnitude": 69, "|unit": "°C" } ], "body_exposure": [ { "|code": "at0033" } ], "description_of_thermal_stress": [ "Description of thermal stress 92" ] } ], "site_of_measurement": [ { "|code": "at0055" } ] } ], "blood_pressure": [ { "any_event": [ { "systolic": [ { "|magnitude": 710, "|unit": "mm[Hg]" } ], "diastolic": [ { "|magnitude": 300, "|unit": "mm[Hg]" } ], "mean_arterial_pressure": [ { "|magnitude": 114, "|unit": "mm[Hg]" } ], "pulse_pressure": [ { "|magnitude": 866, "|unit": "mm[Hg]" } ], "comment": [ "Comment 63" ], "position": [ { "|code": "at1001" } ], "sleep_status": [ { "|code": "at1044" } ], "tilt": [ { "|magnitude": 0, "|unit": "°" } ] } ], "cuff_size": [ { "|code": "at1018" } ], "location": [ { "location_of_measurement": [ { "|code": "at0026" } ] } ], "method": [ { "|code": "at1040" } ], "diastolic_endpoint": [ { "|code": "at1012" } ], "device": [ { "device_name": [ "Device name 21" ], "description": [ "Description 64" ], "type": [ "Type 74" ], "size": [ { "count_value": [ 6 ] } ], "manufacturer": [ "Manufacturer 70" ], "date_of_manufacture": [ "2019-02-07T15:55:17.516+01:00" ], "batch_number": [ "Batch number 3" ], "date_of_expiry": [ "2019-02-07T15:55:17.516+01:00" ], "safety_feature": [ { "type_of_feature": [ "Type of feature 78" ], "description": [ "Description 3" ] } ], "comment": [ "Comment 84" ] } ] } ], "body_mass_index": [ { "any_event": [ { "body_mass_index": [ { "|magnitude": 851.3, "|unit": "kg/m2" } ] } ], "method": [ { "|code": "at0008" } ], "formula": [ "Formula 77" ], "comment": [ "Comment 35" ] } ], "height_length": [ { "any_event": [ { "body_height_length": [ { "|magnitude": 742.37, "|unit": "cm" } ], "comment": [ "Comment 6" ], "position": [ { "|code": "at0016" } ] } ] } ], "body_weight": [ { "any_event": [ { "body_weight": [ { "|magnitude": 691.29, "|unit": "kg" } ], "comment": [ "Comment 58" ], "state_of_dress": [ { "|code": "at0011" } ] } ] } ], "pulse": [ { "any_event": [ { "rate": [ { "|magnitude": 97, "|unit": "/min" } ], "comment": [ "Comment 9" ], "position": [ { "|code": "at1001" } ] } ], "method": [ { "|code": "at1020" } ], "description": [ "Description 49" ], "location_of_measurement": [ { "|code": "at0.15" } ] } ], "respirations": [ { "any_event": [ { "rate": [ { "|magnitude": 47, "|unit": "/min" } ], "rhythm": [ { "|code": "at0006" } ], "depth": [ { "|code": "at0018" } ], "description": [ "Description 79" ] } ] } ], "indirect_oximetry": [ { "spo2": [ { "|numerator": 52.53, "|denominator": 68.93 } ], "location_of_measurement_sao2": [ { "|code": "at0063" } ], "comment": [ "Comment 82" ] } ] } }';

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
                "blood_pressure": [
                    {
                        "any_event": [
                            {
                                "systolic": [
                                    {
                                        "|unit": "mm[Hg]",
                                        "|magnitude": self.sysBloodPressure
                                    }
                                ],
                                "diastolic": [
                                    {
                                        "|unit": "mm[Hg]",
                                        "|magnitude": self.diaBloodPressure
                                    }
                                ],
                                "position": [
                                    {
                                        "|code": "at1001",
                                        "|value": "Sitting"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            'pulse': self.pulse,
            'oxygen_Saturation': self.oxSaturation,
            'breathing_Frequency': self.breathingFreq,
            'alertness': self.alertness
        }

    def short_form(self):
        return {
            'pid': self.Personnummer,
            'firstNames': self.firstNames,
            'lastNames': self.lastNames
        }
