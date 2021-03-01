class pirmas:
 def rusiuoti(self):
  try:
   x = [1, 2, 3, 4, 5, 100, 200, 300, 1000]
   y = [100, 1000, 250, 200, 2, 2]
   rusiavimas=x+y
   rusiavimas.sort()
   print(str(rusiavimas))

  except:
   print('Bandyk is naujo..')


p=pirmas()
p.rusiuoti()



