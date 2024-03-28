#限定卡池抽卡計算2
import random
import math

c = int(input(''))

blue = 0
goldny = 0
goldy = 0
goldycount = 0
perple = 0
count = 1
gold = 0
gchance = 6
print('')

for i in range(1,c+1,1):
  if gold<=73:
    a=random.randint(1,1000)
    if a<=3 and goldny==0:
     print(f'{count}////歪掉')
     goldy=goldy+1
     goldycount = goldycount+1
     count = count+1
     gold = 0
     
    elif a<=6:
     print(f'{count}/////沒歪的金光')
     goldny = goldny+1
     goldy = 0
     count = count+1
     gold = 0

    elif a>=900 or blue==9:
       print(f'{count}/紫光')
       blue=0
       count = count+1
       gold = gold+1
       perple = perple+1
    
    else:
       print(f'{count}藍光') 
       blue = blue+1
       count = count+1
       gold = gold+1

  elif gold>=74 and gold<89:
    a=random.randint(1,1000)
    gchance = gchance + 60
    if a<=gchance:
      a=random.randint(1,2)
      gold = 0
      if a==1 and goldy==0:
        print(f'{count}////歪掉')
        goldycount = goldycount+1
        goldy=1
        count = count+1
      else:
        print(f'{count}/////沒歪的金光')
        goldny = goldny+1
        goldy = 0
        count = count+1

    elif a>=900 or blue==9:
       print(f'{count}/紫光')
       blue=0
       count = count+1
       gold = gold+1
       perple = perple+1
    
    else:
       print(f'{count}藍光') 
       blue = blue+1
       count = count+1
       gold = gold+1

  if gold==89:
      gold = 0
      a=random.randint(1,2)
      if a==1 and goldy==0:
        print(f'{count}////歪掉')
        goldycount = goldycount+1
        goldy=1
        count = count+1
      else:
        print(f'{count}/////沒歪的金光')
        goldny = goldny+1
        goldy = 0
        count = count+1
        
count = count-1
print(f'\n抽數{count}')
print(f'\n金光數 沒歪{goldny}隻 歪掉{goldycount}隻')
print(f'紫光數 {perple}隻')
