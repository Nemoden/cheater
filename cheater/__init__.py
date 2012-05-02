from flask import Flask, render_template, abort, Markup, redirect, request, flash, url_for, session, make_response

def create_app(config=None):
  app = Flask(__name__)
  from cheater.admin import admin
  app.register_blueprint(admin)
  return app

app = create_app()
app.secret_key = 'debugging'

@app.route('/')
def index():
  from .models import Cheat
  from .database import session, select
  cheats = Cheat.__table__
  s = select([cheats.c.name, cheats.c.slug])
  cheats = session.execute(s).fetchall()
  return render_template("cheats_list.html", cheats = cheats)

@app.route('/login/', methods=['GET', 'POST'])
def login():
  from cheater.forms import LoginForm
  from cheater.models import User
  from sqlalchemy.orm.exc import NoResultFound
  form = request.method == 'POST' and LoginForm(request.form) or LoginForm()
  if request.method == 'POST' and form.validate():
    user = User.query.filter_by(username = form.username.data).first()
    app.logger.debug(user)
    if user and user.validate_password(form.password.data):
      session['logged_in'] = 1
      session['username'] = user.username
      session['role'] = user.role
      return redirect(url_for('admin.index'))
    else:
      flash('Username or password is incorrect', 'error')
  return render_template("login.html", form = form)

@app.route('/logout/', methods=['GET'])
def logout():
  session.pop('logged_in')
  session.pop('username')
  session.pop('role')
  return redirect(url_for('index'))

@app.route('/<string:slug>/')
def show_cheat(slug):
  if slug == 'favicon.ico':
    abort(404)
  from .models import Cheat
  from markdown import markdown
  cheat = Cheat.query.filter_by(slug = slug).first()
  return render_template("cheat.html", cheat = cheat)
  #return render_template("cheat.html", cheat = Markup(markdown(cheat.cheat, ['codehilite'])))

@app.errorhandler(404)
def not_found(status):
  response = make_response(render_template('404.html'))
  response.status_code = 404
  return response

if __name__ == "__main__":
  app.run(debug = True)
