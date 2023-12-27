shopping_dict = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}

total_items = 0

for shop, items in shopping_dict.items():
    shop = shop.upper() 
    items = [item.upper() for item in items]  
    print(f"Idę do {shop} i kupuję tam: {items}.")

    total_items += len(items)

print(f'W sumie kupuję {total_items} produktów.')
