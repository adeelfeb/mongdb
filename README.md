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
```
show dbs
```
but first make sure to run the database

```
the below command will create a database if not exist and if does then simply move switch to that one 

```
use databaseName
```

To create a simple collection inside the respective databse but need to be in that databse first

```
db.createCollection("NameIt")
```

Now to drop a databse 
```
db.dropDatabase("YourDatabaseName")
```

### To iNsert objects into the collection created use the commands below
```
db.UserCredentials.insertOne({name: "theName", age:23, gpa:3.4})
```

## To insert many Set of objects at a time useing the command called insertMany first need to be in the databse use mood or thing like that 

```
db.CollectionName.insertMany([{name:"temp", age:34, gpa:3.4}, {object: "NeedNot To be COnsistent", age:2}])
```

to check the object use command 
```
db.collectionName.find()
```