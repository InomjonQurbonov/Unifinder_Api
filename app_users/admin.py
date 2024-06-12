from django.contrib import admin
from app_users.models import User, Gender, PasswordResets, Author, Paper

admin.site.register(User)
admin.site.register(Gender)
admin.site.register(PasswordResets)
admin.site.register(Author)
admin.site.register(Paper)
