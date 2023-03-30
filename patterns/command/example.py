#!/usr/bin/env python3

"""
Why would someone use the command pattern?  
You can use it to run some action and by keeping the state of the action in the command you can undo it.
"""

import os

class MoveFileCommand(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        os.rename(self.src, self.dst)

stack = []
stack.append(MoveFileCommand('hello.txt', 'foo.txt'))
stack.append(MoveFileCommand('foo.txt', 'bar.txt'))


#stack.pop().undo()
#stack.pop().undo()