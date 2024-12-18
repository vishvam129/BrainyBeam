from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

# Custom AdminSite
class CustomAdminSite(AdminSite):
    # Customizing the title, header, and index
    site_header = _("Custom Admin Header")
    site_title = _("Custom Admin Title")
    index_title = _("Welcome to the Admin Panel")

    # Adding custom CSS
    def each_context(self, request):
        context = super().each_context(request)
        context['extra_css'] = 'admin/custom_admin.css'
        return context


# Instantiate the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

