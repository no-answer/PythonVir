from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

# 建议在开始写代码之前规划好各个URL的作用（分割视图） 
@app.route('/')
def home():
   return render_template('home.html')
 
@app.route('/enternew')
def new_student():
   return render_template('student_SQLite.html')

# 获取新记录的POST表单并将其插入数据库 
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
 
 # with 表达式A as a 会将表达式A的返回值赋给a，并自己获取上下文的异常信息
 # with返回的对象必须要有__enter__()/__exit__()这两个方法
         with sql.connect("database.db") as con:
            cur = con.cursor()
 
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
 
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
 
      finally:
         return render_template("result_SQLite.html",msg = msg)
         con.close()
# 这里是python的异常处理，try语句包含一个或多个except语句
# 在执行try的过程中，若发生了异常，并且异常类型和某个except语句之后的名称相符，则转而执行相应的except语句
# 最后执行try之外的代码（finally），无论异常发生与否finally都会执行，但finally不是必须选项
# finally常用于文件关闭，释放锁，数据库关闭等
# try语句中可以有else语句，表示没有异常则执行的语句


# 展示整个数据库 
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
 
   cur = con.cursor()
   cur.execute("select * from students")
 
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)
 
if __name__ == '__main__':
   app.run(debug = True)