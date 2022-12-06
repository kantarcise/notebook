# Over the years since its first 1.x release, Spark has become the de facto big data unified processing engine.

# Recommended to download these while working:

# • Apache Spark 3.0 (prebuilt for Apache Hadoop 2.7)
# • Java Development Kit (JDK) 1.8.0

# If you intend to use only Python, then you can simply run pip install pyspark.

# The Genesis Of Spark

# In this section, we’ll chart the course of Apache Spark’s short evolution: its genesis,
# inspiration, and adoption in the community as a de facto big data unified processing engine.

# Big Data and Distributed Computing at Google

# When we think of scale, we can’t help but think of the ability of Google’s search
# engine to index and search the world’s data on the internet at lightning speed. The
# name Google is synonymous with scale.

# Neither traditional storage systems such as relational database management systems
# (RDBMSs) nor imperative ways of programming were able to handle the scale at
# which Google wanted to build and search the internet’s indexed documents. The
# resulting need for new approaches led to the creation of the Google File System (GFS),
# MapReduce (MR), and Bigtable.

# While GFS provided a fault-tolerant and distributed filesystem across many commodity
# hardware servers in a cluster farm, Bigtable offered scalable storage of
# structured data across GFS. MR introduced a new parallel programming paradigm,
# based on functional programming, for large-scale processing of data distributed over
# GFS and Bigtable.

# In essence, your MR applications interact with the MapReduce system that sends
# computation code (map and reduce functions) to where the data resides, favoring
# data locality and cluster rack affinity rather than bringing data to your application.

# The workers in the cluster aggregate and reduce the intermediate computations and
# produce a final appended output from the reduce function, which is then written to a
# distributed storage where it is accessible to your application. This approach 
# significantly reduces network traffic and keeps most of the input/output (I/O) local to disk
# rather than distributing it over the network.

# Most of the work Google did was proprietary, but the ideas expressed in the aforementioned
# three papers spurred innovative ideas elsewhere in the open source community—
# especially at Yahoo!, which was dealing with similar big data challenges of
# scale for its search engine.

# Hadoop at Yahoo!

# The computational challenges and solutions expressed in Google’s GFS paper provided
# a blueprint for the Hadoop File System (HDFS), including the MapReduce
# implementation as a framework for distributed computing. Donated to the Apache
# Software Foundation (ASF), a vendor-neutral non-profit organization, in April 2006,
# it became part of the Apache Hadoop framework of related modules: Hadoop Common
# , MapReduce, HDFS, and Apache Hadoop YARN.

# Although Apache Hadoop had garnered widespread adoption outside Yahoo!, inspiring
# a large open source community of contributors and two open source–based commercial
# companies (Cloudera and Hortonworks, now merged), the MapReduce
# framework on HDFS had a few shortcomings.

# First, it was hard to manage and administer, with cumbersome operational 
# complexity. Second, its general batch-processing MapReduce API was verbose and required a
# lot of boilerplate setup code, with brittle fault tolerance. Third, with large batches of
# data jobs with many pairs of MR tasks, each pair’s intermediate computed result is
# written to the local disk for the subsequent stage of its operation (see Figure 1-1).
# This repeated performance of disk I/O took its toll: large MR jobs could run for hours
# on end, or even days.
