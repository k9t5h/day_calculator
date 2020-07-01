from datetime import datetime, timedelta
import sys

TW_SCHOOL = "tw-school"
TW_ONLINE = "tw-online"
SI = "si"
WEEKEND = "weekend"

def calculate_day_type(date, ab):
    """Return the type of a day for a student on a given week type (A/B)
    Parameters:
    date (datetime): A day you want to calculate the type of
    ab (string): The week type of the student (A or B)
    
    There are 4 different day types returned:
    tw-school - When student has to be in school on a TW week
    tw-online - When student has to be onlineon a TW week
    si - When student is on an SI week
    weekend - On weekend
    """
    pass
