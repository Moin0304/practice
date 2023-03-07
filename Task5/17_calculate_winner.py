# 17.Create a function that takes the number of wins, draws and losses and 
# calculates the number of points obtained so far for 'n' number of football teams . 
# Print the winner team in the end .
# wins get +3 points, draws get +1 point, losses get -1 points .

# I/p:
# Team1(3, 4, 2) ## calculation : 3*3 +4*1 + 2(-1) = 11

# Team2(5, 0, 2) ## calculation : 5*3 + 0*1 + 2(-1) = 13
# Team3(0, 0, 1) ## calculation : 0*3 + 0*1 + 1(-1) = -1

# O/p:
# Winner: Team2

def calculate_winner(*args):
    win = 3
    lose = -1
    draw = 1
    team_1_total= team_1[0]*win + team_1[1]*draw +team_1[2]*lose
    team_2_total= team_2[0]*win + team_2[1]*draw +team_2[2]*lose
    team_3_total= team_3[0]*win + team_3[1]*draw +team_3[2]*lose

    if team_1_total > team_2_total and team_1_total > team_3_total:
        return f"The winner is team-1 : {team_1_total}"
    elif team_2_total > team_1_total and team_2_total > team_3_total:
        return f"The winner is team-2 : {team_2_total}"
    elif team_3_total > team_1_total and team_3_total > team_2_total:
        return f"The winner is team-3 : {team_3_total}"

team_1 = eval(input("enter the win,draw,lose in tuple:" ))
team_2 = eval(input("enter the win,draw,lose in tuple:" ))
team_3 = eval(input("enter the win,draw,lose in tuple:" ))
print(calculate_winner(team_1,team_2,team_3))