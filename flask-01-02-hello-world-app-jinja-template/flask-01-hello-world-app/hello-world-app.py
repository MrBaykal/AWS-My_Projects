from flask import Flask 

app = Flask(__name__)

@app.route('/')
def head():
<<<<<<< HEAD
    return 'Hello world, I am Emre Baykal'
=======
    return 'Hello world Emre'
>>>>>>> 5d29ba92bcf3ac24ba393444c84f236ae4bb4144


@app.route('/second')
def second():
    return 'This is second page'

@app.route('/third')
def third():
    return 'This is third page'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'


if __name__ == '__main__':

    # app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)

