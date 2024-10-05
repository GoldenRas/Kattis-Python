message = input()
has_smiley = ":)" in message
has_frowny = ":(" in message
if has_smiley and has_frowny:
    print("double agent")
elif has_smiley:
    print("alive")
elif has_frowny:
    print("undead")
else:
    print("machine")