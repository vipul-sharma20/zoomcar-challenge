from django.shortcuts import render, render_to_response
from django.template import Context, RequestContext
from operator import itemgetter
import requests

def item_view(request):
    """
    makes api call to get items
    """
    #items = requests.get("http://zoomcar-ui.0x10.info/api/courier?type=json&query=list_parcel")

    context = RequestContext(request)
    #data = items.json()
    return render_to_response("items.html", context)


def search(request):
	context = RequestContext(request)
	result = {}
	result['parcels'] = []
	if 'q' in request.GET:
		q = request.GET['q']
		if q:
			items = requests.get("http://zoomcar-ui.0x10.info/api/courier?type=json&query=list_parcel")
			for d in items.json()['parcels']:
				if q.lower() in d[u'name'].lower() or q == d['price'] or q == d['weight']:
					result['parcels'].append(d)
			return render(request, 'items.html', result)

	return render(request, 'items.html', result)

def sort_list(request):
	result = {}
	items = requests.get("http://zoomcar-ui.0x10.info/api/courier?type=json&query=list_parcel")
	content = items.json()['parcels']
	if 'p' in request.POST:
		newlist = sorted(content, key=itemgetter(u'price')) 
		result['parcels'] = newlist
	if 'w' in request.POST:
		newlist = sorted(content, key=itemgetter(u'weight'))
		result['parcels'] = newlist
	print newlist
	return render(request, 'items.html', result)
