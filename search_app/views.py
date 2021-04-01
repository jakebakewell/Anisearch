from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import requests
from .models import Anime
from login_reg_app.models import User
import bcrypt

def home(request):
    return render(request, 'home.html')

def process_search(request):
    try:
        errors = Anime.objects.url_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='url')
            return redirect('/anisearch/')
        else:
            img_url = request.POST['search_img_url']
            response = requests.get(f'https://trace.moe/api/search?url={img_url}').json()
            user = User.objects.get(id=request.session['userid'])
            print(response['docs'][0]['filename'])
            filename = response['docs'][0]['filename']
            tokenthumb = response['docs'][0]['tokenthumb']
            title_en = response['docs'][0]['title_english']
            title_jp = response['docs'][0]['title']
            at_time = response['docs'][0]['at']
            from_time = response['docs'][0]['from']
            to_time = response['docs'][0]['to']
            mal_id = response['docs'][0]['mal_id']
            anilist_id = response['docs'][0]['anilist_id']
            mal_link = f"https://myanimelist.net/anime/{mal_id}"
            anilist_link = f"https://anilist.co/anime/{anilist_id}"
            query = '''
            query ($id: Int) { # Define which variables will be used in the query (id)
            Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
                id
                coverImage {
                large
                color
                }
                genres
            }
            }
            '''
            variables = {
                'id': anilist_id
            }
            url = 'https://graphql.anilist.co'
            anilist_response = requests.post(url, json={'query': query, 'variables': variables}).json()
            print(anilist_response)
            genres = anilist_response['data']['Media']['genres']
            genres = ", ".join(genres)
            cover_image = anilist_response['data']['Media']['coverImage']['large']
            search_result = Anime.objects.create(user=user, filename=filename, tokenthumb=tokenthumb, title_en=title_en, title_jp=title_jp, genres=genres, cover_image=cover_image, at_time=at_time, from_time=from_time, to_time=to_time,mal_id=mal_id, anilist_id=anilist_id, mal_link=mal_link, anilist_link=anilist_link)
            request.session['search_result_id'] = search_result.id
            request.session['search_img'] = img_url
            return redirect('/anisearch/search_results')
    except:
        return redirect('/anisearch/')

def search_results(request):
    context = {
        'anime': Anime.objects.get(id=request.session['search_result_id']),
    }
    return render(request, 'search_results.html', context)

def my_account(request):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'user': User.objects.get(id=request.session['userid']),
    }
    return render(request, 'user_account.html', context)

def process_update(request):
    errors = Anime.objects.update_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='update')
        return redirect('/anisearch/my_account')
    else:
        user = User.objects.get(id=request.session['userid'])
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user.username = username
        user.email = email
        user.password = password
        user.save()
        return redirect('/anisearch/my_account')

def remove(request):
    show_id = request.POST['anime_id']
    anime_to_remove = Anime.objects.get(id=show_id)
    anime_to_remove.delete()
    return redirect('/anisearch/my_account')

def logout(request):
    request.session.flush()
    return redirect('/')