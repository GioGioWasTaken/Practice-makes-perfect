from Classes import multiple_question
multiple_question1=multiple_question(True,False,False,False)
multiple_question2=multiple_question(False,False,True,False)
questions=[{'What color are apples?\nA. Red/Green\nB. Orange\nC. invisble\nD. Purple':multiple_question1},
           {'What color are bananas?\nA. Blue\nB. Orange\nC. Yellow\nD. They are a conspiracy':multiple_question2}] # a dict list, each item is a dict, which means each item has a question and a value
def user_input():
    score=0
    for question in questions:
        print(list(question.keys())[0])  #there's only 1 key so list[0] will be the question prompt in the location the for loop is iterating through.
        user_answer=str(input('Enter the answer number you think is correct: '))
        if user_answer.lower()=='a':
            user_answer=list(question.values())[0].a #access all the values of the question element, since it has only 1 key we can than make it into a list and access the 0 element, and it'll be our class. we can than easily get the class value
        elif user_answer.lower()=='b':
            user_answer=list(question.values())[0].b
        elif user_answer.lower() == 'c':
            user_answer=list(question.values())[0].c
        elif user_answer.lower()=='d':
            user_answer=list(question.values())[0].d
        if user_answer==True:
            score=score+1
    print(f'Your score is {score}, Which means you got {score} questions correctly.')
    return score
user_input()