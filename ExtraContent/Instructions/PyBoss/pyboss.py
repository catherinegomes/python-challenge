import csv, os

file_to_load=os.path.join("../PyBoss","employee_data.csv")
from datetime import datetime

with open(file_to_load) as data_file:
    reader = csv.DictReader(data_file)

    for row in reader:
        name = row["Name"]
        firstname = name.split(" ")
        print(firstname)

        dob = row["DOB"]
        new_dob=datetime.strptime(dob,'%Y-%m-%d')
        new_dob=dob.strftime("%m/%d/%Y")

        ssn = row["SSN"]
        new_ssn = '***-**-' + row["SSN"][-4:]

        