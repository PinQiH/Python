from django.contrib import admin
from .models import Location, Post

# 景點位置
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# 貼文內容
class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content', 'author', 'location')
    #exclude = ('create_date', ) #不顯示該欄位
    #fields = ('subject', 'content', 'author', 'location') #設定顯示的欄位

admin.site.register(Location, LocationAdmin)  #註冊至Administration(管理員後台)
admin.site.register(Post, PostAdmin)  #註冊至Administration(管理員後台)