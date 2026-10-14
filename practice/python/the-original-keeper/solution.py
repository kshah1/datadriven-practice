def dedup_preserve_order(items: list) -> list:
  seen = set()
  result = []
  
  for val in items:
    if val not in seen:
      result.append(val)
      seen.add(val)
    else:
      pass
    
  return result
      
  
