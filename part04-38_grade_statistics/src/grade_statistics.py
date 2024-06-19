# Write your solution here
import math

def sum_of_points(points_list):
    index=0
    points_sum=[]
    while index<len(points_list)-1:
        points_sum.append(math.floor(int(points_list[index][1])*0.1) + int(points_list[index][0]))
        index+=1
        
    return points_sum

    
def points_average(sum_of_points, students):
    points_average=sum(sum_of_points)/(students)

    return points_average


def pass_percentage(points_list, sum_of_points, students):
    failed=0
    index=0
    while index<len(points_list)-1:
        if int(points_list[index][0]) < 10 or sum_of_points[index]<14:
            failed+=1
        index+=1
    pass_percentage=((students-failed)/(students))*100
    return pass_percentage


def grade_dist(points_list):
    grades_dict={
        "5:": "",
        "4:": "",
        "3:": "",
        "2:": "",
        "1:": "",
        "0:": ""}
    index=0
    while index<len(points_list)-1:
        x=math.floor(int(points_list[index][1])*0.1) + int(points_list[index][0])
        if int(points_list[index][0]) < 10 or x <=14:
            grades_dict['0:']+='*'
        elif 17 >= x > 14:
            grades_dict['1:']+='*'
        elif 20 >= x > 17:
            grades_dict['2:']+='*'
        elif 23 >= x > 20:
            grades_dict['3:']+='*'
        elif 27 >= x > 23:
            grades_dict['4:']+='*'
        elif x > 27:
            grades_dict['5:']+='*'
        index+=1
    return grades_dict



def main():
    students=-1
    points=[]
    while True:
        text=input("Exam points and exercises completed: ")
        points.append(text.split(" "))
        students+=1
        if not text:
            break
    stat_sum=sum_of_points(points)
    stat_avg=points_average(stat_sum, students)
    stat_pass=pass_percentage(points, stat_sum, students)
    grades=grade_dist(points)
    print(f"Statistics: \nPoints average: {stat_avg}\nPass percentage: {stat_pass:.1f}\nGrade distribution:")
    for x,y in grades.items():
        print (x,y)
main()