Taken from [this SE.PPCG question](https://codegolf.stackexchange.com/questions/120688/snowball-fight-koth).

# The Game
This is a very simple KoTH game. It's a one-on-one snowball fight. You have an initially-empty container that can hold up to `k` snowballs. You can duck up to `j` times. Each turn, both players are asked to simultaneously give a choice for what move to make. There are three moves:

- reload: gives you another snowball (up to `k`) 
- throw: throws a snowball, which will kill the other player if they decide to reload. If both players throw a snowball, nobody dies (they have such good aim that they will hit each other's snowballs)
- duck: does nothing, and avoids getting hit if the other player throws a snowball. If you have no more ducks left, then nothing happens and if the other player throws a snowball you die.

# Objective
Don't die.

# Challlenge Specifications
Your program can be written in any language. You are to take each of these 
variables as an argument on each execution:

    [turn, snowballs, opponent_snowballs, ducks, opponent_ducks, max_snowballs]

`turn` - how many turns have elapsed (`0` on the first iteration)  
`snowballs` - how many snowballs you have  
`opponent_snowballs` - how many snowballs the opponent has  
`ducks` - how many more times you can duck  
`opponent_ducks` - how many more times the opponent can duck  
`max_snowballs` - the maximum number of snowballs you can store (`k`)  

The key function's output should be `0` for reload, `1` for throw, and `2` for duck. You must output your move, newline terminated. Please don't output invalid moves, but the controller is very resilient and will not break if you output invalid moves (even if your move isn't even an integer). It **must** be newline-terminated though. If the move isn't in `[0, 1, 2]`, it will default your move to `0`. The winner will be decided as the player with the most wins from a full round-robin tournament.

# Rules
You can read/write from/to one file for memory storage between iterations. Your bot will be placed in its own directory so filename conflicts will not occur. You cannot change built-in functions (such as the random generator). It was quite funny [the first time it was done](https://codegolf.stackexchange.com/a/25392/42649), but it won't be anymore. Your program is not allowed to do things that are just blatant execution stalling. [Standard Loopholes Apply](https://codegolf.meta.stackexchange.com/questions/1061/loopholes-that-are-forbidden-by-default).

# Testing
The source code for the controller can be found [here](https://hastebin.com/ahejuwubok.java). Example of running it: `java Controller "python program1/test1.py" "python program2/test2.py" 10 5` for 10 snowballs and 5 ducks.

# Judging
The winner will be decided by selecting the person with the most wins after a full round-robin. While this is a tie, remove all people who do not have the most wins. Then, repeat until one person wins. The judging standard will be 50 snowballs and 25 ducks.

Happy KoTHing!
