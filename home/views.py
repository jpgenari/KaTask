from django.shortcuts import render
from django.views import View
from .models import Features, HowToUse, UserFeedback

# Create your views here.


class DisplayHomeView(View):
    '''
    Renders the most recent information on the website about
    features, instructions and testimonials (user feedback).
    Retrieves data from 3 different models `Features`, `HowToUse` and
    `UserFeedback` passing them to home/home.html for display.
    **Context**
    ``features``
        The most recent instance of :model:`home.Features`.
    ``instructions``
        The most recent instance of :model:`home.HowToUse`.
    ``feedbacks``
        The most recent instance of :model:`home.UserFeedback`.
    **Template:**
    :template:`home/home.html`
    '''

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
