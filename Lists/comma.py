def comma_join(strings):
    listlength = len(strings)

    if not (strings):
        return
    elif listlength == 1:
        return strings[0]
    else:
        mid = ("," if listlength > 3 else "") + " and "
        return ", ".join(strings[:-1]) + mid + strings[-1]
