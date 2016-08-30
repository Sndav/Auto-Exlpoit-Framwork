# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Author: Mauro Soria

import threading
import time
import sys
from colorama import *
import platform
if platform.system() == 'Windows':
    from ctypes import windll, create_string_buffer
    from colorama.win32 import *


class CLIOutput(object):

    def __init__(self):
        init()
        self.lastLength = 0
        self.lastOutput = ''
        self.lastInLine = False
        self.mutex = threading.Lock()
        self.checkedPaths = []
        self.blacklists = {}
        self.mutexCheckedPaths = threading.Lock()
        self.basePath = None

    def printInLine(self, string):
        self.eraseLine()
        sys.stdout.write(string)
        sys.stdout.flush()
        self.lastInLine = True

    def eraseLine(self):
        if platform.system() == 'Windows':
            csbi = GetConsoleScreenBufferInfo()
            line = "\b" * int(csbi.dwCursorPosition.X)
            sys.stdout.write(line)
            width = csbi.dwCursorPosition.X
            csbi.dwCursorPosition.X = 0
            FillConsoleOutputCharacter(
                STDOUT, ' ', width, csbi.dwCursorPosition)
            sys.stdout.write(line)
            sys.stdout.flush()
        else:
            sys.stdout.write('\033[1K')
            sys.stdout.write('\033[0G')

    def printNewLine(self, string):
        if self.lastInLine:
            self.eraseLine()
        if platform.system() == 'Windows':
            sys.stdout.write(string)
            sys.stdout.flush()
            sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            sys.stdout.write(string + '\n')
        sys.stdout.flush()
        self.lastInLine = False
        sys.stdout.flush()

    def printError(self, reason):
        message = Style.BRIGHT + Fore.WHITE + Back.RED
        message += reason
        message += Style.RESET_ALL

        self.printNewLine(message)

    def printWarning(self, reason):
        message = Style.BRIGHT + Fore.YELLOW + reason + Style.RESET_ALL
        self.printNewLine(message)

    def printHeader(self, text):
        message = Style.BRIGHT + Fore.MAGENTA + text + Style.RESET_ALL
        self.printNewLine(message)

    def printYellow(self, text):
        config = Style.BRIGHT + Fore.YELLOW
        config += text
        config += Style.RESET_ALL
        self.printNewLine(config)

    def printRed(self, text):
        output = Style.BRIGHT + Fore.RED
        output += text
        config += Style.RESET_ALL
    # def print
