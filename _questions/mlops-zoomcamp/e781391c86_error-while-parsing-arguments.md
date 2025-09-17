---
course: mlops-zoomcamp
id: e781391c86
question: 'Error while parsing arguments via CLI  [ValueError: Unknown format code
  ''d'' for object of type ''str'']'
section: 'Module 4: Deployment'
sort_order: 1660
---

When passing arguments to a script via command line and converting it to a 4 digit number using f’{year:04d}’, this error showed up.

This happens because all inputs from the command line are read as string by the script. They need to be converted to numeric/integer before transformation in fstring.

year = int(sys.argv[1])

f’{year:04d}’

If you use click library just edit a decorator

@click.command()

@click.option( "--year",  help="Year for evaluation",   type=int)

def  your_function(year):

<<Your code>>

Added by Taras Sh

