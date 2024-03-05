from django.shortcuts import render
from django.views import View
from .models import Features, HowToUse, UserFeedback

# Create your views here.

class DisplayHomeView(View):
    template_name = 'home/home.html'
    
    def get(self, request, *args, **kwargs):
        features = Features.objects.all()
        instructions = HowToUse.objects.all()
        feedbacks = UserFeedback.objects.all()
        
        return render(
            request,
            self.template_name,
            {
                'features': features,
                'instructions': instructions,
                'feedbacks': feedbacks,
            }
        )
