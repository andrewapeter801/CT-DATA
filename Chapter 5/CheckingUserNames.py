current_user = ["User1", "User2", "User3"]\
new_users = ["hi", "new", "Here"]

for new_user in new_users:
    if new_users in current_user:
        print(f"wow, I found you {new_user}")
    else:
        print("sorry, you are a newbie")