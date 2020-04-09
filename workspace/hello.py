from flask import Flask
# 导入Flask模块
app = Flask(__name__)
# 创建Flask对象并且以当前模块的名称作为参数

@app.route('/hello/<name>')
# route是个装饰器，
# app.route(rule, options)，rule 绑定的URL，options 转发给基础Rule对象的参数列表
# route装饰器可将URL绑定到函数，URL需要是规范的URL
# @app.route(‘/hello’) 等同于 app.add_url_rule(‘/’, ‘hello’, hello_world)
def hello_name(name):
   return "Hello %s!" % name

# 通过向规则参数添加变量部分，可以动态构建URL。
# 此变量部分标记为<variable-name>。它作为关键字参数传递给与规则相关联的函数。
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()
   # Flask类的 run方法在本地开发服务器上运行应用程序
   # app.run(host, port, debug, options)
   # host 要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用
   # port 监听端口，默认值为5000
   # debug 默认为false，设置为true可提供调试信息
   # options 要转发到底层的Werkzeug服务器