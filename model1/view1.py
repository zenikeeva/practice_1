from django.shortcuts import get_object_or_404, render
from model1 import MNK


def index(request):
    return render(request, 'index.html')

def showresult(request):
    pair = request.POST['pair'];

    trend = ""

    a = MNK.readfromfile(pair)
    if (a > 0.1):
        trend = "восходящим"
    elif (a < -0.1):
        trend = "нисходящим"
    else:
        trend = "боковой"

    params = {'pair': pair, 'trend': trend}
    return render(request, 'result.html', params)
