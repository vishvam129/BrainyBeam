# Customizing Django Admin Panel Theme and Title

This guide explains how to customize the Django admin panel by changing its title, adding a custom icon, and applying a custom color theme using internal CSS. No models are required for this process.

---

## Step 1: Modify `admin.py`

The `admin.py` file is used to define the customizations for the admin panel. If it doesn't exist, create it in your app directory.

### File Structure
```plaintext
my_app/
├── admin.py
├── static/
│   ├── admin/
│   │   ├── custom_admin.css
```

### Example `admin.py` Content

```python
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


```

---

## Step 2: Add Custom CSS

Create a CSS file to define the color theme and other style customizations.

### File Structure
```plaintext
my_app/
├── static/
│   ├── admin/
│   │   ├── custom_admin.css
```

### Example `custom_admin.css`
```css
/* Change background color */
/* Custom Background for Admin Panel */
body {
    background-color: #f9f9f9 !important;
}

/* Custom Header */
#header {
    background-color: #003366 !important;
    color: #ffffff !important;
}

/* Customize H1 Titles */
h1 {
    font-family: "Verdana", sans-serif;
    color: #0099cc;
}

```

---

## Step 3: Verify Static Files Configuration

Ensure your static files are configured correctly in `settings.py`.



---

## Step 4: Run Your Project

Start your Django development server to view the changes.

```bash
python manage.py runserver
```

Access the admin panel at `http://127.0.0.1:8000/admin/` to see the customized theme and title.

---

## Debugging Tips
- Ensure your app is included in the `INSTALLED_APPS` setting in `settings.py`.
- Confirm that your `custom_admin.css` file is in the correct path within the `static` directory.
- Use browser developer tools to verify if the custom CSS is loading correctly.
- Restart the development server after making changes.

---

By following these steps, you can easily customize the look and feel of the Django admin panel to align with your project's branding.

