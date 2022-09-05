from flask import Flask, request
import json
import math
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



class Calculator(object):

    def __init__(self, formula):
        self.formula = formula

    def getResult(self):
        computation = None
        prev = float(self.formula['previousOperand'])
        current = float(self.formula['currentOperand'])
        if (math.isnan(prev) or math.isnan(current)): 
            return computation
        if self.formula['operation'] == '+':
            computation = prev + current
        elif self.formula['operation'] == '-':
            computation = prev - current
        elif self.formula['operation'] == '*':
            computation = prev * current
        elif self.formula['operation'] == '^':
            computation = math.pow(prev, current)
        elif self.formula['operation'] == '÷':
            computation = prev / current
        return computation




@app.route('/calculate', methods=['POST'])
@cross_origin()
def calculate():
    response = {}
    try:
        formula = request.get_json()
        result = Calculator(formula).getResult()
        response['result'] = result
        response["status_code"] = 200
    except Exception as e:
        print(str(e))
        response["status_code"] = 500
    return json.dumps(response)

if __name__ == "_main_":
     app.run(host='127.0.0.1', port=5000)

