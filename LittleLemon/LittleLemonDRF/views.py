from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']

"""
el serializador es el encargado de transformar los datos de la base de datos a un formato que pueda ser interpretado por el cliente
y viceversa, es decir, transformar los datos que el cliente envía al servidor a un formato que pueda ser interpretado por la base de datos.

que se debe de importar en el serializado? 
Se debe de importar los modelos que se van a serializar, en este caso, Category y MenuItem y para que la serializacion ocurra se debe importar el paquete serializers de django rest framework

como se debe de crear las clases para serializar los modelos?

Se debe de crear una clase por cada modelo que se va a serializar, en este caso, se debe de crear una clase CategorySerializer y una clase MenuItemSerializer, estas clases deben de heredar de la clase ModelSerializer que se importa del paquete serializers de django rest framework

dentro de la clase CategorySerializer se debe de crear una clase Meta que herede de la clase Meta y se debe de definir el modelo que se va a serializar, en este caso, el modelo es Category, ademas se debe de definir los campos que se van a serializar, en este caso, se van a serializar todos los campos del modelo Category. Se debe de hacer lo mismo para la clase MenuItemSerializer

ademas este contendra un campo extra que es el campo category que es una instancia de la clase CategorySerializer, esto se hace para que cuando se serialice un MenuItem, se serialice tambien la categoria a la que pertenece el MenuItem

el archivo models.py quedaria de la siguiente manera:

se importa el paquete models de django

se ingresan las clases Category y MenuItem

Category tiene dos campos, slug y title, slug es un campo de tipo SlugField y title es un campo de tipo CharField. (El campo slugfield es un campo que se utiliza para almacenar cadenas de texto que contienen solo letras, numeros, guiones y guiones bajos, este campo es util para almacenar urls)

y MenuItem tiene cuatro campos, title, price, inventory y category, title es un campo de tipo SlugField, price es un campo de tipo CharField, inventory es un campo de tipo SmallIntegerField y category es un campo de tipo ForeignKey que hace referencia al modelo Category, ademas tiene un argumento on_delete que se le asigna el valor PROTECT, esto significa que si se intenta eliminar una categoria que tiene items asociados, no se podra eliminar la categoria, esto se hace para evitar que se eliminen categorias que tienen items asociados

en el archivo views.py se importa el paquete generics de rest_framework y los modelos MenuItem y Category del archivo models.py y los serializadores MenuItemSerializer y CategorySerializer del archivo serializers.py

el modulo generics se usa para crear vistas basadas en clases, en este caso se crean dos vistas basadas en clases, CategoriesView y MenuItemsView, CategoriesView es una vista que se encarga de listar y crear categorias y MenuItemsView es una vista que se encarga de listar y crear items de menu

en la vista CategoriesView se define el atributo queryset que contiene todas las categorias, el atributo serializer_class que contiene la clase CategorySerializer y en la vista MenuItemsView se define el atributo queryset que contiene todos los items de menu, el atributo serializer_class que contiene la clase MenuItemSerializer, el atributo ordering_fields que contiene una lista con los campos por los que se puede ordenar la lista de items de menu, el atributo filterset_fields que contiene una lista con los campos por los que se puede filtrar la lista de items de menu y el atributo search_fields que contiene una lista con los campos por los que se puede buscar en la lista de items de menu

REST_FRAMEWORK = {
    'DEFAULT_FILTER_CLASSES': [
        'rest_framework.filters.OrderingFilter', 
        'rest_framework.filters.SearchFilter'
        ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3
    
}

La variable REST_FRAMEWORK es un diccionario que contiene la configuracion de rest framework, en este caso, se configuran los filtros por defecto que se van a usar en las vistas basadas en clases, se configura la paginacion por defecto que se va a usar en las vistas basadas en clases y se configura el tamaño de pagina por defecto que se va a usar en las vistas basadas en clases

"""