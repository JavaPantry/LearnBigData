#DEVELOP WITH HADOOP
Start developing with Hadoop. These tutorials are designed to ease your way into developing with Hadoop:

## Apache Spark on HDP
### Hands-on Tour of Apache Spark in 5 Minutes
Apache Spark is a fast, in-memory data processing engine with elegant and expressive development APIs in Scala, Java, Python, and R that allow data workers to efficiently execute machine learning algorithms that require fast iterative access to datasets (see Spark API Documentation for more info). Spark on Apache Hadoop YARN enables deep integration with Hadoop […]
### [A Lap Around Apache Spark](http://hortonworks.com/hadoop-tutorial/a-lap-around-apache-spark/)
This tutorial walks you through many of the newer features of Spark 1.6.2 on YARN. With YARN, Hadoop can now support many types of data and application workloads; Spark on YARN becomes yet another workload running against the same set of hardware resources. The tutorial describes how to: Run Spark on YARN and run the […]

Read before [How To Use 'Sudo' And 'Su' Commands In Linux](https://www.linux.com/blog/how-use-sudo-and-su-commands-linux-introduction)

_where I can set SPARK_HOME?_
If you haven’t already, make sure to set SPARK_HOME before proceeding:

```
export SPARK_HOME=/usr/hdp/current/spark-client
```

### Getting Started with Apache Zeppelin
Apache Zeppelin is a web-based notebook that enables interactive data analytics. With Zeppelin, you can make beautiful data-driven, interactive and collaborative documents with a rich set of pre-built language backends (or interpreters) such as Scala (with Apache Spark), Python (with Apache Spark), SparkSQL, Hive, Markdown, Angular, and Shell. With a focus on Enterprise, Zeppelin has […]
### Learning Spark with Zeppelin
In this tutorial, we will introduce the basic concepts of Apache Spark DataFrames in a hands-on lab. We will also introduce the necessary steps to get up and running with Apache Zeppelin on a Hortonworks Data Platform (HDP) Sandbox. Prerequisites Please ensure you complete the prerequisites before proceeding with this tutorial. There are multiple ways […]
### Intro to Machine Learning with Apache Spark and Apache Zeppelin
In this tutorial, we will give you a taste of the powerful Machine Learning libraries in Apache Spark via a hands-on lab. We will also introduce the necessary steps to get you up and running with Apache Zeppelin on a Hortonworks Data Platform (HDP) Sandbox. Prerequisites Please ensure you complete the prerequisites before proceeding with […]
### Spark on HBase: A Dataframe Based HBase Connector
The technical preview of the Spark-HBase connector was developed by Hortonworks along with Bloomberg. The connector leverages Spark SQL Data Sources API introduced in Spark-1.2.0. It bridges the gap between the simple HBase Key Value store and complex relational SQL queries and enables users to perform complex data analytics on top of HBase using Spark. […]

## Hello World

###Learning the Ropes of the Hortonworks Sandbox
Introduction This tutorial is aimed for users who do not have much experience in using the Sandbox. We will install and explore the Sandbox on virtual machine and cloud environments. We will also navigate the Ambari user interface. Let’s begin our Hadoop journey. Pre-Requisites Downloaded and Installed Hortonworks Sandbox Allow yourself around one hour to […]

### Hadoop Tutorial – Getting Started with HDP
This tutorial will help you get started with Hadoop and HDP. We will use an Internet of Things (IoT) use case to build your first HDP application.

### Analyze Traffic Patterns with Apache NiFi
Traffic Congestion is a problem for commuters. A team of city planners work together to create a location for a new highway based on traffic patterns. Live data originally poses a problem for analyzing traffic data because historical and aggregated traffic counts were used. They selected NiFi for real-time data integration because it leverages the ability to ingest, filter and store data-in-motion. Observe how their team used NiFi to obtain a deeper understanding of traffic patterns and decide on a location for the new highway.
### Introduction to Apache HBase Concepts, Apache Phoenix and New Backup & Restore Utility in HBase
This tutorial will go through the introduction of Apache HBase and Apache Phoenix along with the new Backup and Restore utility in HBase that has been introduced in HDP 2.5. Enjoy HADOOPING!!
### How to Process Data with Apache Hive
This Hadoop tutorial shows how to Process Data with Hive using a set of driver data statistics.
### How To Process Data with Apache Pig
This Hadoop tutorial shows how to Process Data with Apache Pig using a set of driver data statistics.
### Loading and Querying Data with Hadoop
In this tutorial, we will load and review data for a fictitious web retail store in what has become an established use case for Hadoop: deriving insights from large data sources such as web logs.
### Get Started with Cascading on Hortonworks Data Platform 2.1
how to get started with Cascading and Hortonworks Data Platform using the Word Count Example.

### Get Started with Cascading on Hortonworks Data Platform 2.1
If you have any errors in completing this tutorial. Please ask questions or notify us on Hortonworks Community Connection! This is the second tutorial to enable you as a Java developer to learn about Cascading and Hortonworks Data Platform (HDP). Other tutorials are: WordCount with Cascading on HDP 2.3 Sandbox LogParsing with Cascading on HDP […]

### Cascading Pattern
Learn how to use Cascading Pattern to quickly migrate Predictive Models (PMML) from SAS, R, MicroStrategy onto Hadoop and deploy them at scale.

### Interactive SQL on Hadoop with Hive LLAP
Introduction Hive LLAP combines persistent query servers and intelligent in-memory caching to deliver blazing-fast SQL queries without sacrificing the scalability Hive and Hadoop are known for. This tutorial will show you how to try LLAP on your HDP 2.5 Sandbox and experience its interactive performance firsthand using a BI tool of your choice (Tableau will […]
### HBase Reporting with Apache Phoenix via ODBC
Overview Apache HBase is a NoSQL database in the Hadoop eco-system. Many business intelligence tool and data analytic tools lack the ability to work with HBase data directly. Apache Phoenix enables you to interact with HBase using SQL. In HDP 2.5, we have introduced support for ODBC drivers. With this, you can connect any ODBC […]
### Processing streaming data in Hadoop with Apache Storm
How to use Apache Storm to process real-time streaming data in Hadoop with Hortonworks Data Platform.
### Interactive Query for Hadoop with Apache Hive on Apache Tez
How to use Apache Tez and Apache Hive for Interactive Query with Hadoop and Hortonworks Data Platform 2.5
### Indexing and Searching Documents with Apache Solr
In this tutorial we will walk through how to run Solr in Hadoop with the index (solr data files) stored on HDFS and using a map reduce jobs to index files.
### Define and Process Data Pipelines in Hadoop with Apache Falcon
Use Apache Falcon to define an end-to-end data pipeline and policy for Hadoop and Hortonworks Data Platform 2.1
### Introducing Apache Hadoop to Java Developers
Introduction In this tutorial for Hadoop Developers, we will explore the core concepts of Apache Hadoop and examine the process of writing a MapReduce Program. Pre-Requisite Downloaded and Installed latest Hortonworks Sandbox Learning the Ropes of the Hortonworks Sandbox Outline Hadoop Step 1: Explore the Core Concepts of Apache Hadoop 1.1 What is MapReduce? 1.2 […]
## Real World Examples
### Indexing and Searching text within images with Apache Solr
A very common request from many customers is to be able to index text in image files; for example, text in scanned PNG files. In this tutorial we are going to walkthrough how to do this with SOLR. Prerequisites Download the Hortonworks Sandbox Complete the Learning the Ropes of the HDP Sandbox tutorial. Step-by-step guide […]
### Incremental Backup of Data from HDP to Azure using Falcon for Disaster Recovery and Burst capacity
Introduction Apache Falcon simplifies the configuration of data motion with: replication; lifecycle management; lineage and traceability. This provides data governance consistency across Hadoop components. Scenario In this tutorial we will walk through a scenario where email data gets processed on multiple HDP 2.2 clusters around the country then gets backed up hourly on a cloud […]
### Realtime Event Processing in Hadoop with NiFi, Kafka and Storm
Learn to ingest the real-time data from car sensors with NiFi and send it to Hadoop. Use Apache Kafka for capturing that data in between NiFi and Storm for scalability and reliability. Deploy a storm topology that pulls the data from Kafka and performs complex transformations to combine geolocation data from trucks with sensor data from trucks and roads. Once all sub projects are completed, deploy the driver monitor demo web application to see driver behavior, predictions and drools data in 3 different map visualizations.
### Visualize Website Clickstream Data
How do you improve the chances that your online customers will complete a purchase? Hadoop makes it easier to analyze and then change how visitors behave on your website. Here you can see how an online retailer optimized buying paths to reduce bounce rates and improve conversions. HDP can help you capture and refine website clickstream data to exceed your company’s e-commerce goals. The tutorial that comes with this video describes how to refine raw clickstream data using HDP.
### Refine and Visualize Server Log Data
Security breaches happen. And when they do, server log analysis helps you identify the threat and then protect yourself better in the future. See how Hadoop takes server-log analysis to the next level by speeding forensics, retaining log data for longer and demonstrating compliance with IT policies. The tutorial that comes with this video describes how to refine raw server log data using HDP.
### Analyzing Social Media and Customer Sentiment With Apache NiFi and HDP Search
With Hadoop, you can mine Twitter, Facebook and other social media conversations to analyze customer sentiment about you and your competition. With more social Big Data, you can make more targeted, real-time, decisions. The tutorial that comes with this video describes how to refine raw Twitter data using HDP.
### How To Analyze Machine and Sensor Data
Machines know things. Sensors stream low-cost, always-on data. Hadoop makes it easier for you to store and refine that data and identify meaningful patterns, providing you with the insight to make proactive business decisions using predictive analytics. See how Hadoop can be used to analyze heating, ventilation and air conditioning data to maintain ideal office temperatures and minimize expenses
### Natural Language Processing and Sentiment Analysis for Retailers using HDP and ITC Infotech Radar
RADAR is a software solution for retailers built using ITC Handy tools (NLP and Sentiment Analysis engine) and utilizing Hadoop technologies in …
### Predictive Analytics on H2O and Hortonworks Data Platform
Introduction H2O is the open source in memory solution from 0xdata for predictive analytics on big data. It is a math and machine learning engine that brings distribution and parallelism to powerful algorithms that enable you to make better predictions and more accurate models faster. With familiar APIs like R and JSON, as well as […]

##HADOOP ADMINISTRATION
Get Started with Hadoop Administration. These tutorials are designed to ease your way into managing Hadoop:

Hortonworks Sandbox
Hortonworks Sandbox Guide
Operations
Deploying Hortonworks Sandbox on Microsoft Azure
Overview The Azure cloud infrastructure has become a commonplace for users to deploy virtual machines on the cloud due to its’ flexibility, ease of deployment, and cost benefits. In addition, Microsoft has expanded Azure to include a marketplace with thousands of certified, open source, and community software applications, developer services, and data—pre-configured for Microsoft Azure. […]
Deploying, managing and configuring HDP with Ambari 1.7
Overview Apache Ambari is a completely open operational framework for provisioning, managing and monitoring Apache Hadoop clusters. Ambari includes an intuitive collection of operator tools and a set of APIs that mask the complexity of Hadoop, simplifying the operation of clusters. In this tutorial, we will walk through the some of the key aspects of […]
Create a Falcon Cluster
Introduction Apache Falcon is a framework to simplify data pipeline processing and management on Hadoop clusters. It makes it much simpler to onboard new workflows/pipelines, with support for late data handling and retry policies. It allows you to easily define relationship between various data and processing elements and integrate with metastore/catalog such as Hive/HCatalog. Finally […]
Mirroring Datasets between Hadoop clusters with Apache Falcon
Introduction Apache Falcon is a framework to simplify data pipeline processing and management on Hadoop clusters. It provides data management services such as retention, replications across clusters, archival etc. It makes it much simpler to onboard new workflows/pipelines, with support for late data handling and retry policies. It allows you to easily define relationship between […]
Introducing Apache Ambari for deploying and managing Apache Hadoop
Introduction In this tutorial, we will explore how to quickly and easily deploy Apache Hadoop with Apache Ambari. We will spin up our own VM with Vagrant and Apache Ambari. Vagrant is very popular with developers as it lets one mirror the production environment in a VM while staying with all the IDEs and tools in the comfort […]
Processing Data Pipeline with Apache Falcon
Introduction Apache Falcon is a framework to simplify data pipeline processing and management on Hadoop clusters. It makes it much simpler to onboard new workflows/pipelines, with support for late data handling and retry policies. It allows you to easily define relationship between various data and processing elements and integrate with metastore/catalog such as Hive/HCatalog. Finally […]
Configuring YARN Capacity Scheduler with Apache Ambari
In this tutorial we are going to explore how we can configure YARN Capacity Scheduler from Ambari. Introduction YARN’s Capacity Scheduler is designed to run Hadoop applications in a shared, multi-tenant cluster while maximizing the throughput and the utilization of the cluster. Traditionally each organization has it own private set of compute resources that have […]
Using Apache Ambari to add new nodes to your existing cluster
Apache Hadoop clusters grow and change with use. Maybe you used Apache Ambari to build your initial cluster with a base set of Hadoop services targeting known use cases and now you want to add other services for new use cases. Or you may just need to expand the storage and processing capacity of the […]
Manage Files on HDFS via CLI/Ambari Files View
Using HDFS Snapshots to protect important Enterprise datasets
Sometime back, we introduced the ability to create snapshots to protect important enterprise data sets from user or application errors. HDFS Snapshots are read-only point-in-time copies of the file system. Snapshots can be taken on a subtree of the file system or the entire file system and are: Performant and Reliable: Snapshot creation is atomic and […]
How to Install and Configure the Hortonworks ODBC driver on Mac OS X
This Hadoop tutorial describes how to install and configure the Hortonworks ODBC driver on Mac OS X. After you install and configure the ODBC driver, you will be able to access Hortonworks sandbox data using Excel
How to Install and Configure the Hortonworks ODBC driver on Windows 7
This tutorial walks you through how to install and configure the Hortonworks ODBC driver on Windows 7.

## Real World Examples
### Learning the Ropes of the Hortonworks Sandbox
Introduction This tutorial is aimed for users who do not have much experience in using the Sandbox. We will install and explore the Sandbox on virtual machine and cloud environments. We will also navigate the Ambari user interface. Let’s begin our Hadoop journey. Pre-Requisites Downloaded and Installed Hortonworks Sandbox Allow yourself around one hour to […]
## Security
Securing your Data Lake Resource & Auditing User Access with HDP Advanced Security
In this tutorial we will explore how you can use policies in HDP Advanced Security to protect your enterprise data lake and audit access by users to resources on HDFS, Hive and HBase from a centralized HDP Security Administration Console.
Securing HDFS, Hive and HBase with Knox and Ranger
Introduction Apache Ranger delivers a comprehensive approach to security for a Hadoop cluster. It provides a central security policy administration across the core enterprise security requirements of authorization, accounting and data protection. Apache Ranger already extends baseline features for coordinated enforcement across Hadoop workloads from batch, interactive SQL and real–time in Hadoop. In this tutorial, […]
Tag based policies with Apache Ranger and Apache Atlas
Introduction Hortonworks has recently announced the integration of Apache Atlas and Apache Ranger, and introduced the concept of tag or classification based policies. Enterprises can classify data in Apache Atlas and use the classification to build security policies in Apache Ranger. This tutorial walks through an example of tagging data in Atlas and building a […]
Hadoop Security and Data Protection with Protegrity Avatar
Protegrity Avatar™ for Hortonworks® extends the capabilities of HDP native security with Protegrity Vaultless Tokenization (PVT), Extended HDFS Encryption, and the Protegrity Enterprise Security Administrator, for advanced data protection policy, key management and auditing. In the Protegrity Avatar for Hortonworks Sandbox Add-on and Tutorial, you’ll Learn How To: Protect and unprotect field-level data using policy-based […]
PROTEGRITY
Hortonworks Sandbox hosted on Bit Refinery
The hosted Hortonworks Sandbox from Bit Refinery provides an easy way to experience and learn Hadoop with ease. All the tutorials available from HDP work just as if you were running a localized version of the Sandbox. Here is how our “flavor” of Hadoop interacts with the Hortonworks platform: alt text Our new tutorial will […]
BIT REFINERY
Cross Component Lineage with Apache Atlas across Apache Sqoop, Hive, Kafka & Storm
Introduction Hortonworks introduced Apache Atlas as part of the Data Governance Initiative, and has continued to deliver on the vision for open source solution for centralized metadata store, data classification, data lifecycle management and centralized security. Atlas is now offering, as a tech preview, cross component lineage functionality, delivering a complete view of data movement […]
Securing your Hadoop Infrastructure with Apache Knox
Introduction In this tutorial we will walk through the process of Configuring Apache Knox and LDAP services on HDP Sandbox Run a MapReduce Program using Apache Knox Gateway Server What is Apache Knox? The Apache Knox Gateway is a system that provides a single point of authentication and access for Apache™ Hadoop® services. It provides […]
Securing JDBC and ODBC Clients’ Access to HiveServer2 using Apache Knox
Introduction HDP 2.5 ships with Apache Knox 0.6.0. This release of Apache Knox supports WebHDFS, WebHCAT, Oozie, Hive, and HBase REST APIs. Apache Hive is a popular component used for SQL access to Hadoop, and the Hive Server 2 with Thrift supports JDBC access over HTTP. The following steps show the configuration to enable a […]
Fine-Grained Permissions for HDFS Files in Hadoop using HDFS ACLs
Securing any system requires you to implement layers of protection.  Access Control Lists (ACLs) are typically applied to data to restrict access to data to approved entities. Application of ACLs at every layer of access for data is critical to secure a system. The layers for hadoop are depicted in this diagram and in this […]
## Security and Governance
Tag based policies with Apache Ranger and Apache Atlas
Introduction Hortonworks has recently announced the integration of Apache Atlas and Apache Ranger, and introduced the concept of tag or classification based policies. Enterprises can classify data in Apache Atlas and use the classification to build security policies in Apache Ranger. This tutorial walks through an example of tagging data in Atlas and building a […]
Cross Component Lineage with Apache Atlas across Apache Sqoop, Hive, Kafka & Storm
Introduction Hortonworks introduced Apache Atlas as part of the Data Governance Initiative, and has continued to deliver on the vision for open source solution for centralized metadata store, data classification, data lifecycle management and centralized security. Atlas is now offering, as a tech preview, cross component lineage functionality, delivering a complete view of data movement […]
## HADOOP FOR DATA SCIENTISTS & ANALYSTS
Get Started with data analysis on Hadoop. These tutorials are designed to help you make the most of data with Hadoop:

## From our partners
### Using JReport to visualize data on Hortonworks Data Platform
Introduction JReport is a embedded BI reporting tool can easily extract and visualize data from the Hortonworks Data Platform 2.3 using the Apache Hive JDBC driver. You can then create reports, dashboards, and data analysis, which can be embedded into your own applications. In this tutorial we are going to walkthrough the folllowing steps to […]

### Getting started with Pivotal HAWQ on Hortonworks Sandbox
Pivotal HAWQ provides strong support for low-latency analytic SQL queries, coupled with massively parallel machine learning capabilities on Hortonworks Data Platform (HDP). HAWQ is the World’s leading SQL on Hadoop tool. It provides the richest SQL dialect with an extensive data science library called MADlib at milliseconds query response times. HAWQ enables discovery-based analysis of […]
PIVOTAL
## Introduction to Data Analysis with Hadoop
### How to Process Data with Apache Hive
This Hadoop tutorial shows how to Process Data with Hive using a set of driver data statistics.
### How To Process Data with Apache Pig
This Hadoop tutorial shows how to Process Data with Apache Pig using a set of driver data statistics.
### Interactive Query for Hadoop with Apache Hive on Apache Tez
How to use Apache Tez and Apache Hive for Interactive Query with Hadoop and Hortonworks Data Platform 2.5
How to Install and Configure the Hortonworks ODBC driver on Mac OS X
This Hadoop tutorial describes how to install and configure the Hortonworks ODBC driver on Mac OS X. After you install and configure the ODBC driver, you will be able to access Hortonworks sandbox data using Excel
How to Install and Configure the Hortonworks ODBC driver on Windows 7
This tutorial walks you through how to install and configure the Hortonworks ODBC driver on Windows 7.
Using Hive for Data Analysis
Deprecated This tutorial will no longer be available starting May 1st, 2016. Overview Hive is designed to enable easy data summarization and ad-hoc analysis of large volumes of data. It uses a query language called Hive-QL which is similar to SQL. In this tutorial, we will explore the following: Load a data file into a […]
Beginners guide to Apache Pig
This Hadoop tutorial will enable you to gain a working knowledge of Pig and hands-on experience creating Pig scripts to carry out essential data operations and tasks.
How to Use HCatalog, Pig & Hive Commands
This Hadoop tutorial shows how to use HCatalog, Pig and Hive to load and process data using a driver data statistics.
Deriving Business Insight from Data using Microsoft Excel and Hortonworks Data Platform
Learn how to visualize data using Microsoft BI and HDP with 10 years of raw stock ticker data from NYSE.
MICROSOFT
Data Integration with Talend
In this tutorial, you’ll learn how to connect the Sandbox to Talend to quickly build test data for your Hadoop environment.
TALEND
Using Revolution R Enterprise with Hortonworks Sandbox
In this tutorial the user will be introduced to Revolution R Enterprise and how it works with the Hortonworks Sandbox. A data file will be extracted from the Sandbox using ODBC and then analyzed using R functions inside Revolution R Enterprise.
REVOLUTION ANALYTICS
Business Discovery and Visualizing Your Data in HDP Using QlikView
Introduction Welcome to the QlikView (Business Discovery Tools) tutorial developed by Qlik™. The tutorial is designed to help you get connected with QlikView within minutes, to access data from the Hortonworks Sandbox or Hortonworks Data Platform (HDP). QlikView will allow you to immediately gain personalized analytics and discover insights into data residing in the Sandbox […]
QLIK
Real World Examples
Visualize Website Clickstream Data
How do you improve the chances that your online customers will complete a purchase? Hadoop makes it easier to analyze and then change how visitors behave on your website. Here you can see how an online retailer optimized buying paths to reduce bounce rates and improve conversions. HDP can help you capture and refine website clickstream data to exceed your company’s e-commerce goals. The tutorial that comes with this video describes how to refine raw clickstream data using HDP.
Refine and Visualize Server Log Data
Security breaches happen. And when they do, server log analysis helps you identify the threat and then protect yourself better in the future. See how Hadoop takes server-log analysis to the next level by speeding forensics, retaining log data for longer and demonstrating compliance with IT policies. The tutorial that comes with this video describes how to refine raw server log data using HDP.
Analyzing Social Media and Customer Sentiment With Apache NiFi and HDP Search
With Hadoop, you can mine Twitter, Facebook and other social media conversations to analyze customer sentiment about you and your competition. With more social Big Data, you can make more targeted, real-time, decisions. The tutorial that comes with this video describes how to refine raw Twitter data using HDP.
How To Analyze Machine and Sensor Data
Machines know things. Sensors stream low-cost, always-on data. Hadoop makes it easier for you to store and refine that data and identify meaningful patterns, providing you with the insight to make proactive business decisions using predictive analytics. See how Hadoop can be used to analyze heating, ventilation and air conditioning data to maintain ideal office temperatures and minimize expenses
Natural Language Processing and Sentiment Analysis for Retailers using HDP and ITC Infotech Radar
RADAR is a software solution for retailers built using ITC Handy tools (NLP and Sentiment Analysis engine) and utilizing Hadoop technologies in …
ITC INFOTECH
Predictive Analytics on H2O and Hortonworks Data Platform
Introduction H2O is the open source in memory solution from 0xdata for predictive analytics on big data. It is a math and machine learning engine that brings distribution and parallelism to powerful algorithms that enable you to make better predictions and more accurate models faster. With familiar APIs like R and JSON, as well as […]
H2O
INTEGRATION GUIDES FROM PARTNERS
These tutorials illustrate key integration points with partner applications.

Multi-channel Retail Enterprise 360 Degree View of Customers
In this tutorial you will learn how to do a 360 degree view of a retail business’ customers using the Datameer Playground, which is built on the Hortonworks Sandbox.
DATAMEER
Visualize Data with Tableau
In this tutorial you will learn how to connect the Hortonworks Sandbox to Tableau so that you can visualize data from the Sandbox.
TABLEAU SOFTWARE
Deploying Hadoop ETL in the Hortonworks Sandbox
In this tutorial you will learn how to run ETL and construct MapReduce jobs inside the Hortonworks Sandbox.
SYNCSORT
Data Integration with Talend
In this tutorial, you’ll learn how to connect the Sandbox to Talend to quickly build test data for your Hadoop environment.
TALEND
Cascading Pattern
Learn how to use Cascading Pattern to quickly migrate Predictive Models (PMML) from SAS, R, MicroStrategy onto Hadoop and deploy them at scale.
CONCURRENT
Personalized Analytics and Insights with BIRT for Hadoop
Learn to configure BIRT (Business Intelligence and Reporting Tools) to access data from the Hortonworks Sandbox. BIRT is used by more than 2.5 million developers to quickly gain personalized insights and analytics into Java / J2EE applications
ACTUATE
Configure Hortonworks Sandbox Version 2.0 with Hunk: Splunk Analytics for Hadoop
Connect Hortonworks Sandbox Version 2.0 with Hortonworks Data Platform 2.0 to Hunk™: Splunk Analytics for Hadoop. Hunk offers an integrated platform to rapidly explore, analyze and visualize data that resides natively in Hadoop
SPLUNK
Connecting SAP Portfolio of Products to the Hortonworks Sandbox
Learn how to setup SAP Portofolio of products (SQL Anywhere, Sybase IQ, BusinessObjects BI, HANA and Lumira) with the Hortonworks Sandbox to tap into big data at the speed of business.
SAP
MicroStrategy, Apache Hive and the Hortonworks Sandbox
MicroStrategy uses Apache Hive (via ODBC connection) as the defacto standard for SQL access in Hadoop. Establishing a connection from MicroStrategy to Hadoop and the Hortonworks Sandbox is illustrated here
MICROSTRATEGY
Using Revolution R Enterprise with Hortonworks Sandbox
In this tutorial the user will be introduced to Revolution R Enterprise and how it works with the Hortonworks Sandbox. A data file will be extracted from the Sandbox using ODBC and then analyzed using R functions inside Revolution R Enterprise.
REVOLUTION ANALYTICS
Deriving Business Insight from Data using Microsoft Excel and Hortonworks Data Platform
Learn how to visualize data using Microsoft BI and HDP with 10 years of raw stock ticker data from NYSE.
MICROSOFT
Business Discovery and Visualizing Your Data in HDP Using QlikView
Introduction Welcome to the QlikView (Business Discovery Tools) tutorial developed by Qlik™. The tutorial is designed to help you get connected with QlikView within minutes, to access data from the Hortonworks Sandbox or Hortonworks Data Platform (HDP). QlikView will allow you to immediately gain personalized analytics and discover insights into data residing in the Sandbox […]
QLIK
Get Started with Cascading on Hortonworks Data Platform 2.1
how to get started with Cascading and Hortonworks Data Platform using the Word Count Example.
CONCURRENT
Predictive Analytics on H2O and Hortonworks Data Platform
Introduction H2O is the open source in memory solution from 0xdata for predictive analytics on big data. It is a math and machine learning engine that brings distribution and parallelism to powerful algorithms that enable you to make better predictions and more accurate models faster. With familiar APIs like R and JSON, as well as […]
H2O
Natural Language Processing and Sentiment Analysis for Retailers using HDP and ITC Infotech Radar
RADAR is a software solution for retailers built using ITC Handy tools (NLP and Sentiment Analysis engine) and utilizing Hadoop technologies in …
ITC INFOTECH
Analyzing Graph Data with Sqrrl and HDP
In this tutorial we are going to walk through loading and analyzing graph data with Sqrrl and HDP. Sqrrl just announced the availability of the latest Sqrrl Test Drive VM in partnership with the Hortonworks Sandbox, running HDP 2.1! This gives users a frictionless way to try out the features of Sqrrl without needing to […]
SQRRL
Federated Hadoop with Security using HDP and Red Hat JBoss Data Virtualization
This use case is the sentiment analysis and sales analysis with Hadoop and MySQL. It uses one Hortonworks Data Platform VM for the twitter sentiment data and one MySQL database for the sales
data.
RED HAT
Hadoop Security and Data Protection with Protegrity Avatar
Protegrity Avatar™ for Hortonworks® extends the capabilities of HDP native security with Protegrity Vaultless Tokenization (PVT), Extended HDFS Encryption, and the Protegrity Enterprise Security Administrator, for advanced data protection policy, key management and auditing. In the Protegrity Avatar for Hortonworks Sandbox Add-on and Tutorial, you’ll Learn How To: Protect and unprotect field-level data using policy-based […]
PROTEGRITY
Explore the Possibilities of SAS Software and Hortonworks Sandbox
Learn how to prepare, integrate and cleanse big data faster than ever in Hadoop using the power of SAS software with the Hortonworks Sandbox.
SAS
Manage your Data Lake more efficiently with Waterline Data Inventory and HDP
Download the turn-key Waterline Data Sandbox preloaded with HDP, Waterline Data Inventory and sample data with tutorials in one package. Waterline Data Inventory enables users of Hadoop to find, understand, and govern data in their data lake. How do you get the Waterline Data advantage? It’s a combination of automated profiling and metadata discovery, and […]
WATERLINE DATA
Hortonworks Sandbox hosted on Bit Refinery
The hosted Hortonworks Sandbox from Bit Refinery provides an easy way to experience and learn Hadoop with ease. All the tutorials available from HDP work just as if you were running a localized version of the Sandbox. Here is how our “flavor” of Hadoop interacts with the Hortonworks platform: alt text Our new tutorial will […]
BIT REFINERY
Simplified Deployment and Unified Management of HDP on Cisco UCS
Hadoop is fast emerging as a mainstay in enterprise data architectures. To meet the increasing demands of business owners and resource constraints, IT teams are challenged to provide an enterprise grade cluster that can be consistently and reliably deployed. The complexities of the varied Hadoop services and their requirements make it more onerous and time […]
CISCO