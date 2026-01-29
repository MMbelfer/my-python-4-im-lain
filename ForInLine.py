import sys
def print_map(map, r, c):
    for i in map:
        print(i)
def check_input(g_list, r_choice, c_choice):
    for i in range(5):
        try:
            the_input = int(input("choicea colom :"))
            if str(the_input).isdigit() and 0 < int(the_input) <= 7:
                if g_list[the_input - 1] >= 0:
                    r_choice, c_choice = g_list[the_input - 1], the_input - 1
                    g_list[the_input - 1] -= 1
                    return (
                        r_choice,
                        c_choice,
                        g_list,
                    )
                else:
                    raise OverflowError
            else:
                raise ValueError
        except Exception as e:
            print(f"its {type(e).__name__}")
            if 4 - i >= 1:
                print(f"\ntry hagen\tyou have {4 - i} turn's more!")
            else:
                sys.exit("sory bat uar luz the last chense")
def update_map(r_choice, c_choice, my_map, turn):
    my_map[r_choice][c_choice] = turn
    return my_map
def check_viner(turn, my_map, r, c, r_choice, c_choice):
    count = 0
    for j in range(c):
        if my_map[r_choice][j] == turn:
            count += 1
            if count == 4:
                return turn
        else:
            count = 0
    count = 0
    for i in range(r_choice, r):
        if my_map[i][c_choice] == turn:
            count += 1
            if count == 4:
                return turn
        else:
            count = 0
    count = 0
    for i in range(-3, 4):
        curr_r = r_choice + i
        curr_c = c_choice + i
        if 0 <= curr_r < r and 0 <= curr_c < c:
            if my_map[curr_r][curr_c] == turn:
                count += 1
                if count == 4:
                    return turn
            else:
                count = 0  
    count = 0
    for i in range(-3, 4):
        curr_r = r_choice + i
        curr_c = c_choice - i
        if 0 <= curr_r < r and 0 <= curr_c < c:
            if my_map[curr_r][curr_c] == turn:
                count += 1
                if count == 4:
                    return turn
            else:
                count = 0
    return 0
def user_turn(turn, my_map, r, c, g_list, viner):
    r_choice = c_choice = 0
    r_choice, c_choice, g_list = check_input(g_list, r_choice, c_choice)
    my_map = update_map(r_choice, c_choice, my_map, turn)
    viner = check_viner(turn, my_map, r, c, r_choice, c_choice)
    return my_map, g_list, viner
def criat_bord(r, c):
    bord = [[0 for _ in range(c)] for _ in range(r)]
    return bord
def main():
    rows = 6
    columns = 7
    gravity_list = [5, 5, 5, 5, 5, 5, 5]
    print(f"-Walckom!-\nTo the 4 in a wat hever a game's")
    my_map = criat_bord(rows, columns)  # OK.1
    print_map(my_map, rows, columns)
    viner = 0
    turn = 2
    for i in range(42):
        if turn % 2 == 0:  # 1
            turn = 1
        else:  # 2
            turn = 2
        my_map, gravity_list, viner = user_turn(
            turn, my_map, rows, columns, gravity_list, viner
        )
        print_map(my_map, rows, columns)
        if viner != 0:
            break
    match viner:
        case 0:
            print("0 sori bat -nobadi- vin!  ")
        case 1:
            print("1 Bluo is viner!")
        case 2:
            print("2 red is viner!")
if __name__ == "__main__":
    main()