from datetime import date, datetime, timedelta

today = date.today()
birth_date = input("Please enter your birth date (dd/mm/yy): ")
birth = datetime.strptime(birth_date, "%d/%m/%y").date()

if (today.day, today.month) == (birth.day, birth.month):
    print("Happy birthday")
else:
    next_birthday = date(today.year, birth.month, birth.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth.month, birth.day)
    days_until_birthday = (next_birthday - today).days
    print(f"It is not your birthday. {days_until_birthday} days left until your next birthday.")