def bsearch(listm,element):
          Lo =0
          Hi = len(listm)
          while Lo < Hi:
                  mid = (Lo+Hi)/2          #Have to find the midpoint first
                  midvalue = listm[mid]
                  if midvalue < element:       #if the value is less than the wanted value the function will search higher along the list
                      Lo = mid + 1
                  elif midvalue > element:     #if the value is greater than the wanted value the function will search lower along the list.
                      Hi = mid
                  elif midvalue == element:
                      return mid   #Once mid equals the wanted value the function will return it.
                  else:
                      return -1


a = [1,3,2,4,6,7,8,9]

print bsearch(a,4)
