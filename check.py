from datetime import datetime
from day_calculator import calculate_day_type

with open("results", "r") as results:
    error_cnt = 0
    for line in results:
        day, required = line.split(" ")
        date = datetime.strptime(day, '%Y-%m-%d')
        calculated = calculate_day_type(date)
        try:
            if required.strip() != calculated.strip():
                print("Type of day: ", date.date(), "should be: ", required.strip(), "instead it was: ", calculated.strip())
                error_cnt += 1
        except Exception as e:
            print(e)
            error_cnt += 1
    if error_cnt > 0:
        print("finished with " + str(error_cnt) + " errors")
    else:
        print("SUCCESS")
