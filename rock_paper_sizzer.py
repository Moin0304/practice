def rock_paper(winner,count):
    count += 1
    print("\n\nRock\npaper\nscissor\n")
    lists = ["rock","scissor","paper"]
    user1 = input("user1 choose any one above list = ").lower()
    if (user1 not in lists):
        raise TypeError("Your enter wrong")
    user2 = input("user2 choose any one above list = ").lower()
    if (user2 not in lists):
        raise TypeError("Your enter wrong please check")

    if user1 == user2:
        print(count,"Match is Tie play again")
        winner.app

rock_paper(2,5)