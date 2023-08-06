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

import datetime
from string import Template

class RotateFile:

    # "test-$d.log"
    def __init__(self, file_template, path=None, hours=24, mode='a+', encoding='utf-8'):
        self.dt = datetime.datetime.utcnow()
        self.template = Template(file_template)
        self.path = path
        self.mode = mode
        self.hours = hours
        self.encoding = encoding

        self.file = open(self._do_template(self.dt), mode=mode, encoding=encoding)
    
    def _do_template(self, dt) -> str:
        ret = self.template.substitute({'d': dt.strftime('%m%d%Y-%H%M%S')})
        if self.path != None:
            ret = f"{self.path}{ret}"
        return ret
    
    def _datecheck(self) -> None:
        if self.dt < datetime.datetime.utcnow() - datetime.timedelta(hours=self.hours):
            self.file.close()
            self.dt = datetime.datetime.utcnow()
            self.file = open(self._do_template(self.dt), mode=self.mode, encoding=self.encoding)

    def flush(self)-> None: self.file.flush()
    def read(self, n=-1): return self.file.read()
    def readln(self, n=-1): return self.file.readline(n)
    def seek(self, offset, whence=0): self.file.seek(offset, whence)
    def write(self, d) -> int:
        self._datecheck()
        return self.file.write(d)

    def __iter__(self): return self
    def __next__(self) -> str:
        n = self.file.readline()
        if n != '': return n
        else: raise StopIteration

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
