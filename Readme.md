
The functionality Babel provides for internationalization (I18n) and localization (L10N) can be separated into two different aspects:

* Tools to build and work with gettext message catalogs,
* Python interface to the CLDR (Common Locale Data Repository), providing access to various locale display names, localized number and date formatting, etc.

Babel Basics
---
### Message Catalogs
While the Python standard library includes a gettext module that enables applications to use message catalogs, it requires developers to build these catalogs using GNU tools such as xgettext, msgmerge, and msgfmt. And while xgettext does have support for extracting messages from Python files, it does not know how to deal with other kinds of files commonly found in Python web-applications, such as templates, nor does it provide an easy extensibility mechanism to add such support.

Babel addresses this by providing a framework where various extraction methods can be plugged in to a larger message extraction framework, and also removes the dependency on the GNU gettext tools for common tasks, as these aren’t necessarily available on all platforms. See Working with Message Catalogs for details on this aspect of Babel.

### Locale Data
Furthermore, while the Python standard library does include support for basic localization with respect to the formatting of numbers and dates (the locale module, among others), this support is based on the assumption that there will be only one specific locale used per process (at least simultaneously.) Also, it doesn’t provide access to other kinds of locale data, such as the localized names of countries, languages, or time-zones, which are frequently needed in web-based applications.

For these requirements, Babel includes data extracted from the Common Locale Data Repository (CLDR), and provides a number of convenient methods for accessing and using this data. See Locale Data, Date and Time, and Number Formatting for more information on this aspect of Babel.

Install

```
pip install Babel
```

## Working with Locale Data


## Message Extraction with babel
The routines for message extraction in Babel operate on directories.

Babel provides two different front-ends to access its functionality for working with message catalogs:

* A Command-Line Interface, and
* Distutils/Setuptools Integration
Which one you choose depends on the nature of your project. For most modern Python projects, the distutils/setuptools integration is probably more convenient.

### Babel configuration file

### Command line tool

* pybabel --list-locales: Print all known locales

*compile*
The compile sub-command can be used to compile translation catalogs into binary MO files:

```
➜ pybabel compile -d locale
```


*extract*
The extract sub-command can be used to extract localizable messages from a collection of source files:
```
pybabel extract . -o locale/base.mot
```

*init*
The init sub-command creates a new translations catalog based on a PO template file:

```
~/phraseApp-python-babel via phrase-app
➜ pybabel init  -l el_GR de_DE en_US -i locale/base.mot -d locale
creating catalog locale/el_GR/LC_MESSAGES/messages.po based on locale/base.mot

~/phraseApp-python-babel via phrase-app
➜ pybabel init  -l de_DE en_US -i locale/base.mot -d locale
creating catalog locale/de_DE/LC_MESSAGES/messages.po based on locale/base.mot

~/phraseApp-python-babel via phrase-app
➜ pybabel init  -l en_US -i locale/base.mot -d locale
creating catalog locale/en_US/LC_MESSAGES/messages.po based on locale/base.mot
```

*update*
The update sub-command updates an existing new translations catalog based on a PO template file:

```
~/phraseApp-python-babel via phrase-app
➜ pybabel update -i locale/base.pot -d locale
updating catalog locale/en_US/LC_MESSAGES/messages.po based on locale/base.pot
updating catalog locale/el_GR/LC_MESSAGES/messages.po based on locale/base.pot
updating catalog locale/de_DE/LC_MESSAGES/messages.po based on locale/base.pot
```