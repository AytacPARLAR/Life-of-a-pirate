print('''
      ______
   _.-':::::::`.
   \::::::::::::`.-._
    \:::''   `::::`-.`.
     \         `:::::`.\
      \          `-::::`:
       \______       `:::`.
       .|_.-'__`._     `:::\
      ,'`|:::|  )/`.     \:::
     /. -.`--'  : /.\     ::|
     `-,-'  _,'/| \|\\    |:|
      ,'`::.    |/>`;'\   |:|
      (_\ \:.:.:`((_));`. ;:|
      \.:\ ::_:_:_`-','  `-:|
       `:\\|     SSt:
          )`__...---'

''')
print("Welcome to the life of a pirate.")
print("Your mission is to explore.") 

mission_1 = str(input("\nYou see an island that looks fairly inhabitated, Do you want to explore? Yes or No: ")).lower()
if mission_1 == "no":
  print("Game Over...")  

elif mission_1 == "yes":
  mission_2 = str(input("\nThere seems to be a shorcut to the island but you might beach the ship do you want to take the shortcut? Yes or No: ")).lower()
  
  if mission_2 == "no":
    print("It took you too long to get to the island and you got caught by the patrol ship. Game Over") 
  elif mission_2 == "yes":
    
    print("You almost got caught by the patrol ship but now you made it to the island safely by taking a risk...")
    mission_3 = input("\nThe beach might be full of mines. Do you want to proceed by throwing dynamites to create safe path for yourself or just walk in? Dynamite or Walk : ")
    mission_3.lower()
    
    if mission_3 == "walk":
      print("You stepped on a trap. Game Over") 
    
    elif mission_3 == "dynamite":
      print("""\n   _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)

      
      mission_4 = str(input("\nWow! The explosion seems to have cleared a hidden cave entry... Do you want to go in and explore? Yes or No? : ")).lower()

      if mission_1 == "no":
        print("No heart no gold. Game Over") 
      
      elif mission_4 == "yes":
        print("\nCongratulations you have found what seems to be the incredible treasure of the famous pirate Flying Dutchman. You are now the ruler of the seas...")
      