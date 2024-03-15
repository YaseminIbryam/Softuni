def check_side(side, searched_symbol):
    matching_count = 0
    max_matching_count = None
    for symbol in side:
        if symbol == searched_symbol:
            matching_count += 1
        else:
            matching_count = 0
        if matching_count >= 6:
            max_matching_count = matching_count
    return max_matching_count


tickets = [ticket.strip() for ticket in input().split(", ")]
match_symbols = ['@', '#', '$', '^']
for index, ticket in enumerate(tickets):
    if len(ticket) == 20:
        left_side = ticket[:10]
        right_side = ticket[10:]
        for match_symbol in match_symbols:
            if match_symbol in ticket:
                if ticket.count(match_symbol) == 20:
                    print(f'ticket "{ticket}" - 10{match_symbol} Jackpot!')
                    break
                matching_count_left = check_side(left_side, match_symbol)
                matching_count_right = check_side(right_side, match_symbol)
                if matching_count_left and matching_count_right:
                    uninterrupted_match_length = min(matching_count_right, matching_count_left)
                    print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')
                    break
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")