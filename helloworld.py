print("Hello World")
x = 3
z = 3.4
print(x + z)
print("sadasdasd{0}. iam {1}".format(x,z))
if x == 3:
    print("Number is 3")
else:
    print("Number is not 5")
number = 5
if number:
    print("Number is defined  and truty")
text = "Python"
if text:
    print("Text is defined and truty")
print("bigger" if x > number else "smaller")

student_names = ["mark","yifei","yangyang"]

print(student_names[1])
print(student_names[-1])
if "mark" in student_names:
    print("yes")

del student_names[2]
for name in student_names[:-1]:
    print(f"asdasd{name}")
student_names = ["James", "Katarina","Jessica","Mark","Bort","Frank Grimes","Max Power"]
for name in student_names:
    if name == "Bort":

        continue
    print("Current testing " + name)
x = 0;
while x < 10:
    print("Count is {0}".format(x))
    x+=1
student ={
    "name":"Mark",
    "student_id":15163,
    "feedback":None
}
all_students = [
    {"name":"Mark","student_id":15163},
    {"name":"Katarina","student_id":63112},
    {"name":"Jesscia", "stduent_id":30021}
]
for key in all_students:
    if(key["name"] == "Mark"):

        print(key["student_id"])
student["last_name"] = "Yifei"
try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I can't add these two together")
    print(error)

print("this code Executes")

