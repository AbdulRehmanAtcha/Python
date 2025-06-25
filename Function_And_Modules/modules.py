# Two types of modules
# 1. Built in modules
# 2. External modules ====>>> We have to install like pip
import math
import mymodule
import requests

print(int(math.sqrt(4)))
mymodule.Hello()

# External Module
res = requests.get("https://www.facebook.com/")
print(res.text)
