import eventlet
eventlet.monkey_patch()

from flask import Flask,request,render_template
from flask_socketio import SocketIO
import os
import cv2
from base64 import b64encode

app = Flask(__name__)
socketio = SocketIO(app,async_mode="eventlet",async_handlers=True,cookie=None)

@app.route("/")
def home():
    return render_template("home.html")

@socketio.on("skt_load_log_files")
def load_log_files():
    files = os.listdir(r"C:\Users\Amit\Desktop\suraj_poc\logged_images")
    socketio.emit("skt_load_file_response",{"files":files})

#take file name, search image, convert and send

@socketio.on("skt_selected_image")
def selected_image(msg):
    img = cv2.imread(r"C:\Users\Amit\Desktop\suraj_poc\logged_images\\"+msg["img_name"])
    _, photoJpeg = cv2.imencode('.jpg', img)
    strPhotoJpeg = b64encode(photoJpeg).decode('utf-8')
    socketio.emit("skt_show_image",{"image":strPhotoJpeg})

    


if __name__=="__main__":
    socketio.run(app,host="0.0.0.0",port=5000,use_reloader=False,debug=True)
