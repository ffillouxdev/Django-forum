from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage
from django.db.models import Count


from . import forms
from .models import Topic
from .forms import CreateTopicForm

compteur = 0

@login_required
def home(request):
    topics = Topic.objects.annotate(reply_count=Count('replies')).order_by('-reply_count')
    return render(request, 'forum/home.html', {'topics': topics})

@login_required
def account(request):
    return render(request, 'forum/account.html')

@login_required
def new_ftopic(request):
    form = forms.CreateTopicForm()
    message = ''
    if request.method == 'POST':
        form = forms.CreateTopicForm(request.POST)
        if form.is_valid():
            # Create a new topic
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()

            return redirect('topic-detail', slug=topic.slug)

    return render(request, 'forum/new_ftopic.html', {'form': form})

@login_required
def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)

    if request.method == 'POST':
        form = forms.ReplyTopicForm(request.POST)
        if form.is_valid():
            # Create a new reply object
            reply = form.save(commit=False)
            reply.author = request.user
            reply.topic = topic
            reply.save()
            return redirect('topic-detail', slug=slug)
    else:
        form = forms.ReplyTopicForm()

    return render(request, 'forum/topic_detail.html', {'topic': topic, 'form': form})


@login_required
def IT(request):
    topics = Topic.objects.filter(section='IT section')
    return render(request, 'forum/IT-section.html', {'topics': topics, 'section': 'IT'})

@login_required
def MATH(request):
    topics = Topic.objects.filter(section='MATH section')
    return render(request, 'forum/MATH-section.html', {'topics': topics, 'section': 'Math'})

@login_required
def PHYSICS(request):
    topics = Topic.objects.filter(section='PHYS section')
    return render(request, 'forum/PHYS-section.html', {'topics': topics, 'section': 'Physics'})

@login_required
def MEDECINE(request):
    topics = Topic.objects.filter(section='Medecine section')
    return render(request, 'forum/MEDECINE-section.html', {'topics': topics, 'section': 'Medecine'})

@login_required
def SOCIOLOGY(request):
    topics = Topic.objects.filter(section='Sociology section')
    return render(request, 'forum/SOCIOLOGY-section.html', {'topics': topics, 'section': 'Sociology'})

def miscellaneous_topics(request):
    topics = Topic.objects.filter(section='miscellaneous Topics')
    return render(request, 'forum/miscellaneous_topics.html', {'topics': topics, 'section': 'Miscellaneous'})

def your_view(request):
    # votre logique de traitement du formulaire ici
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # instance de FileSystemStorage
        fs = FileSystemStorage()
        # génère un nouveau nom unique pour le fichier
        filename = fs.save(file.name, file)
        # obtient l'URL relative du fichier
        uploaded_file_url = fs.url(filename)
        # redirige vers une autre vue ou renvoie une réponse
        return redirect('account')
    return render(request, 'changeprofile.html')