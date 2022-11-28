// Imports
// Go has a number of built-in functions, such as println, which can be used without reference. We can’t get very
// far though, without making use of Go’s standard library and eventually using third-party libraries. In Go, the import
// keyword is used to declare the packages that are used by the code in the file.

// Let’s change our program:

package main
import (
"fmt"
"os"
)

func main() {
    if len(os.Args) != 2 {
        os.Exit(1)
    }
    fmt.Println("It's over", os.Args[1])
}

// Which you can run via:
// go run main.go 9000

// The program will directly exit if you dont give an argument for it

// We’re now using two of Go’s standard packages: fmt and os. We’ve also introduced another built-in function len. 
// len returns the size of a string, or the number of values in a dictionary, or, as we see here, the number of elements in an
// array. If you’re wondering why we expect 2 arguments, it’s because the first argument – at index 0 – is always the
// path of the currently running executable. (Change the program to print it out and see for yourself.)

// You’ve probably noticed we prefix the function name with the package, e.g., fmt.Println. This is different from many
// other languages. We’ll learn more about packages in later chapters. For now, knowing how to import and use a package
// is a good start.

// Go is strict about importing packages. It will not compile if you import a package but don’t use it. Try to run the following:

package main

import (
"fmt"
"os"
)
func main() {
}

// You should get two errors about fmt and os being imported and not used. Can this get annoying? Absolutely. Over
// time, you’ll get used to it (it’ll still be annoying though). Go is strict about this because unused imports can slow
// compilation; admittedly a problem most of us don’t have to this degree.

// Another thing to note is that Go’s standard library is well documented. 
// You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. 
// You can click on that section header and see the source code. Also, scroll to the top to learn more about Go’s formatting capabilities.

// If you’re ever stuck without internet access, you can get the documentation running locally via:
// godoc -http=:6060
// and pointing your browser to http://localhost:6060

