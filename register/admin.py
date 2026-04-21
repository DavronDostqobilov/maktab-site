from django.contrib import admin
from .models import User, Taklif, Image, FriendPhoto, StudentPhoto
 
@admin.register(FriendPhoto)
class FriendPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
@admin.register(StudentPhoto)
class FriendPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

# User modelini admin panelga qo'shamiz
admin.site.register(User)
admin.site.register(Taklif)

# Register your models here.
# Username: 
# thatistheusernameofmysitedonttrytoohackit
# email: narpay89@gmail.com
# password: agarsenparolnitopganbulsangteginma963