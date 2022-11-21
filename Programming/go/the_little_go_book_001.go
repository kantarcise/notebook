// Why Go? For me, there are two compelling reasons. The first is that it’s
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

// For OSX / Linux

// Download the tar.gz for your platform. For OSX, you’ll most likely be interested in go#.#.#.darwin-amd64-osx10
//  .8.tar.gz, where #.#.# is the latest version of Go.

// Extract the file to /usr/local via 
// $ tar -C /usr/local -xzf go#.#.#.darwin-amd64-osx10.8.tar.gz.
// Set up two environment variables:
//      1. GOPATH points to your workspace, for me, that’s $HOME/code/go.
//      2. We need to append Go’s binary to our PATH.

// You can set these up from a shell:

// $ echo 'export GOPATH=$HOME/code/go' >> $HOME/.profile
// $ echo 'export PATH=$PATH:/usr/local/go/bin' >> $HOME/.profile

// You’ll want to activate these variables. You can close and reopen your shell, or you can run source $HOME/.profile.
// Type go version and you’ll hopefully get an output that looks like go version go1.3.3 darwin/amd64.

// On linux, this can help:
// https://www.digitalocean.com/community/tutorials/how-to-install-go-on-ubuntu-18-04

package main

func main() {
  println("Hello World!")
}
