from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def home_page_view(request):
    # context sends data from the view to the HTML template
    context = {
        "list_of_stuff": ["Thing 1", "Thing 2", "Thing 3"],
        "message": "Thank you for viewing",
    }
    return render(request, "home.html", context)
    

class AboutPageView(TemplateView):
    template_name = "about.html"  # specifies which template to load

    def get_context_data(self, **kwargs):
        # adds custom variables to the about page
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Example Street"
        context["phone_number"] = "123-456-7890"
        context["companyName"] = "Great Company"
        context["numberDepartments"] = 3
        return context
    
class ProductsPageView(TemplateView):
    template_name = "products.html"  # specifies which template to load

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companyName"] = "Great Company"
        context["product1"] = "Ear Cream"
        context["product2"] = "Soul of Lobster"
        context["product3"] = "Totally normal flour"
        context["product4"] = "Bag of soup"
        return context
