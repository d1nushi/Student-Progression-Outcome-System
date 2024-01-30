#Determining variables
progress = []
trailer = []
retriever = []
exclude = []
progression_data = {}

def ask_to_continue():
    while True:
        respond = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results : ")
        if(respond == "y"):
            print(" ")
            get_inputs()
        if(respond == "q"):
            break

def get_inputs():
    while True:
        try:
            #-----check whether the credits entered are in range

            student_id = input("Please eneter your student id : ")
            credits_at_pass = int(input("Please enter your credits at pass : "))
            if credits_at_pass not in [0,20,40,60,80,100,120]: 
                print("Out of  range")
                break
            
            credits_at_defer = int(input("Please enter your credits at defer : "))
            if credits_at_defer not in [0,20,40,60,80,100,120]:
                print("Out of  range")
                break
            
            credits_at_fail = int(input("Please enter your credits at fail : "))
            if credits_at_fail not in [0,20,40,60,80,100,120]:
                print("Out of  range")
                break
            
            #-----check whether the total of credits is 120
            elif credits_at_pass + credits_at_defer + credits_at_fail > 120 or credits_at_pass + credits_at_defer + credits_at_fail < 120:
                print("Total incorrect")

            else:
                if credits_at_pass == 120:
                    print("Progress") 
                    progression_data[student_id] = ["progress",credits_at_pass,credits_at_defer,credits_at_fail]
                    
                elif credits_at_pass == 100:
                    print("Progress(module trailer)")
                    progression_data[student_id] = ["Progress(module trailer)",credits_at_pass,credits_at_defer,credits_at_fail]

                elif credits_at_pass == 80 or credits_at_pass == 60:
                    print("Do not progress-module retriever")
                    progression_data[student_id] = ["Do not progress-module retriever",credits_at_pass,credits_at_defer,credits_at_fail]

                elif credits_at_fail == 120 or credits_at_fail == 100 or credits_at_fail == 80:
                     print("Exclude")
                     progression_data[student_id] = ["Exclude",credits_at_pass,credits_at_defer,credits_at_fail]

                else:
                     print("Do not progress-module retriever")
                     progression_data[student_id] = ["Do not progress-module retriever",credits_at_pass,credits_at_defer,credits_at_fail]

                break
            
        except ValueError:
            print("\nInteger required\n")

get_inputs()
ask_to_continue()

print("\nPart 4:")
for key, value in progression_data.items():
    print(key + ":",end=" ")
    print(*value,sep=",")
