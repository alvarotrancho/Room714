## Descripción

Este proyecto implementa un sistema de ingesta y transformación de recetas basado en la API de TheMealDB.  
El objetivo es preparar los datos para su uso posterior en sistemas de recomendación y modelos de IA.

El sistema:
- Lee una lista de recetas desde un fichero `.txt`
- Consulta la API de TheMealDB
- Normaliza y transforma los datos
- Los almacena en MongoDB


## Stack tecnológico

- Python
- MongoDB 
- PyMongo

## Modelo de datos

Cada receta almacenada en MongoDB sigue esta estructura:

{
  _id: ObjectId('6a27bc250b9eb8a3eecc0c82'),
  meal_id: '52771',
  area: 'Italian',
  category: 'Vegetarian',
  created_at: ISODate('2026-06-09T07:12:59.315Z'),
  ingredients: [
    {
      name: 'penne rigate',
      measure: '1 pound'
    },
    {
      name: 'olive oil',
      measure: '1/4 cup'
    },
    {
      name: 'garlic',
      measure: '3 cloves'
    },
    {
      name: 'chopped tomatoes',
      measure: '1 tin'
    },
    {
      name: 'red chilli flakes',
      measure: '1/2 teaspoon'
    },
    {
      name: 'italian seasoning',
      measure: '1/2 teaspoon'
    },
    {
      name: 'basil',
      measure: '6 leaves'
    },
    {
      name: 'parmigiano-reggiano',
      measure: 'sprinkling'
    }
  ],
  instructions: 'Bring a large pot of water to a boil. Add kosher salt to the boiling water, then add the pasta. Cook according to the package instructions, about 9 minutes.\r\nIn a large skillet over medium-high heat, add the olive oil and heat until the oil starts to shimmer. Add the garlic and cook, stirring, until fragrant, 1 to 2 minutes. Add the chopped tomatoes, red chile flakes, Italian seasoning and salt and pepper to taste. Bring to a boil and cook for 5 minutes. Remove from the heat and add the chopped basil.\r\nDrain the pasta and add it to the sauce. Garnish with Parmigiano-Reggiano flakes and more basil and serve warm.',
  name: 'Spicy Arrabiata Penne',
  source: null,
  tags: [
    'Pasta',
    'Curry'
  ],
  thumbnail: 'https://www.themealdb.com/images/media/meals/ustsqw1468250014.jpg',
  youtube: 'https://www.youtube.com/watch?v=1IszT_guI08'
}

De esta forma los datos podrán ser procesados de forma eficiente a través de llamadas a la base de datos o si se desea se puede crear una API REST para tener mejor escalabilidad.

## Futuras Mejoras

Una de las mejoras más obvias sería refactorizar el código para que sea más facil de mantener, ya que teniendo todas las funciones en un solo fichero suele ser mala idea cuando el proyecto crezca. Se podría tener 3 ficheros
adicionales uno para manejar la lógica de la base de datos , otro para realizar las llamadas a la API y por último un fichero para procesar los datos antes de guardarlo.

Otra mejora sería realizar una API REST para mejorar la escabilidad de los datos y puedan ser usados por varios proyecto sin incluir la lógica de base de datos en cada uno de ellos.
