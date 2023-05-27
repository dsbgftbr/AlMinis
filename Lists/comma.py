spam = ["apples", "bananas", "tofu", "cats"]
pets = ["fish", "squid", "cats"]


def comma_join(strings):
    listlength = len(strings)
    if not (strings):
        return
    elif listlength == 1:
        return strings[0]
    else:
        mid = ("," if listlength > 3 else "") + " and "
        return f"{', '.join(strings[:-1])}{mid}{strings[-1]}"


print(comma_join(spam))
print(comma_join(pets))
print(comma_join([]))
