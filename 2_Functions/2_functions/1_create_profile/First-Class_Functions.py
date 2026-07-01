def echo(arg):
    return arg

type(echo)     # <class 'function'>
hex(id(echo))  # 0x1003c2bf8
print(echo)    # <function echo at 0x1003c2bf8>

foo = echo
hex(id(foo))   # 0x1003c2bf8
print(foo)     # <function echo at 0x1003c2bf8>

'echo' in locals()

isinstance(echo, object)  # => True

print(echo.__name__)  # => echo
print(echo.__doc__)  # => Return the first argument.
print(echo.__code__)  #
"""What can you do with function objects?
What attributes does a function object possess?
Can I pass a function as a parameters to other functions? Can a function return another function?
How can I modify a function object?"""