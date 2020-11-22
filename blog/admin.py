from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Post_rimc
from .models import Post_ssb



admin.site.register(Post)
admin.site.register(Post_rimc)
admin.site.register(Post_ssb)