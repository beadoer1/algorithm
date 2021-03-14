all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    present_check_dict = {}
    for student in all_students:
        present_check_dict[student] = 0
        # present_check_dict.update({student:0})
    for student in present_students:
        del present_check_dict[student]
        # present_check_dict.pop(student)
    return present_check_dict.keys()

print(get_absent_student(all_students, present_students))