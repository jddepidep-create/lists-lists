list = []
forwarddown = []
while len(list) < 5:
        score = int(input("Please insert scores: "))
        if 0 <= score <= 10:
            list.append(score)
        else:
            print("Please within 10")


forwarddown = list.copy()
print("backup made")
while True:
    choice = int(input("What yo choice"))
    if choice == 1:
        print(f"current list:{list}")
    elif choice == 2:
        additional = int(input("Add an additional score for me boy. "))
        if 0 <= additional <= 10:
            list.append(additional)
            print(f"Added!: {list}")
        else:
            print("Please within 10")
    elif choice ==3:
        try:
            insert=int(input("Where would you like to insert your score(index): "))
            score = int(input("What is your score? "))
            if 0 <= insert <= len(list) and 0 <= score <= 10:
                list.insert(insert, score)
                print(f"Added!: {list}")
            else:
                print("Please within 10")
        except ValueError:
            print("Please try again")

    elif choice == 4:
        remove = int(input("score to remove: "))
        if remove in list:
            list.remove(remove)
            print(f"Updated!: {list}")
        else:
            print("Try a valid")
    elif choice == 5:
        print("Removing last score...")
        if len(list) != 0:
            print(f"removed: {list.pop()}")
            print(f"Updated!: {list}")
        else:
            print("List is empty")
    elif choice == 6:
        search = int(input("Ultimate Search Engine: "))
        if search in list:
            print(f"Count:{list.count(search)}")
            print(f"first index: {list.index(search)}")
    elif choice == 7:
        if len(list) != 0:
            count = len(list)
            total = sum(list)
            avr = total / count
            hi = max(list)
            lo = min(list)
            print(f"count {count}")
            print(f"Total: {total}")
            print(f"Average score: {avr:.2f}")
            print(f"Maximum score: {hi}")
            print(f"Minimum score: {lo}")
        else:
            print("Please try again")
    elif choice == 8:
        sort = input("What would you like to sort by? A OR D ").lower()
        if sort == "a":
            list.sort()
            print(f"Sorted!: {list}")
        elif sort == "d":
            list.sort(reverse=True)
            print(f"Sorted!: {list}")
    elif choice == 9:
        print("Reversing scores...")
        list.reverse()
        print(f"Reversed!{list}")
    elif choice == 10:
        print("Clearing..")
        list.clear()
        print(f"List cLeared! {list}")
    elif choice == 11:
        print("Restoring...")
        list = forwarddown.copy()
        print(f"Probably restored: {list}")
    elif choice == 12:
        print("Its not like I LIKED serving you... B-BAKA!")
        break
    else:
        print("Pick within 1-12")