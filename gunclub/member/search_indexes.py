from haystack import site
from haystack.indexes import *
from member.models import Profile

class ProfileIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    first_name = CharField()
    last_name = CharField()
    rg = CharField()
    cpf = CharField()
    member_id = IntegerField(model_attr='id')

    def index_queryset(self):
        return Profile.objects.order_by('user__first_name')

site.register(Profile, ProfileIndex)
