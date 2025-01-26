from pydantic import BaseModel
from typing import List, Optional

class EvolutionBase(BaseModel):
    id: int
    base_form: str
    evolution_conditions: str
    first_evolution_form: str
    evolution_conditions_2: str
    second_evolution_form: str

    class Config:
        from_attributes = True

class EvolutionCreate(BaseModel):
    base_form: Optional[str] = None
    evolution_conditions: Optional[str] = None
    first_evolution_form: Optional[str] = None
    evolution_conditions_2: Optional[str] = None
    second_evolution_form: Optional[str] = None
