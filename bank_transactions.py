class Account:
    def __init__(self, acno, acname, acntbal):
        self.acno = acno
        self.acname = acname
        self.acntbal = acntbal
        
class AccountDemo:
    def __init__(self):
        pass
    
    def depositAmnt(self, acnt, depamnt):
        global acntbal
        
        acntbal += depamnt
        return acntbal
    
    def withdrawAmnt(self, acnt, withamnt):
        global acntbal
        
        if 1000 >= acntbal:
            return acntbal
        else:
            return "No Adequate balance"
        
if __name__ == '__main__':
    acno = int(input())
    acname = input()
    acntbal = int(input())
    depamnt = int(input())
    withamnt = int(input())
    
    
    acnt = Account(acno, acname, acntbal)
    acntdemoobj = AccountDemo()
    
    
    print(acntdemoobj.depositAmnt(acnt, depamnt))
    print(acntdemoobj.withdrawAmnt(acnt, withamnt))