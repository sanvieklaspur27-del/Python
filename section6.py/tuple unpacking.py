#tuple unpacking
stock_prices=[('APPLE',200),('GOOGLE',400)]
for item in stock_prices:
    print(item)  #()
                 #()
for ticker,price in stock_prices:
    print(ticker)    #apple,goggle
    print(price+(0.1*price))   #200,400 10%increase

work_hours=[('abby',100),('biily',400),('cassie',800)]
def employee_check(work_hours):
    current_max=0
    employee_of_month=''
    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee
        else:
            pass
    #return
    return(employee_of_month,current_max)
print(employee_check)
print(employee_check(work_hours))  #('cassie',800)

result=employee_check(work_hours)  # max of works wrk
name,hours=employee_check(work_hours)
print(result)
print(name)
print(hours)