from .models import Album ,song
from django.shortcuts import render,get_object_or_404

def index(request):
    all_albums=Album.objects.all()

    context={

        "all_albums": all_albums,
    }


    return render(request,'music/index.html',context)


def detail(request ,album_id):
    album= get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{"album": album})

def favorite (request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError , song.DoesNotExist):
        return render(request, 'music/detail.html', {"album": album , 'error_message' : "Error message appered"})

    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/detail.html',{'album' : album})