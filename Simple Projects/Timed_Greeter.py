from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
chour=now.hour
if (6<=chour<12):
    print("Good Morning")
elif(12<=chour<18):
    print("Good Afternoon")
else:
    print("Good Evening")
