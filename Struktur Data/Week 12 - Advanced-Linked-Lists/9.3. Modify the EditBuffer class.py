# getPage(first, last)
def getPage(self, first, last):

    result = []
    current = self._firstLine
    index = 0

    while current is not None:

        if first <= index <= last:
            result.append("".join(current.text))

        current = current.next
        index += 1

    return result

# insertString(str)
def insertString(self, string):

    for char in string:
        self.addChar(char)
        
# moveTo(lineNdx, colNdx)
def moveTo(self, lineNdx, colNdx):

    if lineNdx < 0 or lineNdx >= self._numLines:
        return

    current = self._firstLine
    index = 0

    while index < lineNdx:
        current = current.next
        index += 1

    self._curLine = current
    self._curLineNdx = lineNdx

    if colNdx >= len(current.text):
        self._curColNdx = len(current.text) - 1
    else:
        self._curColNdx = colNdx
        
