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

		if post['table'] == 'herd':
			form = HerdsForm(post)

		elif post['table'] == 'cow':
			form = CowsForm(post)

		elif post['table'] == 'vet':
			form = VetsForm(post)

		elif post['table'] == 'feeding':
			form = FeedingsForm(post)

		elif post['table'] == 'food_source':
			form = Food_SourcesForm(post)

		elif post['table'] == 'consult':
			form = ConsultationsForm(post)

		elif post['table'] == 'treatment':
			form = TreatmentsForm(post)

		elif post['table'] == 'milking':
			form = MilkingsForm(post)

		elif post['table'] == 'supplier':
			form = SuppliersForm(post)

		elif post['table'] == 'food_purchase':
			form = Food_PurchaseForm(post)

		elif post['table'] == 'feed':
			form = FeedForm(post)

		# Check that the event_form has been filled out correctly, then store it in database and redirect to new page
		if form.is_valid():
			# commit=False, means it does not save yet, but we have an instance of our model with the new info
			saved_info = form.save(commit=False)
			saved_info.save() #now save to db

	return HttpResponse(saved_info)