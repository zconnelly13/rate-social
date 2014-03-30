from django.http import HttpResponse
from database.models import User, Rating
from json import dumps

def add_user(request):
    name = request.GET.get('name',None)
    profile_picture = request.GET.get('profile_picture_url',None)
    import ipdb;ipdb.set_trace();
    if name is not None and profile_picture is not None:
        user = User()
        user.name = name
        user.profile_picture = profile_picture
        user.save()
        context = {'success' : 'true'} 
        return get_json_response(context);
    else:
        context = {'success' : 'false','error':'please provide both a username and a profile picture url'}
        return get_json_response(context)

def add_rating(request):
    return HttpResponse("Hello! :)))")

def get_json_response(context):
    return HttpResponse(dumps(context))
