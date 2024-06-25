from typing import Dict  

class PeopleRegisterController:
    def register(selg, new_person_informations: Dict) -> Dict:
        self.__validate_fields(new_person_informations)
        #enviar para models para cadastro de dados
        response = self.__format_response(new_person_informations)
    
    def __validate_fields(self, new_person_informations: Dict) -> None:
        if not isisntance(new_person_informations["name"], str):
            raise Exception('Campo Nome Incorreto')
        
        try: int(new_person_informations["age"])
        except: raise Exception('Campo Idade Incorreto!')
        
        try: int(new_person_informations["height"])
        except: raise Exception('Campo Altura Incorreto!')
        
    def __format_response(self, new_person_informations: Dict) -> Dict:
        pass
        