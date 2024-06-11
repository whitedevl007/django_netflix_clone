from django.contrib import admin
from netflix_app.models import Movie, video, Profile,CustomUser


admin.site.register(Movie)
admin.site.register(video)
admin.site.register(Profile)
admin.site.register(CustomUser)