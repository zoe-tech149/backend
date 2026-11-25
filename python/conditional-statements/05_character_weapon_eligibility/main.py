level = -1
has_training = True
level_message = "None"

if 1 <= level <= 5:
  level_message = "Basic weapons only"
if 6 <= level <= 10:
  if has_training:
    level_message = "Access to advanced weapons granted"
  else:
    level_message = "Need weapon training first"
if level >= 11:
   level_message = "Access to all weapons granted"
if level <= 0:
  level_message = "Invalid level"

print(level_message)