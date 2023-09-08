#Returns the number of digits in d

def GetSize(d):
  d = str(d)
  return len(d)


def GetPrefix(number, k):
  if len(number) < k:
      return number
  else:
    return number[:k]
   
  

def PrefixMatched(number, d):
  number = str(number)
  d = str(d)
  prefix_list = ['4', '5', '37', '6']

  if d in prefix_list and d in number[:2]:
    return True
  else:
    return False


def getDigit(number):
  number = str(number)
  if len(number) == 2:
    digit1 = int(number[0])
    digit2 = int(number[1])

    a = digit1 + digit2
    return a
  else:
    return number


def SumOfDoubleEvenPlace(number):
  number_list = []
  list = []
  number = str(number)
  index = len(number) - 2
  while index >= 0:
    print(number[index])
    if index % 2 == 0:
      list.append(number[index])
      print(number[index])
    index = index -2
    #print(list)
    
  for i in list:
    i = int(i)
   
    i = i * 2
    i = getDigit(i)
    number_list.append(int(i))
    #print(number_list)
  for i in number_list:
    i = int(i)
  total = sum(number_list)
  #print('#####',total)
  return total
  
    
    
def sumOfOddPlace(number):
 
  number_list = []
  list = []
  number = str(number)
  index = len(number) - 1
  while index >= 0:
    #print(number[index])
    if index % 2 != 0:
      list.append(number[index])
      #print(number[index])
    index = index - 1
    print(list)
    
  for i in list:
    i = int(i)
   
    number_list.append(i)
    #print(number_list)
  for i in number_list:
    
    total = sum(number_list)
  #print('###',total)
 
  return total


def IsValid(number):
  if (sumOfOddPlace(number) + SumOfDoubleEvenPlace(number)) % 10 == 0:
    return True
  else:
    return False
#----------------------------------------------------------------------------------

#print(GetSize(438857601841070))

#print(GetPrefix(str(438857601841070), 5))
#print(PrefixMatched(438857601841070, 4))
#print(getDigit('4'))
#print(SumOfDouleEvenPlace(4388576018402626))
#print(sumOfOddPlace(4388576018402626))
#print(IsValid(4388576018410707))