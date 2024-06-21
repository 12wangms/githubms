# import calendar
# # calendar.setfirstweekday(calendar. SUNDAY)
#
# def print_year_month(year, month):
#     cal = calendar. TextCalendar(6)
#     print(cal. formatmonth(year, month))
#
#     for year in (2024, 2027):
#         for month in [6, 7, 8]:
#             # print(f"Calender for {calendar. month_name[month]} {year}")
#              print_year_month(year, month)
#             # print('-' * 40)
import calendar
tourist_season = [6, 7, 8]
for year in range(2024, 2027):
    cal = calendar.Calendar(firstweekday=6)
    print(f"\nYear {year}")
    for month in range(1, 13):
        print(calendar.month(year, month))
        if month in tourist_season:
            print("旅游旺季")
            print(calendar.month(year, month))
