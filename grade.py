English = {}
Maths = {}
History = {}
Science = {}
q="e"
while(q!="Exit"):
    print("Press Y if you want to enter a record of a Student:")
    print("Press M for Highest Marks Subjectwise:")
    print("Press P for Percentage of a student:")
    y=input()
    if(y=='Y'):
        print("*All in lower case*")
        while(y=='Y'):
            print("Enter the Name of the Student")
            Name=input()
            print("******Enter Marks******")
            print("English:")
            v=input()
            English[Name]=v
            print("Maths:")
            v=input()
            Maths[Name]=v
            print("History:")
            v=input()
            History[Name]=v
            print("Science:")
            v=input()
            Science[Name]=v
            print("For more press Y")
            y=input()
    elif(y=='M'):
        print("Maximum marks in English:",English[max(English)],"of",max(English))
        print("Maximum marks in Maths:",Maths[max(Maths)],"of",max(Maths))
        print("Maximum marks in History:",History[max(History)],"of",max(History))
        print("Maximum marks in Maths:",Science[max(Science)],"of",max(Science))
    elif(y=='P'):
        print("Enter the Name of the Student:\n(All in lower case)")
        print(English.keys())
        Name=input()
        Per=(English[Name]+Maths[Name]+History[Name]+Science[Name])/4
        print("Percentage is: ",Per)
    print("Type:\"Exit\" if you want to quit.")
    q=input()
