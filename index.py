import pandas as pd

df=pd.read_csv("C:\\Users\\adity\\OneDrive\\Documents\\hotelm.csv")

art=int(input("Enter the choice:"))

if art==0 :
    
    b=int(input("Enter the CustomerID:"))
    print(df.loc[b])

elif art==1 :


    
    nv=input("Enter your NAME:")
    av=input("Enter your AGE:")
    cv=input("Enter your COUNTRY:")
    dv=input("Enter your PHONE NO.:")
    iv=input("Enter your DATE OF CHECKIN:")
    
    
    print("\n\tWE HAVE FOLLOWING OPTIONS")
    print ("\t----- --")
    print ("1.Ultra Royal -- Rs. 8500") 
    print ("2. Royal ---Rs. 6500")
    print ("3.Elite ---Rs. 4500")

    ch=input ('Enter Your choice: ') 
    da=int (input ("Enter Number Of days: "))
    if ch==1:
        print ("Ultra Royal Room rent: 8500") 
        print ("Your Total Room Rent is : Rs. ",8500*da)
    elif ch==2: 
        print ("Royal Room rent: 6500") 
        print ("Your Total Room Rent is : Rs. ", 6500*da)
    elif ch==3: 
        print ("Elite Room rent: 4500") 
        print ("Your Total Room Rent is : Rs. ", 4500*da)
    elif ch==4: 
        print ("Budget Room rent: 3000") 
        print ("Your Total Room Rent is : Rs. ",3000*da) 
        print (" ") 
        print ("THANK YOU!!! YOUR ROOM HAS BEEN BOOKED FOR: ", da, 'DAYS! ')
                
    rv=input("Enter your ROOM TYPE:")



    
    print("\n\tWE HAVE FOLLOWING OPTIONS")
    print ("\t----- --")
    print ("1. Vegetarian Combo-->>Rs.300") 
    print ("2.Non Vegetarian--->>Rs.500")
    print ("3.Vegterian and Non-Vegetarian------->>Rs. 750") 
    cu=int (input("\nEnter Cuisine Number: ")) 
    qn=int(input("Enter Quantity: "))
    if cu==1:
        pr=300 
        print ("") 
        print ("SO YOU HAVE ORDERED VEGETARIAN COMBO")
        tt=qn*pr
    elif cu==-2:
        pr=500 
        print("SO YOU HAVE ORDERED NON-VEGETARIAN COMBO")
        tt=qn*pr
    elif cu== 3: 
        pr=750 
        print ("SO YOU HAVE ORDERED VEGETARIAN AND NON-VEGETARIAN COMBO")
        tt=qn*pr 
    print ("YOUR TOTAL BILL AMOUNT IS------ Rs. ", tt, )
    print ("ENJOY YOUR MEAL !!! \n")
    fv=input("Enter your FOOD TYPE:")



    print("\n\t THE GAMESMEN") 
    print ("\t--\n") 
    print ("1. Table Tenni------>>150 Rs/Hr")  
    print ("2. Bowling--- ------>>100 Rs./Hr ") 
    print("3. Swimming Pool Games----->>350 Rs/Hr") 
    print ("4. Video Games-- ------>>300 Rs./Hr ")  
    print ("5. Snooker-------->>250 Rs/Hr. ")
 
    wg=int (input ("\nEnter Your Game Choice: ")) 
    tm=int (input ("Enter No. Of Hours You Want To Play : ")) 
    if wg==1:
        pr=150 
        print (" ") 
        print ("YOU HAVE DECIDED TO PLAY: Table Tennis") 
    elif wg==2: 
        pr=100 
        print("YOU HAVE DECIDED TO PLAY: Bowling") 
    elif wg==3: 
        pr=350 
        print ("YOU HAVE DECIDED TO PLAY: Swwiming Pool Games") 
    elif wg==4: 
        pr=300 
        print ("YOU HAVE DECIDED TO PLAY: Video Games") 
    elif wg==5: 
        pr=250 
        print ("YOU HAVE DECIDED TO PLAY: Snooker") 
        tt=pr*tm 
    print ("\nYOUR TOTAL GAMING BILL IS: Rs.", tt, "FOR", tm,' HOURS!')
    print ("WE HOPE YOU WILL ENJOY YOUR GAME!! \n")
    gv=input("Enter your GAME TYPE:")

    

    ov=input("Enter your DATE OF CHECKOUT :")


    
    
    kv=df.size
    
    jv=int(kv/10)



    df.loc[dv]=[jv,nv,av,cv,dv,rv,fv,gv,iv,ov]
    df.to_csv("C:\\Users\\adity\\OneDrive\\Documents\\hotelm.csv",index=False)




    print("\t\t BILL ") 
    print("\t\t**********") 
    
    

    
    print("your customerid is",jv)




else :
    
    print(df)
