#write a program that tests the compatibility between two people.

"""
To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs.

    Then check for the number of times the letters in the word LOVE occurs.

    Then combine these numbers to make a 2 digit number.
"""
#printing welcome note 
print("Welcome to the L Calculator")
print('''

                        __,,,__
                ,-""-,-"       "-,-""-,
               /,-' , .-'-.7.-'-. , '-,\
               \(    /  _     _  \    )/
                '-,  { (0)   (0) }  ,-'
                 /    >  .---.  <    \
                |/ .-'   \___/   '-. \|
                {, /  ,_       _,  \ ,}
                \ {,    \     /    ,} /
                 ',\.    '---'    ./,'
             _.-""""""-._     _.-""""""-._
           .'            `._.`            '.
         _/_               _                \
      .'`   `\            | |                \
     /        |           | |                 ;
     |        /           |_|                 |
     \  ;'---'    _    ___  _  _  ___         ;
      '. ;       | |  /   \| || ||  _|     _ ;
        `-\      | |_ | | || |/ /|  _|   .' `,
           `\    |___|\___/ \__/ |___|  |     \
             \            _ _           \     |
         jgs  `\         | | |         /`   _/
    ,-""-.    .'`\       | | |       /`-,-'` .-""-,
   /      `\.'    `\     \___/     /`    './`      \
  ;  .--.   \       '\           /'       /   .--.  ;
  | (    \   |,       '\       /'        |   /    ) |
   \ ;    }             ;\   /;         `   {    ; /
    `;\   \         _.-'  \ /  `-._         /   /;`
      \ \__.'   _.-'       Y       `-._    '.__//
       '.___,.-'                       `-.,___.'

''')

#for input names
name1 = input("Enter your name.\n")
name2 = input("Enter there name.\n")

#combined two names under the one variable named "combined_string"
combined_string = name1 + name2

#new variable for converting combined_string to lower case
lowercase_string = combined_string.lower()

#counting the numbers of letters
t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("V")
e = lowercase_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"your score is {love_score}, you go together like coke and mentos.")

elif (love_score >= 50) or (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_Score}.")