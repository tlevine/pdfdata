#!/usr/bin/env python3
import argparse
import io, subprocess
import csv
from collections import OrderedDict
import json, sys

# Explain usage if no files are given.
argparser = argparse.ArgumentParser()
argparser.add_argument(dest = 'files', metavar = 'pdf-file', nargs = '+')

def pdfdata(filename):
    '''
    Here's an example. ::

        print(pdfdata('/home/tlevine/git/muckrock/foia_files/Todd_Feathers.pdf'))
    '''
    fp = io.StringIO(subprocess.getoutput("pdfinfo '%s'|sed 's/: */\t/'" % filename))
    return OrderedDict(csv.reader(fp, delimiter = '\t'))

def main():
    args = argparser.parse_args()
    for filename in args.files:
        try:
            sys.stdout.write(json.dumps(pdfdata(filename)) + '\n')
        except KeyboardInterrupt:
            break
        except BrokenPipeError:
            break
        except Exception as error:
            sys.stderr.write('Error at %s: %s\n' % (filename, error))

# Issues
# * \x00
