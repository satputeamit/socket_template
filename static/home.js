var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port );
socket.emit('skt_load_log_files');

socket.on("skt_load_file_response",data=>{
    //load table using data
    console.log("msg",data)
})

//btn click on image and show image