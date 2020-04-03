from flask import Flask, request, render_template
import dict


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/return_info", methods=["POST"])
def return_info():
    return_string = dict.opening
    if request.method == "POST": 
       for i in request.form.keys():
           if i in dict.dict_of_camping_returns.keys():
               return_string = return_string + dict.dict_of_camping_returns[i]
           else:
               continue
    return_string = return_string + dict.close
    return return_string

@app.route("/return_info2", methods=["POST"])
def return_info():
    return_string = dict.opening
    if request.method == "POST": 
       for i in request.form.keys():
           if i in dict.dict_of_camping_returns.keys():
               return_string = return_string + dict.dict_of_camping_returns[i]
           else:
               continue
    return_string = return_string + dict.close
    return return_string

@app.route("/return_info3", methods=["POST"])
def return_info():
    return_string = dict.opening
    if request.method == "POST": 
       for i in request.form.keys():
           if i in dict.dict_of_camping_returns.keys():
               return_string = return_string + dict.dict_of_camping_returns[i]
           else:
               continue
    return_string = return_string + dict.close
    return return_string

@app.route("/return_info4", methods=["POST"])
def return_info():
    return_string = dict.opening
    if request.method == "POST": 
       for i in request.form.keys():
           if i in dict.dict_of_camping_returns.keys():
               return_string = return_string + dict.dict_of_camping_returns[i]
           else:
               continue
    return_string = return_string + dict.close
    return return_string



if __name__ == "__main__":
    app.run(debug=True)

