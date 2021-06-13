from types import MethodType
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The Reult is passed</h1></body></html>"


@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result checker
@app.route('/submit',methods=['POST','GET'])
def sudmit():
    marks = ''
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        dir = ''
        marks = (science+maths+c+datascience)/4
        print(marks)
        
        if marks<50:
          result='fail'
        else:
           result='success'
    return redirect(url_for(result,score=marks))

    

if __name__ == '__main__':
    app.run(debug=True)