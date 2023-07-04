#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

l_c = LockedClass()
l_c.first_name = "John"
print(l_c.first_name)
try:
        l_c.last_name = "Snow"
except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
