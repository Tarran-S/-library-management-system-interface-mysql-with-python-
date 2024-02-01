print("WELCOME TO THE LIBRARY")
while True:
    print("\n*MENU*\n")
    print("1.MEMBERS LIST")
    print("2.BOOKS LIST")
    print("3.DETAILS UPDATION ")
    print("4.BORROWING OF BOOKS")
    print("5.RETURNING OF BOOKS")
    print("6.EXIT")

    A=int(input("Enter preffered choice as numbers:"))

    if A==1:
          x=input("Enter yes if you are a new member:")
          if x=='yes':
              import mysql.connector as myc
              con = myc.connect(host="localhost", user="root", passwd="test123")
              mycursor = con.cursor()
              mycursor.execute("Use library")
              sql='''INSERT INTO members_lists(NAME,LIB_ID)values(y,d)'''
              while True: 
                  l=[]
                  y=input("Enter Name:")
                  d=input("Enter Lib_id:")
                  T=(y,d)
                  l.append(T)
                  ch=input("ENTER y TO CONTINUE")
                  if ch=='y':
                       pass
                
                  else:
                       break
              con.close()      
              
          else:
             import mysql.connector as myc
             con = myc.connect(host="localhost", user="root", passwd="test123")
             mycursor = con.cursor()
             mycursor.execute("Use library")
             mycursor.execute("Select * from members_list")
             result=mycursor.fetchall()
             for i in result:
                    print("NAME:",i[0],"LIB_ID:",i[1])
             con.close()
    elif A==2:
          import mysql.connector as myc
          con = myc.connect(host="localhost", user="root", passwd="test123")
          mycursor = con.cursor()
          mycursor.execute("Use library")
          mycursor.execute("Select * from bookslist")
          result=mycursor.fetchall()
          for i in result:
            print("TITLE:",i[0],"AUTHOR:",i[1],"AVAILABLITY:",i[2])
          con.close()
    elif A==3:
            print("\n*MENU*\n")
            print("UPDATE MEMBERS")
            import mysql.connector as myc
            con = myc.connect(host="localhost", user="root", passwd="test123")
            mycursor = con.cursor()
            mycursor.execute("USE library")
            sql='''INSERT INTO details(NAME,AGE,LIB_ID,DOB)
            values(%s,%s,%s,%s)'''
            L=[]
            while True:
                   c=input("Enter name:")
                   d=int(input("Enter age:"))
                   e=input("Enter library id:")
                   x=input("Enter Date of Birth:")
                   T=(c,d,e,x)
                   L.append(T)
                   ch=input("ENTER y TO CONTINUE")
                   if ch=='y':
                       pass
                
                   else:
                       break
        
            mycursor.executemany(sql,L)
            d=input("Enter libary id to search your details:")
            result=mycursor.fetchall()
            for i in result:
                 print("NAME:",i[0],"AGE:",i[1],"LIB_ID:",i[2],"DOB:",i[3])
            con.close()     
               
                   
          
    elif A==4:
        while True:
              print("\n*MENU*\n")
              print("1. STUDENT")
              print("2. TEACHER ")
              print("3. OTHERS")
              print("4. EXIT")
              ch=input("Enter choice as numbers")
              
              if ch=='1':
                   import mysql.connector as myc
                   con = myc.connect(host="localhost", user="root", passwd="test123")
                   mycursor = con.cursor()
                   mycursor.execute("USE library")
                   sql='''INSERT INTO studentinfo(NAME,CLASS,SECTION,BOOKTITLE,DATE_OF_BORROWING)
                   values(%s,%s,%s,%s,%s)'''
                   L=[]
                   while True:
                       s=input("Name of student:")
                       x=input("Enter the Class:")
                       c=input("Enter Section studying in:")
                       y=input("Enter title of book :")
                       z=input("Enter date of borrowing:")
                       T=(s,x,c,y,z)
                       L.append(T)
                       ch=input("ENTER y TO CONTINUE")
                       if ch=='y':
                           pass
                       else:
                           break
                   mycursor.executemany(sql,L)
                   con.commit()
                   y=input("Enter title of book :")
                   mycursor.execute("update bookslist set availability='Taken' where TITLE='%s'"%(y))
                   con.close()
                   print("Record stored")
                   break
    
              elif ch=='2':
                   import mysql.connector as myc
                   con = myc.connect(host="localhost", user="root", passwd="test123")
                   mycursor = con.cursor()
                   mycursor.execute("USE library")
                   sql='''INSERT INTO teacherinfo(NAME,SUBJECT,BOOKTITLE,DATE_OF_BORROWING)values(%s,%s,%s,%s)'''
                   L=[]
                   while True:
                       s=input("Name of teacher:")
                       x=input("Enter subject:")
                       y=input("Enter title of book :")
                       z=input("Enter date of borrowing:")
                       T=(s,x,y,z)
                       L.append(T)
                       ch=input("ENTER yes TO CONTINUE")
                       if ch=='yes':
                           pass
                       else:
                           break
                   mycursor.executemany(sql,L)
                   con.commit()
                   y=input("Enter title of book :")
                   mycursor.execute("update bookslist set availability='Taken' where TITLE='%s'"%(y))
                   con.close()
                   print("Record stored")
    
              elif ch=='3':
                   import mysql.connector as myc
                   con = myc.connect(host="localhost", user="root", passwd="test123")
                   mycursor = con.cursor()
                   mycursor.execute("USE library")
                   sql='''INSERT INTO othersinfo(NAME,CONTACTINFO,BOOKTITLE,DATE_OF_BORROWING)
                   values(%s,%s,%s,%s)'''
                   L=[]
                   while True:
                       s=input("Name of person:")
                       x=input("Enter contact info:")
                       y=input("Enter title of book :")
                       z=input("Enter date of borrowing:")
                       T=(s,x,y,z)
                       L.append(T)
                       ch=input("ENTER yes TO CONTINUE")
                       if ch=='yes':
                           pass
                       else:
                           break
                   mycursor.executemany(sql,L)
                   con.commit()
                   y=input("Enter title of book :")
                   mycursor.execute("update bookslist set availability='Taken' where TITLE='%s'"%(y))
                   con.close()
                   print("Record stored")
              else:
                   break
    elif A==5:
        
        while True:
              print("\n*MENU*\n")
              print("1. STUDENT")
              print("2. TEACHER ")
              print("3. OTHERS")
              print("4. EXIT")
              ch=input("Enter choice as numbers")
              
              if ch=='1':
                       import mysql.connector as myc
                       con = myc.connect(host="localhost", user="root", passwd="test123")
                       mycursor = con.cursor()
                       mycursor.execute("USE library")
                       d=input('ENTER YOUR NAME')
                       y=input('ENTER BOOK TITLE:')
                       z=input('ENTER DATE OF RETURNING:')            
                       sql=('update studentinfo set date_of_returning="%s"where BOOKTITLE="%s" and name="%s"'%(z,y,d))
                       mycursor.execute(sql)
                       con.commit()
                       mycursor.execute("update bookslist set availability='Open' where TITLE='%s'"%(y))
                       con.close()
                       print("Record stored")
                       break

              elif ch=='2':
                   import mysql.connector as myc
                   con = myc.connect(host="localhost", user="root", passwd="test123")
                   mycursor = con.cursor()
                   mycursor.execute("USE library")
                   d=input('ENTER YOUR NAME')
                   y=input('ENTER BOOK TITLE:')
                   z=input('ENTER DATE OF RETURNING:')            
                   sql=('update studentinfo set date_of_returning="%s"where BOOKTITLE="%s"and name="%s"'%(z,y,d))
                   mycursor.execute(sql)
                   con.commit()
                   mycursor.execute("update bookslist set availability='Open' where TITLE='%s'"%(y))
                   con.close()
                   print("Record stored")
                   break
    
              elif ch=='3':
                   import mysql.connector as myc
                   con = myc.connect(host="localhost", user="root", passwd="test123")
                   mycursor = con.cursor()
                   mycursor.execute("USE library")
                   d=input('ENTER YOUR NAME')
                   y=input('ENTER BOOK TITLE:')
                   z=input('ENTER DATE OF RETURNING:')            
                   sql=('update studentinfo set date_of_returning="%s"where BOOKTITLE="%s"and name="%s"'%(z,y,d))
                   mycursor.execute(sql)
                   con.commit()
                   mycursor.execute("update bookslist set availability='Open' where TITLE='%s'"%(y))
                   con.close()
                   print("Record stored")
                   break
      elif A==6:
          break
    else:
          print("INVALID INPUT PLEASE CHECK YOUR ANSWER")
