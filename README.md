# Implementing Attribute based Access Control for MongoDB 

The goal of the project was to implement Attribute based Access Control in NoSQL Databases like MongoDB. 

NoSQL Databases: Databases with flexible schemas unlike relational databases.

## MongoDB

MongoDB is a cross-platform, document oriented database that provides great performance and availability and is well known for easy scalability.
MongoDB works on the concept of collection and document. In MongoDB, there is no concept of relationship between tables. It is schemaless
and has no complex joins. MongoDB supports dynamic queries on documents using a document-based query language that's nearly as powerful as SQL.
MongoDB stores data records as BSON documents. BSON is a binary representation of JSON documents, though it contains more data types than JSON.
MongoDB documents are composed of field-and-value pairs.

![Image]()

## What's Attribute based Access Control?

ABAC is defined as an access control method where access is mediated based on a set of attributes and their associated values, where each attribute represents a particular characteristic of a subject, object, or the environment in which the access request is being made. Based on the combination of these attributes that is the subject, object and the environment the access is granted or denied. ABAC provides support for access control decision making without a prior knowledge of the object by the subject or knowledge of the subject by the object owner. ABAC is implemented to reduce risks due to unauthorized access, as it can control security and access on a more fine-grained basis.

![Image]()

For instance, in the above figure, if the following predefined policy is satisfied, only then the access is granted:

IF a subject in the Applied Data Science Department with the role of HOD who is trying to read a finance folder during college hours and is connected to the LAN in San Jose, THEN they are permitted to read the folder.

## Data

We created a database using the MongoDB Compass. You can use any data of your choice and append it to MongoDB database.

## Files provided in the repo and how to use them

The code consists of two .py files and a few HTML files. Then we also have a pickle file to load values keyed into the page and to dump the same values to ABAC.py file to grant or revoke access accordingly.

## Flowchart for MongoDB

![Image]()

## Output Generation

The data to be accessed is stored and can be viewed in MongoDB Compass. The data (.csv) is displayed on html file (result.html) only if the subject attributes, object (or resource) attributes and environmental attributes match or agree with the existing policy/policies. (The data accessed here is: Human Resources Attrition Dataset, which contains 50 documents or records).

## Output Images

![Image]()

*Figure: when attributes not satisfying policy are keyed in.*

![Image]()

*Figure: when attributes satisfying policy are keyed in.*






