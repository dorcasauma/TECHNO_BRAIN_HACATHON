num = input()

no_dups = []
for i in num:
    try:
        i = int(i)
    except:
        print("Please enter only numbers, you entered: ", i)
        continue
    if i in no_dups:
        pass
    else:
        no_dups.append(i)
no_dups.sort(reverse=True)
print("No duplicated and sorted in descending order: ", no_dups)