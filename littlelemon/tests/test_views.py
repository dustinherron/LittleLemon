from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Menu.objects.create(
            title="Humus",
            price=7.99,
            inventory=23
        )
        Menu.objects.create(
            title="Pita",
            price=1.99,
            inventory=4
        )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuItemSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)