import getopt
import sys

#getopt example

# python getopt_test.py  --role=r1 --loc=l1 --cluster=c1

try:
    options, remainder = getopt.getopt(
            sys.argv[1:],
            'loc:cluster:role',
            ['loc=','cluster=','role=']
        )
    option_choices = {}
    for opt, arg in options:
        option_choices[str(opt[2:])] = str(arg)
    print option_choices
except Exception as e:
    print(e)
    pass
