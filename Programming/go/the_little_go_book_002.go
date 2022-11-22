// Basics

// Go is compiled, statically typed language with a C like syntax and garbage collection.

// Go is compiled to assembly.

// Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either
// achieved by specifying the type when the variable is declared or, in many cases, letting the compiler infer the type

// Saying that a language has a C like syntax means that if you’re used to any other C like languages such as C, C++,
// Java, JavaScript and C#, then you’re going to find Go familiar – superficially, at least. 

// For example, it means && is used as a boolean AND, == is used to compare equality, { and } start and end a scope, and array indexes start at 0.

if name == "Leto" {
  print("the spice must flow")
}

// And in more complicated cases, parentheses are still useful:
if (name == "Goku" && power > 9000) || (name == "gohan" && power < 4000)  {
  print("super Saiyan")
}


// Some variables, when created, have an easy to define life. A variable local to a function, for example, disappears when
// the function exits. In other cases, it isn’t so obvious – at least to a compiler. For example, the lifetime of a variable
// returned by a function or referenced by other variables and objects can be tricky to determine. Without garbage
// collection, it’s up to developers to free the memory associated with such variables at a point where the developer
// knows the variable isn’t needed. 

// How? In C, you’d literally free(str); the variable.

// Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these
// and free them when they’re no longer used. Garbage collection adds overhead, but it also eliminates a number of devastating bugs.


// Now let's try something

package main

func main() {
    println("it's over 9000!")
}

// If we save this as "main.go" and use 
// "go run main.go"

// It will print out it's over 9000!

// What about the compilation? go run directly complies and runs your code. It uses a temporary directory to build the program.

// You can see the temp file with "go run --work main.go"

// Or you can build it with:
// "go build main.go"

// To run the build, do "./main" on Linux/OS X.
