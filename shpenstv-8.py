if __name__ == "__main__": 
   fail_open = "INPUT.TXT" 
   with open(fail_open, 'r') as fail: 
      text = fail.read() 
   a, b, c = text.split() 
   if int(a) * int(b) == int(c): 
      print("YES") 
   else: 
      print("NO")