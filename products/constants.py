

DATABASE = {
    'users': [],
    'categories': [
        {
            'id': 1,
            'name': 'Vegetables',
            'description': 'Fresh and organic vegetables',
        },
        {
            'id': 2,
            'name': 'Fruits',
            'description': 'Sweet and juicy fruits',
        },
        {
            'id': 3,
            'name': 'Herbs',
            'description': 'Aromatic and flavorful herbs',
        },
        {
            'id': 4,
            'name': 'Flowers',
            'description': 'Beautiful and colorful flowers',
        },
        {
            'id': 5,
            'name': 'Seeds',
            'description': 'High-quality seeds for planting',
        },
    ],
    'tags': [
        {
            'id': 1,
            'name': 'Organic',
            'description': 'Products grown without synthetic fertilizers or pesticides',
        },
        {
            'id': 2,
            'name': 'Non-GMO',
            'description': 'Products that are not genetically modified',
        },
        {
            'id': 3,
            'name': 'Local',
            'description': 'Products sourced from local farms and producers',
        },
        {
            'id': 4,
            'name': 'Sustainable',
            'description': 'Products produced in an environmentally friendly manner',
        },
        {
            'id': 5,
            'name': 'Seasonal',
            'description': 'Products that are in season and freshly harvested',
        }
    ],
    'products': [
        {
            'id': 1,
            'name': 'Tomato',
            'description': 'Fresh and juicy tomatoes',
            'category_id': 1,
            'tags': [1, 3],
            'price': 2.5,
            'time_to_grow': 60,
        },
        {
            'id': 2,
            'name': 'Apple',
            'description': 'Crisp and sweet apples',
            'category_id': 2,
            'tags': [1, 4],
            'price': 3.0,
            'time_to_grow': 90,
        },
        {
            'id': 3,
            'name': 'Basil',
            'description': 'Aromatic basil leaves',
            'category_id': 3,
            'tags': [2, 5],
            'price': 1.5,
            'time_to_grow': 30,
        },
        {
            'id': 4,
            'name': 'Rose',
            'description': 'Beautiful red roses',
            'category_id': 4,
            'tags': [3, 4],
            'price': 5.0,
            'time_to_grow': 45,
        },
        {
            'id': 5,
            'name': 'Carrot',
            'description': 'Crunchy and sweet carrots',
            'category_id': 1,
            'tags': [1, 2],
            'price': 1.0,
            'time_to_grow': 75,
        },
        {
            'id': 6,
            'name': 'Sunflower Seeds',
            'description': 'High-quality sunflower seeds for planting',
            'category_id': 5,
            'tags': [2, 5],
            'price': 0.5,
            'time_to_grow': 120,
        },
        {
            'id': 7,
            'name': 'Cilantro',
            'description': 'Fresh cilantro leaves',
            'category_id': 3,
            'tags': [1, 3],
            'price': 1.2,
            'time_to_grow': 40,
        },
        {
            'id': 8,
            'name': 'Tulip',
            'description': 'Colorful tulip flowers',
            'category_id': 4,
            'tags': [4, 5],
            'price': 4.0,
            'time_to_grow': 60,
        },
    ],
    'greenhouses': [
        {
            'id': 1,
            'name': 'Greenhouse A',
            'location': 'Location A',
            'capacity': 1000,
        },
        {
            'id': 2,
            'name': 'Greenhouse B',
            'location': 'Location B',
            'capacity': 2000,
        },
        {
            'id': 3,
            'name': 'Greenhouse C',
            'location': 'Location C',
            'capacity': 1500,
        },
    ],
}