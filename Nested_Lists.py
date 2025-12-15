#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
    score_list=[]
    names_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_list.append(name)
        score_list.append(score)


    data=[]
    for i in range(len(score_list)):
        data.append([names_list[i],score_list[i]])
    min_score = min(score_list)

    data = [d for d in data if d[1]>min_score]
    
    score_list=[]
    for d in data:
        score_list.append(d[1])
    
    min_score = min(score_list)
    min_names=[]
    for i in range(len(data)):
        if data[i][1] == min_score:
            min_names.append(data[i][0])
    
    min_names.sort()
    for name in min_names:
        print(name)
    