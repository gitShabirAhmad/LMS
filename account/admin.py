from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account,Junc
# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ['id','email','image','address']
    ordering = ["email"]
    list_filter = ['id']

    # fieldsets to display the admin details
    fieldsets = (
        ("Auth", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ('name','image','address','date_of_birth')}),
        (
            ("Permissions"),
            {
                "fields": (
                    # "is_active",
                    # "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates",
         {"fields": ["last_login"]}),
    )


    # add_fieldsets to add user
    add_fieldsets = (
        (
            "Add User",
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2",'address','date_of_birth'),
            },
        ),
    )

    # Linkable some fields
    list_display_links = ['email','id','address']

admin.site.register(Account,AccountAdmin)
admin.site.register(Junc)