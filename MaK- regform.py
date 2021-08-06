from customers import client # Mention the file name and the class name inside the file. In this case file is called 'Customer' and the class is 'client'
list_customer=[] # Here the empty list to store all my data has been declare

#Functions of the code 

def register_client(): #Regstration of the new clients 
    cl=client("", "", "", "", "","")
    cl.input_client()
    list_customer.append(cl)
    print("The data has been added.")

def client_searching(): #Search for customer through clientID
    found=False
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    id=input("Please enter ID of the client: ")
    for record in list_customer:
        if (record.client_id==id):
            found=True
            record.print_client()
    if (found==False):
        print("                                     ")
        print("There is no client with this ID. Please try again! ")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")

def delete_client(): #Delete details of the customer through clientID
    found=False
    print("*************************************")
    id=input("Please enter ID of the client: ")
    for record in list_customer:
        if (record.client_id==id):
            found=True
            list_customer.remove(record)
            print("Data has been deleted.")
    if (found==False):
        print("There is no client with this ID. Please try again!")
        print("                                       ")
    print("***************************************")    


def show_all_clients(): #Shows the saved details 
    show_all_clients = len(list_customer)
    if (show_all_clients == 0):
        print("There is no saved details.")
    else: 
        for record in list_customer:
            record.print_client()
        print("The data has been printed.")    


def client_sort(): #Sorting clients
    list_customer.sort(key=lambda record: record.client_name)
    show_all_clients()
    print("Sorting has been done.")
    

def save_data(): #Save all data, which will be stored 
    f=open("customers.txt", "w")  #Here it says to take the text file called customers and to do it in writing more 
    for record in list_customer:
        #data=""
        data=record.client_id+", "+record.client_name+", "+record.address+", "+record.phone_num+", "+record.email_add+", "+record.interests+"\n"
        f.write(data)
    f.close()
    print("The data has been saved.")

   
def menu(): #Options of the menu
    print("                                           ")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("*=====             Menu              =====*")
    print("**==   Please choose of the following  ==**")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("                                           ")
    print("1. Register new client")
    print("2. Search for a client")
    print("3. Delete a client");
    print("4. Show all clients")
    print("5. Sort the clients")
    print("6. Save the registration and exit");
    print("                                           ")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")


with open("customers.txt", "r") as f: #Body of the code 
    for record in f:
        record=record.strip("\n")
        id, name, address, phone, email, interests=record.split(", ")
        obj=client(id, name, address, phone, email, interests)
        list_customer.append(obj)
print("Welcome to Digital products Ltd")
print("The system is ready for your choice. Thank you! ")


while (True):#Loop for the options return the functions depends of the input number
    menu()
    print("                                                                     ")
    choice=int(input("Please insert the number of your choice and press Enter: "))

    if (choice==1):
        register_client()
    if (choice==2):
        client_searching()   
    if (choice==3):
        delete_client()
    if (choice==4):
        show_all_clients()
    if (choice==5):
        client_sort()
    if (choice==6):
        save_data()
        break
     
