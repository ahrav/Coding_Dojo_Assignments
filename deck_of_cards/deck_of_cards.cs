using System;
using System.Collections.Generic;
// Hmmm, looks good but strikingly the same as Claire's work.  Did you two collaborate or use an answersheet?  Tread carefully.

namespace deck_of_cards{
    
    public class Card{
        public string stringVal{
            get {
                if(val > 1 && val < 11) {
                    return val.ToString();
                }
                else if (val == 11){
                    return "Jack";
                }
                else if (val == 12){
                    return "Queen";
                }
                else if (val == 13){
                    return "King";
                }
                else if (val == 1){
                    return "Ace"
                }
                else {
                    return "Joker";
                }
            }
        }
        public string suit;
        public int val;

        public Card(string cardSuit, int numVal){
            suit = cardSuit;
            val = numVal;
        }

        public override string ToString(){
            return stringVal + " of " + suits;
        }
    }

    public class Deck{
        public List<Card> cards;

        public Deck(){
            Reset();
        }
        public Deck Reset(){
            cards =  new List<Card>();
            string[] suits = new string[4]{"Hearts","Clubs","Spades","Diamonds"};
            foreach(string suit in suits){
                for(int val = 1; val <= 13; val++){
                    cards.Add(new Card(suit,val));
                }
            }
            return this;
        }
        public Card Deal(){
            if(cards.Count > 0){
                Card temp = cards[0];
                cards.RemoveAt(0);
                return temp;
            }
            return null;
        }
        public Deck Shuffle(){
            Random rand = new Random();
            for(int i = cards.Count-1; i > 0; i--){
                int randI = rand.Next(i);
                Card temp = cards[randI]
                cards[randI] = cards[i];
                cards[i] = temp;
            }
            return this;
        }
    }
    public class Player{
        public string name;
        public List<Card> hand;

        public Player(string n){
            name = n;
            hand = new List<Card>();
        }
        public void Draw(Deck currDeck){
            hand.Add(currDeck.Deal());
        }
        public Card Discard(int i){
            Card temp = hand[i];
            hand.RemoveAt(i);
            return temp;
        }
    }
}
