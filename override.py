from turtle import home
from Man import*
from Hombre import*

guy_1 = Man('Richard')
guy_2 = Hombre('Ricardo')

guy_1.speak('It\'s a beautiful evening.\n')
guy_2.speak('Es una tarde harmosa.\n')

Person.speak(guy_1)
Person.speak(guy_2)