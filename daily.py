name=input("name:")
regno=input("regno:")
OOPS_grade,OS_grade,AI_grade,DBMS_grade=input("enter grade of oops,os,ai,dbms").split(" ")
OOPS_credit,OS_credit,AI_credit,DBMS_credit=(input("enter credit hours of OOPS,OS,AI,DBMS")).split(" ")
OOPS_credit,OS_credit,AI_credit,DBMS_credit=int(OOPS_credit),int(OS_credit),int(AI_credit),int(DBMS_credit)
points={"O":5,"A":4,"B":3,"C":2,"U":0}
grade_points=(points[OOPS_grade]*OOPS_credit)+(points[AI_grade]*AI_credit)+(points[DBMS_grade]*DBMS_credit)+(points[OS_grade]*OS_credit)
grade_points=int(grade_points)
credit_points=OOPS_credit+AI_credit+DBMS_credit+OS_credit
cgpa=grade_points/credit_points
print(f"Name:{name} \nRegisterNo:{regno} \ncgpa:{cgpa:.2F} ")