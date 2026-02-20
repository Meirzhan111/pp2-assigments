import datetime
X = datetime.datetime.now()
print(X)
#1
import datetime
current_time = datetime.datetime.now()
print(current_time.month)
print(current_time.strftime("%B"))
#2
import datetime
event_date = datetime.datetime(2025, 12, 31)
print(event_date)
#3
import datetime
chosen_date = datetime.datetime(2024, 10, 25)
print(chosen_date.strftime("%A"))
#4
import datetime
current_timestamp = datetime.datetime.now()
print(current_timestamp)
#5
import datetime
current_info = datetime.datetime.now()
print(current_info.day)
print(current_info.strftime("%m"))