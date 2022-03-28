from typing import Dict
import dictionary
from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    

    #print(type(meaning))
    if type(meaning) is not dict:
        meaning = "Meaning not found"

    
    
    
    context = {
        'meaning': meaning,
    }
    return render(request, 'word.html', context)