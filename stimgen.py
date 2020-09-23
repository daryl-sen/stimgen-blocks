import os
from flask import Flask, render_template, redirect, url_for, flash
# forms
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, SelectField, TextField, TextAreaField, SubmitField, IntegerField)
from wtforms.validators import DataRequired
# database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# other scripts
from coordgen import *

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

################################################################################
# db setup
################################################################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)





################################################################################
# db models
################################################################################

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    status = db.Column(db.Text)

    def __init__(self, title, content, status):
        self.title = title
        self.content = content
        self.status = status

    def __repr__(self):
        return f"{self.id}. {self.title} - {self.status}"

class session_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    session_num = db.Column(db.Integer)
    margin_size = db.Column(db.Integer)
    diff_resolution = db.Column(db.Integer)
    min_obj_distance = db.Column(db.Integer)
    divisions_v = db.Column(db.Integer)
    divisions_h = db.Column(db.Integer)
    obj_width = db.Column(db.Integer)
    obj_height = db.Column(db.Integer)
    label_width_x = db.Column(db.Integer)
    label_width_y = db.Column(db.Integer)
    manip_option_1 = db.Column(db.Integer)
    manip_option_2 = db.Column(db.Integer)
    manip_option_3 = db.Column(db.Integer)

    def __init__(self, quantity, session_num, margin_size, diff_resolution, min_obj_distance, divisions_v, divisions_h, obj_width, obj_height, label_width_x, label_width_y, manip_option_1, manip_option_2, manip_option_3):
        self.quantity = quantity
        self.session_num = session_num
        self.margin_size = margin_size
        self.diff_resolution = diff_resolution
        self.min_obj_distance = min_obj_distance
        self.divisions_v = divisions_v
        self.divisions_h = divisions_h
        self.obj_width = obj_width
        self.obj_height = obj_height
        self.label_width_x = label_width_x
        self.label_width_y = label_width_y
        self.manip_option_1 = manip_option_1
        self.manip_option_2 = manip_option_2
        self.manip_option_3 = manip_option_3

    def __repr__(self):
        return f"Session {self.session_num}"


class generated_properties(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    IID = db.Column(db.Integer)
    SID = db.Column(db.Integer)
    name = db.Column(db.Integer)
    x_pos = db.Column(db.Integer)
    y_pos = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    label_x = db.Column(db.Integer)
    label_y = db.Column(db.Integer)
    label_width = db.Column(db.Integer)
    label_height = db.Column(db.Integer)
    trial_type = db.Column(db.Integer)
    trial_location = db.Column(db.Integer)
    manipulations = db.Column(db.Integer)

    def __init__(self, IID, SID, name, x_pos, y_pos, width, height, label_x, label_y, label_width, label_height, trial_type, trial_location, manipulations):
        self.IID = IID
        self.SID = SID
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.label_x = label_x
        self.label_y = label_y
        self.label_width = label_width
        self.label_height = label_height
        self.trial_type = trial_type
        self.trial_location = trial_location
        self.manipulations = manipulations




################################################################################
# form models
################################################################################

class add_todo(FlaskForm):
    todo_title = StringField('Todo Title')
    todo_content = TextAreaField('Content', validators = [DataRequired()])
    todo_status = SelectField('Status', choices = [
        ('normal', 'Normal Todo Item'),
        ('urgent', 'Needs Urgent Attention'),
        ('complete', 'Completed'),
        ])
    todo_submit = SubmitField('Add Todo')

class stimgen_parameters_form(FlaskForm):
    quantity = IntegerField('Quantity of images')
    session_num = IntegerField('Session number')
    margin_size = IntegerField('Image margins')
    diff_resolution = IntegerField('Difference resolution')
    min_obj_distance = IntegerField('Minimum object distance')
    divisions_v = IntegerField('Vertical divisions')
    divisions_h = IntegerField('Horizontal divisions')
    obj_width = IntegerField('Object width')
    obj_height = IntegerField('Object height')
    label_width_x = IntegerField('Label width')
    label_width_y = IntegerField('Label height')
    manip_option_1 = BooleanField('Flip')
    manip_option_2 = BooleanField('Rotate')
    manip_option_3 = BooleanField('Color change')

    submit = SubmitField('Generate Stimuli Images')




################################################################################
# views
################################################################################

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/template')
def template():
    return render_template('base.html')

@app.route('/todo', methods=['GET', 'POST'])
def todo_list():
    form = add_todo()

    if form.validate_on_submit():
        todo_title = form.todo_title.data
        todo_content = form.todo_content.data
        todo_status = form.todo_status.data
        new_todo = todo(todo_title, todo_content, todo_status)
        db.session.add(new_todo)
        db.session.commit()
        flash('You new Todo item has been added.', 'Success')

    all_todo = todo.query.all()
    return render_template('pages/todo.html', form = form, all_todo = all_todo)

@app.route('/todo/delete/<id>')
def del_todo(id):
    id = id
    target_todo = todo.query.get(id)
    target_todo_title = target_todo.title
    db.session.delete(target_todo)
    db.session.commit()
    flash('Your Todo item, "{}", has been deleted'.format(target_todo_title), 'Deleted')
    return redirect(url_for('todo_list'))

@app.route('/todo/complete/<id>')
def com_todo(id):
    id = id
    target_todo = todo.query.get(id)
    target_todo.status = "complete"
    target_todo_title = target_todo.title
    db.session.commit()
    flash('Your Todo item, "{}", has been completed.'.format(target_todo_title), 'Deleted')
    return redirect(url_for('todo_list'))

@app.route('/create')
def stimgen_parameters():
    form = stimgen_parameters_form()

@app.route('/checkStim/<mode>')
def check_stim(mode):
    # sector_list = [
    #     '1,1', '2,1', '3,1',
    #     '1,2', '2,2', '3,2',
    #     '1,3', '2,3', '3,3',
    #     '1,4', '2,4', '3,4',
    #     '1,5', '2,5', '3,5'
    #     ]

    sector_list = [
        '1,1', '3,1',
        '1,2', '3,2',
        '1,3', '3,3',
        '1,4', '3,4',
        '1,5', '3,5'
        ]
    change_location = sector_list[random.randint(1,len(sector_list)-1)]
    list_pack = {item:generate_obj_properties(item) for item in sector_list}
    mode = mode
    return render_template('pages/canvas.html', sel = list_pack, change_location = change_location, mode=mode)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')

if __name__ == "__main__":
    app.run(debug = True)
