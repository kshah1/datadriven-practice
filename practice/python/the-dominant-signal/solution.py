def most_frequent(items: list) -> list:
  maxCount = {}
  
  for item in items:
    maxCount[item] = maxCount.get(item, 0) + 1
    
    
  maxValue = 0
  
  for v in maxCount.values():
    if v > maxValue:
      maxValue = v
  
  result = []
  for k, v in maxCount.items():
    if v == maxValue:
      result.append(k)

  return sorted(result)
