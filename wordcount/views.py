from operator import itemgetter

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    usertext = request.GET['usertext']
    words = usertext.split()
    word_dict={}
    for i in words:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    word_dict_sort = {k: v for k, v in sorted(word_dict.items(), key=itemgetter(1),reverse=1)}
    return render(request,'count.html',{"words_count":len(words),"usertext":usertext,"words":word_dict_sort})
