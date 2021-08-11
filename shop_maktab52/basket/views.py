from django.shortcuts import render


# Create your views here.
def detail(request):
    return render(request, 'basket/detail.html', {'form': 'request'})


def AddProduct(request, ProductId):
    pass
