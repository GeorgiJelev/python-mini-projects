import random

question = ["Кога е основана България?", "Колко са цветовете на българското знаме?", \
            "През коя година се е състояла битката при река Ахелой?"]
correct_answers = 0
wrong_answers = 0
questions_answered = []

for i in range(10):
    current_question = random.choice(question)

    if current_question not in questions_answered:
        questions_answered.append(current_question)
        print(current_question)
    else:
        continue

    if current_question == "Кога е основана България?":
        answer = input("Моля отгоровете на въпроса:")
        if answer == "681":
            print("Правилен отговор!\n")
            correct_answers +=1
        else:
            print("Грешен отговор!\n")
            wrong_answers += 1

    elif current_question == "Колко са цветовете на българското знаме?":
        answer = input("Моля отгоровете на въпроса:")
        if answer == "3":
            print("Правилен отговор!\n")
            correct_answers +=1
        else:
            print("Грешен отговор!\n")
            wrong_answers += 1

    elif current_question == "През коя година се е състояла битката при река Ахелой?":
        answer = input("Моля отгоровете на въпроса:")
        if answer == "917":
            print("Правилен отговор!\n")
            correct_answers +=1
        else:
            print("Грешен отговор!\n")
            wrong_answers += 1

    if correct_answers > 2:
        print("Вие се справихте отлично с теста!")

    elif wrong_answers > 2:
        print("Вие се справихте слабо с теста!")

