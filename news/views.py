from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from . forms import ReporterForm

def home(request):
    #messages.add_message(request, messages.INFO, 'Hello world.')
    #print(messages.get_messages(request).__dict__)
    #mymessage=messages.get_messages(request)
    #print(mymessage)
    if request.method == 'POST':

        form = ReporterForm(request.POST)
        if form.is_valid():
            #http: // www.effectivedjango.com / forms.html
            #https: // www.pythoncentral.io / how - to - check - if -an - object - has - an - attribute - in -python /
            #print(form.cleaned_data)
            #form.save()
            messages.success(request, 'User Successfully Added.')
            print(request.META)
            return redirect('news:home')

        else:
            return render(request, 'news/meta.html', {'form':form})

    else:
        form = ReporterForm()

    context = {

        'form':form,
        'data':'Nothing to show'
    }

    return render(request,'news/meta.html',context)





