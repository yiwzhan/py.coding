# leap=0
def wutyear(year):
    if year%4==0 and year%100!=0:
        leap=True
    return leap
    
def wutday(year,month,date):
    ifleap=wutyear(year)
    if ifleap==True:
        md=[31,29,31,30,31,30,31,30,31,31,30,31]
    else:
        md=[31,28,31,30,31,30,31,30,31,31,30,31]
    day=0
    for i in range(month-1):
        day+=md[i]
    day+=date
    return day
print(wutday(2020,7,17))

