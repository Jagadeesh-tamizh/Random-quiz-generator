import random


def print_user_credentials(name, topic):  # prints user credentials
    print("CREDENTIALS\nName  : %s\nTopic : %s" % (name, topic))


def generate_report(total, crt):  # generates quiz report
    print("Total number of questions - ", total,
          "\nNumber of questions answered correctly - ", crt, "\n")


def get_number_question():  # gets number of question to be generated from the user
    N = int(input("\nEnter the number of questions to be generated : "))
    return N


class RandomIntegerGenerator:
    def generate(self):  # method to generate a random number
        return random.randint(1, 100)


class Choices(RandomIntegerGenerator):
    def generate_choices(self):  # generate random number sequence
        arr = []
        for i in range(0, 10):
            arr.append(self.generate())
        return arr


class PrintQuestion:
    def printer(self, options, answers, ans, position):  # prints the questin and choices
        print("\nThe number sequence is ", answers)
        print("What is the position of ", ans)
        global crt_option
        for i in range(1, 5):
            print(i, ")", options[i-1])
            if(options[i-1] == position):
                crt_option = i


class GetUserResponse:
    def get_response(self):  # get user response for the corresponding question
        response = int(input("Enter the correct option : "))
        return response


class Question(Choices, PrintQuestion, GetUserResponse):
    def generate_question(self):
        global answers
        global cs
        answers = self.generate_choices()  # generate number sequence
        ans = random.choice(answers)
        options = []
        position = answers.index(ans) + 1
        options.append(position)

        for i in range(0, 3):  # BLOCK TO GENERATE ALTERNATE WRONG OPTIONS
            opt = random.randrange(1, position+3)
            flag = 0
            if(opt in options):
                flag = 1
                while(flag == 1):
                    opt = random.randrange(position-2, position+2)
                    if(opt not in options):
                        flag = 0
            options.append(opt)
        random.shuffle(options)  # shuffle generated options

        # call method printer to print the question
        self.printer(options, answers, ans, position)

        response = self.get_response()  # get user response by calling get_response() method
        if(response == crt_option):
            print("It is the correct answer\n")
            cs += 1
        else:
            print("It is the wrong answer\n")


N = get_number_question()  # get number of questions to be generated from the user
total = N
cs = 0
questions = Question()


while(N > 0):
    questions.generate_question()
    N -= 1
    try:
        if(N == 0):
            # Promt to finish the quiz
            input("Press enter to finish the quiz\n\n\n")
        else:
            # Block to prompt for next question
            input("Press enter to move to next question...")
    except SyntaxError:
        pass


generate_report(total, cs)  # report generation
# credits generation
print_user_credentials("Jagadeesh", "Find position problem")
