
def main():
    age = int(input("How old are you? "))
    statement = input("Say something")
    if age <16 or "floglegroopp" > statement:
        print("you are young enough to be silly")
    else:
        print("oh no you are so old!")

#main()

def little_sister():
    number_of_times = 0
    say_it = "Yeet it now"
    what_you_said = ""
    while number_of_times <10 and say_it.lower() != what_you_said.lower():
        what_you_said = input("Say it Comp151 Student")
        number_of_times += 1
        what_you_said = what_you_said[:12]
    if number_of_times < 10:
        print("Hooray you said it")
    else:
        print("Aww you are so boring")



little_sister()