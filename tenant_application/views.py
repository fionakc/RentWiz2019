from django.shortcuts import render
from django.views.generic.edit import UpdateView

from tenant_application.models import Tenant
from .forms import TenantProfile_part1_Form

# Create your views here.
def apply(request):
    return render(request, 'apply.html')

def addTenants(request):
    return render(request, 'addTenants.html')

def addMoreT(request):
    return render(request, 'addMoreT.html')

def conditions(request):
    return render(request, 'conditions.html')

def confirmation(request):
    return render(request, 'confirmation.html')


class UpdateTenantProfilePart1(UpdateView):
    def tenant_profile(request):
        # return render(request, 'tenantProfile.html')

        # user_id = request.POST.get('tenant_id')
        # tenant = Tenant.objects.get(pk=request.GET.get('tenant_id'))
        if request.method == 'POST':
            form = TenantProfile_part1_Form(request.POST)
            if form.is_valid():
                pass
                form.save(request)  #still need this??
        else:
            form = TenantProfile_part1_Form()

        return render(request, 'tenantProfile.html',{'form': form})

# def ProfileView(request):
#     user_id = request.POST.get('user_id')
#     user = UserInfo.objects.get(pk=user_id)
#     if request.method == 'POST':
#         form = Editform(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#     else:
#         form = Editform(instance=user)
#
#     return render (request, 'profile_view.html', {'user':username, 'form':form})


# def register_tenant(request):
#
#     if request.method == 'POST':
#         form = TenantCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = TenantCreationForm()
#     return render(request, 'register_tenant.html', {'form': form})