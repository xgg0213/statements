# Create a function that determines whether a string is a valid hex code.

# A hex code must begin with a pound key # and is exactly 6 characters in
# length. Each character must be a digit from 0-9 or an alphabetic character
# from A-F. All alphabetic characters may be uppercase or lowercase.

# Write your function here.
def is_valid_hex_code(a):
    digit = [0,1,2,3,4,5,6,7,8,9]
    char = ['a','b','c','d','e','f']

    if (a[0] != '#') or (len(a) != 7):
        return False
    
    newA = a[1:]

    for i in newA:
        # if (not i.isdigit()) and (i.lower() not in char):
        if not (i.isdigit() or i.lower() in char):
            return False


    return True

print(is_valid_hex_code("#CD5C5C"))  #> True
print(is_valid_hex_code("#EAECEE"))  #> True
print(is_valid_hex_code("#eaecee"))  #> True

print(is_valid_hex_code("#CD5C58C"))
# Prints False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z"))
# Prints False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C"))
# Prints false
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C"))
# Prints False
# Missing #
