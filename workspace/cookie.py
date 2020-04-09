from flask import Flask, render_template, request, json, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_cookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'

'''
@app.route('/delcookie', methods=['GET'])
def delCookie():
    response = make_response('delCookie')
    response.delete_cookie('id')
    return response
'''
# 上面是删除cookie的方法，不知道怎么才算测试正确，可用性不保证

app.run(debug = True)