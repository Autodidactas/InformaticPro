var io = require('socket.io').listen(8008);
var http = require('http');

io.sockets.on('connection', function(socket){
	socket.on('enVivo', function(data){
		http.get('http://google.com/', function(res){
			res.setEncoding('utf8');
			res.on('data', function(data){
				io.sockets.emit('isLive', data);
			});
		});
	});
});