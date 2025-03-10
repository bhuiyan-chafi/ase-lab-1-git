from flask import Flask, request, make_response, jsonify

app = Flask(__name__, instance_relative_config=True)


@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a+b), 200)  # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

# Endpoint /sub for subtraction which takes a and b as query parameters.


@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a-b), 200)
    else:
        return make_response('Invalid input\n', 400)

# Endpoint /mul for multiplication which takes a and b as query parameters.


@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a*b), 200)
    else:
        return make_response('Invalid input\n', 400)

# Endpoint /div for division which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.


@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        if b == 0:
            return make_response('Division by zero\n', 400)
        return make_response(jsonify(s=a/b), 200)
    else:
        return make_response('Invalid input\n', 400)

# Endpoint /mod for modulo which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.


@app.route('/mod')
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        if b == 0:
            return make_response('Division by zero\n', 400)
        return make_response(jsonify(s=a % b), 200)
    else:
        return make_response('Invalid input\n', 400)

# Endpoint /random which takes a and b as query parameters and returns a random number between a and b included. Returns HTTP 400 BAD REQUEST if a is greater than b.


@app.route('/random')
def random():
    import random
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a and b:
        if a > b:
            return make_response('Invalid input\n', 400)
        return make_response(jsonify(s=random.randint(a, b)), 200)
    else:
        return make_response('Invalid input\n', 400)


if __name__ == '__main__':
    app.run(debug=True)

# /upper which gives the string a and it returns it in a JSON all in uppercase.


@app.route('/upper')
def upper():
    a = request.args.get('a', type=str)
    if a:
        return make_response(jsonify(s=a.upper()), 200)
    else:
        return make_response('Invalid input\n', 400)
