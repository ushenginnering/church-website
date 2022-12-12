from django.shortcuts import render, redirect
from .models import VideoMessage, BookLibrary, LeadPastors, NewsLetterUsers, NewsLetter
from .forms import PrayerRequestForm, NewsLetterUsersForm

from django.views import View
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
class home(View):

    def get(self, request):
        context = {
            'LatestVideo': VideoMessage.objects.first(),
            'BookLIbrary': BookLibrary.objects.all(),
            'form': PrayerRequestForm(),
        }
    
        return render(request, 'index.html', context)

    def post(self, request):
        context = {
            'LatestVideo': VideoMessage.objects.first(),
            'BookLIbrary': BookLibrary.objects.all(),
        }
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'prayer request saved')
            
            return redirect('home')

        context['form'] = form
        return render(request, 'index.html', context)
            

def about(request):
    return render(request, 'about.html')

def gallery(request):
    context = {
        'LeadPastors': LeadPastors.objects.all(),
    }
    return render(request, 'gallery.html', context)

class grow_deeper(View):
    form = NewsLetterUsersForm
    def get(self, request):
        news_letter_index = request.GET.get('next_index')

        ''''
        geting a next_index query paremeter. If index is not found or not specified
        we set it to 0. if it is specified but greater than the items in the model we set it back to zero.
        '''
        if not news_letter_index:
            news_letter_index = 0
        else:
            news_letter_index = int(news_letter_index) if len(NewsLetter.objects.all()) > int(news_letter_index) else 0

        context = {
            'form': self.form,
            'newsletter': NewsLetter.objects.all()[news_letter_index],
            'next_index': news_letter_index + 1,
        }
        
        return render(request, 'grow_deeper.html', context)

    def post(self, request):
        user = self.form(request.POST)
        # checking if email has already been subscribed to newletter
        if not user.is_valid():
            messages.error(request, 'email already subscribed to news letter')
            return redirect('grow_deeper')

        user.save()
        messages.success(request, "successfully subscribed to news letter")
        return redirect('grow_deeper')
