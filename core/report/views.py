from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReportForm, ReportDeleteForm, CommentForm
from .models import Report

@login_required
def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('report:success')
    else:
        form = ReportForm()
    return render(request, 'report.html', {'form': form})

@login_required
def success_view(request):
    return render(request, 'success.html')

@login_required
def report_list(request):
    reports = Report.objects.filter(user=request.user)
    comment_form = CommentForm()
    return render(request, 'report_list.html', {'reports': reports, 'comment_form': comment_form})

@login_required
def edit_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report:report_list')
    else:
        form = ReportForm(instance=report)
    
    return render(request, 'edit_report.html', {'form': form})

@login_required
def delete_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        report.delete()
        return redirect('report:report_list')
    
    form = ReportDeleteForm()
    
    return render(request, 'delete_report.html', {'report': report, 'form': form})


@login_required
def like_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if report.likes.filter(id=request.user.id).exists():
        report.likes.remove(request.user)
    else:
        report.likes.add(request.user)
    return redirect('user:dashboard')

@login_required
def add_comment(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.report = report
            comment.save()
    return redirect('user:dashboard')


@login_required
def map_view(request):
    reports = Report.objects.exclude(latitude__isnull=True, longitude__isnull=True)  # Filtrar reportes con coordenadas
    report_list = [
        {
            'user': report.user.username,
            'pet_description': report.pet_description,
            'post_description': report.post_description,
            'latitude': float(report.latitude),
            'longitude': float(report.longitude),
            'media': report.media.url if report.media else ''
        }
        for report in reports
    ]
    return render(request, 'maps.html', {'reports': report_list})