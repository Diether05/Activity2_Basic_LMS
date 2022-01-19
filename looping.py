import  prompt
import menu
import database


def loop():
    user_input = int(input(menu.manage_menu))
    while user_input != 7:
        if user_input == 1:
            user_input2 = int(input(menu.student_menu))
            while user_input2 != 5:
                # exit
                if user_input2 == 1:
                    # add student
                    prompt.prompt_add_student()
                    break;
                elif user_input2 == 2:
                    # view student list
                    prompt.prompt_view_student()
                    break;
                elif user_input2 == 3:
                    # View student class
                    prompt.prompt_view_student_class()
                    break;
                elif user_input2 == 4:
                    # remove student
                    prompt.prompt_remove_student()
                else:
                    print("Invalid input, please try again!")

                user_input2 = int(input(menu.student_menu))

        elif user_input == 2:
            user_input3 = int(input(menu.teacher_menu))
            while user_input3 != 5:
                # exit
                if user_input3 == 1:
                    # add teacher
                    prompt.prompt_add_teacher()
                elif user_input3 == 2:
                    # view all teacher
                    prompt.prompt_view_teacher()
                elif user_input3 == 3:
                    # View teacher's class
                    prompt.prompt_view_teachers_class()
                elif user_input3 == 4:
                    # remove teacher
                    prompt.prompt_remove_teacher()
                else:
                    print("Invalid input, please try again!")

                user_input3 = int(input(menu.teacher_menu))

        elif user_input == 3:
            user_input4 = int(input(menu.subject_menu))
            while user_input4 != 4:
                # exit
                if user_input4 == 1:
                    # add subject
                    prompt.prompt_add_subject()
                elif user_input4 == 2:
                    # view all subject
                    prompt.prompt_view_subject()
                elif user_input4 == 3:
                    # remove subject
                    prompt.prompt_remove_subject()
                else:
                    print("Invalid input, please try again!")

                user_input4 = int(input(menu.subject_menu))

        elif user_input == 4:
            user_input5 = int(input(menu.class_menu))
            while user_input5 != 4:
                # exit
                if user_input5 == 1:
                    # add class
                    prompt.prompt_add_class()
                elif user_input5 == 2:
                    # view all class
                    prompt.prompt_view_class()
                elif user_input5 == 3:
                    # remove class
                    prompt.prompt_remove_class()
                else:
                    print("Invalid input, please try again!")

                user_input5 = int(input(menu.class_menu))

        elif user_input == 5:
            prompt.prompt_view_student_subject()
        
        elif user_input == 6:
            prompt.prompt_view_teacher_subject()

        else:
            print("Invalid input, please try again!")

        user_input = int(input(menu.manage_menu))
