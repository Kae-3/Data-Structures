
pasta_recipe = ("Pasta Arrabiata", "Italian", "20 mins", "Easy")
biryani_recipe = ("Chicken Biryani", "Indian", "45 mins", "Medium")

print("--- Step 2: Tuple Indexing & Slicing ---")
print("First item (positive indexing):", pasta_recipe[0])
print("Last item (negative indexing):", pasta_recipe[-1])

recipe_box = (pasta_recipe, biryani_recipe)
print("Cuisine of 2nd recipe (double indexing):", recipe_box[1][1])

print("Pasta details slice:", pasta_recipe[2:4])

print("\n--- Step 3: Loop Through Pasta Tuple ---")
for detail in pasta_recipe:
    print(detail)

print("\n--- Step 4: Ingredients Sets ---")
pasta_ingredients = {"pasta", "tomatoes", "garlic", "chilli", "olive oil", "garlic"}
biryani_ingredients = {"chicken", "basmati rice", "garlic", "ginger", "yogurt", "spices"}

print("Pasta ingredients (notice duplicate 'garlic' removed):", pasta_ingredients)

print("\n--- Step 5: Set Modifications ---")
pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("Updated pasta ingredients:", pasta_ingredients)

print("\n--- Step 6: Set Operations ---")
print("Union (All unique ingredients):", pasta_ingredients.union(biryani_ingredients))
print("Intersection (Common ingredients):", pasta_ingredients.intersection(biryani_ingredients))
print("Difference (In pasta, not biryani):", pasta_ingredients.difference(biryani_ingredients))
print("Symmetric Difference (In either, but not both):", pasta_ingredients.symmetric_difference(biryani_ingredients))