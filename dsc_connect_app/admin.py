from django.contrib import admin
from .models import Dsc, User

def make_published(modeladmin, request, queryset):
    queryset.update(status ='1')
make_published.short_description = "publish this!"

class DscAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    ordering = ['created_on']
    actions = [make_published]

    def get_actions(self, request):
        actions = super(DscAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            del actions[make_published]
        return actions
# Register your models here.
admin.site.register(Dsc,DscAdmin)
admin.site.register(User)



# Register your models here.
