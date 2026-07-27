from dataclasses import dataclass, field

# hierarquia do faturamento (mãe) 
@dataclass
class Custo:
    alocacao: str
    conta_faturamento: str