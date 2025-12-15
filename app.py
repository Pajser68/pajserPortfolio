from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/about')
def about():
    """About Me page"""
    return render_template('about.html')


@app.route('/projects')
def projects():
    """My Projects page"""
    return render_template('projects.html')


@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')


if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
