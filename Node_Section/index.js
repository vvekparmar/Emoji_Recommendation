const express = require('express')
const {spawn} = require('child_process')
var bodyParser = require('body-parser')
const path = require('path');
var cors = require('cors')
var env = require('dotenv').config()
const app = express()

app.use(cors())

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
var sentence = ""

app.get('/:text', function(req,res){
  var dataToSend
  sentence = req.params.text
  console.log(sentence)
  const sendData = spawn('python', ['emojiApp.py',sentence])
  
  sendData.stdout.on('data', function (data) {
    dataToSend = data.toString()
    console.log(dataToSend)
   })
  
  sendData.on('close', (code) => {
    res.status(200).json({message : "Emoji\'s fetched successfully", recommendations : dataToSend})
  })
})

app.get('/', function(req,res){
  res.json({getStatus : "Accepted"})
})

app.listen(process.env.PORT || 3000, () => {
  console.log("Running...");
});
