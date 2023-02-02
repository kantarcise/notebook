# Goals, Principles, and Patterns

# As the name implies, the main “actors” in the object-oriented paradigm are called
# objects. Each object is an instance of a class. Each class presents to the outside
# world a concise and consistent view of the objects that are instances of this class,
# without going into too much unnecessary detail or giving others access to the inner
# workings of the objects. The class definition typically specifies instance variables,
# also known as data members, that the object contains, as well as the methods, also
# known as member functions, that the object can execute.

# Object-Oriented Design Goals

# Software implementations should achieve robustness, adaptability, and reusability. (See Figure 2.1.)
# Robustness Adaptability Reusability
  
# Robustness
# Every good programmer wants to develop software that is correct, which means that
# a program produces the right output for all the anticipated inputs in the program’s
# application. In addition, we want software to be robust, that is, capable of handling
# unexpected inputs that are not explicitly defined for its application. For example,
# if a program is expecting a positive integer (perhaps representing the price of an
# item) and instead is given a negative integer, then the program should be able to
# recover gracefully from this error. More importantly, in life-critical applications,
# where a software error can lead to injury or loss of life, software that is not robust
# could be deadly. This point was driven home in the late 1980s in accidents involv-
# ing Therac-25, a radiation-therapy machine, which severely overdosed six patients
# between 1985 and 1987, some of whom died from complications resulting from
# their radiation overdose. All six accidents were traced to software errors.

# Adaptability
# Modern software applications, such as Web browsers and Internet search engines,
# typically involve large programs that are used for many years. Software, therefore,
# needs to be able to evolve over time in response to changing conditions in its
# environment. Thus, another important goal of quality software is that it achieves
# adaptability (also called evolvability). Related to this concept is portability, which
# is the ability of software to run with minimal change on different hardware and
# operating system platforms. An advantage of writing software in Python is the
# portability provided by the language itself.

# Reusability
# Going hand in hand with adaptability is the desire that software be reusable, that
# is, the same code should be usable as a component of different systems in various
# applications. Developing quality software can be an expensive enterprise, and its
# cost can be offset somewhat if the software is designed in a way that makes it easily
# reusable in future applications. Such reuse should be done with care, however, for
# one of the major sources of software errors in the Therac-25 came from inappropriate
# reuse of Therac-20 software (which was not object-oriented and not designed
# for the hardware platform used with the Therac-25)


#  Object-Oriented Design Principles
# Chief among the principles of the object-oriented approach, which are intended to
# facilitate the goals outlined above, are the following (see Figure 2.2):
# • Modularity
# • Abstraction
# • Encapsulation

# Modularity

# Modern software systems typically consist of several different components that
# must interact correctly in order for the entire system to work properly. Keeping
# these interactions straight requires that these different components be well organized.
# Modularity refers to an organizing principle in which different components
# of a software system are divided into separate functional units.
# As a real-world analogy, a house or apartment can be viewed as consisting of
# several interacting units: electrical, heating and cooling, plumbing, and structural.
# Rather than viewing these systems as one giant jumble of wires, vents, pipes, and
# boards, the organized architect designing a house or apartment will view them as
# separate modules that interact in well-defined ways. In so doing, he or she is using
# modularity to bring a clarity of thought that provides a natural way of organizing
# functions into distinct manageable units.

# In like manner, using modularity in a software system can also provide a powerful
# organizing framework that brings clarity to an implementation. In Python,
# we have already seen that a module is a collection of closely related functions and
# classes that are defined together in a single file of source code. Python’s standard
# libraries include, for example, the math module, which provides definitions for key
# mathematical constants and functions, and the os module, which provides support
# for interacting with the operating system.

# Robustness is greatly increased because it is easier to test and debug separate components
# before they are integrated into a larger software system. Furthermore, bugs that persist
# in a complete system might be traced to a particular component, which can be
# fixed in relative isolation. The structure imposed by modularity also helps enable
# software reusability. If software modules are written in a general way, the modules
# can be reused when related need arises in other contexts. This is particularly relevant
# in a study of data structures, which can typically be designed with sufficient
# abstraction and generality to be reused in many applications.

# Abstraction
# The notion of abstraction is to distill a complicated system down to its most fundamental
# parts. Typically, describing the parts of a system involves naming them and
# explaining their functionality. Applying the abstraction paradigm to the design of
# data structures gives rise to abstract data types (ADTs). An ADT is a mathematical
# model of a data structure that specifies the type of data stored, the operations supported
# on them, and the types of parameters of the operations. An ADT specifies
# what each operation does, but not how it does it. We will typically refer to the
# collective set of behaviors supported by an ADT as its public interface

# As a programming language, Python provides a great deal of latitude in regard
# to the specification of an interface. Python has a tradition of treating abstractions
# implicitly using a mechanism known as duck typing. As an interpreted and dy-
# namically typed language, there is no “compile time” checking of data types in
# Python, and no formal requirement for declarations of abstract base classes. In-
# stead programmers assume that an object supports a set of known behaviors, with
# the interpreter raising a run-time e# rror if those assumptions fail. The description
# of this as “duck typing” comes from an adage attributed to poet James Whitcomb
# Riley, stating that “when I see a bird that walks like a duck and swims like a duck
# and quacks like a duck, I call that bird a duck.”

# More formally, Python supports abstract data types using a mechanism known
# as an abstract base class (ABC). An abstract base class cannot be instantiated
# (i.e., you cannot directly create an instance of that class), but it defines one or more
# common methods that all implementations of the abstraction must have. An ABC
# is realized by one or more concrete classes that inherit from the abstract base class
# while providing implementations for those method declared by the ABC. Python’s
# abc module provides formal support for ABCs, although we omit such declarations
# for simplicity. We will make use of several existing abstract base classes coming
# from Python’s collections module, which includes definitions for several common
# data structure ADTs, and concrete implementations of some of those abstractions.

# Encapsulation

# Another important principle of object-oriented design is encapsulation. Different
# components of a software system should not reveal the internal details of their
# respective implementations. One of the main advantages of encapsulation is that it
# gives one programmer freedom to implement the details of a component, without
# concern that other programmers will be writing code that intricately depends on
# those internal decisions. The only constraint on the programmer of a component
# is to maintain the public interface for the component, as other programmers will
# be writing code that depends on that interface. Encapsulation yields robustness
# and adaptability, for it allows the implementation details of parts of a program to
# change without adversely affecting other parts, thereby making it easier to fix bugs
# or add new functionality with relatively local changes to a component.

# Throughout this book, we will adhere to the principle of encapsulation, making
# clear which aspects of a data structure are assumed to be public and which are
# assumed to be internal details. With that said, Python provides only loose support
# for encapsulation. By convention, names of members of a class (both data members
# and member functions) that start with a single underscore character (e.g., secret)
# are assumed to be nonpublic and should not be relied upon. Those conventions
# are reinforced by the intentional omission of those members from automatically
# generated documentation.
