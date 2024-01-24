import main
from random import choice

#lcd displays 16 chars on ea line
QUOTES = [
        ('Stop looking','4 excuses'),
        ('aim 4 mastery','dont settle'),
        ('consistence >>>','perfection'),
        ('persistence >>>','perfection'),
        ('keep showing up!',' ')
        ]

if __name__=="__main__":
    line1,line2=choice(QUOTES)
    main.display(line1,line2)
