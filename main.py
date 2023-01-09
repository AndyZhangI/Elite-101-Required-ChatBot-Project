# Cost of Each Product --------------------------------------------------
Cost1 = [
'---------------               ',
'Grocery:                      ',
'---------------               ',
'Milk = 6$                     ',
'Eggs = 14$                    ',
'Bread = 10$                   ',
'Cereal = 8$                   ',
]

Cost2 = [
'---------------               ',
'Clothing:                     ',
'---------------               ',
'Hat = 16$                     ',
'Cap = 15$                     ',
'Shirt = 18$                   ',
'Pants = 20$                   ',
'Socks = 17$                   ',
'Shoes = 23$                   ',
]

Cost3 = [
'----------------              ',
'Electronics:                  ',
'----------------              ',
'Big Television = 400$         ',
'Medium Television = 300$      ',
'Small Television = 250$       ',
'Tablet = 450$                 ',
'Phone = 350$                  ',
]

# List of Products ------------------------------------------------------
List = [
'---------------               ',
'Grocery:                      ',
'---------------               ',
'Milk                          ',
'Eggs                          ',
'Bread                         ',
'Cereal                        ',
'---------------               ',
'Clothing:                     ',
'---------------               ',
'Hat                           ',
'Cap                           ',
'Shirt                         ',
'Pants                         ',
'Socks                         ',
'Shoes                         ',
'----------------              ',
'Electronics:                  ',
'----------------              ',
'Big Television                ',
'Medium Television             ',
'Small Television              ',
'Tablet                        ',
'Phone                         ',

]

# Mapping ---------------------------------------------------------------
map = [
'___________________           ',
'|#####.&&&&&.%%%%%|           ',
'|#####.&&&&&.%%%%%|           ',
'|#####.&&&&&.%%%%%|           ',
'|.................|           ',
'|..0..0..0..0..0..|           ',
'-------------------           ',
'Map legend:                   ',
'0 = represents Cashier        ',
'# = represents Grocery        ',
'& = represents Clothing       ',
'% = represents Electronics    ',
]

# Days and Hours---------------------------------------------------------
import random #Imported from Library
schedule = [
'Monday: Open for 7 Hours      ',
'Tuesday: Open for 8 Hours     ',
'Wednesday: Open for 9 Hours   ',
'Thursday: Open for 7 Hours    ',
'Friday: Open for 10 Hours     ',
'Saturday: Open for 7 Hours    ',
'Sunday: Closed                ',
]
number = ['6','7','8','9','10']
today = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
#------------------------------------------------------------------------
bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')

while True:
  if bot == 'no':
    print('Okay, Wave your hand if you have any questions.\n')
    bot = input('---Ready with a question? Wave your hand!')
  
    if bot == 'Wave':
      bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')
    else:
      bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')

  elif bot == 'yes':
      print('Great! You have come to the right place!\n')
      choice = input('Select the options: Hours, Map, Products.\n')
#--------------- HOURS ----------------------------------------------------
      if choice == 'Hours': 
         choice1 = input('Would you like to know the store hours for "today" or "specific day?"\n')
         if choice1 == 'today':
           print(f'Today is {random.choice(today)} and the store would be open for {random.choice(number)} Hours.\n')
           bot10 = input('Need anything else? Wave your hand!')
           if bot10 == 'Wave':
             bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')
         if choice1 == 'specific day':
           print('Here is the list of Store Hours. You are welcome to come back!')
           print(schedule)
           bot10 = input('Need anything else? Wave your hand!')
           if bot10 == 'Wave':
              bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')
# -------------------------- MAP -------------------------------------------
      elif choice == 'Map':
         print(map)
         direction = input('Do you want to know how to get to a location? (yes/no)\n')
    
         while direction == 'yes':
           direction = input('Where do you want to go? (Grocery, Clothes, Electronics)\n')
      
           if direction == 'Grocery':
             print('Head to the left of the store.')
             bot11 = input('Need anything else? Wave your hand!')
             if bot11 == 'Wave':
                bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')
        
           elif direction == 'Clothes':
             print ('Head to the center of the store.')
             bot12 = input('Need anything else? Wave your hand!')
             if bot12 == 'Wave':
                bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')
           
           elif direction == 'Electronics':
              print ('Head to the Right of the store.')
              bot13 = input('Need anything else? Wave your hand!')
              if bot13 == 'Wave':
                 bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')
     
         if direction == 'no':
            bot8 = input('Have a great time shopping here at Targots! Wave your hand if you have any questions.\n')
            if bot8 == 'Wave':
               bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')  

#---------------- PRODUCTS ---------------------------------------------------
      elif choice == 'Products':
         print(List)
         product = input('do you want to know the cost of a product? (yes/no)\n')
    
         while product =='no':
           bot2 = input('Nice to see you shopping here at Targots! Wave your hand if you have any questions.\n')
           if bot2 == 'Wave':
              bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')
              break

#--------------------------- COST ------------------------------------      
         if product == 'yes':
            product2 = input('Tell me a category you would like to view th cost of each product.\n')
#----------------------------------------------------------------------------  
            if product2 == 'Grocery':
               print(Cost1)
               product3 = input('Do you want to see the cost of other products? (yes/no)\n')
        
               while product3 == 'no':
                  print('Okay, Wave your hand if you need anything else.')
                  bot = input('---Ready with a question? Wave your hand!')
          
                  if bot == 'Wave':
                     bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')

               if product3 == 'yes':
                  product = input('Tell me a category you would like to view the cost of each product.\n')
#----------------------------------------------------------------------------    
            if product == 'Clothing':
               print(Cost2)
               product3 = input('Do you want to see the cost of other products? (yes/no)\n')
        
               while product3 == 'no':
                  print('Okay, Wave your hand if you need anything else.')
                  bot = input('---Ready with a question? Wave your hand!')
          
                  if bot == 'Wave':
                     bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')

               if product3 == 'yes':
                  product = input('Tell me a category you would like to view the cost of each product.\n')
#----------------------------------------------------------------------------  
            if product == 'Electronics':
               print(Cost3)
               product3 = input('Do you want to see the cost of other products? (yes/no)\n')
        
               while product3 == 'no':
                  print('Okay, Wave your hand if you need anything else.')
                  bot = input('---Ready with a question? Wave your hand!')
          
                  if bot == 'Wave':
                     bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products? (yes/no)\n')

               if product3 == 'yes':
                  product = input('Tell me a category you would like to view the cost of each product.\n')

  else:
    bot = input('Can you repeat that? Do you have any questions for the following: Store hours, Mapping of Categories, List of Products? (yes/no)\n ')