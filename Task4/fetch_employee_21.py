# 21.Imagine a scenario where you are required to fetch the employee names who joined after 02 Sep 2022 and
#  location is Hyderabad
# empIoyee_ data = {
# “priya”:{
# “location”	: “Hyderabad” “joining_date '. “05/09/2022”
# “mahi”. (
# “raja”: (
# “location”	: “Bangalore” “joining_date '. “20/02/2023”
# “location”	: “Hyderabad” “joining_date '. “14/10/2022”
# “prabhu”:(
# “location”	: “Bangalore” “joining_date '. “02/01/2023”

def fetch_location(employee_data):
    employee_name = []
    for k,v in employee_data.items():
        if v['location'] == 'Hyderabad':
            day,month,year = v['joining_date'].split('/')
            if year > '2022' :
                employee_name.append(k)
            elif year == '2022' :
                if (month == '09' and day > '02') or (month > '09'):
                    employee_name.append(k)
               
    return employee_name
        
employee_data = {'priya':{'location':'Hyderabad','joining_date':'05/09/2022'},
'mahi':{'location':'Bengaluru','joining_date':'05/09/2021'},
'prabhu':{'location':'Bengaluru','joining_date':'02/01/2023'},
'raja':{'location':'Hyderabad','joining_date':'20/02/2023'}}
print(fetch_location(employee_data))