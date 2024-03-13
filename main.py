from flask import Flask,jsonify,render_template,request

from project_app.utils import Heart



app = Flask(__name__)
@app.route("/")
def hello_flask():
    print("Welcome to our world")
    return render_template("index.html") 



@app.route("/predict_charges", methods=["POST", "GET"])
def get_heart_pred():
    if request.method == "GET":
        print("We are in a GET Method")
                
        age = eval(request.args.get("age"))
        sex = eval(request.args.get("sex"))
        cp = eval(request.args.get("cp"))
        trestbps = eval(request.args.get("trestbps"))
        chol = eval(request.args.get("chol"))
        fbs = eval(request.args.get("fbs"))
        restecg = eval(request.args.get("restecg"))
        thalach = eval(request.args.get("thalach"))
        exang = eval(request.args.get("exang"))
        oldpeak = eval(request.args.get("oldpeak"))
        slope = eval(request.args.get("slope"))
        ca = eval(request.args.get("ca"))
        thal = eval(request.args.get("thal"))
        
        heart_test =  Heart(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        charges = heart_test.get_predicted_value()
        
        positive = "Yes,person has heart decease"
        negative = "No,person don't have heart decease"
    
        if charges == 1:
            return render_template("index.html", prediction=positive)
            
        else:
            return render_template("index.html", prediction=negative)
            
        
        


print("__name__-->",__name__)

app.run(host="0.0.0.0", port=5000, debug=False)

