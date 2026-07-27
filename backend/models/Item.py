from dataclasses import dataclass, field
from datetime import date

# hierarquia de itens (mãe)
@dataclass
class Item:
    descricao: str
    commodity: str
    preco: float
    data_final: date
    termo_inco: str
    codigo_tributario: str