from random import randint

repeat = True
while repeat:
    print("You rolled", randint(1,6))
    print("Dou you want to roll again?")
    rsp=input().lower().strip()
    repeat=("y"==rsp)or("yes"==rsp)
    
print("********* End of Gme! ********")