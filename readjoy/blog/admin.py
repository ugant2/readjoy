
import csv
from django.contrib import admin
from django.http import HttpResponse

from blog.models import Post, Comment, Profile

class ExportCSVMixin:
    def export_to_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition']  ='attachment: filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_to_csv.short_description = "Export to CSV"


class PostAdmin(admin.ModelAdmin, ExportCSVMixin):
    list_display = ['title', 'author', 'created', 'status']
    search_fields = ['title', 'body']
    list_filter = ['created', 'status']
    change_list_template = 'blog/change_list.html'
    actions = ['export_to_csv', 'abc']

    def abc(self, request, queryset):
        pass
    abc.short_description = "This is ABC metgod"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post_id', 'email']
    actions = ['export_to_csv']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'image']
    actions = ['export_to_csv']



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
