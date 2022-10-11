def current_day(x):
    y = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'  )
    count = y[x]
    while count <= x:
        yield count
        x += 1



print()
print(current_day.__next__())
print(current_day.__next__()) # 'Monday'

print(current_day.__next__()) # 'Tuesday'

print(current_day.__next__()) # 'Wednesday'

print(current_day.__next__()) # 'Thursday'

print(current_day.__next__()) # 'Friday'

print(current_day.__next__()) # 'Saturday'