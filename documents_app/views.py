from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentForm
from django.core.exceptions import PermissionDenied
from django.conf import settings
import os


def home(request):
    return render(request, 'home.html')


@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        try:
            if form.is_valid():
                doc = form.save(commit=False)

                doc.owner = request.user
                doc.name = request.FILES['file'].name
                doc.save()
                return redirect('list_documents')

            else:
                return render(request, 'upload_document.html', {'form': form, 'error': 'Form is not valid.'})
        except Exception as e:
            return render(request, 'upload_document.html',
                          {'form': form, 'error': 'An error occurred during file upload.'})
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})


@login_required
def list_documents(request):
    try:
        documents = Document.objects.filter(owner=request.user)
        return render(request, 'list_documents.html', {'documents': documents})

    except Exception as e:
        return render(request, 'list_documents.html', {'error': 'An error occurred while retrieving documents.'})


@login_required
def download_document(request, doc_id):
    try:
        doc = Document.objects.get(id=doc_id, owner=request.user)
        response = FileResponse(doc.file, as_attachment=True, filename=doc.file.name)
        return response

    except Document.DoesNotExist:
        raise Http404("Document not found")

    except Exception as e:
        return Http404("An error occurred while trying to download the document.")


@login_required
def delete_documents(request, doc_id):
    try:
        doc = get_object_or_404(Document, id=doc_id)
        if doc.owner != request.user:
            raise PermissionDenied
        doc.delete()

        return redirect('list_documents')

    except Document.DoesNotExist:
        raise Http404("Document not found")
    except Exception as e:
        return render(request, 'list_documents.html',
                      {'error': 'An error occurred while trying to delete the document.'})


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            messages.error(self.request, 'Username not found. Please sign up.')
            return redirect('signup')  # Redirect to the signup page
        return super().form_valid(form)
