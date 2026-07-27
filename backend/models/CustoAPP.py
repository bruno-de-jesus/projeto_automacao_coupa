from dataclasses import dataclass, field

from models.Custo import Custo

# faturamento (filhos)
@dataclass
class CustoAPP(Faturamento):
    conta_app: str