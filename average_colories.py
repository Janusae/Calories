def average_calories() :
      day = 1
      empty_list = []
      plus = 0
      while True :
            user = input(F"Day {day} Inter your calory: ")
            day += 1
            if user.capitalize() == "Done" :
                  break
            empty_list.append(user)
      for i in empty_list :
            plus += int(i)
      print(plus/len(empty_list))
average_calories()