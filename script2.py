import random
target_number= 20000000000000000000000000


 #Loop
#counter = 0
#while counter != target_number:
 #   counter+=2000
#  print(f"Counter: {counter}")
  #  print("We reached the target number")
   # while True:
    #    random_number = random.randint (1, 1000000000000000000000000000000000000000000000000000000)
     #   print(f"random number: {random_number}")
      #  counter +=1
       # if random_number == target_number:
        #    print("we reached the target number")
         #   print(f"it took {counter} attempts")
          #  break
          numbers = [random.randint(1,1000000000000000000000000000000000000000000000000000000) for _ in range(random.randint(1, 1000000000000000000000000000000000000000000000000000000))]
          print("original list")
          print(numbers)

                # Bubble Sort
                n = len(numbers)
                for i in range(n):
                    for j in range(0, n-i-1):
                        if numbers [j] > numbers[j+1], numbers[j]
                        print("sorted list")
                        print(numbers)



                        #bogo sort
                        numbers.clear()
                        numbers = [random.randint(1, 1000000000000000000000000000000000000000000000000000000) for in range (1000000000000000000000000000000000000000000000000000000)]
                        print("original list")
                        print(numbers)

                        counter = 0
                        while True:
                            isSorted = True

                            for i in range(len(numbers)-1):
                                if numbers[i] > numbers [i+1]:
                                    isSorted=False
                                    print(numbers[i])
                                    break
                    if isSorted:
                        print("sorted list")
                        print(numbers)
                        print(f"it took {counter} attempts")
                        break
