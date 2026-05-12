# moveLeft()
def moveLeft(self, steps):

    for i in range(steps):

        if self._curColNdx == 0:

            if self._curLineNdx > 0:
                self.moveUp(1)
                self.moveLineEnd()

        else:
            self._curColNdx -= 1

# moveRight()
def moveRight(self, steps):

    for i in range(steps):

        if self._curColNdx < self.numChars() - 1:
            self._curColNdx += 1

        elif self._curLine.next is not None:
            self._curLine = self._curLine.next
            self._curLineNdx += 1
            self._curColNdx = 0