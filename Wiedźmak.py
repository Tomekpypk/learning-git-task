def Land():
    ask = input("Choose your team: Yennefer or Triss ")
    accepted_answers = ["Yennefer", "Yen", "Bez i agrest"]
    if ask.upper() in [answer.upper() for answer in accepted_answers]:
        print("good choice")
    else:
        print("Lol no")

Land()
