# Create a function which adds spaces before every capital in a word. Lower case
# the whole string afterwards.

# Write your function here.
def cap_space(str):
    newStr = ''
    for i in str:
        if i == i.lower():
             newStr = newStr+i
        else:
            newStr = newStr+' '+i.lower()
    return newStr

print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"