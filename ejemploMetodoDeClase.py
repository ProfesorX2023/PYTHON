class Lazaro:
    vivo = "Esta muerto"

    @classmethod
    def revivir(cls):
        cls.vivo = "Lazaro revive"
        print(cls.vivo)

Lazaro.revivir()