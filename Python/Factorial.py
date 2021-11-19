def factorial() :
  entrada = int (input("Enter a number: "))
  result = num = entrada
  
  while num > 1 :
    num = num - 1
    result = result * num
    
  print ("The factorial of", entrada, "is", result)

  


  print ("The factorial of the number is: ", result)

factorial()
