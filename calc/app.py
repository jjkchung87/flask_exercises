from flask import Flask, request
import operations

app = Flask(__name__)


@app.route('/add')
def add():
    a=int(request.args['a'])
    b=int(request.args['b'])
    
    result = operations.add(a,b)
    return f'{a}+{b} = {result}'

@app.route('/sub')
def sub():
    a=int(request.args['a'])
    b=int(request.args['b'])
    
    result = operations.sub(a,b)
    return f'{a}-{b} = {result}'

@app.route('/mult')
def mult():
    a=int(request.args['a'])
    b=int(request.args['b'])
    
    result = operations.mult(a,b)
    return f'{a} x {b} = {result}'

@app.route('/div')
def div():
    a=int(request.args['a'])
    b=int(request.args['b'])
    
    result = operations.div(a,b)
    return f'{a} / {b} = {result}'


operators = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}


@app.route('/math/<operation>')
def calculate(operation):
    a=int(request.args['a'])
    b=int(request.args['b'])
    result = operators[operation](a,b)
    return f'{a} {operation} {b} = {result}'


@app.route('/math')
def inputForm():
    return '''
    <form method="POST">
        <input type='text' name='a' placeholder='value a'><br>
        <input type='text' name='b' placeholder='value b'><br>
        <select name="operation">
            <option value="add">Addition</option>
            <option value="sub">Subtraction</option>
            <option value="mult">Multiplication</option>
        <option value="div">Division</option>
        </select>
        <button type='submit'>SUBMIT</button>
    </form>
    '''

@app.route('/math', methods = ['POST'])
def output():
    a=int(request.form['a'])
    b=int(request.form['b'])
    operator = request.form['operation']
    result = operators[request.form['operation']](a,b)
    return f'{a} {operator} {b} = {result}'
    

    

        # <input type='radio' name='add' id='add'>
        # <label for='add'>Add</label><br>
        # <input type='radio' name='sub' id='sub'>
        # <label for='sub'>sub</label><br>
        # <input type='radio' name='mult' id='mult'>
        # <label for='mult'>mult</label><br>
        # <input type='radio' name='div' id='div'>
        # <label for='div'>div</label><br>
    






# @app.route('/<function>')
# def calculate(function):
#     a=int(request.args('a'))
#     b=int(request.args('b'))

#     print(operations[function])

#     # result =  operations[function](a,b)
#     # return result






# @app.route('/add')
# def add():
#     a= int(request.args['a'])
#     b= int(request.args['b'])

#     result = a+b    
#     return f"{result}"


# @app.route('/subtract')
# def present_form():
#     return '''
#     <form method="POST">
#         <input type='text' name='a'>
#         <input type='text' name='b'>
#         <button type='submit'>SUBMIT</button>
#     </form>
#     '''

# @app.route('/subtract', methods=["POST"])
# def subtract():
#     a = int(request.form['a'])
#     b = int(request.form['b'])
#     result = a-b
#     return f"{a}-{b}={result}"
