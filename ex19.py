def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have: {cheese_count} cheeses!")
    print(f"You have: {boxes_of_crackers} boxes of craxhers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")

print ("We can just give the function nums directly.")
cheese_and_crackers(20, 30)

print ("OR we can use vars from our script:")
amount_of_cheese = 100
amount_of_crackers= 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside!...")
cheese_and_crackers(10+20, 5*6)

print("...and we can combine vars and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
