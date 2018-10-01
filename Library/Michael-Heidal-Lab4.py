# --------------------------------------
# CSCI 127, Lab 4
# September 25, 2018
# Michael Heidal
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    possible_seasons = []
    for i in range(games_played + 1):
        for j in range(games_played + 1):
            for k in range(games_played + 1):
                if 3*i + j + 0*k == points_earned and i + j + k == games_played:
                    possible_seasons.insert(0, [i, j, k])
                    
    for i in possible_seasons:
        string = ''
        for j in i:
            string += str(j) + "-"
        string = string[:-1]
    
        print(string)
    print()
# --------------------------------------

def process_seasons(seasons):
    a = 0
    for i in seasons:
        a+=1
        process_season(a, i[0], i[1])

# --------------------------------------

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]
    process_seasons(soccer_seasons)

# --------------------------------------

main()
