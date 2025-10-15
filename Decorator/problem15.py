
# 15. Design a decorator that wraps the function's output in HTML tags, like <p>output</p>.

# Ek decorator banana hai jo function ka output HTML tags me wrap kare.
# Jaise: <p>output</p>, <h1>output</h1> etc.


def html_wrap(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)         # Original function call
            return f"<{tag}>{result}</{tag}>"     # Wrap output in HTML tag
        return wrapper
    return decorator


# Example usage:

@html_wrap("p")
def greet(name):
    return f"Hello, {name}!"

@html_wrap("h1")
def title():
    return "Welcome to My Website"


# Test calls
print(greet("Vikas"))   # <p>Hello, Vikas!</p>
print(title())           # <h1>Welcome to My Website</h1>


# Logic Step-by-Step

# Decorator Factory (html_wrap(tag))
# Yeh outer function hai jo HTML tag ko argument ke roop me leta hai.
# Return karta hai actual decorator function.
# Actual Decorator (decorator(func))
# Yeh function ko input me leta hai.
# Return karta hai wrapper function jo output modify karega.
# Wrapper Function (wrapper(*args, **kwargs))
# Call karta hai original function: result = func(...)
# Output ko HTML tag me wrap karta hai: f"<{tag}>{result}</{tag}>"
# Return karta hai wrapped result.
# Function Call
# Jab greet("Vikas") call hota hai:
# Wrapper function run hota hai
# Original output "Hello, Vikas!" aata hai
# Decorator usse <p> tag me wrap karta hai → "<p>Hello, Vikas!</p>"
# Ye return hota hai aur print karne pe HTML format me dikhta hai.


# Real-Life Examples of HTML Wrapper Decorator

# Blog Content Generator
# Tumhara function blog ka paragraph generate karta hai.
# Decorator us output ko <p> tag me wrap karta hai.
# Result directly webpage me display hota hai.
# Example: "This is my first paragraph." → <p>This is my first paragraph.</p>