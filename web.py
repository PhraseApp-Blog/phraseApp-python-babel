from flask import Flask, render_template, request
from flask_babel import Babel
from phrase import Phrase, gettext, ngettext

class Config(object):
    LANGUAGES = {
        'it': 'Italian',
        'de_DE': 'Deutsch'
    },
    BABEL_DEFAULT_LOCALE= 'it'
    PHRASEAPP_ENABLED = True
    PHRASEAPP_PREFIX = '{{__'
    PHRASEAPP_SUFFIX = '__}}'

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
phrase = Phrase(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'][0].keys())

@app.route('/')
def index():
    return render_template('index.html', locale=get_locale() or babel.default_locale)
