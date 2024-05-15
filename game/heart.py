"""n=int(input("enter"))
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
    for j in range(i, n):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("* ",end="")
    print()"""
print("Welcome To The Game!!")
player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")
set1 = set(player1)
set2 = set(player2)
common_chars = set1 & set2
for char in common_chars:
    player1 = player1.replace(char, '')
    player2 = player2.replace(char, '')
print("Player 1's name after removing common characters: ", player1)
print("Player 2's name after removing common characters: ", player2)

flames_count=len(player1+player2)
print('Remaining character count:', flames_count)

Flames=['F','L','A','M','E','S']
print('Current Flame list: ',Flames)
i=0
while len(Flames) > 1:
    i = (flames_count + i - 1) % len(Flames)
    Flames.pop(i)
    print("Updated Flames list: ", Flames)
print("The result is: ", Flames[0])


Flames_char=Flames[0]
if Flames_char=='F':
    print('You both are Friend')
elif Flames_char=='L':
   print('You both are Lovers')
elif Flames_char=='A':
    print('You both are Affectionated')
elif Flames_char=='M':
    print('You both will get Married')
elif Flames_char=='E':
    print('You both are Enemies')
else:
    print('You both are Siblings')