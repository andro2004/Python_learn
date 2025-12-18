#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.


####solution#######
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    grades_list = student_marks[query_name]
    sum_grades = 0
    for grade in grades_list:
        sum_grades += grade
    average = sum_grades / len(grades_list)
    print(f"{average:.2f}")