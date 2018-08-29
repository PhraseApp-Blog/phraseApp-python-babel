from babel import Locale
from babel.dates import format_date, format_datetime, format_time
from babel.numbers import format_number, format_decimal, format_percent, parse_decimal
from babel.units import format_unit

from datetime import date, datetime, time

l = Locale.parse('de-DE', sep='-')
print("Locale name: {0}".format(l.display_name))

l = Locale.parse('und_GR', sep='_')
print("Locale name: {0}".format(l.display_name))

l = Locale.negotiate(['de_DE', 'en_AU'], ['de_DE', 'de_AT'])
print("Locale negociated: {0}".format(l.display_name))

print(Locale('it').english_name)
print(Locale('it').get_display_name('fr_FR'))
print(Locale('it').get_language_name('de_DE'))
print(Locale('de', 'DE').languages['zh'])

print(Locale('el', 'GR').scripts['Copt'])

# Calendar
locale = Locale('it')
month_names = locale.days['format']['wide'].items()
print(list(month_names))


# Date, time

d = date(2010, 3, 10)
print(format_date(d, format='short', locale='it'))
print(format_date(d, format='full', locale='it'))

print(format_date(d, "EEEE, d.M.yyyy", locale='de'))

dt = datetime.now()
print(format_datetime(dt, "yyyy.MMMM.dd GGG hh:mm a", locale='en'))


# Numbers/ Units

print(format_decimal(123.45123, locale='en_US'))
print(format_decimal(123.45123, locale='de'))

print(format_unit(12, 'length-meter', locale='en_GB'))
print(format_unit(12, 'length-meter', locale='en_US'))
print(parse_decimal('2.029,98', locale='de'))


