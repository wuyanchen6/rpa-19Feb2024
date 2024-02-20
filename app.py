from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))

@app.route("/",methods=["GET","POST"])
def main()
r = request.form.get("r")
return(render_template("index.html",r=r))

@app.route("/imagegpt",methods=["GET","POST"])
def main()
return(render_template("index.html",))


if __name__ == "__main__":

  
  app.run()
