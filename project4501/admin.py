from django.contrib import admin

from .models import Course, User, Review, Session, Application, Message
# from .models import Course, User, Review, AdditionInfo, Session, Application, Message

admin.site.register(Course)
admin.site.register(User)
admin.site.register(Review)
# admin.site.register(AdditionInfo)
admin.site.register(Session)
admin.site.register(Application)
admin.site.register(Message)


