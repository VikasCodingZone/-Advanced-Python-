# 19. Design a decorator that accepts a list of allowed
#  users and checks if a 'user' keyword argument is in that list.

# Ek decorator banana hai jo function ke user keyword argument ko check kare
# aur ensure kare ki user allowed list me ho.
# Agar user allowed nahi hai → function execute nahi hoga, optional message print kar sakte ho.


def allowed_users(users_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if 'user' in kwargs and kwargs['user'] in users_list:
                return func(*args, **kwargs)
            else:
                print(f"Access denied for user: {kwargs.get('user')}")
                return None
        return wrapper
    return decorator


# Example usage
@allowed_users(["Vikas", "Riya", "Aman"])
def access_dashboard(user):
    print(f"Welcome {user}, you have access to the dashboard.")


# Test calls
access_dashboard(user="Vikas")  # Allowed
access_dashboard(user="shweta")   # Denied


# Logic (Step-by-Step)

# Decorator Factory:
# Outer function allowed_users(users_list) → decorator ko allowed users list deta hai.
# Actual Decorator:
# Function ko input me leta hai (func).
# Wrapper Function:
# Check karta hai: if 'user' in kwargs and kwargs['user'] in users_list:
# Agar true → function call karo
# Agar false → print warning aur return None
# Return Value:
# Function return value same rehta hai agar user allowed ho.
# Otherwise return None.


# Real-Life Examples

# Admin Panel Access:
# Sirf allowed users dashboard ya admin page access kar sake.
# Premium Features:
# Function sirf selected users ke liye execute ho, jaise subscription users.
# API Access Control:
# API endpoints ko sirf certain users ya clients access kar sake.