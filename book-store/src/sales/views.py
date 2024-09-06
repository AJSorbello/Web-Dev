from django.shortcuts import render
from .forms import SalesSearchForm
from .models import Sale
import pandas as pd
from .utils import get_bookname_from_id, get_chart
from django.contrib.auth.decorators import login_required  # to protect function views

# Create your views here.
def home(request):
    return render(request, 'sales/home.html')

# Define function-based view - records()
# Keep protected
@login_required
def records(request):
    # Create an instance of SalesSearchForm that you defined in sales/forms.py
    form = SalesSearchForm(request.POST or None)
    sales_df = None  # Initialize dataframe to None
    chart = None  # Initialize chart to None

    # Check if the button is clicked
    if request.method == 'POST':
        # Read book_title and chart_type
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')

        # Apply filter to extract data
        qs = Sale.objects.filter(book__name=book_title)
        if len(qs) > 0:  # If data found
            # Convert the queryset values to pandas dataframe
            sales_df = pd.DataFrame(qs.values())
            # Convert the ID to Name of book
            sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)
            # Call get_chart by passing chart_type from user input, sales dataframe and labels
            chart = get_chart(chart_type, sales_df, labels=sales_df['book_id'].values)
            # Convert the dataframe to HTML
            sales_df = sales_df.to_html()

        '''
        The following block is to get introduced to querysets
        # Display in terminal - needed for debugging during development only
        print(book_title, chart_type)

        print('Exploring querysets:')
        print('Output of Sale.objects.all()')
        qs = Sale.objects.all()
        print(qs)

        print('Output of Sale.objects.filter(book__name=book_title)')
        qs = Sale.objects.filter(book__name=book_title)
        print(qs)
            
        print('Output of qs.values()')
        print(qs.values())

        print('Output of qs.values_list()')
        print(qs.values_list())

        print('Output of Sale.objects.get(id=1)')
        obj = Sale.objects.get(id=1)
        print(obj)
        '''

    # Pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'sales_df': sales_df,
        'chart': chart
    }

    # Load the sales/record.html page using the data that you just prepared
    return render(request, 'sales/records.html', context)