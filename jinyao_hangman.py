import randomn=input("welcome to hang man! what's your name?")print("good luck "+n)print("the rule is easy. All you have to do is to choose a letter and if it's in the word, you gain a chance. There is 10 games")d=input("choose a for easy, b for hard, any thing else for medium.")for i in range(10):    if d == "b":        word_choice=["Edinburgh","i","pennsylvania","security","bovine","activity","debenture","covid","helmet","rapcity","mango","gluclose","xylem","foil","monology","revolution","overcooked","fortnight","winner","zzzzzzzzz","voltage","zutopia","stream","detail","booooooooooooom","baaaaaam","jump","crazy","zigzag","voltage","zeus","pressure","","optons","format","connected","weekend","event","shoot","laugh"]    elif d == "a":        word_choice=["net","way","why","weigh","what","can","ran","when","pan","turd","bull","java","ruby","html","c","solid","script","ray","bat","pay","may","gay","may","be","ship","nit","rip","hub","show","play","atom","ten","pen","pin","limb","open","zoom","zoo","lamp","less","bull","top","rob","knob","gob","pop","rock","map"]    else:        word_choice=["ravioli","plantiff","user","hangman","student","another","amature","tourist","strike","missile","download","powder","frame","tuesday","monday","flower","book","nook","rookie","server","knight","right","piping","guide","option","command","discuss","refresh","monkey","spegeti","penny","super","feirce","eagle","jewish","christion","rabbi","prince","rince","create","initial","terms","contact","pricing","blog","about"]    word=word_choice[random.randint(0,len(word_choice)-1)]    guesses=""    guess_number=17    win="no"    for char in word:        print("_ ", end="")        print("")    while guess_number>0 and win=="no":        win="maybe"        guess=input("choose letter please : ")        guesses+=guess        guess_number-=1        print("now its round")        print(guess_number)        for char in word:            if char in guesses:                print(char+" ", end="")                            else:                print("_ ", end="")                        win="no"        print("")    if win=="no":        print("sorry, you lost. the word is:")        print(word)    else:        print("horray, you won!")                    