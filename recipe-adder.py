# Prompts me to allow me to enter in recipes more efficiently (auto encodes into json format).
import json
with open("recipesl18.json", "w") as file: # I just changed the name to put it into each file.
    file.write("[\n")
    elements = 0
    while True:
        products = input("List products here (\"(), (), (), ...): ")
        if products == "END": break
        reactants = input("List reactants here (\"(), (), (), ...): ")
        factory = input("Enter factory here: ")
        reactantslist = reactants.split(", ")
        productslist = products.split(", ")
        if elements > 0: file.write(",\n")
        for productindex in range(len(productslist)): 
            file.write("    ")
            json.dump({factory : {"Inputs" : reactantslist, "Output" : productslist[productindex]}}, file)
            if productindex < len(productslist) - 1: file.write(",\n")
            elements += 1
        print("Complete!\n")
    print("Ending...")
    file.write("\n]")
    file.close()