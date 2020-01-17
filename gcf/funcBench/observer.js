var MongoClient = require('mongodb').MongoClient;
const request = require('request');
var url = 'mongodb://mongodb5446kd:na3zez@danu7.it.nuigalway.ie:8717/mongodb5446';


//128MB
var start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench128', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  var stop = Date.now();
  var runtime = stop - start
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

});


//256MB
var start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench256', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  var stop = Date.now();
  var runtime = stop - start
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

});

//512MB
var start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench512', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  var stop = Date.now();
  var runtime = stop - start
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

});

//1024MB
var start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench1024', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  var stop = Date.now();
  var runtime = stop - start
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

});

//2048MB
var start = Date.now();
request('https://us-central1-spherical-plane-258017.cloudfunctions.net/funcBench2048', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  var stop = Date.now();
  var runtime = stop - start
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

});
