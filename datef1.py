chk= True

while chk:
    days =0
    ref=[1,1,1700]
    inp=input(" Enter the date after 1-1-1700 (dd-mm-yyyy): ")
    datetemp = inp.split("-")
    try:
        date=[int(datetemp[x]) for x in range(3)]
    except:
        print(" Enter in the right format")
        continue 
    isleap=False
    def leap(year):
        temp= False
        if year%100 != 0:
            if year%4 == 0:
                temp= True
            else:
                temp= False    
        else:
            if year%400 == 0:
                temp= True 
            else:
                temp= False      
        return temp        
    isleap = leap(date[2])  
    day =["fri","sat", "sun", "mon","tue","wed","thu"]
    months=[]
    monthstday={}
    
    
    # creating [31,28,30...] no of days in a month
    for i in range(12):
        if i == 1:
            months.append(28)
        elif i in (3,5,8,10):
            months.append(30)
        else:
            months.append(31)        
        
    leapmonth=[months[k] for k in range(12)]
    leapmonth[1]=29
    
    # checking input
    if date[1] <= 12:
        if isleap==False:
            if months[date[1]-1] < date[0]:
                
                print(" invalid date")
                continue
        else:
            if leapmonth[date[1]-1] < date[0]:
                print(" invalid date")
                continue
    else:
        print(" invalid date") 
        continue
    
    if date[2] < 1700:
        print(" date must be less than 1-1-1700")  
        continue  
        
        
    #agragate sum of months[0,31,31+30,...]               
    for j in range(12):
        if(date[2]%4 != 0):
            monthstday[j]= sum(months[ :j])
            days = 1
            
        else:
            monthstday[j]= sum(leapmonth[ :j])
            
    #counting number of leap years         
    noleap=0
    noyear=0        
    for i in range(date[2]-ref[2]):
        var=leap(ref[2] +(i+1))
        if var:
            noleap += 1
        else:
            noyear += 1    
            
    # Adding the total days
    days += date[0]- ref[0]
    days += monthstday[date[1]- ref[1]]   
    days += noleap*sum(leapmonth) + noyear*sum(months)
    days -= 1
    
    print(day[days%7])
    # interface    
    while chk:
        a= input("\ndo you wish to continue(y/n): ").lower()
        if a=='y':
            break
        elif a=="n":
            chk= False
            break
        else:
            print("invalid response") 
            continue   
    
        

