class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"


class Recipe:
    def __init__(self, name, category, ingredients, instructions):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"{self.name} - {self.category}"

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_instruction(self, instruction):
        self.instructions.append(instruction)


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def find_recipe_by_name(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                return recipe
        return None

    def find_recipes_by_category(self, category):
        matching_recipes = []
        for recipe in self.recipes:
            if recipe.category.lower() == category.lower():
                matching_recipes.append(recipe)
        return matching_recipes

    def __str__(self):
        return "\n".join(str(recipe) for recipe in self.recipes)


# Example usage: (Unchanged)
ingredient1 = Ingredient("Chicken", 500, "g")
ingredient2 = Ingredient("Tomatoes", 2, "pcs")
ingredient3 = Ingredient("Onion", 1, "pc")

recipe1 = Recipe("Chicken Curry", "Main Course", [ingredient1, ingredient2, ingredient3], [])
recipe1.add_instruction("1. Heat oil in a pan.")
recipe1.add_instruction("2. Add onions and tomatoes.")
recipe1.add_instruction("3. Add chicken and cook until done.")
recipe1.add_instruction("4. Serve hot with rice.")

recipe2 = Recipe("Chocolate Brownies", "Dessert", [Ingredient("Chocolate", 200, "g"), Ingredient("Butter", 100, "g"), Ingredient("Sugar", 150, "g")], [])
recipe2.add_instruction("1. Melt chocolate and butter together.")
recipe2.add_instruction("2. Mix in sugar and eggs.")
recipe2.add_instruction("3. Add flour and baking powder.")
recipe2.add_instruction("4. Bake in preheated oven at 180°C for 25 minutes.")

recipe_book = RecipeBook()
recipe_book.add_recipe(recipe1)
recipe_book.add_recipe(recipe2)

print(recipe_book.find_recipe_by_name("Chicken Curry"))

dessert_recipes = recipe_book.find_recipes_by_category("Dessert")
for recipe in dessert_recipes:
    print(recipe)