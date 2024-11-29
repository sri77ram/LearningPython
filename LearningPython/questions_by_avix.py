import random


def for_loop_question_random():
    main_list = []
    temp_list = []
    for i in range(25):
        temp_list = []
        for x in range(25):
            temp_list.append(random.randint(0, 255))
        main_list.append(temp_list)
        temp_list = 0

    return main_list

