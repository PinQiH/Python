from tastypie.resources import ModelResource
from .models import Music

class MusicResource(ModelResource):
    class Meta:
        queryset = Music.objects.all()
        resource_name = 'music'
        fields = ['name', 'artist']  #設定顯示欄位
        allowed_methods = ['get']

music_resource = MusicResource()  #建立API資源