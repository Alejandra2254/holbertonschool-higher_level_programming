#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(0x16))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(5, -2))
try:
        print(add_integer( 2147483647, 6))
except Exception as e:
        print(e)
        try:
                print(add_integer(None))
        except Exception as e:
                print(e)
