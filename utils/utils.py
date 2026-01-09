import calendar
from datetime import date


def quarter_to_dates(qtr_str):
    year, quarter = qtr_str.split('-')
    year = int(year)
    q = int(quarter[1])

    start_month = (q - 1) * 3 + 1
    end_month = start_month + 2

    start_date = date(year, start_month, 1)
    end_day = calendar.monthrange(year, end_month)[1]
    end_date = date(year, end_month, end_day)

    return start_date.strftime("%Y-%d-%m"), end_date.strftime("%Y-%d-%m")