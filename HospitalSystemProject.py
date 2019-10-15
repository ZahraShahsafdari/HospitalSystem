#This is a system for a hospital

class Person(object):
    def __init__(self, firstname, lastname, position):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position

class Doctor(Person):
    def __init__(self, speciality, doctorward):
        super().__init__(firstname, lastname, position)
        self.speciality = speciality
        self.doctorward = doctorward

    def operation_list(self):
        patients = []
        for p in self.Operation_room:
            if Patient.status == 'hospitalized':
                patients.append(p.Patient)
                print(patients)
    
    def __str__(self):
        return (patients)

class Nurse(Person):
    def __init__(self, nurseward):
        super().__init__(firstname, lastname, position)
        self.nurseward = nurseward

class Patient(Person):
    def __init__(self, disease, status, patientroom): 
        super().__init__(firstname, lastname, position)
        self.disease = disease
        self.status = status
        self.patientroom = patinetroom

class Operation_room(Doctor):
    def __init__(self, patientname, roomnum, time):
        super().__init__(speciality, doctorward)
        self.patientname = patientname
        self.roomnum = roomnum
        self.time = time

    def patient_admission(self):
        pAdmission = []
        for pa in self.Operation_room:
            pAdmission.append(pa.Operation_room)
            print(pAdmission)
            
    def __str__(self):
        return (pAdmission)



class Drug(Patient):
    def __init__(self, drugname, drugUsage):
        super().__init__(disease, status, patientroom)
        self.drugname = drugname
        self.drugUsage = drugUsage


p1 = Patient('Zahra','Shahi','patient','appendix','hospitalized','5')
p2 = Patient('Niusha','Ahmadi','patient','headache','visited','none')
p3 = Patient('Parisa','Yousei','patient','Cyst','hospitalized','4')

d1 = Doctor('Hosein','Safdari','doctor','appendix','surgery')
d2 = Doctor('Hamid','Ahmadi','doctor','cyst','surgery')