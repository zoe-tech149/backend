wind = 5
status = "unset"

if wind < 8:
  status = "Calm"
elif 8 <= wind <= 31:
  status = "Breeze"
elif 32 <= wind <= 63:
  status = "Gale"
else :
  status = "Storm"