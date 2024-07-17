from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.cart.forms import CreateCartForm
from apps.cart.models import Cart


class CreateCartView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cart
    form_class = CreateCartForm
    template_name = 'admin/cart/form.html'
    success_message = "Cart created successfully"
    success_url = reverse_lazy('admin-cart-list')


class UpdateCartView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cart
    form_class = CreateCartForm
    template_name = 'admin/cart/form.html'
    success_message = "Cart updated successfully"
    success_url = reverse_lazy('admin-cart-list')



class ListCartView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/cart/lists.html'


class ListCartViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Cart
    columns = ['user','vender','actions']
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
            #     reverse('admin-cart-detail', kwargs={'pk': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-cart-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-cart-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
        else:
            return super(ListCartViewJson, self).render_column(row, column)

class DeleteCartView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Cart

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)
