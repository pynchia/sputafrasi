# coding=utf-8
# -*- coding: utf-8 -*-
#views.py

# Sputafrasi is a FaceBook app by Pynchia
# March 2013

#Sintassi: 
#Persona-Verbo-[Oggetto-Preposiz]-Persona-[Luogo]-[Tempo] 
#es.: "Pino-abbraccia-[le calze-di/a/con/su/per]-Gina-[in montagna]-[a Natale]" 
import random
#import facebook
from django.shortcuts import render, render_to_response
from django.template import RequestContext
#from django_facebook.decorators import canvas_only

#from mysite.FBcfg import *

from models import FBUser, PubFig, Verb, Thing, Prepos, Place, Time
import forms
#import time as ttime

# CONSTANTS
MAX_QUOTES_PUB = 3

BIAS_THING = 50
BIAS_PLACE = 50
BIAS_TIME = 25
BIAS_PUBFIG = 50
BIAS_SWAP_PERS = 40

def biastoss(bias=50):
    """Performs a biassed toss of a coin. Useful to choose one way
    more frequently than another.
    Returns True if the tossed number is less or equal to the
    given bias param (which goes from one to 100)
    False otherwise.
    Therefore, the closer the bias to 100, the higher
    the probability the event occurs.
    """
    r = random.randint(1,100)
    #print r
    return True if r <= bias else False

#@canvas_only
def home(request):
#    me = request.facebook.graph.get_object('me')
#    #access_token = request.facebook.graph.access_token # user token, expires
#    #access_token = request.facebook.get_app_access_token(FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY) # app token, does not expire
#    #request.session['fbid'] = me['id']
#    #request.session['fbname'] = me['name']
#    #request.session['signed_request'] = access_token
#    friends = request.facebook.graph.get_connections("me", "friends")
#    friendlist = [friend['name'] for friend in friends['data']]

    me = {}
    me['name'] = 'xyz'
    me['id'] = '69DFS3242R'
    friendlist = [str(n) for n in xrange (1000)]

    fbuser, created = FBUser.objects.get_or_create(fbid=me['id'], name=me['name'])
    
    # if the user wants to be included in the quotes
    if fbuser.inc_me:
        # add the user to the list of friends
        friendlist.append(me['name'])

    if fbuser.alfasort:
        # sort the list of friends alphab.
        friendlist.sort()
    else:
        random.shuffle(friendlist)

    # if the user wants to include public figures in the quotes
    if fbuser.inc_pubfig:
        # get the number of public figures 
        npubfig = PubFig.objects.count()

    nfriends = len(friendlist)
    nverb = Verb.objects.count()
    nthing = Thing.objects.count()
    nprepos = Prepos.objects.count()
    nplace = Place.objects.count()
    ntime = Time.objects.count()

    #start= ttime.clock()

    quotelist = []
    for friend in friendlist:
        incthing = biastoss(BIAS_THING)
        incplace = biastoss(BIAS_PLACE)
        inctime = biastoss(BIAS_TIME)

        idverb = random.randint(1,nverb)
        verb = Verb.objects.get(id=idverb)

        if incthing:
            idthing = random.randint(1,nthing)
            thing = Thing.objects.get(id=idthing)
            idprepos = random.randint(1,nprepos)
            prepos = Prepos.objects.get(id=idprepos)
        if incplace:
            idplace = random.randint(1,nplace)
            place = Place.objects.get(id=idplace)
        if inctime:
            idtime = random.randint(1,ntime)
            time = Time.objects.get(id=idtime)
        
        if fbuser.inc_pubfig: # the user wants public figures
            incpubfig = biastoss(BIAS_PUBFIG)
            if incpubfig:
                # include a public figure
                idpubfig = random.randint(1,npubfig)
                pubfig = PubFig.objects.get(id=idpubfig)
                if biastoss(BIAS_SWAP_PERS):
                    # swap subjects (public fig. does the action)
                    pers1 = pubfig.name
                    pers2 = friend
                else:
                    # let subjects be (current friend does the action)
                    pers1 = friend
                    pers2 = pubfig.name
        else: # the user does not want public figures
            incpubfig = False
        if not incpubfig:
            pers1 = friend
            idpers = random.randint(0,nfriends-1)
            pers2 = friendlist[idpers]

        quote = pers1+u' '+verb.name
        if incthing:
            #quote += ' '+thing.name+' '+prepos.name
            quote = u' '.join((quote, thing.name, prepos.name))
        #quote += ' '+pers2
        quote = u' '.join((quote, pers2))
        if incplace:
            #quote += ' '+place.name
            quote = u' '.join((quote, place.name))
        if inctime:
            #quote += ' '+time.name
            quote = u' '.join((quote, time.name))

        # add the quote to the total list
        quotelist.append(quote) 

    #print (ttime.clock() - start)

    #return render_to_response('home.html',
    #                          {'usr': me['name'],
    #                           'access_token': access_token,
    #                           'quotelist': quotelist},
    #                          context_instance=RequestContext(request))
    return render(request, 'home.html',
                  {'usr': me['name'],
                   'usrid': me['id'],
                   'max_quotes_pub': MAX_QUOTES_PUB,
                   'quotelist': quotelist})

def update_status(request):
    """posts the given quote to the user wall
    """
#    #access_token = request.POST['access_token']
#    access_token = APP_ACCESS_TOKEN
#
#    usrid = request.POST['usrid']
#    quotelist = request.POST.getlist('cbquote')
#    graph = facebook.GraphAPI(access_token)
#    #graph.put_object("me", "feed", message=quote)
#    attachment = {
#        "name": "Sputafrasi",
#        "link": "http://apps.facebook.com/sputafrasi/",
#        "caption": "l'app che genera situazioni assurde",
#        #"description": "Scopri anche tu cosa potrebbero fare i tuoi amici!\nE' gratis, divertente e non ruba i tuoi dati.\nL'app non salva i dati dei tuoi amici e pubblica solo su tuo comando esplicito.",
#        "picture": "http://pynchia.pythonanywhere.com/static/iconpost108x108w.png"
#    }
#    #graph.put_wall_post(quote, attachment)
#    i = MAX_QUOTES_PUB;
#    for quote in quotelist:
#        attachment['description'] = quote
#        graph.put_wall_post(quote, attachment, profile_id=usrid)
#        i -= 1
#        if not i:
#            break
#    return render(request, 'all_done.html')
    return render(request, 'all_done.html')

#@canvas_only
def editpref(request):
    """lets the user set her preferences
    """
#    me = request.facebook.graph.get_object('me')
    me = {}
    me['name'] = 'xyz'
    me['id'] = '69DFS3242R'

    try:
        # get user data from DB
        fbuser = FBUser.objects.get(fbid=me['id'])
    except FBUser.DoesNotExist:
        # that id is not in the DB, so create it
        # I am not using get_or_create() because
        # the user might have changed her name on FB
        fbuser = FBUser(fbid=me['id'], name=me['name'])
        fbuser.save()

    form = forms.UserPrefForm(instance=fbuser)
    #return render_to_response('editpref.html',
    #                          {'form': form},
    #                          context_instance=RequestContext(request))
    return render(request, 'editpref.html',
                  {'form': form})

def setpref(request):
    """sets the user preferences
    """
    # check get user is in DB
    fbuser = FBUser.objects.get(fbid=request.POST['fbid'])

    form = forms.UserPrefForm(request.POST, instance=fbuser)
    if form.is_valid():
        fbuser=form.save()
    return render(request, 'pref_done.html')

