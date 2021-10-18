from flask import Flask, render_template, request, redirect, session, url_for
import json

app = Flask(__name__, template_folder= 'templates')
app.secret_key = "created_by_voronovich"

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/feedback", methods = ["POST", "GET"])
def feedback():
    if request.method == "POST":

        def load_data():            
            def get_id(data): return len(data)

            json_data = json.load(open("2task\data.json",))
            data_dict = {}
            print("aaa")
            data_dict["email"] = request.form['email'] if request.form['pers_data'] == "yes" else "anon"
            data_dict["feedback"] = request.form["feedback"]
            features = list()
            for i in range(1, 4):
                key_name = "feature" + str(i)
                try:
                    features.append(request.form[key_name])
                except:
                    pass
            data_dict["features"] = features

            json_data[get_id(json_data)] = data_dict
            json.dump(json_data, open("2task\data.json", "w"))

        session["user"] = request.form['email']
        load_data()
        return redirect(url_for("success"))
    else: return render_template("feedback.html")


@app.route("/success")
def success():
    if "user" in session: return render_template("success.html")
    else: return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug = True)