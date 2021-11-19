from fuzzywuzzy import process
str2Match = "please turn on the light"
str2Match = "άναψε το φως"
str2Match = input('write a sentence: ')
strOptions = ["turn light on","lock door","unlock door","άνοιξε το φως"]
Ratios = process.extract(str2Match,strOptions)
print(Ratios)
# You can also select the string with the highest matching percentage
highest = process.extractOne(str2Match,strOptions)
print(highest)

