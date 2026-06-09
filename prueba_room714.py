import os
import requests
from pymongo import MongoClient, UpdateOne
from datetime import datetime
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

# GENERAL CONFIG.


MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_URI = os.getenv("MONGO_URI")

DB_NAME = "recipes_db"
COLLECTION_NAME = "recipes"

API_URL = "https://www.themealdb.com/api/json/v1/1/search.php"


# MONGO DB SETUP


client = MongoClient(MONGO_URI)

db = client[DB_NAME]
recipes_collection = db[COLLECTION_NAME]

recipes_collection.create_index("meal_id", unique=True)



# Data clean up, and better structuring of ingredients and tags.
def extract_ingredients(meal: dict) -> list:

    ingredients = []

    for i in range(1, 21):
        ingredient = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")

        if ingredient and ingredient.strip():
            ingredients.append({
                "name": ingredient.strip().lower(),
                "measure": (measure or "").strip()
            })

    return ingredients


def extract_tags(tags_value):

    if not tags_value:
        return []

    return [
        tag.strip()
        for tag in tags_value.split(",")
        if tag.strip()
    ]

# Data cleanup.
def transform_meal(meal: dict) -> dict:


    return {
        "meal_id": meal["idMeal"],
        "name": meal["strMeal"],
        "category": meal.get("strCategory"),
        "area": meal.get("strArea"),
        "instructions": meal.get("strInstructions"),
        "thumbnail": meal.get("strMealThumb"),
        "youtube": meal.get("strYoutube"),
        "source": meal.get("strSource"),
        "tags": extract_tags(meal.get("strTags")),
        "ingredients": extract_ingredients(meal),
        "created_at": datetime.utcnow()
    }


# We consult the API.
def search_recipe(recipe_name: str):

    try:
        response = requests.get(
            API_URL,
            params={"s": recipe_name},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("meals")

    except requests.RequestException as e:
        print(f"Error consultando '{recipe_name}': {e}")
        return None



# We save on the DB
def save_recipes(recipes):

    if not recipes:
        return

    operations = []

    for recipe in recipes:
        operations.append(
            UpdateOne(
                {"meal_id": recipe["meal_id"]},
                {"$set": recipe},
                upsert=True
            )
        )

    if operations:
        result = recipes_collection.bulk_write(operations)

        print(
            f"Insertados: {result.upserted_count} | "
            f"Actualizados: {result.modified_count}"
        )


# we read the text file and extract the names.
def load_recipe_names(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]



def main():

    recipe_names = load_recipe_names("recipes.txt")

    total_recipes = 0

    for recipe_name in recipe_names:

        print(f"Buscando: {recipe_name}")

        meals = search_recipe(recipe_name)

        if not meals:
            print(f"No se encontraron recetas para '{recipe_name}'")
            continue

        transformed = [
            transform_meal(meal)
            for meal in meals
        ]

        save_recipes(transformed)

        total_recipes += len(transformed)

    print(f"\nProceso finalizado.")
    print(f"Recetas procesadas: {total_recipes}")


if __name__ == "__main__":
    main()