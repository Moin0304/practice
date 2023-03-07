# heading = ["customer_id", "customer_name", "place"]
# customer_details=[("1", "moin", "bengaluru"), ("2", "ramesh", "karnataka"), ("3", "madhu", "hyderabad")]
# customer_detail=[["10", "moin", "bengaluru"], ["20", "ramesh", "karnataka"], ["30", "madhu", "hyderabad"]]
# with open ("test.csv", "w") as fp:
#     fp.write(",".join(heading)+ '\n')
#     for row in customer_details:
#         fp.write(",".join(row) + '\n')
#     for row in customer_detail:
#         fp.write(",".join(row) + '\n')
    

a = 10
b = a
c = 10

print(id(a), id(b), id(c))

print(a is b)
print(a is c)