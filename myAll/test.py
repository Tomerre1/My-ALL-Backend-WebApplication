days=["ראשון","שני","שלישי","שישי","שבת"]

def stringDaysToIntDays(stingDays):
    days=["ראשון","שני","שלישי","רבעי","חמישי","שישי","שבת"]
    return [(days.index(day)+1) for day in stingDays]


temp={day:False for day in stringDaysToIntDays(days)}
print (temp)
temp.pop(1)
print (temp)
