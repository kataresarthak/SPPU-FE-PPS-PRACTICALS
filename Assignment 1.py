basic_pay=float(input("Enter the Basic Pay of the Employee: "))

hra = 0.1*basic_pay
ta = 0.05*basic_pay

gross_salary=basic_pay + hra + ta

professional_tax=0.02*gross_salary

net_salary=gross_salary-professional_tax

print(f"Gross Salary: {gross_salary}")
print(f"Professional Tax: {professional_tax}")
print(f"Net Salary: {net_salary}")
