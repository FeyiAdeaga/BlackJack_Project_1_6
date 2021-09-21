from random import randint
from deck import card_name, card_value, end_turn_status, end_game_status

def main():
  print("-----------")
  print("YOUR TURN")
  print("-----------")



  # Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
  user_hand = 0
  drawn_count = 0
  hit = True
  while hit:
    card_rank = randint(1, 13)
    user_card_name = card_name(card_rank) 
    user_card_value = card_value(card_rank)  
    print('Drew a ' + str(user_card_name))
    user_hand += user_card_value
    drawn_count = drawn_count + 1
    
    if user_hand >= 21:
      hit = False
    elif drawn_count >= 2:
      hit = input('You have ' + str(user_hand) + '. Hit (y/n)? ') == 'y'

  print('Final hand: ' + str(user_hand) + '.')
  print(end_turn_status(user_hand))
    


  print("-----------")
  print("DEALER TURN")
  print("-----------")

  dealer_hand = 0 
  drawn_count = 0 

  while dealer_hand <= 17:
    if drawn_count >= 2:
      print('Dealer has ' + str(dealer_hand) + '.')
    
    card_rank = randint(1, 13)
    dealer_card_name = card_name(card_rank)
    dealer_card_value = card_value(card_rank)
    print('Drew a ' + dealer_card_name)
    dealer_hand += dealer_card_value
    drawn_count += 1

  print('Final hand: ' + str(dealer_hand) + '.')
  print(end_turn_status(dealer_hand))

  print("-----------")  
  print("GAME RESULT")  
  print("-----------")

  print(end_game_status(user_hand,dealer_hand))


if __name__ == "__main__":
  main()