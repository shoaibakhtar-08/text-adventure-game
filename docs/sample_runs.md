# Sample Runs

All output below is real program output. Text after `Choice:` is what the player typed.

## Test Case 1: Normal input

```text
========================================
       TEXT-BASED ADVENTURE GAME
========================================
You start in the Forest. Health: 100 | Score: 0

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 2
You found a treasure!
Score: 50 | Health: 100

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 3
You left the adventure. Final score: 50 | Health: 100
```

## Test Case 2: Boundary / minimum input
Command: `python adventure_game.py --health 30 --damage 30`

```text
========================================
       TEXT-BASED ADVENTURE GAME
========================================
You start in the Forest. Health: 30 | Score: 0

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 30. Health: 0
Game Over! Final score: 0
```

## Test Case 3: Invalid input

```text
========================================
       TEXT-BASED ADVENTURE GAME
========================================
You start in the Forest. Health: 100 | Score: 0

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 7
Invalid choice. Enter 1, 2 or 3.
Choice: abc
Invalid choice. Enter 1, 2 or 3.
Choice: 3
You left the adventure. Final score: 0 | Health: 100
```

## Test Case 4: Different valid scenario
Command: `python adventure_game.py --damage 30`

```text
========================================
       TEXT-BASED ADVENTURE GAME
========================================
You start in the Forest. Health: 100 | Score: 0

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 30. Health: 70
You found a key! Score: 20

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 2
You found a treasure!
Score: 70 | Health: 70

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 3
You left the adventure. Final score: 70 | Health: 70
```

## Extra run: random damage, player quits

```text
========================================
       TEXT-BASED ADVENTURE GAME
========================================
You start in the Forest. Health: 100 | Score: 0

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 20. Health: 80
You found a key! Score: 20

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 2
You found a treasure!
Score: 70 | Health: 80

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 40. Health: 40
You found a key! Score: 90

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 14. Health: 26
You found a key! Score: 110

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 3
You left the adventure. Final score: 110 | Health: 26
```

## Extra run: random damage, player loses all health

```text
========================================
       TEXT-BASED ADVENTURE GAME
========================================
You start in the Forest. Health: 100 | Score: 0

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 2
You found a treasure!
Score: 50 | Health: 100

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 17. Health: 83
You found a key! Score: 70

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 28. Health: 55
You found a key! Score: 90

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 27. Health: 28
You found a key! Score: 110

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 14. Health: 14
You found a key! Score: 130

You are in the Forest. Where do you want to go?
1. Cave
2. River
3. Quit
Choice: 1
Monster attacks! Damage: 21. Health: 0
Game Over! Final score: 130
```
