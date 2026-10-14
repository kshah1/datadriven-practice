def forward_fill(values: list) -> list:
  i = 1
  
  while i < len(values):
    if values[0] == None:
      pass
    if values[i] == None:
      values[i] = values[i - 1]
    
    i += 1
    
  return values
  
