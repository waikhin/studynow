from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from .recommendation import create_sim   # make sure the create_sim function is in the utils.py in the same directory
from markupsafe import Markup

class RecommendCourse(APIView):
    def post(self, request):
        namec = request.data.get('course')
        output = create_sim(namec)
        if output.empty:
            ms='Sorry! we did not find any matching courses, Try adding more keywords in your search.'
            ht=' '
        else:
            ht=output.to_html(render_links=True, index=True)
            ht= Markup(ht)
            ms='Here are some recommendations :'
        return JsonResponse({"message": ms, "pred": ht})
