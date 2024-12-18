import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from .utils import convert_docx_to_pdf

def upload_and_convert(request):
    """Handles file upload and conversion"""
    if request.method == 'POST' and request.FILES['docx_file']:
        docx_file = request.FILES['docx_file']

        # Save the file to the file system
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # Save in the MEDIA_ROOT folder
        filename = fs.save(docx_file.name, docx_file)
        uploaded_file_path = fs.path(filename)  # Get the full path to the file
        print(f"File uploaded at: {uploaded_file_path}")

        # Define the directory where the file is stored (outside the app)
        docx_file_path = uploaded_file_path

        # Convert .docx to .pdf (calling the conversion function)
        pdf_file_path = convert_docx_to_pdf(docx_file_path)

        if pdf_file_path:
            with open(pdf_file_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_file_path)}"'
                return response
        else:
            return HttpResponse("Error converting the file.", status=500)

    return render(request, 'upload_form.html')
