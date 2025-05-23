
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include, reverse_lazy
from django.views.generic import CreateView


auth_patterns = [
    path('', include('django.contrib.auth.urls')),
    path(
        'registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('products:index'),
        ),
        name='registration',
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(auth_patterns)),
    path('', include('products.urls', namespace='products')),
]
