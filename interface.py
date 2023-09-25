from flask import Flask, render_template, jsonify, request
import config
from utils import Redwinequality
from werkzeug.datastructures import MultiDict
import traceback
app = Flask(__name__)

@app.route('/')
def home():
    return render_template ("index.html")


@app.route('/predict_quality', methods = ["GET","POST"])
def predict_quality():
    try:
        if request.method == "POST":
            data = request.form.get

            fixed_acidity = eval(data('fixed_acidity'))
            volatile_acidity  = eval(data("volatile_acidity"))
            citric_acid = eval(data("citric_acid"))
            residual_sugar  = eval(data("residual_sugar"))
            chlorides = eval(data("chlorides"))
            free_sulfur_dioxide = eval(data("free_sulfur_dioxide"))
            total_sulfur_dioxide = eval(data("total_sulfur_dioxide"))
            density = eval(data("density"))
            pH = eval(data("pH"))
            sulphates = eval(data("sulphates"))
            alcohol  = eval(data("alcohol"))

            wine_quality= Redwinequality(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol)
            quality = wine_quality.get_predict_quality()

            if quality == 0:
                return render_template('index.html',prediction = 'The quality of red wine is Bad')
            elif quality == 1:
                return render_template('index.html',prediction = 'The quality of red wine is Good')
            # return  render_template("index.html",prediction = quality)
            
             
        else:
            data = request.args.get

            # print("User Data is :",data)
            fixed_acidity = eval(data('fixed_acidity'))
            volatile_acidity  = eval(data("volatile_acidity"))
            citric_acid = eval(data("citric_acid"))
            residual_sugar  = eval(data("residual_sugar"))
            chlorides = eval(data("chlorides"))
            free_sulfur_dioxide = eval(data("free_sulfur_dioxide"))
            total_sulfur_dioxide = eval(data("total_sulfur_dioxide"))
            density = eval(data("density"))
            pH = eval(data("pH"))
            sulphates = eval(data("sulphates"))
            alcohol  = eval(data("alcohol"))

            wine_quality = Redwinequality(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol)
            quality = wine_quality.get_predict_quality()

            if quality == 0:
                return render_template('index.html',prediction = 'The quality of red wine is Bad')
            elif quality == 1:  
                return render_template('index.html',prediction = 'The quality of red wine is Good')
            # return  render_template("index.html" ,prediction=quality)
            
    except:
        print(traceback.print_exc())
        # return  jsonify({"Message" : "Unsuccessful"})           


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config.PORT_NUMBER,debug=False)




   
