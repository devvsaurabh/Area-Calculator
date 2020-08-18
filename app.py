from flask import Flask,render_template,request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",value="")

@app.route('/success/',methods=["POST"])
def fetch_data():
    try:
        data = request.form.to_dict()
        area_c = int(data["circle"])
        d = {}
        d['area_square'] = area_c
        d['area_c'] = area_c
        d['side'] = math.sqrt(area_c)
        d['dia'] = math.sqrt((area_c*7*4)/(22))
        return render_template('index.html',value = d)
    except Exception as e:
        print(e)
    return render_template("index.html",value="")



if __name__ == '__main__':
    app.run(debug=True)