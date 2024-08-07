# Bid Auction Program

This Python program allows users to participate in a bid auction. Participants can enter their names and bid amounts, and the program keeps track of the highest bid and the winning bidder.

## Usage

1. **Run the Program:**
- Make sure you have Python installed.
- Execute the `main.py` script in your terminal or IDE.

2. **Instructions:**
- When prompted, enter your name and bid amount.
- The program will store the bids in a dictionary.
- If there are other bidders, continue entering their bids.
- To stop bidding, type "no" when asked if there are any other bidders.
- The program will display the winner and the highest bid.

## Requirements

- Python 3.x
- `BidAuctionArt` module (imported in the code), it contains ascii art of a hammer.

## Example

```
$ python main.py
What is your name?: Alice
Enter your bid: $500
Is there any other bidder? Type yes or no: yes
What is your name?: Bob
Enter your bid: $600
Is there any other bidder? Type yes or no: no
Bid goes to Bob for $600
```

