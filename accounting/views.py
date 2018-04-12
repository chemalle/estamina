from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from .forms import accountingFORM
from .models import Accounting
from django.core.files.storage import FileSystemStorage
import pandas as pd

# Create your views here.


def home(request):
    return render(request, 'accounting/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounting/acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate your #econobilidade account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'accounting/acc_active_sent.html')
            #return HttpResponse('Please confirm your email address to complete the registration.')
            # return render(request, 'acc_active_sent.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'accounting/thankyou.html')
    else:
        return HttpResponse('Activation link is invalid!')



def xlsx_upload_accounting(request):
    if request.method == 'POST' and request.FILES['tnt']:
        myfile = request.FILES['tnt']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        GL = pd.read_excel(filename,'geral')
        


        for index,row in GL.iterrows():
            try:
                if row[0] != 'create_date':
                    accounting = Accounting()
                    accounting.geralId = row[0]
                    accounting.dataMovimento = row[1]
                    accounting.unidade = row[2]
                    accounting.tipo = row[3]
                    accounting.categoria = row[4]
                    accounting.origem = row[5]
                    accounting.destino = row[6]
                    accounting.observacao = row[7]
                    accounting.valorReais = row[8]
                    accounting.status = row[9]
                    accounting.save()
            except Exception:
                pass

        return render_to_response('accounting/thankyou2.html')
        raise Http404()

    else:
        return render(request, 'accounting/import.html')



@login_required
def General_Ledger(request):

    qs = Accounting.pdobjects.all()
    df2 = qs.to_dataframe()
    return render_to_response('accounting/ledger.html',{'data':df2.to_html(index=False,columns=['dataMovimento','tipo','origem','destino','observacao','valorReais'])})
