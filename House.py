from pydantic import BaseModel
from typing import Optional, Literal
import math

class House(BaseModel):
    Region: Literal[
        'Ariana', 'Nabeul', 'La_Manouba', 'Ben_Arous', 'Bizerte', 'Tunis', 'Sfax',
        'Monastir', 'Sousse', 'Zaghouan', 'Médenine', 'Gafsa', 'Béja', 'Jendouba',
        'Le_Kef', 'Kairouan', 'Gabès', 'Mahdia', 'Siliana', 'Sidi_Bouzid', 'Tozeur',
        'Kasserine'
    ]
    Type: Literal['Appartement', 'Villa']
    Area: float
    Bathrooms: int
    Bedrooms: int

    def Area_x_Bathrooms(self) -> float:
        return self.Area * self.Bathrooms

    def Log_Area(self) -> float:
        return math.log1p(self.Area)

    def Bathrooms_per_Bedroom(self) -> Optional[float]:
        if self.Bedrooms > 0:
            return self.Bathrooms / self.Bedrooms
        return None
    
    def format_region(self) -> str:
        return self.Region.replace(' ', '_')
    
    def format_type(self) -> str:
        return self.Type.replace(' ', '_')

    def transformed_features(self) -> dict:
        return {
            'Region': self.format_region(),
            'Type': self.format_type(),
            'Area_x_Bathrooms': self.Area_x_Bathrooms(),
            'Log_Area': self.Log_Area(),
            'Bathrooms_per_Bedroom': self.Bathrooms_per_Bedroom()
        }