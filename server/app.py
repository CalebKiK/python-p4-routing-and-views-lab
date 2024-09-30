#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return Response(parameter, content_type='text/plain')

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "\n".join(str(i) for i in range(parameter)) + "\n"
    return Response(numbers, content_type='text/plain')

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            return Response("Error:Division by zero", status=400)
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return Response("Error: Unexpected operation", status=400)
        
    return Response(str(result), content_type='text/plain')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
