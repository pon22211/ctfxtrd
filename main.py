with open("1.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)

author=input("Хто написав ці рядки?")
with open ("quotes.txt", "a", encoding="UTF-8") as file:
    file.write(f"({author})\n")

while True:
    answer=input("Бажаєте додати ще одну цитату? (так/ні)")
    answer=answer.lower()
    if answer == "так":
        quote=input("")
        author=input("")
        file=open("quotes.txt", "a", encoding="UTF-8")
        file.write(f"{quote}\n({author})\n")
        file.close()
    else:
        break

with open("quotes.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)
