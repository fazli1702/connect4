# CONNECT 4

### Video demo: https://youtu.be/qAlR-URkgmU  

<br>

This is a simple game of connect 4 where you will play against an AI.
The game of connect 4 is very simple. The game objective of this game is 
to be the first player to have 4 circles in a row, which can be horizontal, 
vertical or diagonal. This game requires a bit of thinking as you need to
also prevent your opponent from getting 4 in a row. The AI uses the minimax 
algorithm in which it calculates the game a few moves in advance (in my case 
5 moves in advance) and evaluate which move will give the best outcome for the
AI. To further improve this AI, I then further optimise it by using alpha-beta
pruning, which is a method that works together with the minimax algorithm. 
Alpha-beta pruning works by essentially eliminating moves that are very 
obviously bad moves (such as not blocking opponent when opponent is one move 
away from wining). This will help make the minimax algorithm run faster 
and avoid time wasting calculating moves that are bad. In this case, it is not
very obvious to see the time difference as the depth is only 5. However, if we
want to go deeper and have a higher depth (depth > 10), we can see a 
significant time difference between a normal minimax algorithm and the minimax
algorithm with alpha-beta pruning for optimisation. However, at very large 
depth, we may need to use other optimisation to further improve the AI as 
alpha-beta pruning may still take a long time. Hence, we need to find a depth
that is suitable where it is strong enough to play a human player and yet able
to calculate the different moves and depth quickly.

This game is coded in python as I am most familiar / comfortable with. Python
also has a very large collection of libraries that are available to use. 
Thus, I use python for this project. I am using the pygame library to display
the GUI as it is one of the most commonly used library in python for games 
/ GUI. For this project, you can either play using the GUI which display a 
real connect 4 game board or you can play on the terminal which displays 
each players in different colours

<br>

Ensure that you have the appropriate libraries before running the program. You can do this by running
```
pip install -r requirements.txt
```

You can play on the terminal by running `connect4.py`

![](images/terminal.png)

You can play using the GUI by running `main.py`

![](images/gui.png)


## References

### Medium aritcle  
https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f

### Keith Galli  
Github: https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py  
Youtube: https://www.youtube.com/watch?v=MMLtza3CZFM

### Wikipedia article  
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
https://en.wikipedia.org/wiki/Minimax

### Numberphile (extra information)
https://www.youtube.com/watch?v=yDWPi1pZ0Po