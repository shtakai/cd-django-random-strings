from django.shortcuts import render
import random


def index(request):
    if not request.session.get( 'attempts' ):
        print('not found')
        request.session['attempts'] = 1
    else:
        print('found')
        request.session['attempts'] += 1
    print('attempts', request.session['attempts'])
    randomstr = ''
    for i in range(0, 14):
        randomstr += random.choice(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567789'
        )

    context = {
        'randomstr': randomstr,
    }
    return render(request, 'randomstr/index.html', context)
