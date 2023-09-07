class Turnero():
    def __init__(self, empresa: str, area: str) -> None:
        self.empresa = empresa
        self.area = area

    
    def __str__(self) -> str:
        return f"Va a solicitar un turno para {self.empresa}. En su area de {self.area} "


    def generar_turno(self) -> None:
        num_turno = 1
        while True:
            yield num_turno
            num_turno += 1