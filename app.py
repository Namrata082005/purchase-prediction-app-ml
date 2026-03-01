from flask import *
from pickle import load

# load model and scaler
f=open("purchase_knn.pkl", "rb")
model = load(f)
f.close()

f=open("scaler.pkl", "rb")
scaler = load(f)
f.close()

# flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    proba_no = None
    proba_yes = None

    if request.method == "POST":
        age = float(request.form.get("age"))
        salary = float(request.form.get("salary"))

        d = [[age, salary]]
        d_scaled = scaler.transform(d)

        prediction_val = model.predict(d_scaled)[0]
        proba = model.predict_proba(d_scaled)[0]

        prediction = "Will Purchase (1)" if prediction_val == 1 else "Will Not Purchase (0)"
        proba_no = round(proba[0]*100, 2)
        proba_yes = round(proba[1]*100, 2)

    return render_template("home.html", 
                           prediction=prediction, 
                           proba_no=proba_no, 
                           proba_yes=proba_yes)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
