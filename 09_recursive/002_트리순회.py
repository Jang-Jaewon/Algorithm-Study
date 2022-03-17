# 이진트리 순회

# 전위 순회
def solutuon(N, visited):
  if N > 7:
    return
  else:
    visited.append(N)
    solutuon(N*2, visited)
    solutuon(N*2+1, visited)
  return visited
visited = []    
print(solutuon(1, visited))

# 중위 순회
def solutuon(N, visited):
  if N > 7:
    return
  else:
    solutuon(N*2, visited)
    visited.append(N)
    solutuon(N*2+1, visited)
  return visited
visited = []    
print(solutuon(1, visited))

# 후위 순회
def solutuon(N, visited):
  if N > 7:
    return
  else:
    solutuon(N*2, visited)
    solutuon(N*2+1, visited)
    visited.append(N)
  return visited  
visited = []    
print(solutuon(1, visited))