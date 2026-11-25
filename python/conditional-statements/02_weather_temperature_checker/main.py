temperature = 3
weather = "unset"

if temperature < 0:
  weather = "Freezing"
elif 0 <= temperature <= 15:
  weather = "Cold"
elif 16 <= temperature <=25:
  weather = "Mild"
else :
  weather = "Hot"

