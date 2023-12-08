"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, contract_type, monthly_salary, hourly_wage, contracts_landed, commission_per_contract):
        self.contract_type = contract_type
        self.monthly_salary = monthly_salary
        self.hourly_wage = hourly_wage
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        if self.contract_type == "salary":
            pay = self.monthly_salary
        elif self.contract_type == "hourly":
            pay = self.hourly_wage * self.contracts_landed
        else:
            raise ValueError("Invalid contract type")

        commission = 0
        if self.commission_per_contract:
            commission = self.commission_per_contract * self.contracts_landed

        return pay + commission

    def __str__(self):
        pay_explanation = ""

        if self.contract_type == "salary":
            pay_explanation = f"on a monthly salary of {self.monthly_salary}."
        elif self.contract_type == "hourly":
            pay_explanation = f"on a contract of {self.hourly_wage} per hour for {self.contracts_landed} hours."
        else:
            raise ValueError("Invalid contract type")

        if self.commission_per_contract:
            pay_explanation += f" Their total pay is {self.get_pay()}."

        return pay_explanation


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("salary", 4000, None, None, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("hourly", 25, 100, None, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("salary", 3000, None, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("hourly", 25, 150, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("salary", 2000, None, None, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("hourly", 30, 120, None, 600)

#print(billie.get_pay(), str(billie))
#print(charlie.get_pay(), str(charlie))
#print(renee.get_pay(), str(renee))
#print(jan.get_pay(), str(jan))
#print(robbie.get_pay(), str(robbie))
#print(ariel.get_pay(), str(ariel))
