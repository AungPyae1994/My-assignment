class Minibank:
    userInfo={}
    def first_option(self):
        try:
            option : int = int(input("press 1 to register\npress 2 to login\n"))
            if option == 1:
                self.register()
            elif option == 2:
                self.login()
            else:
                print("please enter 1 or 2")    
        except:
            print("invalid input")        
            
    def register(self):
        print("\n____________this is from register____________\n")
        r_user_name : str =input("please enter your username: ")
        registeruserExit=self.user_exit_reg(r_user_name)
        if registeruserExit==True:
            print("Username already exit")
        else:
            try:
                r_password : int =int(input("please enter your password: "))
                r_password2 : int =int(input("please reenter your password: "))
                r_amount : int = int(input("please enter your amount: "))
                if r_password == r_password2:
            
                    id : int =self.checkingUserCount()
            
                    userinfoForm : dict ={id:{"register_name" : r_user_name, "registerpassword" : r_password, "r_amount" : r_amount}}
                    Minibank.userInfo.update(userinfoForm)
                    print("#####'registeration is complete #####!")
                    print(Minibank.userInfo)
                else:
                    print("password do not match. please try again") 
            except Exception as err:
                print("Invalid input")
            
    def login(self):
        try:
            print("\n____________this is from login____________\n")
            l_user_name : str =input("please enter your username: ")
            l_password : int =int(input("please enter your password: "))    
            userexit=self.user_exit(l_user_name, l_password)
            if userexit:
                print("\n### Login is successful ###\n")
                self.second_option(l_user_name)
            else:    
                print("\n### username or password is wrong ###\n")
        except:
            print("invalid input")    
    
    def second_option(self, l_user_name):
        try:
            select=int(input("press 1 to Transfer\npress 2 to withdraw\npress 3 to update user info\n"))
            if select==1:
                self.transfer(l_user_name)
            if select==2:    
                self.withdrawal(l_user_name)
            if select==3:
                self.user_update_info(l_user_name)
            else:
                print("please enter the correct number 1 or 2 or 3")        
                self.second_option(l_user_name)
        except:
            print("invalid input")
            self.second_option(l_user_name)        
            
    def transfer(self, l_user_name): 
        transfer_user:str =input("please enter username to transfer to: ")
        t_user_id = self.get_id(transfer_user)
        user_id=self.get_id(l_user_name)
        if t_user_id == None:
            print("User dont exit")
            return
        elif t_user_id==user_id:
            print("this is your own acc")
            return
        else:
            print(f" This is transer user account id, {t_user_id} to transfer money from your account id, {user_id}")
            transfer_amount:int =int(input("plsase enter the amount to transfer: "))
            if transfer_amount > Minibank.userInfo[user_id]["r_amount"]:
                print("No insuffient amount")
                return
            elif transfer_amount < 0:
                print("Transfer amount must be positive")
                return
            else:
                Minibank.userInfo[user_id]["r_amount"] -= transfer_amount
                Minibank.userInfo[t_user_id]["r_amount"] += transfer_amount
                print(Minibank.userInfo)
                
    def withdrawal(self, l_user_name):
        try:
            user_id=self.get_id(l_user_name)
            x=Minibank.userInfo[user_id]["r_amount"]
            withdrawal_amount:int = int(input("please enter the amount to withdrawal: "))
            if withdrawal_amount > x:
                print("No insuffient amount")
                return
            elif withdrawal_amount < 0:
                print("withdrawal_amount must be positve")
                return
            else:    
                x -= withdrawal_amount
                print(f"Remaing balance: {x}")
                Minibank.userInfo[user_id]["r_amount"]=x
            
        except:
            print("invalid input")    
                    
    def user_update_info(self, l_user_name):
        try:
            user_id=self.get_id(l_user_name)
            update_option=int(input("press 1 to change username\npress 2 to change password\n"))
        
            if update_option == 1:
                Minibank.userInfo[user_id]["register_name"]= input("please enter the new user name: ")
                print(" This is your new user name", Minibank.userInfo[user_id]["register_name"])
                return  
            elif update_option == 2:
                old_password = int(input("please enter the old password to change"))
                if old_password == Minibank.userInfo[user_id]["registerpassword"]:
                    new_password = int(input("please enter new password: "))
                    new_password2 = int(input("please enter password again to confirm: "))
                    if new_password==new_password2:
                        Minibank.userInfo[user_id]["registerpassword"]=new_password
                        print("password have successfully changed")
                    
                    else:
                        print("passwords do not match")
                        
                else:
                    print("please try again")
            else:
                return self.user_update_info(l_user_name)            
            print(Minibank.userInfo) 
        except:
            print("invalid input")
            
    def user_exit_reg(self, username):
        usercount=len(Minibank.userInfo)
        for i in range(1, usercount + 1):
            if Minibank.userInfo[i]["register_name"]== username:
                return True
        return False
    
    def user_exit(self, l_user_name, l_password):
        usercount=len(Minibank.userInfo)
        for i in range(1, usercount + 1):
            if Minibank.userInfo[i]["register_name"]==l_user_name and Minibank.userInfo[i]["registerpassword"] == l_password:
                return True
        return False
                                    
    def get_id(self,username):
        usercount2=len(Minibank.userInfo)
        for i in range(1, usercount2 +1):
            if Minibank.userInfo[i]["register_name"]==username:
                return i
        return None        
            
    def checkingUserCount(self):
        count= len(Minibank.userInfo)
        return count + 1
        
        
if __name__ == "__main__":
    minibank : Minibank = Minibank()
    while True:
        minibank.first_option()