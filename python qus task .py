1. History of python ?
        
           *guido von rossam---->Father of python
               1989--develop--->1991--->version 0.9
               1994--version 1.0,2000-->version 2.0
               2008-->version 3.0
           *python----name:
              christmas holiday----internship project
              Tv-mondy python circus---->logo

2. IDE ?
       IDE---->Integrated Developement Envinronment
	       pycharm,vs code,spyder,notepad,anaconda

3. Types of tokens?

       There are 5 types of tokens.
            *Keywords                
            *Identifiers                 
            *Literals -----> String , Numeric Literals (Int,Float,Complex), Boolean , Literal Collection (List , Tuple , Dictionary , Set)                     
            *Operators ----> Arithmetic operators , Assignment operators , Comparison operators , Logical operators , Identity operators , Membership operators , Bitwise operators.                
            *Punctuators

4. Datatypes?

        *Text-string--->str---"text"
        *Number--->int,float,complex
        *Boolean--->bool-->True,False
        *None---->type--->NoneType

5. write the programme for the output?
	name: XXX
	age:22
	tamil:100
	eng:100
	maths:100
	s.s:100
	s:100
	total:500
	and find average?

              ANSWER :  name = "Divya"
                        print("name:", name)
                        age=22
                        print("age:", age)
                        s1=100
                        print("tamil:", s1)
                        s2=100
                        print("eng:", s2)
                        s3=100
                        print("maths:", s3)
                        s4=100
                        print("s.s:", s4)
                        s5=100
                        print("s:", s5)
                        tt = s1+s2+s3+s4+s5
                        print("total:", tt)
                        avg=tt/5
                        print("average :",avg)  O/p : average : 100.0


6. (5 & 12) & (2 | 6)
 
              (5 & 12) = 0100 = 4
              (2 | 6)  = 0110 = 6
              (5 & 12) & (2 | 6) = 0100 = 4

                   O/P : (5 & 12) & (2 | 6) = 4


7. (54 | 6 & 5) | (21 & 9)

              (54 | 6 & 5) = (54 | 6) = 110110 = 54
                             (54 & 5) = 000100 = 4
              (54 | 6 & 5) = 000100 = 4
              (21 & 9)     = 00001 = 1
              (54 | 6 & 5) | (21 & 9) = 000101 = 5

                   O/P : (54 | 6 & 5) | (21 & 9) = 5


                           (or)

               (54 | 6 & 5) = (6 & 5) = 0100 = 4
                             (54 & 4) = 110110 = 54
              (54 | 6 & 5) = 110110 = 54
              (21 & 9)     = 00001 = 1
              (54 | 6 & 5) | (21 & 9) = 110111 = 55

                   O/P : (54 | 6 & 5) | (21 & 9) = 55

8. True or falseif it is false give the reason?
	1) a="name"
	   a=12
	   print(a)

               O/P : 12 [ It prints current value of a ]

        2) b="kalai""tamil"
	   print(b)

               O/P : kalaitamil

9. a=10
   b=2
   print(a/b+a%1)

           ANSWER : print(10/2)    = 5.0
                    print(5.0+a)   =15.0
                    print(15.0%1)  = 0.0

                        O/P : 0.0 

                          (or)

                    print(10/2)   = 5.0    
                    print(10%1)   = 0
                    print(5.0+0)  = 5.0 

                         O/P : 5.0 

10. 5>>2 and 9<<3 

             5>>2 = 0001 = 1
             9<<3 = 1001000 = 72

             O/P : 5>>2 and 9<<3  = 1001000 = 72

11. What is membership operator.Give the example?

	Return boolean value (True or False)---->in, not in
           Example :

              in:

                fruit="apple"
                print('p' in fruit)-------->True

                fruit="apple"
                print('i' in fruit)--------->False

             not in:

                fruit="apple"
                print('p' not in fruit)-------->False

                fruit="apple"
                print('i' not in fruit)--------->True

12. Explain Identity?

        *It is  used to identify a specific element, varible name, function name, class name.
	*Cannot start with (0-9) or symbol(./,:),except underscore.
	*Start with (a-z) and (A-Z) or (underscore) 
	*Cannot use reserved keywords.
	*Case sensitive.


13. Output:hello hello hello hello hi hi hi hi------write a code.

               a="hello\thello\thello\thello\thi\thi\thi\thi"
               print(a) 

14. How to find the datatype and explain?

        To determine the type of a variable in Python, use the built-in type() function.

15. Convert the a='154' to integer?

          a='154'
          print(type(a)) ----> <class 'str'>

          b=int(a)
          print(type(b))    -------> <class 'int'>

                      (or)

          a='154'
          print(type(a)) ----> <class 'str'>

          b=int(a)
          print(b)    -------> 154

          


               



