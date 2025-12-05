from flask import Flask, render_template, request
import pickle
import numpy as np

# Flask uygulamasını başlat
app = Flask(__name__)

# Eğitilmiş modeli yükle
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    years_exp = float(request.form["years_exp"])
    num_projects = int(request.form["num_projects"])
    prog_langs = int(request.form["prog_langs"])
    remote = int(request.form["remote"])
    certs = int(request.form["certs"])
    lisans = int(request.form["lisans"])

    # Tek şehir dropdown'u
    city_level = int(request.form["city_level"])

    # One-Hot Encoding dönüşümü
    if city_level == 1:
        city2 = 0
        city3 = 0
    elif city_level == 2:
        city2 = 1
        city3 = 0
    else:
        city2 = 0
        city3 = 1

    # Modele uygun giriş
    input_data = np.array([[years_exp, num_projects, prog_langs, remote,
                            certs, city2, city3, lisans]])

    prediction = model.predict(input_data)[0]
    prediction = round(prediction, 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)