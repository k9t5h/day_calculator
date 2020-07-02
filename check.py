from datetime import datetime
from day_calculator import calculate_day_type

with open("result", "r") as result:
    for line in result:
        day, required = line.split(" ")
        date = datetime.strptime(day, '%Y-%m-%d')
        calculated = calculate_day_type(date, "b")
        if required.strip() != calculated.strip():
            print("Type of day: ", date.date(), "should be: ", required.strip(), "instead it was: ", calculated.strip())
