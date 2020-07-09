from datetime import datetime, timedelta


SCHOOL = "school"
NOT_SCHOOL = "not-school"


def calculate_school_days(date, date_range, start_mon, start_thu):
    school_days = []
    tw_Mon = date_range[start_mon::28]
    for date in tw_Mon:
        school_days.append(date)
        school_days.append(date + timedelta(days=1))
        school_days.append(date + timedelta(days=2))
    tw_Thu = date_range[start_thu::28]
    for date in tw_Thu:
        school_days.append(date)
        school_days.append(date + timedelta(days=1))
    return school_days


def calculate_day_type(date):
    start = datetime(2020, 7, 20)
    date_list = [start + timedelta(days=x) for x in range(40)]
    week_number = date.isocalendar()[1]
    if week_number % 2 == 0:
        school_days = calculate_school_days(date, date_list, 0, 17)
        if date in school_days:
            return f"TW week for group A: {SCHOOL}"
        else:
            return f"TW week for group A: {NOT_SCHOOL}"
    else:
        school_days = calculate_school_days(date, date_list, 7, 24)
        if date in school_days:
            return f"TW week for group B: {SCHOOL}"
        else:
            return f"TW week for group B: {NOT_SCHOOL}"
