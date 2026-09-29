#AB 7th functions

income=float(input("what is your monthly income"))
rent=float(input('what is your rent'))
utilities=float(input('what is your montthly utillities'))
groceries=float(input("what is your monthly income"))
transportation=float(input('what is your rent'))
savings=income*1
                                                                                                                                     
print(f"your rent is ${rent:.2f}that is{calc_percent(rent,utilities)}%of your utillities")                                        
print(f"your income is ${income:.2f}that is{calc_percent(income,utilities)}%of your utillities")                    
print(f"your utillities is ${utilities:.2f}that is{calc_percent(utilities,utilities)}%of your utillities")
print(f"your groceries is ${groceries:.2f}that is{calc_percent(groceries,utilities)}%of your utillities")
print(f"your transportation is ${transportation:.2f}that is{calc_percent(transportation,utilities)}%of your utillities")

def calc_percent(income, bill):
    return round(bill/income *100)

def stupid_proof(money):
    amount=float