import csv
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.category.models import Category
from apps.product.forms import CreateProductForm, CSVUploadForm, CreateProductAddOnForm, CreateProductAddOnOptionForm
from apps.product.models import Product, ProductAddOn, ProductAddOnOption


class CreateProductView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'admin/product/form.html'
    success_message = "Product created successfully"
    success_url = reverse_lazy('admin-product-list')


class UpdateProductView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'admin/product/form.html'
    success_message = "Product updated successfully"
    success_url = reverse_lazy('admin-product-list')



class ListProductView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/product/lists.html'


class ListProductViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Product
    columns = ['category','name','price','description','available','stock','is_feature','is_popular','actions']
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

        if column == 'actions':
            addon_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">add on</a>'.format(
                reverse('admin-product-addon-list', kwargs={'product_id': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-product-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-product-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action + addon_action
        else:
            return super(ListProductViewJson, self).render_column(row, column)


class DeleteProductView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            if not csv_file.name.endswith('.csv'):
                form.add_error('csv_file', 'This is not a CSV file.')
                return render(request, 'admin/product/csv_upload.html', {'form': form})


            file_data = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(file_data)
            for row in reader:
                print("row", row)
                category = row['Category']
                name = row['Product']
                price = row['Price']
                description = row['Description']
                available = row['Available']
                stock = row['Stock']
                is_feature = row['Feature']
                is_popular = row['Popular']

                category_obj, created = Category.objects.get_or_create(name=category)
                Product.objects.create(
                    category=category_obj,
                    name=name,
                    price=price,
                    description=description,
                    available=available,
                    stock=stock,
                    is_feature=is_feature,
                    is_popular=is_popular,

                )




            return render(request,'admin/product/lists.html')

    else:
        form = CSVUploadForm()

    return render(request, 'admin/product/csv_upload.html', {'form': form})



#product-addon--------------------------------------------------


class CreateProductAddOnView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ProductAddOn
    form_class = CreateProductAddOnForm
    template_name = 'admin/product/form.html'
    success_message = "Add-on created successfully"
    success_url = reverse_lazy('admin-product-list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_id'] = self.kwargs['product_id']
        return context

    def form_valid(self, form):
        addon_obj = form.save(commit=False)
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        addon_obj.product = product
        addon_obj.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ListProductAddOnView(TemplateView):
    template_name = 'admin/product/addon_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_id'] = kwargs['product_id']
        return context



class ListProductAddOnViewJson(AdminRequiredMixin, AjayDatatableView):
    model = ProductAddOn
    columns = ['product', 'title', 'type', 'is_required','actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        product_id = self.request.GET.get('product_id')
        return self.model.objects.filter(product_id=product_id)

#add-on-option-button--------
    def render_column(self, row, column):
        if column == 'is_active':
            if row.is_active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'

        if column == 'actions':
            addonoption_action = '<a href={} role="button" class="btn btn-danger btn-xs mr-1 text-white">add on option</a>'.format(
                reverse('admin-product-addon-option-list', kwargs={'productaddon_id': row.pk}))

            return addonoption_action
        else:
            return super(ListProductAddOnViewJson, self).render_column(row, column)


#product-addon-option----------------------
class CreateProductAddOnOptionView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ProductAddOnOption
    form_class = CreateProductAddOnOptionForm
    template_name = 'admin/product/form.html'
    success_message = "Add-on-option created successfully"
    success_url = reverse_lazy('admin-product-list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productaddon_id'] = self.kwargs['productaddon_id']
        return context

    def form_valid(self, form):
        addonoption_obj = form.save(commit=False)
        productaddon_id = self.kwargs['productaddon_id']
        product = get_object_or_404(ProductAddOn, id=productaddon_id)
        addonoption_obj.addon = product
        addonoption_obj.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ListProductAddOnOptionView(TemplateView):
    template_name = 'admin/product/addon_option_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productaddon_id'] = kwargs['productaddon_id']
        return context



class ListProductAddOnOptionViewJson(AdminRequiredMixin, AjayDatatableView):
    model = ProductAddOnOption
    columns = ['addon', 'title', 'price']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        addon_id = self.request.GET.get('productaddon_id')
        return self.model.objects.filter(addon_id=addon_id)