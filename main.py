with open('test.txt','r') as f:
  lines = f.readlines()
  lines = [l.strip().split(' ') for l in lines]

nCases = int(lines.pop(0)[0])
for i in range(nCases):
  case = lines.pop(0)
  dependency = {}
  for j in range(int(case[0])):
    p = lines.pop(0)
    dependency[p[1]]=p[0]
  delays = lines.pop(0)
  for delay in delays:
    if delay in dependency:
      delays.append(dependency.get(delay))
  print("Case #{}: {}".format(i, sorted(set(delays))))
