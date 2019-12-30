from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'hithere': 'Hello wordcount'})


def eggs(requeest):
    return HttpResponse('I love eggs')


def count(request):
    max_value = 0
    max_word = ""
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase the counter
            worddictionary[word] += 1

        else:
            # Add to dictionary
            worddictionary[word] = 1

    for key in worddictionary:
        if worddictionary[key] > max_value:
            max_value = worddictionary[key]
            max_word = key

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': worddictionary.items(), 'maxvalue': max_value, 'maxword': max_word})


def about(request):
    return render(request, 'about.html')