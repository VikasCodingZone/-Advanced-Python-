def person(func):
    def inner():
        print("i am vikas")
        func()
        print("hello bhai vikas")
      
    return inner
@person
def say_hello():
    print("hello ")

say_hello()

# person ek decorator function hai.
#  Ye ek function (func) ko argument ke roop me leta hai.
# inner() ek nested function hai jo kuch extra kaam (before & after) karta hai.
# return inner ka matlab hai — jab @person use hota hai,
# to inner() function return hota hai (jo original function ke behavior ko modify karta hai).


# Matlab:

# say_hello function ko person ke andar bheja gaya.
# person ne inner function return kiya.
# Ab say_hello actually inner ban gaya hai (jo original say_hello() ko include karta hai).

# Flow Diagram
# say_hello()  →  inner() run hota hai  → 
#      print("I am Vikas")
#      func() → print("Hello")
#      print("Hello bhai Vikas")