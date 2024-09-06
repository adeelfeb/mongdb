const express = require("express")
const mongoose = require("mongoose")

const app = express()

const port = 3000

mongoose.connect('mongodb/Localhost:27017/test-db', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(()=>{
    console.log("Connected To MongoDb")
})
.catch((error)=>{
    console.log("Error While Connecting To DataBase: ", error)
})

app.listen(port, ()=>{
    console.log(`Server running on port ${port}`)
})

app.get('/hello', (req, res)=>{
    res.json({message: "Don't Know how this one is working but can relate to the thingi done in the Computer Networks Lab!!!!"})
})