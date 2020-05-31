#Import necessary packages
from flask import render_template, request
from models.ml_algorithms.models import diagnosis_type
from views import app, back

# A route to the homepage
@app.route('/')
@back.anchor
def index():
    return render_template('index.html')

# A route to the about page
@app.route('/about/')
@back.anchor
def about():
    return render_template('about.html')

# A route to the classification(prediction)
@app.route('/classification/')
@back.anchor
def classification():
    return render_template('classification.html')


@app.route('/upload', methods=['GET', 'POST'])
@back.anchor
def upload():
  if request.method == 'POST':
    print(request.files)
    file = request.files['file']
    image = file.read()
    name = diagnosis_type(image_bytes=image)
    return render_template('result.html', name=name)


@app.route('/arecommend')
@back.anchor
def arecommendation():
  return render_template('arecommend.html')


@app.route('/nrecommend')
@back.anchor
def nrecommendation():
  return render_template('nrecommend.html')

@app.route('/crecommend')
@back.anchor
def crecommendation():
  return render_template('crecommend.html')

@app.route('/precommend')
@back.anchor
def precommendation():
  return render_template('precommend.html')

@app.route('/dataset/')
@back.anchor
def dataset():
    return render_template('dataset.html')




@app.route('/labtest/')
@back.anchor
def labtest():
    return render_template('labtest.html')


@app.route('/asthma/')
@back.anchor
def asthma():
    return render_template('asthma.html')


@app.route('/malaria/')
@back.anchor
def malaria():
    return render_template('malaria.html')

@app.route('/covid-19/')
@back.anchor
def covid19():
    return render_template('covid-19.html')

@app.route('/viralpneumonia/')
@back.anchor
def viral():
    return render_template('viral.html')
