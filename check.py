from datetime import datetime
from day_calculator import calculate_day_type

with open("a_week", "r") as a_week:
    for line in a_week:
        day, required = line.split(" ")
        date = datetime.strptime(day, '%Y-%m-%d')
        calculated = calculate_day_type(date, "b")
        if required.strip() != calculated.strip():
            print("Type of day: ", date.date(), "should be: ", required.strip(), "instead it was: ", calculated.strip())
