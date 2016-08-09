from flask import Flask
from flask import make_response
from flask import render_template,request, session

from src.calculator.score_calculate import score_calculate
from src.common.database import Database
from src.models.score import Score
from src.models.user import User

app = Flask(__name__)

app.secret_key = "i am SHER locked"


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')
def default_function():
    return render_template('default.html')


@app.route('/login')
def login_function():
    return render_template('login.html')


@app.route('/auth/login', methods=['POST'])
def home_function():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email,password):
        User.login_valid(email,password)
    else:
        session['email'] = None

    return render_template('homepage.html',user=session['email'])


@app.route('/register')
def register_function():
    return render_template('register.html')


@app.route('/auth/register', methods=['POST'])
def auth_register_function():
    email = request.form['email']
    password = request.form['password']
    User.register_user(email,password)
    return render_template('homepage.html',user = session['email'])


@app.route('/1of15')
def first_question():
    return render_template('ques1.html')


@app.route('/2of15')
def second_question():
    return render_template('ques2.html')


@app.route('/3of15')
def third_question():
    return render_template('ques3.html')


@app.route('/4of15')
def fourth_question():
    return render_template('ques4.html')


@app.route('/5of15')
def fifth_question():
    return render_template('ques5.html')


@app.route('/6of15')
def sixth_question():
    return render_template('ques6.html')


@app.route('/7of15')
def seventh_question():
    return render_template('ques7.html')


@app.route('/8of15')
def eigth_question():
    email = session['email']
    username = User.get_by_email(email)
    return render_template('ques8.html', user = username.email, id = username.score_id)


@app.route('/calculate1/<string:_id>',methods = ['GET','POST'])
def hello(_id):
    return render_template('input.html', id = _id)


@app.route('/calculate/<string:_id>', methods=['GET','POST'])
def calculate(_id):
    letters=str(request.form['word'])

    score = score_calculate(letters)
    user = Score(score,_id)
    user.save_to_mongo_score()

    return render_template("this_score.html", result = score, id = _id)


@app.route('/list_of_scores/<string:_id>')
def get_all_scores(_id):
    email = session['email']
    username = User.get_by_email(email)
    scores = Score.get_from_mongo_score(_id)
    return render_template('score_list.html', scores = scores, user = username.email, id = username._id)


@app.route('/all_scores/<string:_id>')
def all_scores(_id):
    return make_response(get_all_scores())


if __name__=='__main__':
    app.run(port=5000,debug=True)