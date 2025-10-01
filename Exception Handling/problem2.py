# 2. Code after raise in try block
# "In a try-except block, if an exception is raised in 
# the try block and caught by a matching except, does the code 
# after the raise statement in the try block execute? Why or why not?"

# Short Answer (Hindi explanation):

# Nahi 🚫.
# Jab bhi try block me exception aata hai, us line ke baad ka sara code skip ho jata hai.
#  Python turant matching except block me chala jata hai, 
# isliye raise ke baad ka code kabhi execute nahi hota.
try:
    print("Start")
    x = 10 / 0   # exception
    print("This will not run")  # skip ho jayega
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
