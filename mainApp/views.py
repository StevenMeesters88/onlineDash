from django.shortcuts import render
from django.http import HttpResponse
from .forms import LandingPageForm
import pandas as pd
import io
from .models import Document
import csv
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def index(request):

    if not request.session.session_key:
        request.session.save()
    session_id = request.session.session_key
    print(session_id)

    if request.method == 'POST':
        form = LandingPageForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(session_key=session_id, docfile=request.FILES['csv_data'])
            newdoc.save()

            return redirect('show_data')

    form = LandingPageForm()

    return render(request, template_name='base.html', context={'form': form})


def show_data(request):
    max_id = Document.objects.filter(session_key=request.session.session_key).latest('id').id
    file_name = Document.objects.values_list('docfile', flat=True).get(id=max_id)

    df = pd.read_csv(r'/Users/stevenmeesters/PycharmProjects/onlineDash/media/' + file_name, delimiter=';')

    return render(request, template_name='show_data.html', context={'columns': list(df.columns), 'data': df})


def build_dash(request):

    return render(request, template_name='build_dash.html')

