day = input("enter day of the week\n")
timetable_dict = {
"monday": ["Eng","Text","BM","Chem",],
"tuesday": ["Eng","BM","Chem","Text"],
"wednesday": ["BM","Text","Eng","Chem",],
"thursday": ["Eng","GM","Applied","Text"],
"friday": ["Chem","Applied","BM","GM"]}
period = int(input("enter period\n"))
print(timetable_dict[day][period])