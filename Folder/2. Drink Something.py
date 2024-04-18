age = int(input())
"""
if age <= 14:
    print("drink toddy")
elif 14 < age <= 18:
    print("drink coke")
elif 18 < age <= 21:
    print("drink beer")
else:                           # age > 21
    print("drink whisky")
"""

#optimised
if age <= 14:
    print("drink toddy")
elif age <= 18:
    print("drink coke")
elif age <= 21:
    print("drink beer")
else:
    print("drink whisky")

