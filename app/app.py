from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<br> Time is :"+time.strftime('%A %B, %d %Y %H:%M:%S')+"</p>"

if __name__== '__main__':    
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80) 