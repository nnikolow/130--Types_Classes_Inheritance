from typing import TypedDict
import spoonacular as sp

api = sp.API("7e8a32c703094062a6f7e0160fea0387")


class Range(TypedDict):
    min: float
    max: float


class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standartDeviation: float


class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation


def get_nutrition_from_spoonacular(recipe_name: str) -> RecipeNutritionInformation:
    response = api.guess_nutrition_by_dish_name(recipe_name)
    data = response.json()
    return data


spaghetti = get_nutrition_from_spoonacular("Spaghetti Aglio et Olio")
print(spaghetti)

# # Parse an ingredient
# response = api.visualize_recipe_nutrition("pasta", 2)
# data = response.json()
# print(data)
#
# response = api.get_a_random_food_joke()
# data = response.json()
# print(data['text'])
#
#
# rec1 = get_nutrition_from_spoonacular("mangusta")
# print(rec1)
#
# snack = RecipeNutritionInformation(recipes_used=2, calories=300, fat=50, protein=204, carbs=100)
# snack = get_nutrition_from_spoonacular("yasha")
# print(snack)
#
# snack1: RecipeNutritionInformation = dict(recipes_used=2, calories=300, fat=50)
# print(snack1)
#
# RecipeNutritionInformation.recipe
