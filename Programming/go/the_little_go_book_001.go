// I’ve always had a love-hate relationship when it comes to learning new languages. On the one hand, languages are so
// fundamental to what we do, that even small changes can have measurable impact. That aha moment when something
// clicks can have a lasting effect on how you program and can redefine your expectations of other languages. On the
// downside, language design is fairly incremental. Learning new keywords, type system, coding style as well as new
// libraries, communities and paradigms is a lot of work that seems hard to justify. Compared to everything else we have
// to learn, new languages often feel like a poor investment of our time.

// That said, we have to move forward. We have to be willing to take incremental steps because, again, languages are the
// foundation of what we do. Though the changes are often incremental, they tend to have a wide scope and they impact
// productivity, readability, performance, testability, dependency management, error handling, documentation, profiling,
// communities, standard libraries, and so on. Is there a positive way to say death by a thousand cuts?

// That leaves us with an important question: why Go? For me, there are two compelling reasons. The first is that it’s
// a relatively simple language with a relatively simple standard library. In a lot of ways, the incremental nature of Go is
// to simplify some of the complexity we’ve seen being added to languages over the last couple of decades. The other
// reason is that for many developers, it will complement your existing arsenal.

// Go was built as a system language (e.g., operating systems, device drivers) and thus aimed at C and C++ developers.
// According to the Go team, and which is certainly true of me, application developers, not system developers, have
// become the primary Go users. Why? I can’t speak authoritatively for system developers, but for those of us building
// websites, services, desktop applications and the like, it partially comes down to the emerging need for a class of systems
// that sit somewhere in between low-level system applications and higher-level applications.

// Maybe it’s a messaging, caching, computational-heavy data analysis, command line interface, logging or monitoring.
// I don’t know what label to give it, but over the course of my career, as systems continue to grow in complexity
// and as concurrency frequently measures in the tens of thousands, there’s clearly been a growing need for custom
// infrastructure-type systems. You can build such systems with Ruby or Python or something else (and many people do),
// but these types of systems can benefit from a more rigid type system and greater performance. Similarly, you can use
// Go to build websites (and many people do), but I still prefer, by a wide margin, the expressiveness of Node or Ruby for
// such systems.

// Getting Started:

// Installing Go is straightforward. You can install it from source, but I suggest you use one of the precompiled binaries.
// When you go to the download page, you’ll see installers for various platforms. Let’s avoid these and learn how to set
// up Go ourselves. As you’ll see, it isn’t hard.

// Except for simple examples, Go is designed to work when your code is inside a workspace. The workspace is a folder
// composed of bin, pkg and src subfolders. You might be tempted to force Go to follow your own style, don’t.

// Normally, I put my projects inside of ~/code. For example, ~/code/blog contains my blog. For Go, my workspace is
// ~/code/go and my Go powered blog would be in ~/code/go/src/blog.

// In short, create a go folder with a src subfolder wherever you expect to put your projects.

// Will continue about the setup. Here is a teaser in the meantime.

package main

func main() {
  println("Hello World!")
}
