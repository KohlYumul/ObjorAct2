from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweetForm


@login_required
def create_tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.user = request.user
            new_tweet.save()
            return redirect('create_tweet')
    else:
        form = TweetForm()

    context = {'form': form}
    return render(request, 'tweet_form.html', context)