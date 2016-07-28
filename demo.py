import views

def run(player, skills):
    for each in views.sixteen_years_later:
        print(each)
        input(views.cont)
    while True:
        choice = input("What will you do?\nTalk to Elder [S]aerl\nTalk to Elder [J]ou\n[C]heck surroundings\n[L]eave room\n")
        if choice.lower() == 's':
            print("Elder Saerl: Unfortunately, we have to... accelerate our training somewhat. I wish we had more time, but... we must hurry to the Wellspring Primus.")
            input(views.cont)
        elif choice.lower() == 'j':
            print("Elder Jou: I hope you're up to the task, kid. You haven't had a lot of training but it'll have to do. Don't let my daughter's death be in vain.")
            input(views.cont)
        elif choice.lower() == 'c':
            for each in ["Your room is small, but still larger than most. Ancient books are in a pile in one corner, and a few wooden swords and staffs lay strewn across the floor.", "Elder Saerl raised you since you were a child and the look of concern on his face is very telling. Elder Jou, besides being your grandfather, was always tough and sheltered. He's  tapping his fingers on his ceremonial belt.", "They both hover over your bed, waiting for you to move. How rude."]:
                print (each)
                input(views.cont)
        elif choice.lower() == 'l':
            print('WATCH OUT!')
            input(views.cont)
            return("battle")
        else:
            print(views.try_again)
            input(views.cont)
            pass