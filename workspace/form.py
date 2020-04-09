from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if(request.method == 'POST'):
        return render_template('result.html', result = request.form)
#    else:
#        return render_template('student.html')
# 加了else之后也能跑，确实可以根据请求方法的不同（GET/POST）来路由到不同的模板页面
# 这里请求一开始挂了，URL不支持请求，后面在装饰器中指定了methods就好了
# request.form是个字典对象，也有迭代器，在模板中迭代就好了

app.run(debug = True)