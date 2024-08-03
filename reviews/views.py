from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Review
from django.views.generic.edit import FormView, CreateView
# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name  = "reviews/review.html"
    success_url = "/thank-you"
    
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
         
    
    
    
    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html",{
    #      "form":form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST,)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     else:
    #         return render(request, "reviews/review.html",{
    #         "form":form
    #         })
class Thankyou(TemplateView):
    template_name= "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["message"] = 'This works'
        return context
   
    
class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"  
    model=Review
    context_object_name = "reviews"
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte=3)
    #     return data 
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context
    
class ReviewDetailView(DetailView):
    template_name = "reviews/single-review.html"
    model = Review
    # def get_context_data(self, **kwargs):
    #     review_id = kwargs.get('id')
    #     context = super().get_context_data(**kwargs) 
    #     review = Review.objects.get(id=review_id)
    #     context['review'] =  review
    #     return context