# Assertion Errors

# If your program is bug-free, these conditions will never occur. But if
# they do occur, the program will crash with an assertion error telling
# you exactly which “impossible” condition was triggered. This makes
# it much easier to track down and fix bugs in your programs. And I like
# anything that makes life easier—don’t you?

def apply_discount(product,discount):
    price = int(product["price"] * (1 - discount))
    assert 0 <= price <= product["price"]
    return price
