# This chapter is all about Maps, Hash Tables and Skip Lists

## Recap

### Dicts

Dicts are associative arrays or maps.
They are implemented as hash tables which has a hash code and compression fucntion. 
 
hash code takes a string and returns an index between -inf and +inf
compression fucntion makes that index in between 0 and N - 1 
where N is the bucket array size.

"""Cool info"""

Python dicts actually store the hash value for their keys, beacause computing hash methods each time is costly

### Collison handling schemes

#### SeperatE Chaining or Open Adressingp

seperate chainign is like holding long lists in each slot of the bucket array to avoid coillisons

Open addressing is things like, linear probing, quadratic probing, doublke hsahing.

linear probing - if occupied go next
quadratic probing - if occupied go next but i ^2
double hashing - insert another hash to the calculation

"""Cool info"""

Python dicts use Open Addressing with a pseudo random number generator. With load factor threshold 2/3

load factor should NOT go over 1. For python dicts, if it goes over 2/3, bucket array is resized.

 IN default python dictionaries will initialize woth bucket array with size 8

### Sorted Maps

Keys are sorted.these are really good for finding nearest keys range queries.
they provide both fast key:value lookups and maintain keys in order.

EXAMPLE - FLIGHT DATABASES - Maxima Sets

### Skip Lists

tHEY STORE DATA MORE EFFICIENTLY.  PERFORM operations like insert, delete, search in logarithmic time.

##### REALLY GOOD
in sorted data management
range queries
they are easier to implement than TREES

##### BAD
Takes A LOT of memory with all those lists in it
not widely known.
