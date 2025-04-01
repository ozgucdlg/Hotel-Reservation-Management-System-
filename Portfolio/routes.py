from Portfolio import app


@app.route('/')
def index():

    return "<h1 style='color:blue;'>Hello again and again</h1>"