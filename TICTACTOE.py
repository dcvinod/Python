
# Vinod DC(django Developter)
from random import choice
input('''Welcome to XO TicTacToe game against AI
CONTROLS : Numpad 1,2,3,4,5,6,7,8,9
BOARD:\t 7 | 8 | 9\n\t---|---|---\n\t 4 | 5 | 6\n\t---|---|---\n\t 1 | 2 | 3
Press ENTER to continue...''')
def game():
    (nums, values) = ([], [4,1,4,1,16,1,4,1,4])
    for n in range(9):nums.append((str(n+1)+' ')*values[n])
    nums = (' '.join(nums)).split()
    sets = [[1,2,3],[4,5,6],[7,8,9],[7,4,1],[8,5,2],[9,6,3],[1,5,9],[7,5,3]]
    (ai, dead, players, board) = ([], [], [], [0,0,0,0,0,0,0,0,0])
    (marks, line) = ([' ','O','X'], '\n ---|---|---\n')
    def pb(): print('\n ',marks[board[6]],'|',marks[board[7]],'|',marks[board[8]],line,
              '',marks[board[3]],'|',marks[board[4]],'|',marks[board[5]],line,
              '',marks[board[0]],'|',marks[board[1]],'|',marks[board[2]],'\n',)
    (player,center) = (choice([-1,1]),False)
    while True:
        rr = None
        try:
            if player == -1:
                for ss in sets:
                    sss = ss
                    p = 0
                    for s in ss:
                        if s in players:
                            p += 1
                            if p == 2:
                                for x in sss:
                                    if (x not in players) and (x not in dead): rr = x
                for ss in sets:
                    sss = ss
                    a = 0
                    for s in ss:
                        if s in ai:
                            a += 1
                            if a == 2:
                                for x in sss:
                                    if (x not in ai) and (x not in dead): rr = x
                if rr == None: rr = int(choice(nums))
                ai.append(int(rr))
                if rr == 5: center = True
                board[rr - 1] = 1
                while str(rr) in nums: nums.remove(str(rr))
                dead.append(rr) 
                player *= -1

                inset_ai = 0
                for s in sets:
                    inset_ai = 0
                    for n in s:
                        if n in ai: inset_ai += 1
                    if inset_ai == 3: break

                if inset_ai == 3:
                    pb()
                    print("############\n# YOU LOST #\n############")
                    break
                    
            if player == 1:
                print('\n','AI Turn > {}'.format(rr))
                pb()
                r = abs(int(input('Player Turn > ')))
                if r not in players:
                    players.append(r)
                    board[r - 1] = -1
                    if r == 5: center = True
                    if (r != 5) and (str(10 - r) in nums) and (center == False):
                        for t in range(10): nums += [str(10 - r)]
                    if r in ai:
                        print('###############\n# YOU ARE LOL #\n###############')
                        board[r - 1] = 1
                        player *= -1
                        players.remove(r)   
                else:
                    print('###############\n# YOU ARE LOL #\n###############')
                    player *= -1
                while str(r) in nums: nums.remove(str(r))
                dead.append(r)
                player *= -1

            inset_p = 0
            for s in sets:
                inset_p = 0
                for n in s:
                    if n in players: inset_p += 1
                if inset_p == 3: break

            if inset_p == 3:
                print("###########\n# YOU WON #\n###########")
                break

        except: 
            print('####################\n# Let\'s play again #\n####################')
            game()
    print('####################\n# Let\'s play again #\n####################')
    game()
game()
