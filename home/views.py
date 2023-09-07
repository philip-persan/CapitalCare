from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from users.forms import LoginForm, UserForm


class HomeView(View):
    def get(self, request):
        return render(request, 'home/pages/index.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        ctx = {
            'form': form
        }
        return render(request, 'home/pages/login.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            authenticated_user = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', ''),
            )

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect("home:index")

            messages.error(request, 'Credenciais Inválidas')
            return redirect("home:index")

        messages.error(request, 'Credenciais Inválidas')
        return redirect("home:index")


class RegisterView(View):
    def get(self, request):
        form = UserForm()
        ctx = {
            'form': form
        }
        return render(request, 'home/pages/register.html', ctx)

    def post(self, request):
        POST = request.POST
        request.session['register_form_data'] = POST
        form = UserForm(POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.set_password(data.password)
            data.save()

            del (request.session['register_form_data'])
            messages.success(request, 'Usuário criado, por favor entre em sua conta')  # noqa
            return redirect('home:login')

        messages.error(request, 'Corrija os erros nos formulários')
        return render(request, 'home/pages/register.html', {
            "form": form
        })


@login_required(login_url='home:index', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect('home:index')

    if request.POST.get('username') != request.user.username:
        return redirect('home:index')

    logout(request)
    return redirect('home:index')
