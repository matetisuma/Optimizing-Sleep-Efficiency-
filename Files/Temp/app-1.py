import pickle
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
model = pickle.load(open('Flask\model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sec', methods=["POST","GET"])
def sec():
    return render_template('second.html')

@app.route('/predict', methods=["POST","GET"])
def predict():
    a = float(request.form["a"])
    b = float(request.form["b"])
    c = float(request.form["c"])
    d = float(request.form["d"])
    e = float(request.form["e"])
    f = float(request.form["f"])
    g = float(request.form["g"])
    h = float(request.form["h"])
    i = float(request.form["i"])
    j = float(request.form["j"])
    k = float(request.form["k"])
    l = float(request.form["l"])
    feature_val = [a,b,c,d,e,f,g,h,i,j,k,l]
    result = model.predict([feature_val])
    
    return render_template('second.html',eff=result)



if __name__ == '__main__':
   app.run(debug=True)