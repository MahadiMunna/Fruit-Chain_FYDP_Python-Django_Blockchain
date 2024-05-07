from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.views.generic import FormView, View
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm


# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'signup.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        print(form.cleaned_data)
        messages.warning(self.request, 'User Information is incorrect')
        return super().form_invalid(form)

class UserLogoutView(View):
    def get(self, request):
        messages.success(self.request, 'Successfully logged out!')
        logout(request)
        return redirect('login')
    
class Profile(TemplateView):
    template_name = 'profile.html'

class UserAccountUpdateView(View):
    template_name = 'update_profile.html'

    def get(self, request):
        form = forms.EditProfile(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = forms.EditProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Profile updated successfully!')
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

class ChangePasswordView(TemplateView):
    template_name = 'change_pass.html'

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('update_profile')
        else:
            for field in form:
                for error in field.errors:
                    messages.warning(request, f"{field.label}: {error}")
                    return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(self.request.user)
        return context

def forgot_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request,'Password has been changed successfully!')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form  = SetPasswordForm(user=request.user)

        return render(request, 'forget_pass.html', {'form': form, 'type':'Set a new password'})
    else:
        return redirect('signup')
    



