from django.contrib import admin
from .models import MyUsers
from .models import MyUsersInfo
from .models import MyRecords
from .models import MyTheme
from .models import MyComments

admin.site.register(MyUsers)
admin.site.register(MyUsersInfo)
admin.site.register(MyRecords)
admin.site.register(MyTheme)
admin.site.register(MyComments)
