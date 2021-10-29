from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('recipe_upload/<int:id>', views.recipe, name='recipe_upload'),
    path('', views.home,name='home'),
    path('recipe/<int:id>', views.recipe, name='recipe'),
    path('upload/<int:id>', views.upload, name='upload'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)