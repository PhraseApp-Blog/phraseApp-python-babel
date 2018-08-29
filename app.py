from jinja2 import Environment, FileSystemLoader, select_autoescape
from babel.support import Translations

templateLoader = FileSystemLoader( searchpath="templates" )

env = Environment(
    loader=templateLoader,
    extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape'],
    autoescape=select_autoescape(['html', 'xml'])
)

translations = Translations.load('locale', ['it'])
env.install_gettext_translations(translations)

template = env.get_template('index.html')

print(template.render(mailservers=range(10), name='mail'))

translations = Translations.load('locale', ['en_US'])
env.install_gettext_translations(translations)

template = env.get_template('index.html')

print(template.render(mailservers=range(10), name='mail'))
