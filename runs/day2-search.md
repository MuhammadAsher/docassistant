# Day 2 search runs (2026-11-11)

Swift book commit 16a2a4c (2026-10-28). 1179 chunks, BAAI/bge-small-en-v1.5, index built in 73s (4.9 MB).

```
Q: How do I capture values in a closure?

1. [0.839] Closures > Capturing Values
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures#Capturing-Values
   A closure can *capture* constants and variables from the surrounding context in which it's defined. The closure can then refer to and modify the values of those...

2. [0.783] Closures > Capturing Values
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures#Capturing-Values
   The `incrementer()` function doesn't have any parameters, and yet it refers to `runningTotal` and `amount` from within its function body. It does this by captur...

3. [0.780] Closures > Capturing Values
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures#Capturing-Values
   ```swift let incrementBySeven = makeIncrementer(forIncrement: 7) incrementBySeven() // returns a value of 7 ``` Calling the original incrementer (`incrementByTe...

4. [0.779] Closures > Closures
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures
   Group code that executes together, without creating a named function. *Closures* are self-contained blocks of functionality that can be passed around and used i...

5. [0.775] Expressions > Closure Expression
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/expressions#Closure-Expression
   ```swift class SimpleClass { var value: Int = 0 } var x = SimpleClass() var y = SimpleClass() let closure = { [x] in print(x.value, y.value) } x.value = 10 y.va...

Q: What is the difference between a struct and a class?

1. [0.839] Structures and Classes > Comparing Structures and Classes
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures#Comparing-Structures-and-Classes
   Structures and classes in Swift have many things in common. Both can: - Define properties to store values - Define methods to provide functionality - Define sub...

2. [0.835] Structures and Classes > Definition Syntax
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures#Definition-Syntax
   Structures and classes have a similar definition syntax. You introduce structures with the `struct` keyword and classes with the `class` keyword. Both place the...

3. [0.825] A Swift Tour > Enumerations and Structures
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour#Enumerations-and-Structures
   Use `struct` to create a structure. Structures support many of the same behaviors as classes, including methods and initializers. One of the most important diff...

4. [0.810] Structures and Classes > Structures and Classes
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures
   Model custom types that encapsulate data. *Structures* and *classes* are general-purpose, flexible constructs that become the building blocks of your program's ...

5. [0.806] Structures and Classes > Comparing Structures and Classes
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures#Comparing-Structures-and-Classes
   The additional capabilities that classes support come at the cost of increased complexity. As a general guideline, prefer structures because they're easier to r...

Q: How does async let work?

1. [0.789] A Swift Tour > Concurrency
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour#Concurrency
   Use `async` to mark a function that runs asynchronously. ```swift func fetchUserID(from server: String) async -> Int { if server == "primary" { return 97 } retu...

2. [0.765] Concurrency > Defining and Calling Asynchronous Functions
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency#Defining-and-Calling-Asynchronous-Functions
   An *asynchronous function* or *asynchronous method* is a special kind of function or method that can be suspended while it's partway through execution. This is ...

3. [0.761] Concurrency > Defining and Calling Asynchronous Functions
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency#Defining-and-Calling-Asynchronous-Functions
   When calling an asynchronous method, execution suspends until that method returns. You write `await` in front of the call to mark the possible suspension point....

4. [0.760] Declarations > Asynchronous Functions and Methods
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations#Asynchronous-Functions-and-Methods
   Functions and methods that run asynchronously must be marked with the `async` keyword. These functions and methods are known as *asynchronous functions* and *as...

5. [0.758] Concurrency > Calling Asynchronous Functions in Parallel
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency#Calling-Asynchronous-Functions-in-Parallel
   Calling an asynchronous function with `await` runs only one piece of code at a time. While the asynchronous code is running, the caller waits for that code to f...

Q: What does the weak keyword do?

1. [0.755] Automatic Reference Counting > Weak References
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting#Weak-References
   A *weak reference* is a reference that doesn't keep a strong hold on the instance it refers to, and so doesn't stop ARC from disposing of the referenced instanc...

2. [0.723] Automatic Reference Counting > Weak References
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting#Weak-References
   ```swift class Person { let name: String init(name: String) { self.name = name } var apartment: Apartment? deinit { print("\(name) is being deinitialized") } } ...

3. [0.717] Lexical Structure > Keywords and Punctuation
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/lexicalstructure#Keywords-and-Punctuation
   The following keywords are reserved and can't be used as identifiers, unless they're escaped with backticks, as described above in <doc:LexicalStructure#Identif...

4. [0.712] Automatic Reference Counting > Weak and Unowned References
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting#Weak-and-Unowned-References
   Define a capture in a closure as an unowned reference when the closure and the instance it captures will always refer to each other, and will always be dealloca...

5. [0.701] Automatic Reference Counting > Unowned References and Implicitly Unwrapped Optional Properties
   https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting#Unowned-References-and-Implicitly-Unwrapped-Optional-Properties
   The examples for weak and unowned references above cover two of the more common scenarios in which it's necessary to break a strong reference cycle. The `Person...

```

Note: for the async let question, the section that explains it (Calling Asynchronous Functions in Parallel) ranked 5th.
