from django.contrib import admin
from .models import (TopicForum, MessageForum, SectionForum)

admin.site.register(SectionForum)
admin.site.register(TopicForum)
admin.site.register(MessageForum)
