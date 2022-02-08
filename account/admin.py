from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(Teacher)


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'first_name',  'last_name',)
    list_filter = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    # list_display = ('email', 'username', 'first_name',  'last_name',
    #                 'is_active', 'is_staff')
    # fieldsets = (
    #     (None, {'fields': ('email', 'username', 'first_name', 'last_name',)}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    #
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
    #      ),
    # )
    def get_fieldsets(self, request, obj=None):
         if not obj:
             return self.add_fieldsets

         if request.user.is_superuser:
             perm_fields = ('is_active', 'is_staff', 'is_superuser',
                            'groups', 'user_permissions')
         else:
             # modify these to suit the fields you want your
             # staff user to be able to edit
             perm_fields = ('is_active', 'is_staff')

         return [(None, {'fields': ('username', 'password')}),
                 (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                 (('Permissions'), {'fields': perm_fields}),
                 (('Important dates'), {'fields': ('last_login', 'date_joined')})]

admin.site.unregister(User)
admin.site.register(User, UserAdminConfig)
admin.site.register(Dept)
admin.site.register(Batch)
admin.site.register(Semester)
admin.site.register(Staff)
