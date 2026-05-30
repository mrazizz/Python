# days_month = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}

# states_USA = {"CA": "California", "NY": "New York", "TX": "Texas", "FL": "Florida", "IL": "Illinois"}

# for key, value in states_USA.items():
#     print(f"{key}: {value}")

# for month, days in days_month.items():
#     print(f"{month} has {days} days")

# print(sorted(days_month))

footballer_goals = {"Messi": 750, "Ronaldo": 780, "Pele": 767, "Cruss": 345}

max_value = 0
max_key = ""
for key, value in footballer_goals.items():
    if value > max_value:
        max_value = value
        max_key = key

print(f"The footballer with the most goals is {max_key} with {max_value} goals.")