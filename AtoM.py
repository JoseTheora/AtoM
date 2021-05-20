class Morse:
    def __init__(self,a):
        self.a = a

    def morsecode(self):
                     
         c=0
         for e in self.a:
             c=c+1
         for x in range (0,c):
            if self.a[x]=='A' or self.a[x]=='a': 
                print('/.-', end="")
            elif self.a[x]=='B' or self.a[x]=='b': 
                print('/-...', end="")
            elif self.a[x]=='C' or self.a[x]=='c': 
                print('/-.-.', end="")
            elif self.a[x]=='D' or self.a[x]=='d': 
                print('/-..', end="") 
            elif self.a[x]=='E' or self.a[x]=='e': 
                print('/.', end="")
            elif self.a[x]=='F' or self.a[x]=='f': 
                print('/..-.', end="")
            elif self.a[x]=='G' or self.a[x]=='g': 
                print('/--.', end="")
            elif self.a[x]=='H' or self.a[x]=='h': 
                print('/....', end="")
            elif self.a[x]=='I' or self.a[x]=='i': 
                print('/..', end="") 
            elif self.a[x]=='J' or self.a[x]=='j': 
                print('/.---', end="")
            elif self.a[x]=='K' or self.a[x]=='k': 
                print('/-.-', end="")
            elif self.a[x]=='L' or self.a[x]=='l': 
                print('/.-..', end="") 
            elif self.a[x]=='M' or self.a[x]=='m': 
                print('/--', end="")
            elif self.a[x]=='N' or self.a[x]=='n': 
                print('/-.', end="")
            elif self.a[x]=='O' or self.a[x]=='o': 
                print('/---', end="")
            elif self.a[x]=='P' or self.a[x]=='p': 
                print('/.--.', end="")
            elif self.a[x]=='Q' or self.a[x]=='q': 
                print('/--.-', end="") 
            elif self.a[x]=='R' or self.a[x]=='r': 
                print('/.-.' , end="")
            elif self.a[x]=='S' or self.a[x]=='s': 
                print('/...', end="") 
            elif self.a[x]=='T' or self.a[x]=='t': 
                print('/-' , end="")
            elif self.a[x]=='U' or self.a[x]=='u': 
                print('/..-', end="") 
            elif self.a[x]=='V' or self.a[x]=='v': 
    	        print('/...-', end="" )
            elif self.a[x]=='W' or self.a[x]=='w': 
    	        print('/.--', end="") 
            elif self.a[x]=='X' or self.a[x]=='x': 
    	        print('/-..-', end="") 
            elif self.a[x]=='Y' or self.a[x]=='y': 
                print('/-.--' , end="")
            elif self.a[x]=='Z' or self.a[x]=='z': 
                print('/--..', end="")
            elif self.a[x]=='1':
                print('/.----', end="")
            elif self.a[x]=='2':
                print('/..---', end="")
            elif self.a[x]=='3':
                print('/...--', end="")
            elif self.a[x]=='4':
                print('/....-', end="")
            elif self.a[x]=='5':
                print('/.....', end="")
            elif self.a[x]=='6':
                print('/-....', end="")
            elif self.a[x]=='7':
                print('/--...', end="")
            elif self.a[x]=='8':
                print('/---..', end="")
            elif self.a[x]=='9':
                print('/----.', end="")
            elif self.a[x]=='0':
                print('/-----', end="")
            elif self.a[x]==' ':
                print('/ ', end="")


    


b =Morse(str(input('Test : ')))
b.morsecode()
