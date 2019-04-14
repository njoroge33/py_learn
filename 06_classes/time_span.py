# Complete the class TimeSpan 
# A TimeSpan object stores a span of time in hours and minutes (for example, the time span between 8:00am and 10:30am is 2 hours, 30 minutes) 
# Each TimeSpan object should have the following methods:
      - get_hours()
      Returns the number of hours in this time span 
# - get_minutes()
      Returns the number of minutes in this time span, between 0 and 59 
# - add(hours, minutes)
      Adds the given amount of time to the span 
# For example, (2 hours, 15 min) + (1 hour, 45 min) = (4 hours) 
# Assume that the parameters are valid: the hours are non-negative, and the minutes are between 0 and 59 
# - add(timespan)
      Adds the given amount of time (stored as a time span) to the current time span 
# - get_total_hours()
Returns the total time in this time span as the real number of hours, such as 9 
# 75 for (9 hours, 45 min), rounded to two decimal places 
# The minutes should always be reported as being in the range of 0 to 59 
# That means that you may have to "carry" 60 minutes into a full hour 
# for more info on this quiz, go to this url: http://www.programmr.com/time-span