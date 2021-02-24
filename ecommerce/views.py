import random

from django.views import generic
from django.templatetags.static import static

from faker import Faker
fake = Faker()


def generate_random_product():
    return {
        "brand_name": fake.name(),
        "product_name": fake.name(),
        "image_url": "Test",
        "price": abs(round(fake.pyfloat(), 2)),
        "sale": fake.pybool(),
        "img_url": static(f'images/{random.choice(["numeric", "keyboard", "mouse", "ethernet", "hdmi-adapter"])}.png')
    }


def product_generator(count):
    return [generate_random_product() for _ in range(0, count)]


class ProductBase:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = product_generator(self.DUMP_PRODUCT_COUNT)
        return context


class Ecommerce(ProductBase, generic.TemplateView):
    template_name = "ecommerce.html"
    DUMP_PRODUCT_COUNT = 6
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = product_generator(4)
        return context


class ProductsView(ProductBase, generic.TemplateView):
    DUMP_PRODUCT_COUNT = 5
    template_name = "product_list.html"
