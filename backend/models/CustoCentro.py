from dataclasses import dataclass, field

from models.Custo import Custo

# faturamento (filhos)
@dataclass
class CustoCentro(Faturamento):
    centro_custo: str
