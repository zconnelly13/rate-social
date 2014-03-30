from django.http import HttpResponse
from database.models import User, Rating
from json import dumps

def add_user(request):
    name = request.GET.get('name',None)
    profile_picture = request.GET.get('profile_picture_url',None)
    if name is not None and profile_picture is not None:
        user = User()
        user.name = name
        user.profile_picture = profile_picture
        user.rating = 5
        user.save()
        return HttpResponse('woot!')
    else:
        return HttpResponse('awh :( something went wrong') 

def add_rating(request):
    rater_id = request.GET.get('rater')
    ratee_id = request.GET.get('ratee')
    comment = request.GET.get('comment')
    number = request.GET.get('number')
    rater = User.objects.filter(id=rater_id)[0]
    ratee = User.objects.filter(id=ratee_id)[0]
    rating = Rating()
    rating.rater = rater
    rating.ratee = ratee
    rating.comment = comment
    rating.number = number
    rating.save()
    return HttpResponse("yay! success!")
