from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/hello_name/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)
# 之前这里一直链接不到templates文件夹下的html文件
# 原来是在route装饰器绑定的URL参数里面没有加变量
# templstes文件的模板中
# {% ... %}用于语句
# {{ ... }}用于表达式可以打印到模板输出
# {# ... #}用于未包含在模板输出中的注释
# # ... ##用于行语句

@app.route('/hello/<name>')
def hellp(name):
   return "hello! %s" % name

@app.route('/result/')
def result():
   dict = {'phy':50,'che':80,'maths':70}
   return render_template('result.html', result = dict)
# 这里也出现了一些问题，主要是教程中使用的python2，我使用的python3，有些函数接口不同
# 另外html模板文件也有点问题，修改之后就好了
# 对了，dict类在json包中，需要导入

app.run(debug = True)