from django.contrib import admin
from .models import MyUsers
from .models import MyUsersInfo
from .models import MyRecords

admin.site.register(MyUsers)
admin.site.register(MyUsersInfo)
admin.site.register(MyRecords)

