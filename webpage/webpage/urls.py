# """webpage URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin

from django.urls import path

from webapp import views

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('college/',views.college,name="college"),

    path('college/<pk>',views.college,name="college"),

    path('facility/<pk>',views.facility,name="facility"),

    path('facility/<pk>',views.facility,name="facility"),

    path('admission/<pk>',views.Admission_view,name="admission"),

	path('admission/<pk>',views.Admission_view,name="admission"),

    path('approval/<pk>',views.approval,name="approval"),


    # path('alumini/',views.Alumini,name="alumini"),
]
