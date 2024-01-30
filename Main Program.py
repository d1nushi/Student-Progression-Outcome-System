# Create empty lists to store the progression outcomes
progress = []
trailer = []
retriever = []
exclude = []
progress_data = []


def ask_to_continue():
    while True:
        respond = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results : ")
        if(respond == "y"):
            print(" ")
            get_inputs()
        if(respond == "q"):
            break
#-----Getting inputs from the user
def get_inputs():
    while True:
        try:

            #-----check whether the credits entered are in range
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
                
            #-----Determining the progression outcome and appending to the appropriate list
            else:
                if credits_at_pass == 120:
                    print("Progress") 
                    progress.append("Progress")
                    progress_data.append(["Progress", credits_at_pass, credits_at_defer, credits_at_fail])
            
                elif credits_at_pass == 100:
                    print("Progress(module trailer)")
                    trailer.append("Progress(module trailer)")
                    progress_data.append(["Progress(module trailer)", credits_at_pass, credits_at_defer, credits_at_fail])
                
                elif credits_at_pass == 80 or credits_at_pass == 60:
                    print("Do not progress-module retriever")
                    retriever.append("Do not progress-module retriever")
                    progress_data.append(["Do not progress-module retriever", credits_at_pass, credits_at_defer, credits_at_fail])
                                
                elif credits_at_fail == 120 or credits_at_fail == 100 or credits_at_fail == 80:
                    print("Exclude")
                    exclude.append("Exclude")
                    progress_data.append(["Exclude", credits_at_pass, credits_at_defer, credits_at_fail])

                else:
                    print("Do not progress-module retriever")
                    retriever.append("Do not progress-module retriever")
                    progress_data.append(["Do not progress-module retriever", credits_at_pass, credits_at_defer, credits_at_fail])
                                            
                break
            
        except ValueError:
            print("\nInteger required\n")#-----credit inputs should be integer
#-----calling the functions
get_inputs()
ask_to_continue()

#---Histogram
progress_count = len(progress)
trailer_count = len(trailer)
retriever_count = len(retriever)
exclude_count = len(exclude)
total_count = progress_count + trailer_count + retriever_count + exclude_count

print("\n--------------------------------------------------")
print("Histogram")
print("Progress ", progress_count,":", "*"*progress_count)
print("Trailer ", trailer_count,":", "*"*trailer_count)
print("Retriever ", retriever_count,":", "*"*retriever_count)
print("Excluded ", exclude_count,":", "*"*exclude_count)
print("")
if total_count == 1:
    print(total_count ,"outcome in total. ")
else:
    print(total_count ,"outcomes in total. ")
    
print("----------------------------------------------------------")

#---Part 2 – List
print("Part 2:")
for data in progress_data:
    print(data[0], "-", data[1], ",", data[2], ",", data[3])
print("--------------------------------------------------")
progress_count = len(progress)
trailer_count = len(trailer)
retriever_count = len(retriever)
exclude_count = len(exclude)

#---Part 3 - Text File
text_file = open("Text_file.txt", "w")
text_file.write("Part 3:\n")
for data in progress_data:
  text_file.write(",".join(str(x) for x in data) + "\n")
text_file.close()





