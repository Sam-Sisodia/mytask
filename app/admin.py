 
 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

from .forms import *



admin.site.register(User)

# class UserAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Myuser
#         fields ="__all__"

# admin.site.register(Myuser)


# class CustomUserAdmin(UserAdmin):
#    add_form = UserCreationForm
 
  
#    list_display = ('email', )
#    list_filter = ('',)
#    fieldsets = (
#        (None, {'fields': ('email', 'password')}),
#        ('Permissions', {'fields': ('',)}),
#    )
#    add_fieldsets = (
#        (None, {
#            'classes': ('wide',),
#            'fields': ('email','password1', 'password2'),
#        }),
#    )
#    ordering = ('email',)
#    filter_horizontal = ()
 
 
# # Now register the new UserAdmin...
# admin.site.register(Myuser, CustomUserAdmin)

 
