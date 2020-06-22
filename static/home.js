var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port );
socket.emit('skt_load_log_files');

socket.on("skt_load_file_response",data=>{
    //load table using data
    console.log(data);
    var tabl = $("#log_table");

    $("#log_table > tbody").html("");
    var i;
    var j;
    var cnt=0;


    for (i = 0; i < data.files.length; i++) {
          cnt=i+1;
          //added
          console.log(cnt);
          tabl.append(
          '<tr id="row'+cnt+'">' +
          '<td id =""'+cnt+'">'+cnt+'</td>'+
          '<td id =""'+cnt+'"><a href="#" onclick="edit_row(`'+data.files[i]+'`)">' +data.files[i]+'</a></td>'+
          '</tr>'
            );
        }
})

socket.on("skt_show_image",data=>{
  var dataURL="data:image/jpeg;base64,"+data.image;
  document.getElementById("logged_image").src = dataURL;
})
//btn click on image and show image

function edit_row(img_name)
{
  console.log(img_name);
  socket.emit('skt_selected_image',{img_name:img_name});
}