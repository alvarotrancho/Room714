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

```json
{
  _id: ObjectId('6a27bc260b9eb8a3eecc0c83'),
  meal_id: '52795',
  area: 'India',
  category: 'Chicken',
  created_at: ISODate('2026-06-09T07:12:59.868Z'),
  ingredients: [
    {
      name: 'chicken',
      measure: '1.2 kg'
    },
    {
      name: 'onion',
      measure: '5 thinly sliced'
    },
    {
      name: 'tomatoes',
      measure: '2 finely chopped'
    },
    {
      name: 'garlic',
      measure: '8 cloves chopped'
    },
    {
      name: 'ginger paste',
      measure: '1 tbsp'
    },
    {
      name: 'vegetable oil',
      measure: '¼ cup'
    },
    {
      name: 'cumin seeds',
      measure: '2 tsp'
    },
    {
      name: 'coriander seeds',
      measure: '3 tsp'
    },
    {
      name: 'turmeric powder',
      measure: '1 tsp'
    },
    {
      name: 'chilli powder',
      measure: '1 tsp'
    },
    {
      name: 'green chilli',
      measure: '2'
    },
    {
      name: 'yogurt',
      measure: '1 cup'
    },
    {
      name: 'cream',
      measure: '¾ cup'
    },
    {
      name: 'fenugreek',
      measure: '3 tsp Dried'
    },
    {
      name: 'garam masala',
      measure: '1 tsp'
    },
    {
      name: 'salt',
      measure: 'To taste'
    }
  ],
  instructions: 'Take a large pot or wok, big enough to cook all the chicken, and heat the oil in it. Once the oil is hot, add sliced onion and fry them until deep golden brown. Then take them out on a plate and set aside.\r\nTo the same pot, add the chopped garlic and sauté for a minute. Then add the chopped tomatoes and cook until tomatoes turn soft. This would take about 5 minutes.\r\nThen return the fried onion to the pot and stir. Add ginger paste and sauté well.\r\nNow add the cumin seeds, half of the coriander seeds and chopped green chillies. Give them a quick stir.\r\nNext goes in the spices – turmeric powder and red chilli powder. Sauté the spices well for couple of minutes.\r\nAdd the chicken pieces to the wok, season it with salt to taste and cook the chicken covered on medium-low heat until the chicken is almost cooked through. This would take about 15 minutes. Slowly sautéing the chicken will enhance the flavor, so do not expedite this step by putting it on high heat.\r\nWhen the oil separates from the spices, add the beaten yogurt keeping the heat on lowest so that the yogurt doesn’t split. Sprinkle the remaining coriander seeds and add half of the dried fenugreek leaves. Mix well.\r\nFinally add the cream and give a final mix to combine everything well.\r\nSprinkle the remaining kasuri methi and garam masala and serve the chicken handi hot with naan or rotis. Enjoy!',
  name: 'Chicken Handi',
  source: '',
  tags: [],
  thumbnail: 'https://www.themealdb.com/images/media/meals/wyxwsp1486979827.jpg',
  youtube: 'https://www.youtube.com/watch?v=IO0issT0Rmc'
}
```

De esta forma los datos podrán ser procesados de forma eficiente a través de llamadas a la base de datos o si se desea se puede crear una API REST para tener mejor escalabilidad.

## Futuras Mejoras

Una de las mejoras más obvias sería refactorizar el código para que sea más facil de mantener, ya que teniendo todas las funciones en un solo fichero suele ser mala idea cuando el proyecto crezca. Se podría tener 3 ficheros
adicionales uno para manejar la lógica de la base de datos , otro para realizar las llamadas a la API y por último un fichero para procesar los datos antes de guardarlo.

Otra mejora sería realizar una API REST para mejorar la escabilidad de los datos y puedan ser usados por varios proyecto sin incluir la lógica de base de datos en cada uno de ellos.
