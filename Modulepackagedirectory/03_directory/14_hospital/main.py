from patients.management import patient_details
from doctors.management import doctor_details
from billing.charges import calculate_bill
from medical_records.records import create_record

patient = patient_details(1, "Asha", 21)
doctor = doctor_details(11, "Dr. Rao", "General Medicine")
record = create_record(1, "Seasonal fever", "Rest and prescribed medicine")
bill = calculate_bill(500, 800, 350)
print("Patient:", patient)
print("Doctor:", doctor)
print("Medical record:", record)
print("Total bill: Rs.", bill)
