inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    count = 0
    for k, v in inventory.items():
        print(str(v)+" "+k)
        count = count + v
    return count

total = display_inventory(inventory)
print("Total number of items: "+str(total))

