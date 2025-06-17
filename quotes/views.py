from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Quote, Source

class IndexView(generic.ListView):
    template_name = "quotes/index.html"
    context_object_name = "quotes_list"

    def get_queryset(self):
        return Quote.objects.all()

class DetailView(generic.DetailView):
    model = Quote
    template_name = "quotes/detail.html"

    def get_queryset(self):
        return Quote.objects.all()

class FormView(generic.ListView):
    template_name = "quotes/form.html"

    def get_queryset(self):
        return 
    

def create_quote(request):
    if request.method == "POST":
        quotetext = request.POST.get('qtext', '')
        author_name = request.POST.get('author_name', '')
        outlook_value = request.POST.get('outlook_value', '')
        created_at = timezone.now()

        source_type = request.POST.get('source_type', '')
        link = request.POST.get('link', '')
        source_name = request.POST.get('source_name', '')
        description = request.POST.get('description', '')
        pubdate = timezone.now()

        # Save source
        s = Source(
            type_text=source_type,
            url=link,
            title_text=source_name,
            description_text=description,
            pub_date=pubdate
        )
        s.save()

        q = Quote(
            quote_text=quotetext,
            author_text=author_name,
            sentiment=outlook_value,
            create_date=created_at,
            source=s
        )
        q.save()

        return HttpResponseRedirect(reverse('quotes:index'))

    return render(request, 'quotes/form.html')


def quote_view(request):
    selected_value = request.POST.get('quotetypes')

    if selected_value == '2' or selected_value is None:
        quotes = Quote.objects.all()
    else:
        quotes = Quote.objects.filter(sentiment=selected_value)

    return render(request, 'quotes/index.html', {
        'quotes_list': quotes,
        'selected_value': selected_value
    })

def source_view(request):
    selected_value = request.POST.get('sourcetypes')

    if selected_value == '5' or selected_value is None:
        quotes = Quote.objects.all()
    else:
        quotes = Quote.objects.filter(source__type_text = selected_value)

    return render(request, 'quotes/index.html', {
        'quotes_list': quotes,
        'selected_value': selected_value
    })


