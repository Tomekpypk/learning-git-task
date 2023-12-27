shopping_dict = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}

total_items = 0

for shop, items in shopping_dict.items():
    shop = shop.capitalize() 
    print(f"Idę do {shop} i kupuję tam: {(items)}.").capitalize()