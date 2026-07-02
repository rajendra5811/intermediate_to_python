import functools
import inspect

def check_types(severity=1):
    if severity == 0:
        # If severity is 0, do nothing: just return the original function unmodified
        return lambda function: function
    
    def message(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)
            
    def checker(function):
        expected = function.__annotations__

        # Ensure all provided annotations are actually valid types
        if not all(map(lambda exp: isinstance(exp, type), expected.values())):
            raise ValueError("All annotations must be valid types.")
            
        if not expected:
            return function
            
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            # Using inspect to perfectly map positional and keyword args to their names
            sig = inspect.signature(function)
            bound_arguments = sig.bind(*args, **kwargs).arguments
            
            # Check the input arguments
            for arg, val in bound_arguments.items():
                if arg not in expected:
                    continue
                if not isinstance(val, expected[arg]):
                    message(f"Bad Argument! Received {arg}={val}, expecting object of type {expected[arg].__name__}")
            
            # Execute the actual function
            retval = function(*args, **kwargs)
            
            # Check the return value
            if 'return' in expected and not isinstance(retval, expected['return']):
                message(f"Bad Return Value! Received {retval}, but expected value of type {expected['return'].__name__}")
                
            return retval
        return wrapper
    return checker

# Apply the decorator with severity=1 (print warnings)
@check_types(severity=1)
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

# 1. This works perfectly
print(greet("Alice", 30)) 

print("\n--- Triggering a warning ---")
# 2. This will trigger your custom warning because age is a string, not an int
print(greet("Bob", "twenty-five"))