##
## 1.1. Unpacking a Sequence into Separate Variables
##
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name)
print(date)

_, _, _, (year, mon, day) = data
print(year)
print(mon)
print(day)

