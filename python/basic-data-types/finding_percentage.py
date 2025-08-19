if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

#for i in student_marks.keys():
   # if i==query_name:
      #  print(format((sum(scores)/n),".2f"))
      
avg1 = sum(student_marks[query_name])/ len(student_marks[query_name])
print(format(avg1, ".2f"))
