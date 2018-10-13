##def f():
##    print('In function f')
##print('When does this print?')
##f()
##
##
##def f():
##    print('In function f')
##    print('When does this print?')
##f()


def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

def main():
    userName = input("Enter the Birthday person's name: ")
    happyBirthday(userName)

main()

##self = 0
##P = input('Enter the total loan amount: ')
##i = input('Enter the APR for a fixed mortgage: ')
##APRpoints = input ('Enter the APR for a mortgage by points: ')
##N = input('Enter the total months for this loan: ')
##class mortage(object):
##    def __init__(self, P, i, APRpoints, N):
##        self.P = P
##        self.i = i
##        self.APRpoints = APRpoints
##        self.N = None
##    def getP (self):
##        return self.P
##    def geti (self):
##        return self.i
##    def getN (self, N):
##        self.N = N
##    def mortages (self):
##        if self.N == None:
##            raise ValueError
##        else:
##            fixedratemortgage = int((self.P*((self.i*((1+self.i)**(self.N)))))/(((1+self.i)**self.N)-1))
##    def mortage (self):
##         print(fixedratemortgage)
##    mortage (self)
##
##
##
##    class mortgagefixed (object):
##        def getAPRpoints (self):
##            return self.APRpoints
##        def getN (self, N):
##            self.N = N
##        def mortages (self):
##            if self.N == None:
##                raise ValueError
##            else:
##            ##fixedratemortgage = int((self.P*((self.i*((1+self.i)**(self.N)))))/(((1+self.i)**self.N)-1))
##                fixedratemortgagewithpoints = int((self.P*((self.APRpoints*((1+self.APRpoints)**(self.N)))))/(((1+self.APRpoints)**self.N)-1))
##        def mortgagefixed (self):
##            print(fixedratemortgagewithpoints)
##        mortages(self)
##
##
##
##def f():
##    print('In function f')
##print('When does this print?')
##f()
