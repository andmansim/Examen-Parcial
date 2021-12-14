# BANANA
print("The word is 'BANANA'")
initial_word = list('BANANA')
print(initial_word)
vowels = ['A']
consonant = ['B', 'N']
print("Player 1 have to make words started by vowels")
print("Player 2 have to make words started by consonant")
print("Player 1:")
player_1 = str(input())
player_1_list = list(player_1)

if player_1_list[0] == vowels[0]:
    print("Player 1:")
    player_1 = str(input())
    player_1_list = list(player_1)
    print("Have you finished?: Y/N")
    user = str(input())
    while user == 'Y':
        print("Player 1:")
        player_1 = str(input())
        player_1_list = list(player_1)
        print("Have you finished?: Y/N")
        user = str(input())
    if user != 'Y':
        a = player_1_list.count('A')
        points = a * 3
        n = player_1_list.count('N')
        points1 = n * 2
        
        total_points_1 = points1 + points
        print("Total points player 1:")
        print(total_points_1)

print("Player 2:")
player_2 = str(input())
player_2_list = list(player_2)
for x in consonant:
    
    if player_2_list[0] == consonant[x]:
        print("Player 2:")
        player_2 = str(input())
        player_2_list = list(player_1)
        print("Have you finished?: Y/N")
        user = str(input())
        while user == 'Y':
            print("Player 2:")
            player_2 = str(input())
            player_2_list = list(player_2)
            print("Have you finished?: Y/N")
            user = str(input())
        if user != 'Y':
            a = player_2_list.count('A')
            points2 = a * 3
            n = player_2_list.count('N')
            points3 = n * 3
            total_points_2 = points2 + points3
            print("Total points player 2:")
            print(total_points_2)
