from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyTicket, MyUser
from .forms import MyUserCreationForm, MyUserChangeForm

# Register your models here.

admin.site.register(MyTicket)

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'age', ]
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('age', 'password', 'display_name,')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    
admin.site.register(MyUser, MyUserAdmin)