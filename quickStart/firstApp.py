from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
@app.route('/')
def index():
    return render_template("index.html")
# app.add_url_rule('/', 'index', index)
# add_url_rule(<url rule>, <endpoint>, <view function>) 


@app.route('/success/<name>')
def success(name):
    return "Welcome %s" % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, port=8000)



'''
GET: to request data from the server.
POST: to submit data to be processed to the server.
PUT: A PUT request is used to modify the data on the server. It replaces the entire content at a particular location with data that is passed in the body payload. If there are no resources that match the request, it will generate one.
PATCH: PATCH is similar to a PUT request, but the only difference is, it modifies a part of the data. It will only replace the content that you want to update.
DELETE: A DELETE request is used to delete the data on the server at a specified location.
'''


'''
Syntax: flask.redirect(location,code=302)
Parameters:
    location(str): the location which URL directs to.
    code(int): The status code for Redirect.
    Code: The default code is 302 which means that the move is only temporary.


Error:
Syntax: abort(code, message)
    code: int, The code parameter takes any of the following values
    message: str, create your custom message Error.

'''