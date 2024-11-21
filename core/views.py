from django.views.generic import TemplateView
import json


class HomeView(TemplateView):
    template_name = 'home/index.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'


class ClassificationView(TemplateView):
    template_name = 'home/classification.html'


class RoutesView(TemplateView):
    template_name = 'home/routes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        routes = [
            {
                "name": "Ruta 1",
                "distance": 5.2,
                "time": 15,
                "start": {"lat": -34.6037, "lng": -58.3816},
                "end": {"lat": -34.6100, "lng": -58.4000},
                "coordinates": [
                    {"lat": -34.6037, "lng": -58.3816},
                    {"lat": -34.6060, "lng": -58.3900},
                    {"lat": -34.6100, "lng": -58.4000},
                ],
            },
            {
                "name": "Ruta 2",
                "distance": 8.3,
                "time": 20,
                "start": {"lat": -34.6037, "lng": -58.3816},
                "end": {"lat": -34.6200, "lng": -58.4100},
                "coordinates": [
                    {"lat": -34.6037, "lng": -58.3816},
                    {"lat": -34.6150, "lng": -58.3950},
                    {"lat": -34.6200, "lng": -58.4100},
                ],
            },
        ]

        # Convertir rutas a JSON para enviarlas al template
        context["routes"] = routes
        context["routes_json"] = json.dumps(routes)
        return context
    

class ContainersView(TemplateView):
    template_name = 'home/containers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Simular datos de contenedores
        containers = [
            {
                "name": "Contenedor 1",
                "location": "Av. Siempre Viva 123",
                "status": "Lleno",
                "lat": -34.6037,
                "lng": -58.3816,
            },
            {
                "name": "Contenedor 2",
                "location": "Calle Falsa 456",
                "status": "Medio",
                "lat": -34.6067,
                "lng": -58.3916,
            },
            {
                "name": "Contenedor 3",
                "location": "Boulevard 789",
                "status": "Vacío",
                "lat": -34.6087,
                "lng": -58.4016,
            },
        ]

        # Convertir a JSON para enviarlo al template
        context["containers"] = containers
        context["containers_json"] = json.dumps(containers)
        return context