def factorial() :
  entrada = int (input("Enter a number: "))
  result = num = entrada
  
  if num == 0:
    result = 1
  else:
    while num > 1 :
      num = num - 1
      result = result * num
    
  print ("The factorial of", entrada, "is", result)
factorial()
