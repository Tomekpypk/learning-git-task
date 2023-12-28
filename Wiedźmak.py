def Land():
    ask = input("Choose your team: Yennefer or Triss ")
    accepted_answers = ["Triss", "Merigold"]
    if ask.upper() in [answer.upper() for answer in accepted_answers]:
        print("Lambert Lambert, Ty...")
    else:
        print("( ͡° ͜ʖ ͡°)")

Land()
