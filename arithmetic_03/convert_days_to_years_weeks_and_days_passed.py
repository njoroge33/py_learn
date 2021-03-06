# Write a program to convert given number of days to a measure of time in years, weeks and days
# For example 375 days is equal to 1 year, 1 week and 3 days (ignore leap year)

# return should be a tuple of (years, weeks, days)
# for more info on this quiz, go to this url: http://www.programmr.com/convert-days-years-weeks-and-days-passed-0


def days_to_years_weeks_days(days):
    year = int(days / 365)
    week = int((days % 365)/7)
    day = int((days % 365) % 7)
    return year, week, day


if __name__ == "__main__":
    print(days_to_years_weeks_days(375))
