# BANANA
print("The word is 'BANANA'")
initial_word = list('BANANA')
print(initial_word)
print("Player 1 have to make words started by vowels")
print("Player 2 have to make words started by consonant")
print("Player 1:")
player_1 = str(input())
print("Player 2:")
player_2 = str(input())
player_1_list = list(player_1)
player_2_list = list(player_2)

vowels = ['A']
consonant = ['B', 'N']
while player_1_list[0] == vowels[0]:
    print("Player 1:")
    player_1 = str(input())
    player_1_list = list(player_1)
    for x in player_1_list:
        a = player_1_list.count('A')
        points = a * 3
        n = player_1_list.count('N')
        points = n * 3