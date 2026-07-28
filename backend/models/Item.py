from dataclasses import dataclass
from datetime import date

@dataclass
class Item:
    """Classe mãe para itens da requisição."""
    descricao: str
    commodity: str
    preco: float
    data_final: date
    termo_inco: str
    codigo_tributario: str

@dataclass
class ItemMaterial(Item):
    quantidade: float = 1.0
    codigo_ncm: str = ""
    origem_material: str = ""

@dataclass
class ItemServico(Item):
    data_inicio: date = None
    confirmador_servico: str = ""