

import useful_tools

from questions import Question
from chef import Chef
from chinesechef import ChineseChef

from pathlib import Path


from student import Student



def examples_class () :
    student1 = Student("Jim", "Business", 3.1, False)
    student2 = Student("Pam", "Art", 3.5, True)
    print (student1.name)
    print (student1.gpa)
    print (student2.on_honor_roll())
    return


question_prompts = [
    "What color are apples\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are strawberies?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print ("You got got " + str(score) + " out of " + str(len(questions)) + " correct")
    return



def examples_inheritance():
    #my_chef = Chef()
    #my_chef.make_chicken()
    my_chinese_chef = ChineseChef()
    my_chinese_chef.make_chicken()
    my_chinese_chef.make_special_dish()
    return



# ------ main
#examples_class()
#run_test(questions)
#examples_inheritance()

