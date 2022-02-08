from django.contrib import admin

from .models import *

# Register your models here.
class ReviewDetailsAdmin(admin.ModelAdmin):
    readonly_fields = ('review', 'usergiven', 'totalpoint', 'avg')
class ReviewAdmin(admin.ModelAdmin):
    exclude = ('user','point','reviewfor','question')

admin.site.register(Subject)
admin.site.register(SemesterSubject)
admin.site.register(Question)
admin.site.register(ReviewSet)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewDetails, ReviewDetailsAdmin)
