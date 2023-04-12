# Create your views here.

from django.http import HttpResponse
from .scouting import generatereport
from django.shortcuts import render
from .models import Team


def DocxView(request):

    data = Team.objects.all()
    teams = {"Teams": data}

    return render(request, 'scout/search_form.html', teams)



def download(request):


    scoutteam = request.POST.get('Team')
    season = "2019-20"
    playerstats = [[int(request.POST.get('P1Num')), int(request.POST.get('P1Pm')), int(request.POST.get('P1Pa')), ],
                   [int(request.POST.get('P2Num')), int(request.POST.get('P2Pm')), int(request.POST.get('P2Pa')), ],
                   [int(request.POST.get('P3Num')), int(request.POST.get('P3Pm')), int(request.POST.get('P3Pa')), ],
                   [int(request.POST.get('P4Num')), int(request.POST.get('P4Pm')), int(request.POST.get('P4Pa')), ],
                   [int(request.POST.get('P5Num')), int(request.POST.get('P5Pm')), int(request.POST.get('P5Pa')), ],
                   [int(request.POST.get('P6Num')), int(request.POST.get('P6Pm')), int(request.POST.get('P6Pa')), ],
                   [int(request.POST.get('P7Num')), int(request.POST.get('P7Pm')), int(request.POST.get('P7Pa')), ],
                   [int(request.POST.get('P8Num')), int(request.POST.get('P8Pm')), int(request.POST.get('P8Pa')), ],
                   [int(request.POST.get('P9Num')), int(request.POST.get('P9Pm')), int(request.POST.get('P9Pa')), ],
                   [int(request.POST.get('P10Num')), int(request.POST.get('P10Pm')), int(request.POST.get('P10Pa')), ],
                   [int(request.POST.get('P11Num')), int(request.POST.get('P11Pm')), int(request.POST.get('P11Pa'))]]
    teampaint = [int(request.POST.get('TPm')), int(request.POST.get('TPa'))]

    '''
    scoutteam = 'STR'
    season = "2018-19"
    playerstats = [[1, 45, 70],
                   [1, 17, 35],
                   [1, 9, 20],
                   [1, 29, 55],
                   [1, 61, 103],
                   [1, 36, 73],
                   [1, 37, 80],
                   [1, 6, 10]]
    teampaint = [273, 500]
    '''

    doc = generatereport(scoutteam, season, playerstats, teampaint)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=scoutingreport.docx'

    doc.save(response)
    return response
