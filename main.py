from typing import TypedDict
import spoonacular as sp

# API key
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
    # request response for 'recipe_name' from the API
    response = api.guess_nutrition_by_dish_name(recipe_name)
    # translating from json
    data = response.json()
    return data


# getting the name of the recipe / ex: Spaghetti Aglio et Olio
recipe_check = get_nutrition_from_spoonacular(
    input("What's the name of the recipe you want to get the nutritional information of?" + '\n'))
print(recipe_check)
