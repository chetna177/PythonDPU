#wap to create student feedback

while True:

    #student name
    name = ""
    while(not name.isalpha()):# and name ==""
        print("Validating student name ");
        print("Invalid  Student name ");
        name = input("enter student name \n").strip();
    print("student name validated")
    print("validating course name")

    #course name
    course_name = ""
    while (not course_name.isalpha()):  # and name ==""
        print("Validating course name ");
        print("Invalid  course name ");
        course_name = input("enter course name \n").strip();
    print("course  name validated")
# while True:
#     course = input("enter your course code \n").strip();
#
#     if(course !=""):
#         print("Course code is:",course);
#         break;
#
#     else:
#         print("Invalid course code \n");

    #course code
   #course name
    course_code = ""
    while (not course_code.isalnum()):  # and name ==""
        print("Validating course code ");
        print("Invalid  course code \n");
        course_code = input("enter course code \n").strip();
    print("course  code validated")

    #faculty name
    faculty_name="";
    while (not faculty_name.isalpha()):  # and name ==""
        print("Validating faculty name ");
        print("Invalid  faculty name \n");
        faculty_name = input("Enter faculty name:").strip();
    print("faculty  name validated")

    #user rating
    rating = "0";
    while (not rating.isnumeric() or (int(rating)<1 or int(rating)>5)):  # and name ==""
        print("Validating rating ");
        print("Invalid rating \n");
        rating = input("Enter rating:").strip();
    print("rating is  validated");

    break
print("______________________________________________________________");
print(f"student name: {name}")
print(f"course name: {course_name}")
print(f"course code: {course_code}")
print(f"faculty name: {faculty_name}")
if(rating ==5):
    print("Excellent");
elif(rating==4):
    print("Great");
elif(rating==3):
    print("Good");
else:
    print("better luck next time")













































    #display rating