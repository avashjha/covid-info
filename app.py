from flask import Flask,render_template,url_for,request
from cinfo import covid_info
from countries import country_name
app = Flask(__name__)




@app.route('/')
def main():
    title="Home"
    return render_template('base.html',title=title)

@app.route('/covid',methods=['GET','POST'])
def covid():
    if request.method=='POST':
        cname=request.form['cname']
        result=covid_info(country_name(cname))
        return render_template('covid.html',data=result)
    else:    
        return render_template ('covid.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    
    return render_template('404.html'), 404



if __name__ == "__main__":
    app.run(debug=True, port=80)
