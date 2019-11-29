def check_prime(n):
  if (n==1):
    return False
  elif (n==2):
    return True
  else:
    flag = 0
    for i in range(2, (n/2)+1):
      if n%i == 0:
        flag = 1
        break
    if flag == 0:
      return True
    else:
      return False

if __name__ == "__main__":
  for i in range(2, 100):
    if check_prime(i) == True:
      print(i)

