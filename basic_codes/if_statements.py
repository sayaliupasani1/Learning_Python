are_hungry = False
are_veg = False

if are_hungry and are_veg:
    print("You are hungry!")
    print("We only have an option of Salads for vegetarians!")
else:
    print("You don't seem to be hungry or you are a non-vegetarian!")
    if not(are_veg):
        print("We have a whole bunch of options that include meat!")
