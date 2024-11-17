from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quote , Author, Tag
from .forms import TagForm, AuthorForm, QuoteForm



def main(request, page=1):
    
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)

    return render(request, 'quotes/index.html', context = {'quotes': quotes_on_page})
from django.shortcuts import render, redirect, get_object_or_404



def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {"author": author})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit = False)
            tag.user = request.user
            tag.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_tag.html', {'form': form})

    return render(request, 'quotes/add_tag.html', {'form': TagForm()})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit = False)
            author.user = request.user
            author.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            quote = form.save()
            quote.user = request.user
            # quote.tags.add(form.cleaned_data.get('tags'))
            quote.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_quote.html', {'form': form})

    return render(request, 'quotes/add_quote.html', {'form': QuoteForm()})
