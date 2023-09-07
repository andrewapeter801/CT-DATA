languages = ["python", "ruby", "C"]
print(languages[0])
print(languages[1])
print(languages[2])

messages = f"My first language was {languages[0].title()}!"
print(messages)
languages[1] = "C++"
print(languages)
languages.append("ruby")
print(languages.insert(1, "javascript"))
print(languages)
del languages[2]
print(languages)
popped = languages.pop()
print(languages)
print(popped)
languages.reverse()
print(languages)
print(sorted(languages))
print(len(languages))
