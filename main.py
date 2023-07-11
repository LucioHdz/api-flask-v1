from flask import Flask,request
app = Flask(__name__) 


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

@app.route('/test/<n_celcius>')
def test(n_celcius):
    farenheit = n_celcius
    return {"farenheit":farenheit}


@app.route('/calcular',methods=['POST'])
def calcular():
    body = request.get_json()
    celcius=0
    if 'celcius'in body :
        celcius=body['celcius']
        return({'farenheit':celcius*2})
    return({'farenheit':celcius})



if __name__== '__main__':
    app.run()