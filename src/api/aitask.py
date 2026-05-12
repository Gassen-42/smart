
from openai import OpenAI
import json
class AiTask:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        
    def generate_sub_tasks(self, title: str, description: str)->list[dict]:
        prompt = f"""""
        vous etes doue en decomposition de taches pour arriver a une fin.
        #role
        decomposer la tache suivante en 3 a 5 sous taches concretes restez precis
        pour chaque tache.Tache: {title}
         Description: {description}
         
         Réponds uniquement sous forme de JSON (une liste d'objets) avec les clés :
        'title' et 'priority'. CLassez les choix en fonction des priorites (choisir entre low, medium, high).
         """
        response = self.client.chat.completions.create(
             model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
         )
        result = json.loads(response.choices[0].message.content)
        return result.get("subtasks", result) # Selon la structure du JSON renvoyé
        
        
    
    
    
    
    
  