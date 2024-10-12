import random

def date():
    days = list(range(1,31))
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]

    rand_date = []

    for i in range(20):
        month = random.choice(months)
        if month in ["Jan","Mar","May","Jul","Aug","Oct","Dec"]:
            day = random.randint(1,31)
        elif month in ["Apr", "Jun", "Sept", "Nov"]:
            day = random.randint(1, 30)
        elif month == "Feb":
            day = random.randint(1, 29)
        rand_date.append(f"{day} {month}")

    return rand_date

randomDate = date()
ourMonth = input("enter month: ")

count = 0
for m in randomDate:
    if ourMonth in m:
        count += 1

print(randomDate)
print("к-кість записів: ",count)