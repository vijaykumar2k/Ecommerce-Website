from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.vender.forms import CreateVenderForm
from apps.vender.models import Vender


class CreateVenderView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Vender
    form_class = CreateVenderForm
    template_name = 'admin/vender/form.html'
    success_message = "Vender created successfully"
    success_url = reverse_lazy('admin-vender-list')


class UpdateVenderView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Vender
    form_class = CreateVenderForm
    template_name = 'admin/vender/form.html'
    success_message = "Vender updated successfully"
    success_url = reverse_lazy('admin-vender-list')



class ListVenderView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/vender/lists.html'


class ListVenderViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Vender
    columns = ['user','name','address','open_at','close_at','image','lat','long','actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        return self.model.objects.all()

    def render_column(self, row, column):
        if column == 'is_active':
            if row.is_active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'

        if column=='image':
            return f'<img src="{row.image.url}"  width="100px" >'

        if column == 'actions':
            # detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
            #     reverse('admin-vender-detail', kwargs={'pk': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-vender-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-vender-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
        else:
            return super(ListVenderViewJson, self).render_column(row, column)

class DeleteVenderView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Vender

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)