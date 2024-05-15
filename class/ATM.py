class ATM:
    def __init__(self,pin,acnt,acc_bal):
        self.pin = pin
        self.acnt = acnt
        self.acc_bal=acc_bal
        print("Hello welcome",self.acnt)
    def menu(self):
        p=int(input('Enter pin:'))
        if(p==self.pin):
            print("choices: 1-D, 2-W, 3-MS, 4-CB select one")
            n=int(input("enter here:"))
            if(n==1):
                print('you have choosen option 1 to Deposit')
                dep=int(input("enter deposit amount:"))
                self.acc_bal=self.acc_bal+dep
                print('you have deposited amount:',dep,'your total balance now is:',self.acc_bal+dep)
            elif(n==2):
                print('you have choosen option 2 to Withdraw')
                wit=int(input("enter amount to withdraw:"))
                min=self.acc_bal-wit==1000
                if(wit>=min):
                    print('you are reaching the violation of maintaing mini balance, your balnace will become:',self.acc_bal-wit)
                else:
                    self.acc_bal=self.acc_bal-wit
                    print('you have successfully withdrawed the amount:',wit,'your balance now:',self.acc_bal-wit)
            elif(n==3):
                print('you have choosen to see your mini statement:')
                print('your accnt number:',self.acnt)
                print('your balance:',self.acc_bal)
            elif(n==4):
                print("you have choosen to see your balance:")
                print(self.acc_bal)
                print("you can still debit:",self.acc_bal-1000)
        else:
            print('you have entered the wrong pin number!!')
        print("you still want to continue?")
        confirm=input("yes or no:")
        confirm.lower()
        if(confirm=='yes'):
            an.menu()
an=ATM(1234,1234567890,10000)
an.menu()


