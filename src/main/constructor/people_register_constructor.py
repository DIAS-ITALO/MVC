from src.views.people_register_view import PeopleRegisterView
from src.controllers.people_register_controller import PeopleRegisterController

def people_register_constructor():
    people_register_view = PeopleRegisterView()
    people_register_controller = PeopleRegisterController
    
    new_person_informations = people_register_view.registry_person_view()
    people_register_controller.register(new_person_informations)
    