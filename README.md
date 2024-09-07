# mongdb

# How things were done first of all created the code space
``
one of the best feature that I think the internet has they are providing this much of free services to the world and yet people think shivilery is dead no sir not at all
``

# After that few simple command to run 

``
press F1 in the search bar type dev and select the first option saying add dev 
container config file 
this is basically the environment setting of the whole project
``
![Reference for the setup](./codepace%20connecting%20to%20mongo%20in%20github%20.png)


# after that 
Select create a new one<br>
search for node and Mongo select the version default things for the last don't select anything and hit ok
---

```
npm init -y
```

you will have the option mongodb like thing opening infront of you just got to forms sect the right side one and connect database it will start the thingi 


after that install the mongoose and express
```
npm i mongoose express
```



# After that 

``
setting up the system insdie the github code space to understand how things work their
``


## Mouse is not working properly and database were created from the terminal using commands like 

```js
show dbs
```

but first make sure to run the database


the below command will create a database if not exist and if does then simply move switch to that one 

```js
use databaseName
```

To create a simple collection inside the respective databse but need to be in that databse first

```js
db.createCollection("NameIt")
```

Now to drop a databse 
```js
db.dropDatabase("YourDatabaseName")
```

### To iNsert objects into the collection created use the commands below
```js
db.UserCredentials.insertOne({name: "theName", age:23, gpa:3.4})
```

## To insert many Set of objects at a time useing the command called insertMany first need to be in the databse use mood or thing like that 

```js
db.CollectionName.insertMany([{name:"temp", age:34, gpa:3.4}, {object: "NeedNot To be COnsistent", age:2}])
```

to check the object use command 
```js
db.collectionName.find()
```

to show the objects from specific collection in some sorted manner using following code
```js
db.CollectionName.find().sort({name:1})
```

same goes for the limit thing

```js
db.CollectionName.find().limit(3)
```

And Yes both these can be used 

```js
db.CollectionName.find().sort({age:1})limit(3)
```

here is how you add filter to the method of find
``
two parameters are send to the funtion first the query second the projection
find({query}, {projection})
``

query is the if else thingi 
project will give the values that are true and hide the one's that are false like in the case below the object _id that is default with them
```js
db.UserCredential.find({age:3},{_id:false,name:true})
```
# Operators 

## THE NOT EQUAL operator for comparison

```js
db.CollectionName.find({name:{$ne: "TheName"}})
```

this will give the objects inside the collection that have a name ``not equal`` to the name given


in tha same way the ``gt`` is used for ``greater than`` operation <be>
and for ``greater than equal`` ``gte`` is used 
