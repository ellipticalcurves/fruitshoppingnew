import numpy 
fruit_dictionary = {
    "apple":"Look for pink lady apples for crispy sweet flavor",
    "banana":"green to yellow, yellow indicates more ripeness",
    "watermelon": "Look for a yellow patch or spot on the top/bottom"
}

shopping_list = []
shopping_list_item = input(
    "what do you need to add to the shopping list?\n"
    )
shopping_list.append(str(shopping_list_item))

moreitemscheck = "Y"#"input("add another item? Y/n: ")"

while moreitemscheck!="n":
    shopping_list_item = input(
        """What do you need to buy? \n Type n if no more items need to be added:
        \n"""
            )
    if shopping_list_item=="n":
        moreitemscheck="n"
        break
    else:
        shopping_list.append(shopping_list_item)
    

def good_items(shopping_items, tips_dict):
    tips_list = []
    for item in shopping_items:
        for key in tips_dict:
            if key in item:
                tips_list.append(tips_dict[key])
                break
    return tips_list

good_item_tips = good_items(shopping_list, fruit_dictionary)
print("Tips for finding good items:")
for tip in good_item_tips:
    print(tip)

