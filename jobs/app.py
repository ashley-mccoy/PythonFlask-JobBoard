from flask import Flash, render_template

app = Flash(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
