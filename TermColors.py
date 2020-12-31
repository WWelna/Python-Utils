# Copyright (C) 2020 William Welna (wwelna@occultusterra.com)

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

import random

class TermColors:
	RESET = '\033[0m'
	CLEAR_LINE = '\033[0K'

	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	BLINK = '\033[5m'
	REVERSE = '\033[7m'

	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	MAGENTA = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'

	BOLD_BLACK = '\033[30;1m'
	BOLD_RED = '\033[31;1m'
	BOLD_GREEN = '\033[32;1m'
	BOLD_YELLOW = '\033[33;1m'
	BOLD_BLUE = '\033[34;1m'
	BOLD_MAGENTA = '\033[35;1m'
	BOLD_CYAN = '\033[36;1m'
	BOLD_WHITE = '\033[37;1m'

	BACK_BLACK = '\033[40m'
	BACK_RED = '\033[41m'
	BACK_GREEN = '\033[42m'
	BACK_YELLOW = '\033[43m'
	BACK_BLUE = '\033[44m'
	BACK_MAGENTA = '\033[45m'
	BACK_CYAN = '\033[46m'
	BACK_WHITE = '\033[47m'

	BACK_BOLD_BLACK = '\033[40;1m'
	BACK_BOLD_RED = '\033[41;1m'
	BACK_BOLD_GREEN = '\033[42;1m'
	BACK_BOLD_YELLOW = '\033[43;1m'
	BACK_BOLD_BLUE = '\033[44;1m'
	BACK_BOLD_MAGENTA = '\033[45;1m'
	BACK_BOLD_CYAN = '\033[46;1m'
	BACK_BOLD_WHITE = '\033[47;1m'

	UNDERSCORE_BLACK = '\033[30;4m'
	UNDERSCORE_RED = '\033[31;4m'
	UNDERSCORE_GREEN = '\033[32;4m'
	UNDERSCORE_YELLOW = '\033[33;4m'
	UNDERSCORE_BLUE = '\033[34;4m'
	UNDERSCORE_MAGENTA = '\033[35;4m'
	UNDERSCORE_CYAN = '\033[36;4m'
	UNDERSCORE_WHITE = '\033[37;4m'

	UNDERSCORE_BOLD_BLACK = '\033[30;1;4m'
	UNDERSCORE_BOLD_RED = '\033[31;1;4m'
	UNDERSCORE_BOLD_GREEN = '\033[32;1;4m'
	UNDERSCORE_BOLD_YELLOW = '\033[33;1;4m'
	UNDERSCORE_BOLD_BLUE = '\033[34;1;4m'
	UNDERSCORE_BOLD_MAGENTA = '\033[35;1;4m'
	UNDERSCORE_BOLD_CYAN = '\033[36;1;4m'
	UNDERSCORE_BOLD_WHITE = '\033[37;1;4m'

	def __init__(self):
		self._colors256()
		self.reset()

	def reset(self):
		print(self.RESET, end='')

	def ClearScreen(self):
		print('\033[2J', end='')

	def ClearLine(self):
		print('\033[2K', end='')

	def NextLine(self, n=1):
		print('\033['+str(n)+'E')

	def PrevLine(self, n=1):
		print('\033['+str(n)+'F')

	def _colors256(self):
		self.colors256 = []
		for x in range(0,255):
			self.colors256.append('\033[38;5;'+str(x)+'m')

	def MoveRight(self, n):
		print('\033['+str(n)+'C', end='')

	def MoveLeft(self, n):
		print('\033['+str(n)+'D', end='')

	def MoveUp(self, n):
		print('\033['+str(n)+'A', end='')

	def MoveDown(self, n):
		print('\033['+str(n)+'B', end='')
	
	def rainbow(self, s, end='\n'):
		r = [self.BOLD_RED, self.BOLD_YELLOW, self.BOLD_GREEN, self.BOLD_BLUE, self.BOLD_MAGENTA]
		for c in s:
			print(random.choice(r)+str(c), end='')
		print(end=end)