#Dimitri papadedes
#April, 20, 2018
#Pokemon battle 

#set choice to Yes by default 
option = "Yes" 

#Loop entire program while they want to play
while option == "Yes":
  
  #import time & random numbers & Sound
  from time import sleep
  import random
  

  #give values to pokemon
  Charizard = 1 
  Blastoise = 2
  Venusaur = 3 
  Pikachu = 4
  
  #pick computers pokemon 
  Gary_Pokemon = random.randint(1,4)
  
  
  #name computer pokemon 
  if Gary_Pokemon == 1 :
     Gary_Pokemon = "Charizard"
  elif Gary_Pokemon == 2: 
   Gary_Pokemon = "Blastoise"
  elif Gary_Pokemon == 3:
    Gary_Pokemon = "Venusaur"
  elif Gary_Pokemon == 4 : 
    Gary_Pokemon = "Pikachu"
  
  
  #Stats of pokemon
  Charizard_Attack = 224
  Charizard_Speed = 236
  Charizard_Special = 207
  Charizard_Hp = 297
  Gary_Charizard_Hp = 297
  Charizard_Defence = 192
  
  Blastoise_Attack = 222
  Blastoise_speed = 192
  Blastoise_special = 216
  Blastoise_Hp = 299
  Gary_Blastoise_Hp = 299
  Blastoise_defence = 236
  
  Venusaur_Attack = 220
  Venusaur_speed = 196
  Venusaur_special = 224
  Venusaur_Hp = 301
  Gary_Venusaur_Hp = 301
  Venusaur_defence = 202
  
  Pikachu_Attack = 237
  Pikachu_speed = 256
  Pikachu_special = 196
  Pikachu_Hp = 320
  Gary_Pikachu_Hp = 320
  Pikachu_defence = 160
  

  
  #ask for name 
  print ("What is your name?")
  username = input ()
  
  print ("Ah, I see, Hello", username)
  
  sleep(1)
  #ask what pokemon to choose
  print ("Pick your Pokemon" )
  print ("1 = Charizard")
  print ('2 = Blastoise')
  print ('3 = Venusaur')
  print ("4 = Pikachu")
  user_choice = input ()
  
  
  
  
  #check choice 
  if user_choice == "1": 
    user_pokemon = "Charizard"
  elif user_choice == "2": 
    user_pokemon = "Blastoise"
  elif user_choice == "3":
    user_pokemon = "Venusaur"
  elif user_choice == "4":
    user_pokemon = "Pikachu"
    
    sleep(1)
    #display choice 
  print ("So..." , user_pokemon, "is your choice ")
  
  #display opponents pokemon 
  sleep (1)
  print ("your opponents Pokemon is", Gary_Pokemon)
  
  #Tell them the battle will start
  sleep (2)
  print ("The battle will begin shortly, the trainers are", username, "and Gary")
  
  sleep (3)
  print ("The battle has started") 
  
  
  
  print (username, "sent out", user_pokemon, "and Gary sent out", Gary_Pokemon)
  
  sleep(1)
  #loop move choice and damage 
  while Gary_Blastoise_Hp > 0 and Gary_Pikachu_Hp > 0 and Gary_Venusaur_Hp > 0 and Gary_Charizard_Hp > 0 and Blastoise_Hp > 0 and Pikachu_Hp > 0 and Venusaur_Hp > 0 and Charizard_Hp > 0:
    
    
      #make miss number 
      Miss = random.randint(1,11)
      
      
      #make gary miss number 
      Gary_Miss = random.randint(1,10)
      
      sleep(1)
      print ("What is your move choice?")
      
      #check what pokemon then show their moves 
      if user_pokemon == "Charizard" :
        print ("1 = Wing Attack")
        print ("2 = Flamethrower")
        print ("3 = Dragon Claw")
        print ("4 = Dragon Tail")
          
        user_Move = input()
        
      if user_pokemon == "Charizard" and user_Move == "1": 
          print ("Charizard used Wing Attack")
      if user_pokemon == "Charizard" and user_Move == "2":
          print ("Charizard used Flamethrower")
      if user_pokemon == "Charizard" and user_Move == "3": 
          print ("Charizard used Dragon Claw")
      if user_pokemon == "Charizard" and user_Move == "4": 
          print ("Charizard used Dragon Tail")
          
      elif user_pokemon == "Blastoise" : 
          print ("1 = Hydro Pump")
          print ("2 = Skull Bash")
          print ("3 = Bite")
          print ("4 = Aqua Tail")
            
          user_Move = input()
          
      if user_pokemon == "Blastoise" and user_Move == "1" : 
          print ("Blastoise used Hydro Pump")
      if user_pokemon == "Blastoise" and user_Move == "2":
          print ("Blastoise used Skull Bash")
      if user_pokemon == "Blastoise" and user_Move == "3":
          print ("Blastoise used Bite")
      if user_pokemon == "Blastoise" and user_Move == "4":
          print ("Blastoise used Aqua Tail")
          
      elif user_pokemon == "Venusaur" :
          print ("1 = Razor Leaf")
          print ("2 = Double-Edge")
          print ("3 = Sludge Bomb")
          print ("4 = Protect")
          user_Move = input()
        
        #display attack
      if user_pokemon == 'Venusaur' and user_Move == '1':
          print ("Venusaur used Razor Leaf")
      if user_pokemon == 'Venusaur' and user_Move == '2':
          print ("Venusaur used Double-Edge")
      if user_pokemon == 'Venusaur' and user_Move == '3':
          print ("Venusaur used Sludge Bomb")
      if user_pokemon == 'Venusaur' and user_Move == '4':
          print ("Venusaur used Protect and blocked the incoming damage")
      
        
        
        
        
      elif user_pokemon == "Pikachu" :
        print ("1 = Thunder")
        print ("2 = Electro Ball")
        print ("3 = Slam")
        print ("4 = Quick Attack")
        user_Move = input()
      
      #display attack
      if user_pokemon == 'Pikachu' and user_Move == '1':
          print ('Pikachu used Thunder')
      if user_pokemon == 'Pikachu' and user_Move == '2':
          print ('Pikachu used Eletro Ball')
      if user_pokemon == 'Pikachu' and user_Move == '3':
          print ("Pikachu used Slam")
      if user_pokemon == 'Pikachu' and user_Move == '4':
          print ("Pikachu used Quick Attack")
        
        
        
        
        
        
        
      #create Gary's move 
       
      Gary_Move = random.randint(1,4)
       
       
      
      #catagories 
      Wing_Attack_Power = [60, "Flying", 'Physical'] 
      Flamethrower_Power = [90, "Fire", 'Special'] 
      Dragon_Claw_Power = [80, "Dragon", 'Physical']
      Dragon_Tail_Power = [40, "Dragon", 'Physical']
      Hydro_Pump_Power = [110, 'Water', 'Special']
      Skull_Bash_Power = [130, 'Normal', 'Physical']
      Bite_Power = [60, 'Dark', 'Physical']
      Aqua_Tail_Power = [90, 'Water', 'Physical']
      RazorLeaf_Power = [100, 'Grass', 'Physical']
      Double_Edge_Power = [120, 'Normal', 'Physical']
      Sludge_Bomb_Power = [90, 'Poison', 'Special']
      Protect_Power = [0,'Normal','Physical']
      Thunder_Power = [110, 'Electric', 'Special']
      Electro_Ball_Power = [100, 'Electric', 'Special']
      Slam_Power = [80, 'Normal', 'Physical']
      Quick_Attack = [40,'Normal', 'Physical']    
      
      #check if they missed 
      if Miss == 9 or Miss == 4 or Miss == 6:
        print ("Oh no", user_pokemon, "missed its attack!")
      else:
      
        #damage to Gary's pokemon 
        #damage from Charizard
        sleep (1)
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Charizard' and user_Move == '1': 
          Gary_Blastoise_Hp = Gary_Blastoise_Hp - 57 
          if Gary_Blastoise_Hp < 0 : 
              Gary_Blastoise_Hp = 0 
          print ("Gary's Blastoise Took 57 Damage and is now at",Gary_Blastoise_Hp, 'Hp')
         
         
        sleep (2)
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Charizard' and user_Move == '2': 
            Gary_Blastoise_Hp = Gary_Blastoise_Hp - 69
            if Gary_Blastoise_Hp < 0 : 
              Gary_Blastoise_Hp = 0 
            print ("It was not very effective! Gary's Blastoise took 69 damage and is now at", Gary_Blastoise_Hp,"Hp")
            
        
        
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Charizard' and user_Move == '3':
            Gary_Blastoise_Hp = Gary_Blastoise_Hp - 64
            if Gary_Blastoise_Hp < 0 : 
              Gary_Blastoise_Hp = 0 
            print ("Gary's Blastoise took 64 damage and is now at", Gary_Blastoise_Hp, "Hp")
            
        
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Charizard' and user_Move == '4':
            Gary_Blastoise_Hp = Gary_Blastoise_Hp - 31
            if Gary_Blastoise_Hp < 0 : 
              Gary_Blastoise_Hp = 0 
            print ("Gary's Blastoise took 31 damage and is now at", Gary_Blastoise_Hp, "Hp")
        
        
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Charizard' and user_Move == '1':
            Gary_Charizard_Hp = Gary_Charizard_Hp - 47
            if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0
            print ("It was not very effective! Gary's Charizard took 31 damage and is now at", Gary_Charizard_Hp, "Hp")
        
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Charizard' and user_Move == '2':   
          Gary_Charizard_Hp = Gary_Charizard_Hp - 72
          if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0
          print ("It was not very effective! Gary's Charizard took 72 damage and is now at", Gary_Charizard_Hp, "Hp")
          
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Charizard' and user_Move == '3':
          Gary_Charizard_Hp = Gary_Charizard_Hp - 78
          if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0
          print  ("Gary's Charizard took 78 damage and is now at", Gary_Charizard_Hp, "Hp")
          
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Charizard' and user_Move == '4':
           Gary_Charizard_Hp = Gary_Charizard_Hp - 39
           if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0
           print  ("Gary's Charizard took 39 damage and is now at", Gary_Charizard_Hp, "Hp")
        
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Charizard' and user_Move == '1':
          if Gary_Move == 4:
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
           print  ("Venusaur used Protect and blocked the incoming damage")
          else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 80
            if Gary_Venusaur_Hp < 0 : 
              Gary_Venusaur_Hp = 0 
            print ("It was super effective! Gary's Venusaur took 80 damage and is now at", Gary_Venusaur_Hp, "Hp")
          
          
          
          
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Charizard' and user_Move == '2':
           if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
           else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 117
            if Gary_Venusaur_Hp < 0 : 
              Gary_Venusaur_Hp = 0 
            print ("It was super effective! Gary's Venusaur took 117 damage and is now at", Gary_Venusaur_Hp, "Hp")
          
          
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Charizard' and user_Move == '3':
           if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
           else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 74
            if Gary_Venusaur_Hp < 0 : 
              Gary_Venusaur_Hp = 0 
            print  ("Gary's Venusaur took 74 damage and is now at", Gary_Venusaur_Hp, "Hp")
          
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Charizard' and user_Move == '4':
           if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
           else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 37
            if Gary_Venusaur_Hp < 0 : 
              Gary_Venusaur_Hp = 0 
            print  ("Gary's Venusaur took 37 damage and is now at", Gary_Venusaur_Hp, "Hp")  
          
          
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Charizard' and user_Move == "1":
          Gary_Pikachu_Hp = Gary_Pikachu_Hp - 41
          if Gary_Pikachu_Hp < 0 : 
              Gary_Pikachu_Hp = 0 
          print ("It was not very effective! Gary's Pikachu took 41 damage and is now at", Gary_Pikachu_Hp, "Hp")
          
          
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Charizard' and user_Move == "2":
          Gary_Pikachu_Hp = Gary_Pikachu_Hp - 91
          if Gary_Pikachu_Hp < 0 : 
              Gary_Pikachu_Hp = 0 
          print ("Gary's Pikachu took 91 damage and is now at", Gary_Pikachu_Hp, "Hp")
          
        
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Charizard' and user_Move == "3":
          Gary_Pikachu_Hp = Gary_Pikachu_Hp - 103 
          if Gary_Pikachu_Hp < 0 : 
              Gary_Pikachu_Hp = 0 
          print ("Gary's Pikachu took 103 damage and is now at", Gary_Pikachu_Hp, "Hp")
          
        
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Charizard' and user_Move == "4":
          Gary_Pikachu_Hp = Gary_Pikachu_Hp - 51
          if Gary_Pikachu_Hp < 0 : 
              Gary_Pikachu_Hp = 0 
          print ("Gary's Pikachu took 51 damage and is now at", Gary_Pikachu_Hp, "Hp")
          
        
        
        
        
        #Damage from Blastoise
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Blastoise' and user_Move == '1':
            Gary_Blastoise_Hp = Gary_Blastoise_Hp - 70
            if Gary_Blastoise_Hp < 0 : 
              Gary_Blastoise_Hp = 0 
            print ("It was not very effective! Gary's Blastoise took 31 damage and is now at", Gary_Blastoise_Hp, "Hp")
            
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Blastoise' and user_Move == '2':
            Gary_Blastoise_Hp = Gary_Blastoise_Hp - 102
            if Gary_Blastoise_Hp < 0 : 
              Gary_Blastoise_Hp = 0 
            print ("Gary's Blastoise took 102 damage and is now at", Gary_Blastoise_Hp, "Hp") 
            
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Blastoise' and user_Move == '3':
            Gary_Blastoise_Hp = Gary_Blastoise_Hp - 47
            if Gary_Blastoise_Hp < 0 : 
              Gary_Blastoise_Hp = 0 
            print ("Gary's Blastoise took 47 damage and is now at", Gary_Blastoise_Hp, "Hp")    
            
            
        
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Blastoise' and user_Move == '4':
            Gary_Blastoise_Hp = Gary_Blastoise_Hp - 71
            if Gary_Blastoise_Hp < 0 : 
              Gary_Blastoise_Hp = 0 
            print ("It was not very effective! Gary's Blastoise took 71 damage and is now at", Gary_Blastoise_Hp, "Hp")       
            
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Blastoise' and user_Move == '1':
            Gary_Charizard_Hp = Gary_Charizard_Hp - 135
            if Gary_Charizard_Hp < 0 : 
              Gary_Charizard_Hp = 0 
            print ("It was super effective! Gary's Charizard took 135 damage and is now at", Gary_Charizard_Hp, "Hp")
            
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Blastoise' and user_Move == '2':
            Gary_Charizard_Hp = Gary_Charizard_Hp - 126
            if Gary_Charizard_Hp < 0 : 
              Gary_Charizard_Hp = 0 
            print ("Gary's Charizard took 126 damage and is now at", Gary_Charizard_Hp, "Hp")    
            
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Blastoise' and user_Move == '3':
            Gary_Charizard_Hp = Gary_Charizard_Hp - 58
            if Gary_Charizard_Hp < 0 : 
              Gary_Charizard_Hp = 0 
            print ("Gary's Charizard took 58 damage and is now at", Gary_Charizard_Hp, "Hp")        
           
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Blastoise' and user_Move == '4':
            Gary_Charizard_Hp = Gary_Charizard_Hp - 108
            if Gary_Charizard_Hp < 0 : 
              Gary_Charizard_Hp = 0 
            print ("It was super effective! Gary's Charizard took 108 damage and is now at", Gary_Charizard_Hp, "Hp")       
           
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Blastoise' and user_Move == '1':
          if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
          else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 68
            if Gary_Venusaur_Hp < 0 : 
             Gary_Venusaur_Hp = 0 
            print ("It was not very effective! Gary's Venusaur took 68 damage and is now at", Gary_Venusaur_Hp, "Hp")  
                 
                  
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Blastoise' and user_Move == '2':
          if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
          else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 101
            if Gary_Venusaur_Hp < 0 : 
              Gary_Venusaur_Hp = 0 
            print ("Gary's Venusaur took 101 damage and is now at", Gary_Venusaur_Hp, "Hp") 
                 
                
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Blastoise' and user_Move == '3':
          if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
          else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 55 
            if Gary_Venusaur_Hp < 0 : 
             Gary_Venusaur_Hp = 0 
            print ("Gary's Venusaur took 55 damage and is now at", Gary_Venusaur_Hp, "Hp") 
            
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Blastoise' and user_Move == '4':
          if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
          else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 59
            if Gary_Venusaur_Hp < 0 : 
             Gary_Venusaur_Hp = 0 
            print ("It was not very effective! Gary's Venusaur took 59 damage and is now at", Gary_Venusaur_Hp, "Hp")     
            
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Blastoise' and user_Move == '1':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 101
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 101 damage and is now at", Gary_Pikachu_Hp, "Hp")
           
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Blastoise' and user_Move == '2':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 166
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 166 damage and is now at", Gary_Pikachu_Hp, "Hp")   
           
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Blastoise' and user_Move == '3':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 76
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 76 damage and is now at", Gary_Pikachu_Hp, "Hp")  
           
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Blastoise' and user_Move == '4':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 122
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 122 damage and is now at", Gary_Pikachu_Hp, "Hp")   
           
        #damage from Venusaur   
           
           
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Venusaur' and user_Move == '1':
           Gary_Blastoise_Hp = Gary_Blastoise_Hp - 131
           if Gary_Blastoise_Hp < 0:
             Gary_Blastoise_Hp = 0 
           print ("It was super effective! Gary's Blastoise took 131 damage and is now at", Gary_Blastoise_Hp, "Hp")
           
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Venusaur' and user_Move == '2':
           Gary_Blastoise_Hp = Gary_Blastoise_Hp - 100
           if Gary_Blastoise_Hp < 0:
             Gary_Blastoise_Hp = 0 
           Venusaur_Hp = Venusaur_Hp - 30   
           print ("Gary's Blastoise took 100 damage and is now at", Gary_Blastoise_Hp, "Hp, but Venusaur took 30 recoil damage")   
           
           
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Venusaur' and user_Move == '3':
           Gary_Blastoise_Hp = Gary_Blastoise_Hp  - 90
           if Gary_Blastoise_Hp < 0:
             Gary_Blastoise_Hp = 0 
           print ("Gary's Blastoise took 90 damage and is now at", Gary_Blastoise_Hp, "Hp")   
             
        
        
          
           
           
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Venusaur' and user_Move == '1':
           Gary_Charizard_Hp = Gary_Charizard_Hp - 78 
           if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0 
           print ("It was not very effective! Gary's Charizard took 78 damage and is now at", Gary_Charizard_Hp, "Hp")    
           
           
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Venusaur' and user_Move == '2':
           Gary_Charizard_Hp = Gary_Charizard_Hp - 115
           if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0 
           Venusaur_Hp = Venusaur_Hp - 30
           print ("Gary's Charizard took 115 damage and is now at", Gary_Charizard_Hp, "Hp, but Venusaur took 30 recoil damage") 
           
           
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Venusaur' and user_Move == '3':
           Gary_Charizard_Hp = Gary_Charizard_Hp - 78
           if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0 
           print ("Gary's Charizard took 78 damage and is now at", Gary_Charizard_Hp, "Hp")
           
           
           
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Venusaur' and user_Move == '1':
          if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print ("Venusaur used Protect and blocked the incoming damage")
          else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 15
          if Gary_Venusaur_Hp < 0:
             Gary_Venusaur_Hp = 0 
          print ("It was not very effective! Gary's Venusaur took 15 damage and is now at", Gary_Venusaur_Hp, "Hp")   
           
           
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Venusaur' and user_Move == '2':
          if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
          else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 109 
            if Gary_Venusaur_Hp < 0:
             Gary_Venusaur_Hp = 0 
            Venusaur_Hp = Venusaur_Hp - 30
            print ("Gary's Venusaur took 109 damage and is now at", Gary_Venusaur_Hp, "Hp, but Venusaur took 30 recoil damage")    
           
           
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Venusaur' and user_Move == '3':
          if Gary_Move == 4:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
            print  ("Venusaur used Protect and blocked the incoming damage")
          else:
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 72
            if Gary_Venusaur_Hp < 0:
             Gary_Venusaur_Hp = 0 
            print ("Gary's Venusaur took 72 damage and is now at", Gary_Venusaur_Hp, "Hp")     
            
            
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Venusaur' and user_Move == '1':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp  - 126 
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 126 damage and is now at", Gary_Pikachu_Hp, "Hp")       
            
        
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Venusaur' and user_Move == '2':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 138 
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 138 damage and is now at", Gary_Pikachu_Hp, "Hp")           
            
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Venusaur' and user_Move == '3':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 86 
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 86 damage and is now at", Gary_Pikachu_Hp, "Hp")     
            
          #Damage from Pikachu  
            
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Pikachu' and user_Move == '1':
           Gary_Blastoise_Hp = Gary_Blastoise_Hp - 141 
           if Gary_Blastoise_Hp < 0:
             Gary_Blastoise_Hp = 0 
           print ("It was super effective! Gary's Blastoise took 141 damage and is now at", Gary_Blastoise_Hp, "Hp")     
            
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Pikachu' and user_Move == '2':
           Gary_Blastoise_Hp = Gary_Blastoise_Hp - 128 
           if Gary_Blastoise_Hp < 0:
             Gary_Blastoise_Hp = 0 
           print ("It was super effective! Gary's Blastoise took 128 damage and is now at", Gary_Blastoise_Hp, "Hp")    
            
            
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Pikachu' and user_Move == '3':
           Gary_Blastoise_Hp = Gary_Blastoise_Hp - 68 
           if Gary_Blastoise_Hp < 0:
             Gary_Blastoise_Hp = 0 
           print ("Gary's Blastoise took 68 damage and is now at", Gary_Blastoise_Hp, "Hp")     
            
        if Gary_Pokemon == 'Blastoise' and user_pokemon == 'Pikachu' and user_Move == '4':
           Gary_Blastoise_Hp = Gary_Blastoise_Hp - 34
           if Gary_Blastoise_Hp < 0:
             Gary_Blastoise_Hp = 0 
           print ("Gary's Blastoise took 34 damage and is now at", Gary_Blastoise_Hp, "Hp")    
            
            
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Pikachu' and user_Move == '1':
           Gary_Charizard_Hp = Gary_Charizard_Hp - 147
           if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0 
           print ("It was super effective! Gary's Charizard took 147 damage and is now at", Gary_Charizard_Hp, "Hp")     
            
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Pikachu' and user_Move == '2':
           Gary_Charizard_Hp = Gary_Charizard_Hp - 136
           if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0 
           print ("It was super effective! Gary's Charizard took 147 damage and is now at", Gary_Charizard_Hp, "Hp")      
          
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Pikachu' and user_Move == '3':
           Gary_Charizard_Hp = Gary_Charizard_Hp - 83
           if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0 
           print ("Gary's Charizard took 82 damage and is now at", Gary_Charizard_Hp, "Hp")  
          
          
        if Gary_Pokemon == 'Charizard' and user_pokemon == 'Pikachu' and user_Move == '4':
           Gary_Charizard_Hp = Gary_Charizard_Hp - 42 
           if Gary_Charizard_Hp < 0:
             Gary_Charizard_Hp = 0 
           print ("Gary's Charizard took 42 damage and is now at", Gary_Charizard_Hp, "Hp")  
          
          
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Pikachu' and user_Move == '1':
          if Gary_Move == 4:
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
           print ("Venusaur used Protect and blocked the incoming damage")
          else:
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 78  
           if Gary_Venusaur_Hp < 0:
             Gary_Venusaur_Hp = 0 
           print ("Gary's Venusaur took 78 damage and is now at", Gary_Venusaur_Hp, "Hp")  
          
          
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Pikachu' and user_Move == '2':
          if Gary_Move == 4:
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
           print ("Venusaur used Protect and blocked the incoming damage")
          else:
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 71 
           if Gary_Venusaur_Hp < 0:
             Gary_Venusaur_Hp = 0 
           print ("Gary's Venusaur took 71 damage and is now at", Gary_Venusaur_Hp, "Hp")   
          
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Pikachu' and user_Move == '3':
          if Gary_Move == 4:
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
           print ("Venusaur used Protect and blocked the incoming damage")
          else:
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 98 
           if Gary_Venusaur_Hp < 0:
             Gary_Venusaur_Hp = 0 
           print ("Gary's Venusaur took 98 damage and is now at", Gary_Venusaur_Hp, "Hp")   
            
            
            
        if Gary_Pokemon == 'Venusaur' and user_pokemon == 'Pikachu' and user_Move == '4':
          if Gary_Move == 4:
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 0
           print ("Venusaur used Protect and blocked the incoming damage")
          else:
            if Gary_Venusaur_Hp < 0:
              Gary_Venusaur_Hp = 0 
            Gary_Venusaur_Hp = Gary_Venusaur_Hp - 40
            print ("Gary's Venusaur took 40 damage and is now at", Gary_Venusaur_Hp, "Hp")    
            
            
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Pikachu' and user_Move == '1':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 92
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 92 damage and is now at", Gary_Pikachu_Hp, "Hp")    
            
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Pikachu' and user_Move == '2':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 84
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 84 damage and is now at", Gary_Pikachu_Hp, "Hp")    
            
            
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Pikachu' and user_Move == '3':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 79
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 79 damage and is now at", Gary_Pikachu_Hp, "Hp")    
            
        
        if Gary_Pokemon == 'Pikachu' and user_pokemon == 'Pikachu' and user_Move == '4':
           Gary_Pikachu_Hp = Gary_Pikachu_Hp - 48
           if Gary_Pikachu_Hp < 0:
             Gary_Pikachu_Hp = 0 
           print ("Gary's Pikachu took 48 damage and is now at", Gary_Pikachu_Hp, "Hp")
           
      if Gary_Blastoise_Hp == 0 or Gary_Charizard_Hp == 0 or Gary_Pikachu_Hp == 0 or Gary_Venusaur_Hp == 0:
        break 
      
    #make protect not miss 
      if Gary_Pokemon == 'Venusaur' and Gary_Move == 4:
        Gary_Miss == 4
      
      #make Gary miss
      if Gary_Miss == 3 or Gary_Miss == 10:
       print ("The opposing", Gary_Pokemon, "missed its attack")
      else: 
        
        #print gary's move
        sleep (2)
        if Gary_Pokemon == 'Charizard' and Gary_Move == 1:
            print ("The opposing Charizard used Wing Attack")
        if Gary_Pokemon == 'Charizard' and Gary_Move == 2:
            print ("The opposing Charizard used Flamethrower")
        if Gary_Pokemon == 'Charizard' and Gary_Move == 3:
            print ("The opposing Charizard used Dragon Claw")
        if Gary_Pokemon == 'Charizard' and Gary_Move == 4: 
            print ("The opposing Charizard used Dragon Tail")
         
        if Gary_Pokemon == 'Blastoise'and Gary_Move == 1:
            print ('The opposing Blastoise used Hydro Pump')
        if Gary_Pokemon == 'Blastoise'and Gary_Move == 2:
            print ('The opposing Blastoise used Skull Bash')
        if Gary_Pokemon == 'Blastoise'and Gary_Move == 3:
            print ('The opposing Blastoise used Bite')
        if Gary_Pokemon == 'Blastoise'and Gary_Move == 4:
            print ('The opposing Blastoise used Aqua Tail')
          
        if Gary_Pokemon == 'Venusaur'and Gary_Move == 1:
            print ('The opposing Venusaur used Razor Leaf')
        if Gary_Pokemon == 'Venusaur'and Gary_Move == 2:
            print ('The opposing Venusaur used Double-Edge, but took 30 recoil damage')
        if Gary_Pokemon == 'Venusaur'and Gary_Move == 3:
            print ('The opposing Venusaur used Sludge Bomb')
        
          
        if Gary_Pokemon == 'Pikachu'and Gary_Move == 1:
            print ('The opposing Pikachu used Thunder')
        if Gary_Pokemon == 'Pikachu'and Gary_Move == 2:
            print ('The opposing Pikachu used Electro Ball')
        if Gary_Pokemon == 'Pikachu'and Gary_Move == 3:
            print ('The opposing Pikachu used Slam')
        if Gary_Pokemon == 'Pikachu'and Gary_Move == 4:
            print ('The opposing Pikachu used Quick Attack')
        
      
       
        
       
       
        
        #Gary's Blastoise attacks you 
            
            
        sleep(2)
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Blastoise' and Gary_Move == 1:
          Blastoise_Hp = Blastoise_Hp - 70
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("It was not very effective! Your Blastoise took 70 damage and is now at", Blastoise_Hp, "Hp")
          
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Blastoise' and Gary_Move == 2:
          Blastoise_Hp = Blastoise_Hp - 102 
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 102 damage and is now at", Blastoise_Hp, "Hp")  
        
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Blastoise' and Gary_Move == 3:
          Blastoise_Hp = Blastoise_Hp - 47
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 47 damage and is now at", Blastoise_Hp, "Hp")
        
        
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Blastoise' and Gary_Move == 4:
          Blastoise_Hp = Blastoise_Hp - 71
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("It was not very effective! Your Blastoise took 71 damage and is now at", Blastoise_Hp, "Hp")   
          
            
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Blastoise' and Gary_Move == 1:
          Charizard_Hp = Charizard_Hp - 135 
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("It was super effective! Your Charizard took 135 damage and is now at", Charizard_Hp, "Hp")    
       
       
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Blastoise' and Gary_Move == 2:
          Charizard_Hp = Charizard_Hp - 128
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 128 damage and is now at", Charizard_Hp, "Hp")
          
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Blastoise' and Gary_Move == 3:
          Charizard_Hp = Charizard_Hp - 58
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 58 damage and is now at", Charizard_Hp, "Hp")
       
       
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Blastoise' and Gary_Move == 4:
          Charizard_Hp = Charizard_Hp - 108
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("It was super effective! Your Charizard took 108 damage and is now at", Charizard_Hp, "Hp")  
       
       
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Blastoise' and Gary_Move == 1:
          if user_Move == "4":
           Venusaur_Hp = Venusaur_Hp - 0
           print ("Venusaur used Protect and blocked the incoming damage")
          else:
           Venusaur_Hp = Venusaur_Hp - 68
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("It was was not super effective! Your Venusaur took 68 damage and is now at", Venusaur_Hp, "Hp")
       
       
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Blastoise' and Gary_Move == 2:
          if user_Move == "4":
           Venusaur_Hp = Venusaur_Hp - 0
           print ("Venusaur used Protect and blocked the incoming damage")
          else:
           Venusaur_Hp = Venusaur_Hp - 101
           if Venusaur_Hp < 0:
            Venusaur_Hp = 0 
           print ("Your Venusaur took 101 damage and is now at", Venusaur_Hp, "Hp")
       
       
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Blastoise' and Gary_Move == 3:
          if user_Move == "4":
           Venusaur_Hp = Venusaur_Hp - 0
           print ("Venusaur used Protect and blocked the incoming damage")
          else:
           Venusaur_Hp = Venusaur_Hp - 55
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("Your Venusaur took 55 damage and is now at", Venusaur_Hp, "Hp")
         
         
         
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Blastoise' and Gary_Move == 4:
          if user_Move == "4":
           Venusaur_Hp = Venusaur_Hp - 0
           print ("Venusaur used Protect and blocked the incoming damage")
          else:
           Venusaur_Hp = Venusaur_Hp - 59
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("It was was not super effective! Your Venusaur took 59 damage and is now at", Venusaur_Hp, "Hp")
       
       
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Blastoise' and Gary_Move == 1:
          Pikachu_Hp = Pikachu_Hp - 101
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 101 damage and is now at", Pikachu_Hp, "Hp")
       
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Blastoise' and Gary_Move == 2:
          Pikachu_Hp = Pikachu_Hp - 116
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 116 damage and is now at", Pikachu_Hp, "Hp")
          
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Blastoise' and Gary_Move == 3:
          Pikachu_Hp = Pikachu_Hp - 76
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 76 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Blastoise' and Gary_Move == 4:
          Pikachu_Hp = Pikachu_Hp - 122
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 122 damage and is now at", Pikachu_Hp, "Hp")
          
          
          #damage from Gary's Charizard 
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Charizard' and Gary_Move == 1:
          Charizard_Hp = Charizard_Hp - 47
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 47 damage and is now at", Charizard_Hp, "Hp")
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Charizard' and Gary_Move == 2:
          Charizard_Hp = Charizard_Hp - 72
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("It was not very effective! Your Charizard took 72 damage and is now at", Charizard_Hp, "Hp")
        
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Charizard' and Gary_Move == 3:
          Charizard_Hp = Charizard_Hp - 78
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 78 damage and is now at", Charizard_Hp, "Hp")
       
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Charizard' and Gary_Move == 4:
          Charizard_Hp = Charizard_Hp - 39
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 39 damage and is now at", Charizard_Hp, "Hp")
       
      
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Charizard' and Gary_Move == 1:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0
          else:
           Venusaur_Hp = Venusaur_Hp - 80
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("It was super effective! Your Venusaur took 80 damage and is now at", Venusaur_Hp, "Hp")
       
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Charizard' and Gary_Move == 2:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0 
          else:
           Venusaur_Hp = Venusaur_Hp - 117
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("It was super effective! Your Venusaur took 117 damage and is now at", Venusaur_Hp, "Hp")
       
       
       
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Charizard' and Gary_Move == 3:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0 
          else:
           Venusaur_Hp = Venusaur_Hp - 74
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("Your Venusaur took  damage and is now at", Venusaur_Hp, "Hp")
       
       
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Charizard' and Gary_Move == 4:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0 
          else:
           Venusaur_Hp = Venusaur_Hp - 37
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("Your Venusaur took 37 damage and is now at", Venusaur_Hp, "Hp")
          
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Charizard' and Gary_Move == 1:
          Pikachu_Hp = Pikachu_Hp - 41
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("It was not very effective! Your Pikachu took 41 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Charizard' and Gary_Move == 2:
          Pikachu_Hp = Pikachu_Hp - 91
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 91 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Charizard' and Gary_Move == 3:
          Pikachu_Hp = Pikachu_Hp - 103
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 103 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Charizard' and Gary_Move == 4:
          Pikachu_Hp = Pikachu_Hp - 51
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 51 damage and is now at", Pikachu_Hp, "Hp")
       
       
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Charizard' and Gary_Move == 1:
          Blastoise_Hp = Blastoise_Hp - 57
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 57 damage and is now at", Blastoise_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Charizard' and Gary_Move == 2:
          Blastoise_Hp = Blastoise_Hp - 69
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("It was not very effective! Your Blastoise took 69 damage and is now at", Blastoise_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Charizard' and Gary_Move == 3:
          Blastoise_Hp = Blastoise_Hp - 64
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 64 damage and is now at", Blastoise_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Charizard' and Gary_Move == 4:
          Blastoise_Hp = Blastoise_Hp - 31
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 31 damage and is now at", Blastoise_Hp, "Hp")
          
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Venusaur' and Gary_Move == 1:
          Charizard_Hp = Charizard_Hp - 78
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("It was not very effective! Your Charizard took 78 damage and is now at", Charizard_Hp, "Hp")
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Venusaur' and Gary_Move == 2:
          Charizard_Hp = Charizard_Hp - 115
          Gary_Venusaur_Hp = Gary_Venusaur_Hp - 30
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 115 damage and is now at", Charizard_Hp, "Hp")
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Venusaur' and Gary_Move == 3:
          Charizard_Hp = Charizard_Hp - 78
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 78 damage and is now at", Charizard_Hp, "Hp")
    
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Venusaur' and Gary_Move == 1:
          Blastoise_Hp = Blastoise_Hp - 131
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("It was super effective! Your Blastoise took 131 damage and is now at", Blastoise_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Venusaur' and Gary_Move == 2:
          Blastoise_Hp = Blastoise_Hp - 100
          Gary_Venusaur_Hp = Gary_Venusaur_Hp - 30
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 100 damage and is now at", Blastoise_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Venusaur' and Gary_Move == 3:
          Blastoise_Hp = Blastoise_Hp - 90
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 90 damage and is now at", Blastoise_Hp, "Hp")
          
        
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Venusaur' and Gary_Move == 1:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0 
          else:
           Venusaur_Hp = Venusaur_Hp - 15
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("It was not very effective! Your Venusaur took 15 damage and is now at", Venusaur_Hp, "Hp")
          
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Venusaur' and Gary_Move == 2:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0 
          else:
           Venusaur_Hp = Venusaur_Hp - 109
           Gary_Venusaur_Hp = Gary_Venusaur_Hp - 30
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("It was not very effective! Your Venusaur took 109 damage and is now at", Venusaur_Hp, "Hp")
          
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Venusaur' and Gary_Move == 3:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0 
          else:
           Venusaur_Hp = Venusaur_Hp - 72
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("Your Venusaur took 72 damage and is now at", Venusaur_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Venusaur' and Gary_Move == 1:
          Pikachu_Hp = Pikachu_Hp - 126
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 126 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Venusaur' and Gary_Move == 2:
          Pikachu_Hp = Pikachu_Hp - 138
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 138 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Venusaur' and Gary_Move == 3:
          Pikachu_Hp = Pikachu_Hp - 86
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 86 damage and is now at", Pikachu_Hp, "Hp")
          
        #damage from gary's pikachu  
          
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Pikachu' and Gary_Move == 1:
          Charizard_Hp = Charizard_Hp - 147
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("It was super effective! Your Charizard took 147 damage and is now at", Charizard_Hp, "Hp")
       
       
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Pikachu' and Gary_Move == 2:
          Charizard_Hp = Charizard_Hp - 136
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("It was super effective! Your Charizard took 136 damage and is now at", Charizard_Hp, "Hp")
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Pikachu' and Gary_Move == 3:
          Charizard_Hp = Charizard_Hp - 83
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 83 damage and is now at", Charizard_Hp, "Hp")
          
        if user_pokemon == 'Charizard' and Gary_Pokemon == 'Pikachu' and Gary_Move == 4:
          Charizard_Hp = Charizard_Hp - 42
          if Charizard_Hp < 0:
            Charizard_Hp = 0 
          print ("Your Charizard took 42 damage and is now at", Charizard_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Pikachu' and Gary_Move == 1:
          Blastoise_Hp = Blastoise_Hp - 141
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("It was super effective! Your Blastoise took 141 damage and is now at", Blastoise_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Pikachu' and Gary_Move == 2:
          Blastoise_Hp = Blastoise_Hp - 128
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("It was super effective! Your Blastoise took 128 damage and is now at", Blastoise_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Pikachu' and Gary_Move == 3:
          Blastoise_Hp = Blastoise_Hp - 68
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 68 damage and is now at", Blastoise_Hp, "Hp")
          
        if user_pokemon == 'Blastoise' and Gary_Pokemon == 'Pikachu' and Gary_Move == 4:
          Blastoise_Hp = Blastoise_Hp - 34
          if Blastoise_Hp < 0:
            Blastoise_Hp = 0 
          print ("Your Blastoise took 34 damage and is now at", Blastoise_Hp, "Hp")
       
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Pikachu' and Gary_Move == 1:
          if Gary_Move == 4:
            Venusaur_Hp = Venusaur_Hp - 0
          else: 
           Venusaur_Hp = Venusaur_Hp - 78
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("Your Venusaur took 78 damage and is now at", Venusaur_Hp, "Hp")
           
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Pikachu' and Gary_Move == 2:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0
          else: 
           Venusaur_Hp = Venusaur_Hp - 71
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("Your Venusaur took 71 damage and is now at", Venusaur_Hp, "Hp")
           
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Pikachu' and Gary_Move == 3:
          if user_Move == "4":
            Venusaur_Hp = Venusaur_Hp - 0
          else: 
           Venusaur_Hp = Venusaur_Hp - 98
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("Your Venusaur took 98 damage and is now at", Venusaur_Hp, "Hp")
           
        if user_pokemon == 'Venusaur' and Gary_Pokemon == 'Pikachu' and Gary_Move == "4":
          if Gary_Move == 4:
            Venusaur_Hp = Venusaur_Hp - 0
          else: 
           Venusaur_Hp = Venusaur_Hp - 40
           if Venusaur_Hp < 0:
             Venusaur_Hp = 0 
           print ("Your Venusaur took 40 damage and is now at", Venusaur_Hp, "Hp")
           
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Pikachu' and Gary_Move == 1:
          Pikachu_Hp_Hp = Pikachu_Hp - 92
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("It was not very effective! Your Pikachu took 92 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Pikachu' and Gary_Move == 2:
          Pikachu_Hp_Hp = Pikachu_Hp - 84
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("It was not very effective! Your Pikachu took 84 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Pikachu' and Gary_Move == 3:
          Pikachu_Hp_Hp = Pikachu_Hp - 79
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 79 damage and is now at", Pikachu_Hp, "Hp")
          
        if user_pokemon == 'Pikachu' and Gary_Pokemon == 'Pikachu' and Gary_Move == 4:
          Pikachu_Hp_Hp = Pikachu_Hp - 48
          if Pikachu_Hp < 0:
            Pikachu_Hp = 0 
          print ("Your Pikachu took 48 damage and is now at", Pikachu_Hp, "Hp")
            
        
  #loop ends and displays who won the battle 
  sleep (2)     
  if Gary_Blastoise_Hp == 0 or Gary_Charizard_Hp == 0 or Gary_Pikachu_Hp == 0 or Gary_Venusaur_Hp == 0:
    #tell them they won 
    print ("Gary's", Gary_Pokemon, "has fainted,", username, "won the battle")
  else:
    sleep (2)
    #tell them they lost 
    print ("Your", user_pokemon, "has fainted, Gary won the battle")
    
    #ask if they want to play again 
    #sleep for 1 second 
  sleep (1)
  #ask if they want to play again 
  print ("Would you like to play again? Type Yes or No")
  #get input if they want to play again 
  option = input()
  
  #tell they bye 
print ("Bye, Have a good day!")

  
