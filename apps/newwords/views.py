from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import gmtime, strftime, localtime


def index(request):
    return render(request, 'newwords/index.html')


def process(request):
    if request.method == "POST":

        word = request.POST['word']
        color = request.POST['color']
        size = request.POST.get('size', 'small')
        time_now = strftime("%Y-%m-%d %H:%M %p", localtime())

        if 'all' in request.session:
            monkey = request.session['all']
            monkey.append((word,color,size,time_now))
            request.session['all'] = monkey
        else:
            request.session['all'] = []
            monkey = request.session['all']
            monkey.append((word,color,size,time_now))
            request.session['all'] = monkey

        return redirect('/session_words')

def reset(request):
    try:
        # del request.session['all']
        request.session.clear()
    # this try except is needed just in case the key doesn't exist! Also don't need both del count and count = 0 choose one.
        return redirect('/')
    except:
        return redirect('/')

    