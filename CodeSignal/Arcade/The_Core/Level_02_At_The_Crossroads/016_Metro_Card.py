# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/J7PQDxpWqhx7HrvBZ
def metroCard(last_number_of_days):
    # Months days:
    # JAN/31, FEB/28, MAR/31, APR/30, MAY/31, JUN/30,
    # JUL/31, AUG/31, SEP/30, OCT/31, NOV/30, DEC/31
    # Given the number of days in the last month, what could be the next month?
    days_next = {
        28: [31],
        30: [31],
        31: [28, 30, 31]
    }
    
    return days_next[last_number_of_days]
