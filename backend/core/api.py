from ninja_extra import NinjaExtraAPI, api_controller, route


api = NinjaExtraAPI(title="Teste", version="1.0.0")


@api_controller(
    '/teste',
    tags=["Teste"],
)

class TesteController:
    @route.get('/')
    def get(self, request):
        return "GET"

    @route.post('/')
    def post(self, request):
        return "POST"

    @route.put('/')
    def put(self, request):
        return "PUT"

    @route.delete('/')
    def delete(self, request):
        return "DELETE"
    

api.register_controllers(TesteController)