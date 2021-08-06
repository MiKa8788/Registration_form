class client:
    
    def __init__(self, id, name, address, phone, email, interests):
        self.client_id=id
        self.client_name=name
        self.address=address
        self.phone_num=phone
        self.email_add=email
        self.interests=interests
        self.interestsMap = ["Software", "Laptops and PC", "Games", "Office tools", "Accessories"]
        

    def input_client(self): #Function of all fields when the customer wants to register 
        print("=========================================")
        self.client_id=input("Please enter Client's ID: ")
        self.client_name=input("Please enter Client's Name: ")
        self.address=input("Please enter Client's address: ")
        self.phone_num=input("Please enter Client's phone number : ")
        self.email_add=input("Please enter Client's email: ")
        
        interestInputMessage = "In what of the following products you are interested in (1 - 5)? \n" #Statement for the products 
        for index in range(len(self.interestsMap)): 
            visualIndex = str(index + 1);
            interestInputMessage += visualIndex + ". for " + self.interestsMap[index] + "\n"        
        interestInputMessage += "Enter the number of your product's interest: "

        inderestsIndex = int(input(interestInputMessage)) - 1

        if(inderestsIndex > len(self.interestsMap) - 1):
              self.interests = ""
              print("There is no products")
        else:
            self.interests = self.interestsMap[inderestsIndex]
            
        print("=========================================")

    def print_client(self): #Function when searching or sorting is called from the customer 
        print("=========================================")
        print("Customer's Id: ", self.client_id)
        print("Customer's Name: ", self.client_name)
        print("Customer's Address: ", self.address)
        print("Customer's Phone: ", self.phone_num)
        print("Customer's Email: ", self.email_add)
        print("Customer product Interests: ", self.interests)
        print("=========================================") 


