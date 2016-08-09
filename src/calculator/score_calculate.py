
def score_calculate(string):
    correct=incorrect=0
    if string[0] == 'a':
        correct = correct + 1
    else:
        incorrect = incorrect + 1


    if string[1] == 'b':
        correct = correct + 1
    else:
        incorrect = incorrect + 1

    if string[2] == 'a':
        correct = correct + 1
    else:
        incorrect = incorrect + 1

    if string[3] == 'c':
        correct = correct + 1
    else:
        incorrect = incorrect + 1

    if string[4] == 'd':
        correct = correct + 1
    else:
        incorrect = incorrect + 1

    if string[5] == 'b':
        correct = correct + 1
    else:
        incorrect = incorrect + 1

    if string[6] == 'c':
        correct = correct + 1
    else:
        incorrect = incorrect + 1

    if string[7] == 'd':
        correct = correct + 1
    else:
        incorrect = incorrect + 1

    if string[8] == 'a':
        correct = correct + 1
    else:
        incorrect = incorrect + 1



    correct = correct*6.25
    incorrect = incorrect*4.75
    total = correct + incorrect
    total = total/100

    return total





