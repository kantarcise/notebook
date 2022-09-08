#  Fun With *args and **kwargs

# *args and **kwargs allow a function to accept optional arguments, s owe can make flexible API's in modules and classes.

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo()
# TypeError: "foo() missing 1 required positional arg: 'required'"
foo('hello')
# hello
foo('hello', 1, 2, 3)
# hello
# (1, 2, 3)
foo('hello', 1, 2, 3, key1='value', key2=999)
# hello
# (1, 2, 3)
# {'key1': 'value', 'key2': 999}


        
