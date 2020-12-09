from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms import UserLoginForm, UserRegistrationForm


def login_view(request):
    form = UserLoginForm(request.POST or None)
    next_ = request.GET.get('next')
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username.strip(),
                            password=password.strip())
        login(request, user)
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or '/'
        return redirect(redirect_path)
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраяем его в базу
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованый пароль
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем пользователя в базе
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
        return render(request, 'users/register.html', {'form': user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': user_form})
