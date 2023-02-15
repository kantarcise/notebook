# Protected Members

# Our PredatoryCreditCard subclass directly accesses the data member self. balance,
# which was established by the parent CreditCard class. The underscored name, by
# convention, suggests that this is a nonpublic member, so we might ask if it is okay
# that we access it in this fashion. While general users of the class should not be
# doing so, our subclass has a somewhat privileged relationship with the superclass.
# Several object-oriented languages (e.g., Java, C++) draw a distinction for nonpublic
# members, allowing declarations of protected or private access modes. Members
# that are declared as protected are accessible to subclasses, but not to the general
# public, while members that are declared as private are not accessible to either. In
# this respect, we are using balance as if it were protected (but not private).

# Python does not support formal access control, but names beginning with a single
# underscore are conventionally akin to protected, while names beginning with a
# double underscore (other than special methods) are akin to private. In choosing to
# use protected data, we have created a dependency in that our PredatoryCreditCard
# class might be compromised if the author of the CreditCard class were to change
# the internal design. 
