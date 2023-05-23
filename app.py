from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Bug Report Form
class BugReportForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = StringField('Category', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    reproduction_steps = TextAreaField('Reproduction Steps', validators=[InputRequired()])
    workarounds = TextAreaField('Workarounds')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    categories = ['gameplay', 'visual', 'audio']
    form = BugReportForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Process the bug report form
        new_bug = {
            'id': len(bugs) + 1,
            'title': form.title.data,
            'category': form.category.data,
            'description': form.description.data,
            'reproduction_steps': form.reproduction_steps.data,
            'workarounds': form.workarounds.data
        }
        bugs.append(new_bug)
        return render_template('index.html', categories=categories, form=form, success_message='Bug reported successfully!')
    return render_template('index.html', categories=categories, form=form)

@app.route('/category/<name>')
def category(name):
    category_bugs = [bug for bug in bugs if bug['category'] == name]
    return render_template('category.html', category=name.capitalize(), bugs=category_bugs)

@app.route('/bug/<int:id>')
def bug(id):
    bug = next((bug for bug in bugs if bug['id'] == id), None)
    if bug:
        return render_template('bug.html', bug=bug)
    else:
        return 'Bug not found.', 404

@app.route('/report', methods=['GET', 'POST'])
def report():
    form = BugReportForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Process the bug report form (same as above)
        new_bug = {
            'id': len(bugs) + 1,
            'title': form.title.data,
            'category': form.category.data,
            'description': form.description.data,
            'reproduction_steps': form.reproduction_steps.data,
            'workarounds': form.workarounds.data
        }
        bugs.append(new_bug)
        return render_template('report.html', form=form, success_message='Bug reported successfully!')
    return render_template('report.html', form=form)

bugs = [
    {
        'id': 1,
        'title': 'Bug 1',
        'category': 'gameplay',
        'description': 'Bug 1 description...',
        'reproduction_steps': 'Steps to reproduce Bug 1...',
        'workarounds': 'Workarounds for Bug 1...'
    },
    {
        'id': 2,
        'title': 'Bug 2',
        'category': 'visual',
        'description': 'Bug 2 description...',
        'reproduction_steps': 'Steps to reproduce Bug 2...',
        'workarounds': 'Workarounds for Bug 2...'
    },
    {
        'id': 3,
        'title': 'Bug 3',
        'category': 'audio',
        'description': 'Bug 3 description...',
        'reproduction_steps': 'Steps to reproduce Bug 3...',
        'workarounds': 'Workarounds for Bug 3...'
    }
]

if __name__ == '__main__':
    app.run(debug=True)
