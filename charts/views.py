from django.shortcuts import render
from django.db.models import Sum
from .models import Richest

def TotalNetWorth(request):
    # Query the database to get the data
    data = Richest.objects.values('country').annotate(total_net_worth=Sum('net_worth')).order_by('-total_net_worth')

    # Prepare the data for the chart
    chart_data = []
    for item in data:
        chart_data.append({
            'country': item['country'],
            'total_net_worth': item['total_net_worth']
        })

    # Render the template with the chart data
    return render(request, 'total_net_worth.html', {'chart_data': chart_data})



def TopTenRichest(request):
    # Query the database to get the data
    data = Richest.objects.order_by('-net_worth')[:10]

    # Prepare the data for the chart
    chart_data = []
    for item in data:
        chart_data.append({
            'name': item.name,
            'net_worth': item.net_worth
        })

    # Render the template with the chart data
    return render(request, 'top_ten_richest.html', {'chart_data': chart_data})


def TopRichestWomen(request):
    data = Richest.objects.filter(gender='F').order_by('-net_worth')[:10]
    names = [item.name for item in data]
    net_worths = [item.net_worth for item in data]
    return render(request, 'top_richest_women.html', {
        'names': names,
        'net_worths': net_worths
    })



def WealthByGender(request):
    # Query the database to get the total net worth for each gender
    male_net_worth = Richest.objects.filter(gender='M').aggregate(Sum('net_worth'))['net_worth__sum']
    female_net_worth = Richest.objects.filter(gender='F').aggregate(Sum('net_worth'))['net_worth__sum']

    # Prepare the data for the chart
    data = {
        'labels': ['Male', 'Female'],
        'datasets': [{
            'data': [male_net_worth, female_net_worth],
            'backgroundColor': ['#36A2EB', '#FF6384']
        }]
    }

    # Render the chart using the Chart.js library
    return render(request, 'wealth_by_gender.html', {'data': data})

