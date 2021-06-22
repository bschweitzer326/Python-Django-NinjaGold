from django.shortcuts import render, redirect
from time import localtime, strftime
import random

def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'number' not in request.session:
        request.session['number'] = 0

    if 'result' not in request.session:
        request.session['result'] = []
    
    context = {
        'gold': request.session['gold'],
        'number': request.session['number'],
        'result': request.session['result'],
    }
    
    return render(request,'ninja_gold.html',context)

def process_money(request):
    if 'gold' in request.session:

        if request.POST['location'] == "farm":
            request.session['number'] = random.randint(10, 20)
            request.session['gold'] += request.session['number']
            time = strftime('%I:%M %p, %m %d, %Y')
            number = request.session ['number'] 
            results = f' Earn {number} from the Farm {time}'
            request.session['result'].append(results)
    
    if 'gold' in request.session:

        if request.POST['location'] == "cave":
            request.session['number'] = random.randint(5, 10) 
            request.session['gold'] += request.session['number']
            time = strftime('%I:%M %p, %m %d, %Y')
            number = request.session ['number'] 
            results = f' Earn {number} from the Cave {time}'
            request.session['result'].append(results)        
    
    if 'gold' in request.session:

        if request.POST['location'] == "house":
            request.session['number'] = random.randint(2, 5) 
            request.session['gold'] += request.session['number']
            time = strftime('%I:%M %p, %m %d, %Y')
            number = request.session ['number'] 
            results = f' Earn {number} from the House {time}'
            request.session['result'].append(results)

    if 'gold' in request.session:
        
        if request.POST['location'] == "casino":
            request.session['number'] = random.randint(-50,50)
            request.session['gold'] += request.session['number']
            if request.session['number'] > 0:
                time = strftime('%I:%M %p, %m %d, %Y')
                number = request.session ['number'] 
                results = f' Earn {number} from the Casino {time}'
                request.session['result'].append(results)
            elif request.session['number'] < 0:
                time = strftime('%I:%M %p, %m %d, %Y')
                number = request.session ['number'] 
                results = f' Take {number} from the Casino {time}'
                request.session['result'].append(results)

    print(request.session['number'])
    return redirect('/')

def restart(request):
    request.session.clear()
    return redirect('/')
