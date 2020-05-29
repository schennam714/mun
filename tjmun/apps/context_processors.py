from .awards.models import Year
from .techmun.models import Commtype

def years(request):
    years = Year.objects.order_by('-name')

    return {
        'years': years,
    }

def commtypes(request):
    commtypes = Commtype.objects.order_by('rank')
    highcommtypes = Commtype.objects.filter(name__contains='High').order_by('-rank')
    midcommtypes = Commtype.objects.filter(name__contains='Middle')


    return{
        'commtypes': commtypes,
        'highcommtypes': highcommtypes,
        'midcommtypes': midcommtypes,
    }