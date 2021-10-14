# [START gae_flex_quickstart]
import logging

from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    #return 'Hello World!'
    return render_template('index.html')

@app.route('/index.html')
def homepage2():
    return render_template('index.html')

@app.route('/about.html')
def aboutpage():
    return render_template('about.html')

@app.route('/components.html')
def componentspage():
    return render_template('components.html')

@app.route('/project.html')
def projectspage():
    return render_template('project.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]