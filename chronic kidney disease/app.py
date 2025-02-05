from flask import *
import pickle
model=pickle.load(open("ckd.pkl","rb"))
encoder=pickle.load(open("encoderckd.pkl","rb"))
scaler=pickle.load(open('scalerckd.pkl',"rb"))
app=Flask(__name__)
@app.route("/")
def home():
    return render_template('ckd.html')
@app.route("/predict",methods=["POST",'GET'])
def predict():
    age=float(request.form.get['age'])
    bp=float(request.form.get['bp'])
    su=float(request.form.get['su'])
    rbc=encoder.transform([str(request.form.get['rbc'])])
    bgr=float(request.form.get['bgr'])
    bu=float(request.form.get['bu'])
    sod=float(request.form.get['sod'])
    pot=float(request.form.get['pot'])
    hemo=float(request.form.get['hemo'])
    rc=encoder.transform([str(request.form.get['rc'])])
    dm=encoder.transform([str(request.form.get['dm'])])
    input=[[age,bp,su,rbc,bgr,bu,sod,pot,hemo,rc,dm]]
    prediction=scaler.transform(input)
    output=prediction[0]
    if output==1:
        prediction_text="CKD as present"
    else:
        prediction_text="CKD as absent"