import pyautogui as chess
from Moves import Moves
import time

numbermoves = 500
#Set it high because the bot inputs moves randomnly whithout knowing if they 
# are legal or not in chess (i.p. 500).

time.sleep(3)
#Set the time you need to move from the python editor to the chess game.

chess.moveTo(549,921)
chess.click(549,921)

for i in range(1,numbermoves):
    
    move = Moves.Moves()
    chess.write(move)
    chess.doubleClick(549,921)
    chess.press('delete')


