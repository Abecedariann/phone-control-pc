var express=require('express');
var app=express();
app.listen(3001,()=>console.log('start'));
app.all('*', function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
	next();
});
app.get('/calc',function(req,res){
	res.json('calc');
	var exec=require('child_process').exec;
	var cmdstr='start notepad';
	exec(cmdstr,function(err,stdout,stderr,windowsHide=false){
		if(stdout){
			console.log('stderr');
		}else{
			var data=stdout;
			console.log('calc');
		}
	})
})
app.get('/pic',function(req,res){
	res.json('http://192.168.1.104:8080/?action=snapshot');
})
app.get('/close_pic',function(req,res){
	res.json('');
})
app.get('/shut',function(req,res){
	res.json('shutdown');
	var exec=require('child_process').exec;
	var cmdstr='shutdown -s -t 60';
	exec(cmdstr,function(err,stdout,stderr){
		if(stdout){
			console.log('stderr');
		}else{
			var data=stdout;
			console.log('shutdown -s -t 60');
		}
	})
})

//这里cmd要用绝对路径，不然会报错
app.get('/music',function(req,res){
	res.json('music');
	var exec=require('child_process').exec;
	// var cmdstr='py -3 music.py';
	
	var cmdstr='py -3 D:\\python program\\control_git\\music.py';
	exec(cmdstr,function(err,stdout,stderr,windowsHide=false){
		if(stdout){
			console.log('stderr');
		}else{
			var data=stdout;
			console.log('music');
		}
	})
})
app.get('/music_next',function(req,res){
	res.json('music_next');
	var exec=require('child_process').exec;
	// var cmdstr='py -3 music.py';
	var cmdstr='py -3 D:\\python program\\control_git\\music_next.py';
	exec(cmdstr,function(err,stdout,stderr,windowsHide=false){
		if(stdout){
			console.log('stderr');
		}else{
			var data=stdout;
			console.log('music_next');
		}
	})
})
app.get('/sound_add',function(req,res){
	res.json('+');
	var exec=require('child_process').exec;
	// var cmdstr='py -3 music.py';
	var cmdstr='D:\\python program\\control_git\\nircmd.exe changesysvolume 3000';
	exec(cmdstr,function(err,stdout,stderr,windowsHide=false){
		if(stdout){
			console.log('stderr');
		}else{
			var data=stdout;
			console.log('+');
		}
	})
})
app.get('/sound_low',function(req,res){
	res.json('-');
	var exec=require('child_process').exec;
	// var cmdstr='py -3 music.py';
	var cmdstr='D:\\python program\\control_git\\nircmd.exe changesysvolume -3000';
	exec(cmdstr,function(err,stdout,stderr,windowsHide=false){
		if(stdout){
			console.log('stderr');
		}else{
			var data=stdout;
			console.log('-');
		}
	})
})
app.get('/xiumian',function(req,res){
	res.json('xiumian');
	var exec=require('child_process').exec;
	// var cmdstr='py -3 music.py';
	var cmdstr='shutdown -h';
	exec(cmdstr,function(err,stdout,stderr,windowsHide=false){
		if(stdout){
			console.log('stderr');
		}else{
			var data=stdout;
			console.log('xiumian');
		}
	})
})
app.get('/unlock',function(req,res){
	res.json('unlock');
	var exec=require('child_process').exec;
	var cmdstr='start explorer.exe';
	exec(cmdstr,function(err,stdout,stderr,windowsHide=false){
		if(stdout){
			console.log('stderr');
		}else{
			var data=stdout;
			console.log('unlock');
		}
	})
})
app.get('/lock',function(req,res){
	res.json('lock');
	var exec=require('child_process');
	//taskkill /f /t /im explorer.exe //t=tree im=name
	exec.exec('taskkill /f /im explorer.exe',(err,stdout,stderr)=>{
		console.log(stdout)
	})
})
app.get('/face',function(req,res){
	res.json('face');
	var child_process=require('child_process')
	var workerProcess = child_process.exec('py -3 D:\\python program\\control_git\\face_comp.py', {})

	workerProcess.stdout.on('data', function (data) {
	    console.log('stdout: ' + data);
	});

	workerProcess.stderr.on('data', function (data) {
	    console.log('stderr: ' + data);
});

})