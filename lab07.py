#Creating the class with the most basic 'object'
class Mortgage(object):

    #Initializing (constructors) and creating a self to later make an object as m1
    #Creating/initializing three variables to put into the second method
    def __init__(self, pr, inte, no):
        self.p = pr
        self.i = inte
        self.n = no

    #Solving for the payment per month
    def monthlyPayment(self):
        self.monthlyLoan = self.p*((self.i*(1+self.i)**(self.n))/((1+self.i)**(self.n)-1))
        
    #Solving for the total payment for N months
    def totalPayment(self):
        self.totalPayment = self.monthlyLoan*self.n
        print('Fixed ' + str(round((self.i*12)*(100),2)) + '%: ')
        print('Total payment is ' + '$'+ str(int(self.totalPayment)))

#Creating a subclass for mortgage points
class MortgagePoints(Mortgage):

    #When initializing, I'm creating another variable pts that would be added to the object, self
    def __init__(self, p, i, n, pts):
        Mortgage.__init__(self, p, i, n)
        self.pts = pts
 
    #Calculating the total payment with points
    #I dont have to change any of the variables because it will be referring to one of the conditions
    def totalPayment(self):
        self.totalPayment = (self.monthlyLoan*self.n) + ((self.pts/100)*self.p)
        print('Fixed ' + str(round(self.i*12,2)*(100)) + '% + ' + str(self.pts) + ' points: ')
        print('Total payment is ' + '$'+ str(int(self.totalPayment)))

def main():
    #User input
    loan = int(input('Enter the total loan amount: '))
    APR = float(input('Enter the APR for a fixed mortgage: '))
    APRpts = float(input('Enter the APR for a mortgage by points: '))
    points = float(input('Enter the number of points: '))
    years = int(input('Enter the total years for this loan: '))

    #Converting the values based on what the inputs are offering
    reali = APR/12
    realipts = APRpts/12
    months = 12*years

    #Calling the object (Mortgage) a name, and calling their method
    m1 = Mortgage(loan, reali, months)
    m1.monthlyPayment()
    m1.totalPayment()

    #Calling the fixed-rate-mortgage a name, and calling their method
    m2 = MortgagePoints(loan, realipts, months, points)
    m2.monthlyPayment()
    m2.totalPayment()
main()


    
    
