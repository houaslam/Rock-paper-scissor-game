import random

choices = ['rock', 'paper', 'scissors'];
running = True

while running:
    player = None
    computer = random.choice( choices )
    while player not in choices:
        player = input( "choose (rock 🪨, paper 📄, scissors ✂️) : " );

    print(f"Player = {player}" )
    print(f"Computer = {computer}" )

    if ( player == computer ):
        print(  'DRAW!'  )

    elif( player == 'rock' and computer == 'scissors' ):
        print(  'YOU WON 🎉'  )

    elif( player == 'paper' and computer == 'rock' ):
        print(  'YOU WON 🎉'  )

    elif( player == 'scissors' and computer == 'paper' ):
        print(  'YOU WON 🎉'  )

    else:
        print(  'YOU LOST ❌'  )
    
    again = input("Wanna play again (y/n) : ")
    if again.lower() != 'y':
        running = False