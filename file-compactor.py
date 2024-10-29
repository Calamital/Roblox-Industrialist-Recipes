# Combines all eighteen files into RECIPES.json.
import json
row1 = row2 = row3 = row4 = row5 = row6 = row7 = row8 = row9 = row10 = row11 = row12 = row13 = row14 = row15 = row16 = row17 = row18 = None
totallist = []
with open("source\\rows\\recipesl1.json", "r") as file: row1 = json.load(file)
with open("source\\rows\\recipesl2.json", "r") as file: row2 = json.load(file)
with open("source\\rows\\recipesl3.json", "r") as file: row3 = json.load(file)
with open("source\\rows\\recipesl4.json", "r") as file: row4 = json.load(file)
with open("source\\rows\\recipesl5.json", "r") as file: row5 = json.load(file)
with open("source\\rows\\recipesl6.json", "r") as file: row6 = json.load(file)
with open("source\\rows\\recipesl7.json", "r") as file: row7 = json.load(file)
with open("source\\rows\\recipesl8.json", "r") as file: row8 = json.load(file)
with open("source\\rows\\recipesl9.json", "r") as file: row9 = json.load(file)
with open("source\\rows\\recipesl10.json", "r") as file: row10 = json.load(file)
with open("source\\rows\\recipesl11.json", "r") as file: row11 = json.load(file)
with open("source\\rows\\recipesl12.json", "r") as file: row12 = json.load(file)
with open("source\\rows\\recipesl13.json", "r") as file: row13 = json.load(file)
with open("source\\rows\\recipesl14.json", "r") as file: row14 = json.load(file)
with open("source\\rows\\recipesl15.json", "r") as file: row15 = json.load(file)
with open("source\\rows\\recipesl16.json", "r") as file: row16 = json.load(file)
with open("source\\rows\\recipesl17.json", "r") as file: row17 = json.load(file)
with open("source\\rows\\recipesl18.json", "r") as file: row18 = json.load(file)
filelist = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15, row16, row17, row18]
with open("RECIPES.json", "w") as recipefile:
    recipefile.write("[\n   ")
    for file in filelist:
        for recipe in file:
            if recipe in totallist:
                continue
            else:
                totallist.append(recipe)
                json.dump(recipe, recipefile)
                recipefile.write(",\n   ")
    recipefile.write("\n]")