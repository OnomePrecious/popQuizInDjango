from django.contrib import admin

import popQuiz


# Register your models here.
@admin.register(popQuiz)
class Admin(admin.ModelAdmin):
    list_display = ['admin_id', 'first_name', 'last_name', 'password', 'email']
    list_per_page = 10
    list_editable = ['first_name', 'last_name', 'account_type']
