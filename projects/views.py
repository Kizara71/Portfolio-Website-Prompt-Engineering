from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    # Split key features by newline or comma for better rendering if needed
    features = [f.strip() for f in project.key_features.replace('\n', ',').split(',') if f.strip()]
    
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'features': features
    })

def resume(request):
    return render(request, 'projects/resume.html')
