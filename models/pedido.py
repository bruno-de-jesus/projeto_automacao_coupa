from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum, auto
from datetime import date

# definição de tipos de pedidos com enum
class TipoPedido(Enum):
    MATERIAL = auto()
    SERVICO = auto()

# informações gerais do pedido
@dataclass
class InformacoesGerais:
    solicitante: str
    fornecedor: str
    texto_cabecalho: str
    tipo: TipoPedido
    orcamento: Optional[str] = None

# hierarquia do faturamento (mãe) 
@dataclass
class Faturamento:
    alocacao: str
    conta_faturamento: str

# faturamento (filhos)
@dataclass
class CustoCentro(Faturamento):
    centro_custo: str

@dataclass
class CustoAPP(Faturamento):
    conta_app: str

# hierarquia de itens (mãe)
@dataclass
class Item:
    descricao: str
    commodity: str
    preco: float
    data_final: date
    termo_inco: str
    codigo_tributario: str

# item (filhos)
@dataclass
class ItemMaterial(Item):
    quantidade: float
    codigo_ncm: str
    origem_material: str

@dataclass
class ItemServico(Item):
    data_inicio: date
    confirmador_servico: str

# classe principal
@dataclass
class Pedido:
    informacoes: InformacoesGerais
    faturamento: Faturamento
    itens: List(Item) = field(default_factory=list)