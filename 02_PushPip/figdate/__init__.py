from pyfiglet import Figlet
from time import time, strftime
import locale

def date(time_format="%Y %d %b, %A", font='graceful'):
    locale.setlocale(locale.LC_ALL, 'Russian')

    time_f = strftime(time_format)
    figlet = Figlet(font=font)
    return figlet.renderText(time_f)