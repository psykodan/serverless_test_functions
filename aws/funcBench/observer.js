var MongoClient = require('mongodb').MongoClient;
const request = require('request');
var url = 'mongodb://mongodb5446kd:na3zez@danu7.it.nuigalway.ie:8717/mongodb5446';


//128MB
let start = Date.now();
request('https://45vbcux00g.execute-api.eu-west-1.amazonaws.com/bench/funcbench128', { json: true }, (err, res, body) => {
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
  dbo.collection("AWS").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

});


//256MB
let start = Date.now();
request('https://45vbcux00g.execute-api.eu-west-1.amazonaws.com/bench/funcbench256', { json: true }, (err, res, body) => {
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
  dbo.collection("AWS").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

});

//512MB
let start = Date.now();
request('https://45vbcux00g.execute-api.eu-west-1.amazonaws.com/bench/funcbench512', { json: true }, (err, res, body) => {
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
  dbo.collection("AWS").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

});

//1024MB
let start = Date.now();
request('https://45vbcux00g.execute-api.eu-west-1.amazonaws.com/bench/funcbench1024', { json: true }, (err, res, body) => {
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
  dbo.collection("AWS").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

});

//2048MB
let start = Date.now();
request('https://45vbcux00g.execute-api.eu-west-1.amazonaws.com/bench/funcbench2048', { json: true }, (err, res, body) => {
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
  dbo.collection("AWS").insertOne(data, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); 

});
