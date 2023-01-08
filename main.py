# Days and Hours---------------------------------------------------------
import random

Monday = 7
Tuesday = 8
Wednesday = 9
Thursday = 8
Friday = 10
Saturday = 7
Sunday = 'Closed'

week = ['Monday', 'Tuesday','Wednesday','Thursday','Firday','Sunday','Saturday','Sunday']
#------------------------------------------------------------------------

bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products?\n')

if bot == 'no':
  print('Okay, Come back later if you have anymore questions.\n')
  print('Wave your hand and I will be summoned.\n')
  bot = input('Ready with a question? Wave your hand!')
  if bot == 'Wave':
    bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products?\n')
  else:
    bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products?\n')

if bot == 'yes':
  print('Great! You have come to the right place!\n')
  choice = input('Select the options: Hours, Map, Products.\n')

else:
    bot = input('Welcome to Targots! Do you have questions for the follow: Store hours, mapping of categories, list of products?\n')
  
  if choice == 'Hours': 
    
    
  if choice == 'Map':
    
  if choice == 'Products':
    
while True:
  if choice == 