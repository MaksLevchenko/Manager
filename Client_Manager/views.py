from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, BadHeaderError, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View, generic

from Client_Manager.forms import SignInForm, LandingForm, CommentForm
from Client_Manager.models import Client, Comment


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'signin.html', context={
                      'form': form})

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
        return render(request, 'signin.html', context={
            'form': form
        })


class LandingView(View):
    def get(self, request, *args, **kwargs):
        form = LandingForm()
        return render(request, 'lending.html', context={
                      'form': form,
                      'title': 'Написать мне'
        })

    def post(self,request, *args, **kwargs):
        form = LandingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastName = form.cleaned_data['lastName']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            try:
                landing = Client.objects.create(name=name, lastName=lastName, phone=phone, email=email)
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'lending.html', context={
                'form': form,
            })


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html', context={
            'title': 'Спасибо'
        })


class ClientListView(generic.ListView):
    model = Client
    template_name = 'home.html'

    def get_queryset(self):
        if self.request.user.username == 'manager1':
            queryset = Client.objects.all().order_by('id')[1::2]
            return queryset
        else:
            queryset = Client.objects.all().order_by('id')[::2]
            return queryset


class ClientDetailView(generic.DetailView):
    comment_form = CommentForm()
    model = Client
    slug_field = 'id'
    template_name = 'client_detail.html'

    def post(self, request, pk, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            client = get_object_or_404(Client, id=pk)
            comment = Comment.objects.create(client=client, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'client_detail.html', context={
            'comment_form': comment_form
        })
