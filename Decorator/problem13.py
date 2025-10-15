# 13. Create a decorator that converts all string arguments to
#  lowercase before passing them to the function.

# Ek decorator banana hai jo function ke saare string arguments ko lowercase me convert kare
# aur fir unhe function me bheje.

def to_lowercase(func):
    def wrapper(*args):
        # sabhi string arguments ko lowercase me badal do
        new_args = []
        for arg in args:
            if type(arg) == str:
                new_args.append(arg.lower())
            else:
                new_args.append(arg)
        return func(*new_args)
    return wrapper


@to_lowercase
def greet(name, city):
    print(f"Hello {name} from {city}!")


# function call
greet("VIKAS", "INDORE")
greet("RIYA","DELHI")

# Logic (Simple Explanation)

# Jab function call hota hai (greet("VIKAS", "INDORE")),
# decorator sabhi arguments ko check karta hai.
# Agar argument string hai → usse .lower() karke new list me daal deta hai.
# Fir function ko lowercase arguments ke saath call karta hai.
# Result: sab words lowercase me chale jaate hain. 

#  Example for Understanding

# Socho tumhara function naam aur city print karta hai.
# User galti se likhta hai:
# greet("VIKAS", "INDORE")

# Without decorator:
# Hello VIKAS from INDORE!

# With decorator:
# Hello vikas from indore!
# Yani decorator ne input sanitize kar diya 💪