class Remote():    
    pass

class Player():
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()   # remote is added in class Remote
player1 = Player()   # player is added in class Player

if (remote1.isLeftpressed()):    # it states that player1 is operated with remote1
    player1.moveLeft()           # the movements are commanded here

