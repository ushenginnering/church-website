from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.http import HttpResponse, JsonResponse
from django.contrib import admin
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

class MyModelModelAdmin(ExtraButtonsMixin, admin.ModelAdmin):

    @button(permission='demo.add_demomodel1',
            change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def refresh(self, request):
        self.message_user(request, 'refresh called')
        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)
    
    @button(html_attrs={'style': 'background-color:#DC6C6C;color:black'})
    def confirm(self, request):
        def _action(request):
            pass

        return confirm_action(self, request, _action, "Confirm action",
                          "Successfully executed", )

    @link(href=None, 
          change_list=False, 
          html_attrs={'target': '_new', 'style': 'background-color:var(--button-bg)'})
    def search_on_google(self, button):
        original = button.context['original']
        button.label = f"Search '{original.name}' on Google"
        button.href = f"https://www.google.com/?q={original.name}"

    @view()
    def select2_autocomplete(self, request):
        return JsonResponse({})

    @view(http_basic_auth=True)
    def api4(self, request):
        return HttpResponse("Basic Authentication allowed")

    @view(decorators=[csrf_exempt, xframe_options_sameorigin])
    def preview(self, request):
        if request.method == "POST":
            return HttpResponse("POST")
        return HttpResponse("GET")