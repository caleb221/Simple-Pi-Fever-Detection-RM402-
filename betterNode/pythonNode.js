//start.js
//
var code='sensorRandom.py';

const {PythonShell} = require('python-shell');
//i need to create main.js

var pyshell=new PythonShell(code);
var datData



	pyshell.on('message',function(message) 
	{
		console.log("Message from python:  "+message);
		//datData = message;
	});

	pyshell.stdout.on('data',function(data)
		{
		
			datData = data;
			console.log(data);
	//	return datData;
		});
	
	//load image here
	
	pyshell.end(function(err)
	{
		if(err)  throw err;
	  console.log('what happened?');
	});
