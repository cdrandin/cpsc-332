from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect

from dairy_farm.models import *

# url(r'^apps/', include('Vol_Event_App.urls', namespace='Vol_Event_App'))

# Corresponding url pages link to their views
# url(r'^home/$')
def app_main(request):
	return HttpResponse("App main")


def create(request, table):
	if table == 'herd':
		form = HerdsForm()

	elif table == 'cow':
		form = CowsForm()

	elif table == 'vet':
		form = VetsForm()

	elif table == 'feeding':
		form = FeedingsForm()

	elif table == 'food_source':
		form = Food_SourcesForm()

	elif table == 'consult':
		form = ConsultationsForm()

	elif table == 'treatment':
		form = TreatmentsForm()

	elif table == 'milking':
		form = MilkingsForm()

	elif table == 'supplier':
		form = SuppliersForm()

	elif table == 'food_purchase':
		form = Food_PurchaseForm()

	elif table == 'feed':
		form = FeedForm()

	return render(request, 'create_form.html', {'create_form': form, 'save_url': 'dairy_farm:save', 'table': table})

def save(request):
	if request.method == 'POST':
		# request.POST is immutable, so copy it
		post = request.POST.copy()

	print(post)

	return HttpResponse(request)