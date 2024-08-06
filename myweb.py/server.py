from flask import Flask,render_template


app=Flask(__name__,template_folder="template",static_folder="static")
app.config['TESTING'] = True

@app.route("/")
def home():
    return render_template("t index.html")

if __name__=="__main__":
    app.run()
