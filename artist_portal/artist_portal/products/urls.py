from django.urls import path, include
from .views import fashion_photography,Classical_music,Folk_music,Instrumental_music,Bollywood_music,Sonnets_poetry,Rhymed_poetry,Narrative_poetry,Lyrics_poetry,Classical_dance,Contemporary_dance,Folk_dance,Pencil_sketch_painting,acrylic_painting,spray_painting,Hip_hop_dance,wedding_photography,events_photography,business_photography,productcreate,products_list,singleproduct,update_product,delete_product,my_products,search,ratings,pastel_painting

app_name = 'Products'

urlpatterns = [
	path('shop/',products_list,name='shop'),
	path('productcreate/',productcreate,name='productcreate'),
	path('singleproduct/<int:pk>/',singleproduct,name='singleproduct'),
	path('update_product/<int:pk>/', update_product, name='update_product'),
	path('delete_product/<int:pk>/', delete_product, name='delete_product'),
	path('my_products/',my_products,name='my_products'),
	path('search/',search,name='search'),
	path('cart/',include('cart.urls')),
	path('business_photography/',business_photography,name='business_photography'),
	path('events_photography/',events_photography,name='events_photography'),
	path('wedding_photography/',wedding_photography,name='wedding_photography'),
	path('fashion_photography/',fashion_photography,name='fashion_photography'),
	path('pastel_painting/',pastel_painting,name='pastel_painting'),
	path('spray_painting/',spray_painting,name='spray_painting'),
	path('acrylic_painting/',acrylic_painting,name='acrylic_painting'),
	path('Pencil_sketch_painting/',Pencil_sketch_painting,name='Pencil_sketch_painting'),
	path('Hip_hop_dance/',Hip_hop_dance,name='Hip_hop_dance'),
	path('Folk_dance/',Folk_dance,name='Folk_dance'),
	path('Contemporary_dance/',Contemporary_dance,name='Contemporary_dance'),
	path('Classical_dance/',Classical_dance,name='Classical_dance'),
	path('Lyrics_poetry/',Lyrics_poetry,name='Lyrics_poetry'),
	path('Narrative_poetry/',Narrative_poetry,name='Narrative_poetry'),
	path('Rhymed_poetry/',Rhymed_poetry,name='Rhymed_poetry'),
	path('Sonnets_poetry/',Sonnets_poetry,name='Sonnets_poetry'),
	path('Bollywood_music/',Bollywood_music,name='Bollywood_music'),
	path('Instrumental_music/',Instrumental_music,name='Instrumental_music'),
	path('Folk_music/',Folk_music,name='Folk_music'),
	path('Classical_music/',Classical_music,name='Classical_music'),
	path('ratings/<int:pk>/',ratings,name='ratings'),
]