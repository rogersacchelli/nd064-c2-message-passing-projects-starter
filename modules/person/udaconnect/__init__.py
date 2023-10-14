from person.udaconnect.models import Person  # noqa
from person.udaconnect.schemas import  PersonSchema  # noqa


def register_routes(api, person, root="api"):
    from person.udaconnect.main import api as udaconnect_api_person

    api.add_namespace(udaconnect_api_person, path=f"/api")
