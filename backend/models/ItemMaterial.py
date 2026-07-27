from dataclasses import dataclass, field

from models.Item import Item

# item (filhos)
@dataclass
class ItemMaterial(Item):
    quantidade: float
    codigo_ncm: str
    origem_material: str