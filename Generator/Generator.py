# Generator Python me ek special type of function
#  hota hai jo data ko ek-ek karke produce (generate)
#  generate karta hai — puri list memory me  store nahi karta hai ..

# matlab— generator lazy evaluation use karta hai
# (data tabhi generate karta hai jab zarurat hoti hai).
# Isse memory efficient code likha ja sakta hai..

#  Generator Function Syntax
# Generator function banane ke liye hum return ki jaghe yield keyword use karte hai..

def my_generator():
    for i in range(1, 6):
        yield i   # return nahi, yield use kiya

# generator object banate hain
gen = my_generator()

# ek-ek value nikalte hain
for value in gen:
    print(value)
