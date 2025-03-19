from flask import Flask
app= Flask(__name__)

@app.route('/')
def settingUp():

    return "<h1 style='color:blue;'>Hello again and again</h1>"