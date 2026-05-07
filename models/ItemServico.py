from dataclasses import dataclass, field

from models.Item import Item

# item (filhos)
@dataclass
class ItemServico(Item):
    data_inicio: date
    confirmador_servico: str
