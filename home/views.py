from django.shortcuts import render, redirect
from django.views import View
from .models import Features, HowToUse, UserFeedback

# Create your views here.

class DisplayHomeView(View):
    template_name = 'home/home.html'
    
    def get(self, request, *args, **kwargs):
        features = Features.objects.all()
        instructions = HowToUse.objects.all()
        feedbacks = UserFeedback.objects.all()
        
        # if request.user.is_authenticated:
        #     return redirect('tasks')
        
        return render(
            request,
            self.template_name,
            {
                'features': features,
                'instructions': instructions,
                'feedbacks': feedbacks,
            }
        )
