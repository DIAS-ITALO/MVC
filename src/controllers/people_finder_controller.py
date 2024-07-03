from typing import Dict
from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person

class PeopleFinderController:
    def find_by_name(self, person_finder_informations: Dict) -> Dict:
        try:
            self.__validate_fields(person_finder_informations)
            person = self.__find_person(person_finder_informations)
            response = self.__format_response(person)
            return {"sucess": True, "message": response}
        except Exception as exception:
            pass
        
    def __validate_fields(self, person_finder_informations: Dict) -> None:
        if not isinstance(person_finder_informations["name"], str):
            raise Exception('Campo Nome Invalido')
        
    def __find_person(self, person_finder_informations: Dict):
        name = person_finder_informations["name"]
        
        person = person_repository.find_person_by_name(name)
        if not person: raise Exception('Pessoa não encontrada!')
        
        return person
        
        
    def __format_response(self, person: any) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "infos": {
                "name": person.name,
                "age": person.age,
                "height": person.height
            }
        }
        