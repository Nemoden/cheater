# vim: set fenc=utf-8: set ts=2: set sw=2:
from flask import (
    Blueprint,
    session as flask_session,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    Markup,
    flash)
from cheater.models import *
from .forms import *
from markdown import markdown

admin = Blueprint('admin',
                  __name__,
                  url_prefix='/admin',
                  template_folder='templates',
                  static_folder='static')


@admin.before_request
def check_permissions():
    if 'username' not in flask_session:
        abort(404), 404


@admin.route('/')
def index():
    return render_template("actions_list.html")


@admin.route('/add/', methods=['GET', 'POST'])
def add():
    preview = None
    form = request.form and AddForm(request.form) or AddForm()
    if request.method == 'POST':
        if request.form.get('preview'):
            preview = Markup(markdown(form.cheat.data, ['codehilite']))
        elif form.validate():
            c = Cheat(form.name.data, form.cheat.data)
            session.add(c)
            session.commit()
            return redirect(url_for('show_cheat', slug=c.slug))
    return render_template("add.html", form=form, preview=preview)


@admin.route('/edit/<string:slug>/', methods=['GET', 'POST'])
def edit(slug=None):
    cheat = Cheat.query.filter_by(slug=slug).first()
    form = request.method == 'POST' and EditForm(request.form) \
                             or EditForm(cheat=cheat.cheat, name=cheat.name)
    if request.method == 'POST' and form.validate():
        cheat.html = form.cheat.data
        cheat.cheat = form.cheat.data
        cheat.name = form.name.data
        session.commit()
        return redirect(url_for('show_cheat', slug=cheat.slug))
    return render_template('edit.html',
                           form=form,
                           slug=slug,
                           cheat_id=cheat.id)


@admin.route('/delete/<string:slug>/', methods=['GET', 'POST'])
def delete(slug=None):
    d = session.execute(Cheat.__table__.delete().
                        where(Cheat.__table__.c.slug == slug)
                        )
    if d.rowcount:
        session.commit()
    else:
        # just a stab if we will want to say something
        # if the rows wasn't existed
        # probably, we could've drop this request with 404
        #or email warning, etc.
        pass
    flash('Record deleted', 'info')
    return redirect(url_for('index'))
