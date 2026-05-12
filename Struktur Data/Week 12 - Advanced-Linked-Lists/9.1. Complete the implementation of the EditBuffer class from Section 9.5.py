# Constructor
def __init__(self):
    self._firstLine = _EditBufferNode(['\n'])
    self._lastLine = self._firstLine
    self._curLine = self._firstLine
    self._curLineNdx = 0
    self._curColNdx = 0
    self._numLines = 1
    self._insertMode = True
    
# Cursor Movement
def moveLeft(self):
    if self._curColNdx == 0:
        if self._curLineNdx > 0:
            self.moveUp(1)
            self.moveLineEnd()
    else:
        self._curColNdx -= 1
        
# Adding Characters
def addChar(self, char):
    if self.inInsertMode():
        self._curLine.text.insert(self._curColNdx, char)
    else:
        self._curLine.text[self._curColNdx] = char
        
# Deleting Characters
def deleteChar(self):
    self._curLine.text.pop(self._curColNdx)
    
# Breaking a Line
def breakLine(self):
    newText = self._curLine.text[self._curColNdx:]