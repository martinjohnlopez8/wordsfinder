from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    if request.POST.get('login'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            print('Error logging in')
    # elif request.POST.get('register'):
    #     username = request.POST['register_username']
    #     password = request.POST['register_password']
    #     user = authenticate(username=username, password=password)
    #     login(request, user)
    elif request.POST.get('wordsfinder'):
        dictionary = open("wordsfinder/dictionary.txt", "r").read().split('\n')
        letters = list(request.POST['word'].lower()) + list(request.POST['word'].upper())
        wordInput = request.POST['word']
        wordList = []
        for word in dictionary:
            if len(word) > len(letters):
                continue
            if all(letters.count(char) >= word.count(char) for char in word):
                wordList.append(word)
        return render(request, 'wordsfinder/index.html', {
            'words': wordList,
            'word': wordInput
        })

    elif request.POST.get('logout'):
        logout(request)

    return render(request, 'wordsfinder/index.html', {
        # 'dictionary': dictionary,
    })

def signup(request):
    if request.POST.get('signup'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'wordsfinder/signup.html', {'form': form})

# def getwords(request):
