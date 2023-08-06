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

def walk(q):
    if isinstance(q, dict):
        ret = {}
        for k in q.keys():
            if isinstance(q[k], (int, str, float, type(True), type(False), type(None))):
                ret[k] = q[k]
                continue
            if isinstance(q[k], dict) or isinstance(q[k], list):
                ret[k] = walk(q[k])
                continue
            ret[k] = str(q[k])
        return ret
    elif isinstance(q, list):
        ret = []
        for e in q:
            if isinstance(e, (int, str, float, type(True), type(False), type(None))):
                ret.append(e)
                continue
            if isinstance(e, (dict, list)):
                ret.append(walk(e))
                continue
            ret.append(str(e))
        return ret
