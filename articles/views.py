from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Article

def articles_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})

def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        author = request.POST.get('author', '').strip()
        
        if title and content and author:
            article = Article.objects.create(
                title=title,
                content=content,
                author=author
            )
            messages.success(request, 'Статья успешно создана!')
            return redirect('articles/articles_list')
        else:
            messages.error(request, 'Все поля обязательны для заполнения!')
    
    return render(request, 'articles/article_form.html')

def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        author = request.POST.get('author', '').strip()
        
        if title and content and author:
            article.title = title
            article.content = content
            article.author = author
            article.save()
            messages.success(request, 'Статья успешно обновлена!')
            return redirect('articles/articles_list')
        else:
            messages.error(request, 'Все поля обязательны для заполнения!')
    
    return render(request, 'articles/article_form.html', {'article': article})