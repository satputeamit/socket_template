import eventlet
eventlet.monkey_patch()

from flask import Flask,request,render_template
from flask_socketio import SocketIO
import os
import cv2


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
    


if __name__=="__main__":
    socketio.run(app,host="0.0.0.0",port=5000,use_reloader=False,debug=True)
