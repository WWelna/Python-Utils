#!/bin/python3

# Copyright (C) 2023 William Welna (wwelna@occultusterra.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
import argparse
import sys

ip_regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

parser = argparse.ArgumentParser(description='Regex all the IPs')
parser.add_argument('--inp', help='File or stdin', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('--out', help='File or stdout', type=argparse.FileType('a+'), default=sys.stdout)
args = parser.parse_args()

for l in args.inp:
    try:
        ips = ip_regex.findall(l)
        for e in ips:
            args.out.write(f"{e}\n")
    except: pass
