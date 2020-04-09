from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')

def hello_guest(guest):
   return 'Hello %s as Guest' % guest

# url_for函数用于动态构建特定函数的URL，函数名称为第一个参数，后续是函数的关键字参数（URL变量）
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
   app.run(debug = True)