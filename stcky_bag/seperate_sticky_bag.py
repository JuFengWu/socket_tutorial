testString = ['look#','look#lo','ok#','l','oo','k#','look#look#']

lastString = ''

sortString = []

def get_string(inputString):
  global lastString
  global sortString
  finalString = lastString + inputString
  if finalString.find('#')!=-1:
    allOutput = finalString.split('#')
    print(allOutput)
    for i in range(len(allOutput)-1):
      sortString.append(allOutput[i])
    lastString = allOutput[len(allOutput)-1]
  else:
    print("put it into lastString")
    lastString = finalString

for t in testString:

  get_string(t)

print("ready to print sorting string")
for s in sortString:
  print(s)
  
  
