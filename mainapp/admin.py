from django.contrib import admin
from .models import Request, Volunteer, Contributor, DistrictNeed, DistrictCollection, DistrictManager ,vol_categories, RescueCamp, Person
import csv
from django.http import HttpResponse

class RequestAdmin(admin.ModelAdmin):
    actions = ['download_csv','Mark_as_completed','Mark_as_new','Mark_as_ongoing']
    readonly_fields = ('dateadded',)
    ordering = ('district',)
    list_display = ('district', 'location', 'requestee_phone', 'status','summarise')

    def Mark_as_completed(self, request, queryset):
        for i in queryset:
            Request.objects.all().filter(id = i.id).update(status = "sup")
        return

    def Mark_as_new(self, request, queryset):
        for i in queryset:
            Request.objects.all().filter(id = i.id).update(status = "new")
        return
    
    def Mark_as_ongoing(self, request, queryset):
        for i in queryset:
            Request.objects.all().filter(id = i.id).update(status = "pro")
        return

    def download_csv(self, request, queryset):
        f = open('req.csv', 'w')
        writer = csv.writer(f)
        l = []
        for i in (Request._meta.get_fields()):
            l.append(i.name)
        writer.writerow(l)
        data = Request.objects.all().values_list()
        for s in data:

            writer.writerow(s)
        f.close()
        f = open('req.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Requests.csv'
        return response

    list_filter = ('district', 'status',)


class VolunteerAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    readonly_fields = ('joined',)
    list_display = ('name', 'phone', 'organisation', 'joined')
    list_filter = ('district', 'joined',)
    def download_csv(self, request, queryset):
        options = vol_categories
        mapper = {}
        for i in vol_categories:
            mapper[i[0]] = i[1] 
        f = open('vol.csv', 'w')
        writer = csv.writer(f)
        l = []
        for i in (Volunteer._meta.get_fields()):
            l.append(i.name)
        writer.writerow(l)
        data = Volunteer.objects.all().values_list()
        for s in data:
            s = list(s)
            s[6] = mapper[s[6]]
            writer.writerow(s)
        f.close()
        f = open('vol.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Volunteers.csv'
        return response


class ContributorAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_filter = ('district', 'status',)
    def download_csv(self, request, queryset):
        f = open('con.csv', 'w')
        writer = csv.writer(f)
        l = []
        for i in (Contributor._meta.get_fields()):
            l.append(i.name)
        writer.writerow(l)
        data = Contributor.objects.all().values_list()
        for s in data:

            writer.writerow(s)
        f.close()
        f = open('con.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Contributors.csv'
        return response

class RescueCampAdmin(admin.ModelAdmin):
    list_display = ('district', 'name', 'location')

admin.site.register(Request, RequestAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(DistrictNeed)
admin.site.register(DistrictCollection)
admin.site.register(DistrictManager)
admin.site.register(RescueCamp,RescueCampAdmin)