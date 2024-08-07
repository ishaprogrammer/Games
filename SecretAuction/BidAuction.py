import os
from BidAuctionArt import logo
print(logo)
new_dict={}
stop=False
while not stop:
    name=input("What is your name?:")
    bid=int(input("Enter your bid:$"))
    new_dict[name]=bid
    highest=max(new_dict.values())
    
    bidders=input(" Is there any other bidders? Type yes or no:")
    winner=max(new_dict,key=new_dict.get)
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear') 
    if bidders=="yes":
        clear_console()
    else:
        stop=True
        print(f" Bid goes to {winner} for ${highest}")
    
          
    
   

        
    