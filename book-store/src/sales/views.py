from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale

@login_required
def home(request):
    return render(request, 'sales/home.html')

@login_required
def records(request):
    # Create an instance of SalesSearchForm that you defined in sales/forms.py
    form = SalesSearchForm(request.POST or None)

    # Check if the button is clicked
    if request.method == 'POST':
        # Read book_title and chart_type
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        # Display in terminal - needed for debugging during development only
        print(book_title, chart_type)

        print('Exploring querysets:')
        print('Case 1: Output of Sale.objects.all()')
        qs = Sale.objects.all()
        print(qs)

        print('Case 2: Output of Sale.objects.filter(book__name=book_title)')
        qs = Sale.objects.filter(book__name=book_title)
        print(qs)

        print('Case 3: Output of qs.values')
        print(qs.values())

        print('Case 4: Output of qs.values_list()')
        print(qs.values_list())

        print ('Case 5: Output of Sale.objects.get(id=1)')
        obj = Sale.objects.get(id=1)
        print (obj)

    # Pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
    }

    # Load the sales/record.html page using the data that you just prepared
    return render(request, 'sales/records.html', context)