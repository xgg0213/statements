# Create a function `add_upper` that takes a string and returns all of the
# uppercase characters in the string.

# Write your solution here.
def add_upper(str):
    count=0
    newStr=''
    for i in str:
        if i==i.upper():
            count+=1
            newStr=newStr+i
    return newStr

print(add_upper("ApPlE"))        #> APE
print(add_upper("Coding"))       #> C
print(add_upper("PIano"))        #> PI
print(add_upper("SUPREME"))      #> SUPREME