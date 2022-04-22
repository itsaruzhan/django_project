from django.contrib import admin
from .models import  Clothes, Customs,  Home, Questions
from .models import Profile

admin.site.register(Profile)
admin.site.register(Clothes)
admin.site.register(Customs)
admin.site.register(Home)
admin.site.register(Questions)


