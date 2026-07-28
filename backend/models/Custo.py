from dataclasses import dataclass

@dataclass
class Custo:
    """Classe mãe para alocação de custos/faturamento."""
    alocacao: str
    conta_faturamento: str

@dataclass
class CustoAPP(Custo):
    conta_app: str = ""

@dataclass
class CustoCentro(Custo):
    centro_custo: str = ""