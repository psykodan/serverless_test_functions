var MongoClient = require('mongodb').MongoClient;
const request = require('request');
var url = 'mongodb://mongodb5446kd:na3zez@danu7.it.nuigalway.ie:8717/mongodb5446';



//128MB
function f128(){
let start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench128', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let stop = Date.now();
  let runtime = stop - start
  MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mongodb5446");
  var data = body;
  data.request = start;
  data.response = stop;
  data.runtime = runtime;
  data.memory = 128;
  dbo.collection("GCF").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

})};


//256MB
function f256(){
let start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench256', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let stop = Date.now();
  let runtime = stop - start
  MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mongodb5446");
  var data = body;
  data.request = start;
  data.response = stop;
  data.runtime = runtime;
  data.memory = 256;
  dbo.collection("GCF").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

})};

//512MB
function f512(){
let start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench512', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let stop = Date.now();
  let runtime = stop - start
  MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mongodb5446");
  var data = body;
  data.request = start;
  data.response = stop;
  data.runtime = runtime;
  data.memory = 512;
  dbo.collection("GCF").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

})};

//1024MB
function f1024(){
let start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench1024', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let stop = Date.now();
  let runtime = stop - start
  MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mongodb5446");
  var data = body;
  data.request = start;
  data.response = stop;
  data.runtime = runtime;
  data.memory = 1024;
  dbo.collection("GCF").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

})};

//2048MB
function f2048(){
let start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench2048', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let stop = Date.now();
  let runtime = stop - start
  MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mongodb5446");
  var data = body;
  data.request = start;
  data.response = stop;
  data.runtime = runtime;
  data.memory = 2048;
  dbo.collection("GCF").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

})};



f128();
f256();
f512();
f1024();
f2048();