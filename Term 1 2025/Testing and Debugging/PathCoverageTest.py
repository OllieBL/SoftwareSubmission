def ticket_price(age):
    if age < 5:
        return "Free"
    elif 5 <= age <= 17:
        return "$5"
    elif 18 <= age <= 64:
        return "$10"
    else:
        return "Senior Discount - $7"

# TODO: Write test cases for all paths

print(ticket_price(4))
print(ticket_price(5))
print(ticket_price(18))
print(ticket_price(65))