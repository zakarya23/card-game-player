def comp10001go_valid_groups(groups):
    '''Takes a group of cards and returns whether they are valid or not'''
    
    # Checks which cards in the groups were valid. 
    valid = []
    for group in groups: 
        output = comp10001go_score_group(group)
        if output > 0: 
            valid.append(output) 
    
    # If all groups were valid then returns True else returns False.
    if len(valid) == len(groups): 
        return True
    return False
            
       
        
        
def comp10001go_score_group(cards):
    '''Takes a list of cards and returns the score based on a set of rules'''
            
    str_cards = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11,
             'Q': 12, 'K': 13, 'A': 20}
    black = ('S', 'C') 
    red = ('D', 'H')
    
    # Using the itertool 'groupby' the set of cards are separated according 
    # to the number or symbol on the card.
    from itertools import groupby 
    group_list = []
    values = []    
    for rank, group in groupby(sorted(cards), first): 
                groups = list(group)
                group_list.append(groups) 
                values.append(int(str_cards[groups[0][0]]))
        
    # If theres only one type of card then its considered singleton so that 
    # card is returned with a negative value.
    if len(cards) ==1:
        return str_cards[cards[0][0]] 
    
    # Separtes Aces into a separate list             
    ace = []         
    for group in group_list:         
        for card in group: 
            if card[0] =='A': 
                ace.append(card) 
    
    # If cards only consists of aces therefore its invalid and hence nothing 
    # is returned. 
    if len(ace) == len(cards): 
        return invalid(cards) 
    
    # If theres only one type of value and not a ace then that value is 
    # multiplied by the factorial of the number of cards/ 
    elif len(values) == 1: 
        return str_cards[cards[0][0]] * factorial(len(cards)) 
    
    # If length of cards is just 2 therfore its invalid and a negative score 
    # is returned 
    elif len(cards) == 2: 
        return invalid(cards) 
    

        
    # Separates aces into one list and all others into a separate list. And 
    # also the cars type is also stored separately in a list to be used to 
    # compare later on.
    aces = []
    new_list = []
    final_list = []
    card_type = []
    for card in sorted(cards): 
        if card[0] == 'A': 
            aces.append(card) 
        else: 
            card_type.append(card) 
            new_list.append(str_cards[card[0]])
            
    # If cards only consists of aces therefore its invalid and hence nothing 
    # is returned. 
    if len(aces) == len(cards): 
        return invalid(cards) 
           
      
   
    # Checks differences between values in the list of cards and stores them 
    # in a list.
    differences = []  
    list_sorted = sorted(new_list) 
    for position in range(len(new_list) - 1):
        dif = int(list_sorted[position + 1]) - int(list_sorted[position])
        differences.append(dif) 
    
    # If list has repeating cards invalid ouput is produced. 
    for position in range(len(new_list) - 1):
        if list_sorted[position] == list_sorted[position + 1]: 
            return invalid(cards) 
        
    # Goes through the differences and checks whether there are correct runs 
    # or not. 
    score = 0  
    for diff in differences:
        # If aces are present. 
        if aces:
            # If difference is divisible by 2 and has a length of 4, this 
            # part is executed. 
            if diff % 2 != 0 and len(aces) == 4:                
                for diff in differences:                     
                    for position in range(len(aces) - 1):                 
                        if (([aces[position]][0][1]) in black and
                                ([aces[position + 1]][0][1]) in red or
                                ([aces[position]][0][1]) in red and
                                ([aces[position + 1]][0][1]) in black):
                            aces.pop(position)
                            aces.pop(position + 1) 
                           
                  
                            for num in range(int(list_sorted[0]),
                                   int(list_sorted[-1]) + 1):
                                score +=num 
                            break
                            
                    break
            
            # If difference is divisible by 2 and has a length of 2, this 
            # part is executed. 
            elif diff % 2 != 0 and len(aces) == 2: 
                score = 0               
                for diff in differences:                     
                    for position in range(len(aces) - 1):                 
                        if (([aces[position]][0][1]) in black and
                                ([aces[position + 1]][0][1]) in red or
                                ([aces[position]][0][1]) in red and
                                ([aces[position + 1]][0][1]) in black):
                            aces.pop(position)
                            aces.pop(position) 
                           
                  
                            for num in range(int(list_sorted[0]),
                                   int(list_sorted[-1]) + 1):
                                score +=num 
                            break
                        else: 
                            return invalid(cards) 
                    break 
         
            elif diff % 2 == 0:
                for position in range(len(new_list) - 1): 
                    if ([card_type[position]][0][1] in black and 
                        [aces[0]][0][1] in red or [card_type[position]][0][1] 
                        in red and [aces[0]][0][1] in black):
                    
                        if (([card_type[position + 1]][0][1]) in black and
                            [aces[0]][0][1] in red or 
                            ([card_type[position + 1]][0][1]) in red and
                            [aces[0]][0][1] in black):
                        
                            for num in range(int(str_cards[card_type[0][0]]), 
                               int(str_cards[card_type[-1][0]]) + 1): 
                                score += num
                            return score
                    else: 
                        return invalid(cards) 
                else: 
                    return invalid(cards) 
            
            # If difference is not divisible by 2 and has a length of more 
            # then one, this part is executed.
            elif diff % 2 != 0 and len(aces) > 1: 
                for position in range(len(aces)): 
                   
                    if (([aces[position]][0][1]) in black and
                        ([aces[position + 1]][0][1]) in red or
                        ([aces[position]][0][1]) in red and
                        ([aces[position + 1]][0][1]) in black): 
                        for num in range(int(new_list[0][0]),
                                       int(new_list[-1][0]) + 1):
                            score +=num 
                        return score
                    else: 
                        return invalid(cards) 
            else: 
                return invalid(cards) 
            
        # If no aces are present.         
        else: 
            revstr_cards = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9, '10': '0', '11': 'J',
             '12': 'Q', '13': 'K', '20': 'A'}
            f_list = []
            for num in list_sorted: 
                val = revstr_cards[str(num)]
                
                for card in cards: 
                    if int(str_cards[card[0]]) == int(str_cards[str(val)]):
                        f_list.append(card)
           
            for position in range(len(f_list) - 1): 

                if (f_list[position][1] in black and f_list[position + 1][1]
                    in red or f_list[position][1] in red and
                    f_list[position + 1][1] in black): 
                   
                    final_list.append(cards[position])
                else: 
                    return invalid(cards) 
        # If all cards met the requirements given, then that means they will 
        # have the same length and therfore a positive score is returned. 
        if len(final_list)  == len(cards) - 1: 
            for num in range(list_sorted[0],
                           list_sorted[-1] + 1): 
                score += num 
            return score
    return score   

                
def first(x): 
    return x[0]

def factorial(num): 
    '''Returns the factorial of the number
    '''
    if num == 0: 
        return 1 
    else: 
        return num * factorial(num - 1)
    
def invalid(cards):
    '''If cards don't meet the requirements then this function is called 
    and returns the negative score of the player'''
    
    str_cards = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11,
             'Q': 12, 'K': 13, 'A': 20}
    total = 0
    for card in sorted(cards):
        if card[0] == 'A': 
            total += 20 
        else: 
            total += int(str_cards[card[0]])
    return total * -1




