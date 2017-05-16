# Throws most of its snowballs immediately, but always saves one in case the opponent is watching for a lack of ammo
# Then, ducks as long as possible before reloading unless there is a guaranteed safe reload or guaranteed kill
import sys
turn, snowballs, opponent_snowballs, ducks, opponent_ducks, max_snowballs = map(int, sys.argv[1:])

reload_snowball=0
throw=1
duck=2

if snowballs==1:
    if opponent_snowballs==0:
        if opponent_ducks==0:
            print throw
        else:
            print reload_snowball
    elif ducks > 0:
        print duck
    else:
        print reload_snowball
else:
    print throw
