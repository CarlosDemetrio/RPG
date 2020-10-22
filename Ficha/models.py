from django.db import models


class Vantagem(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    level = models.IntegerField(default=1)
    
    def __str__(self):
        return self.nome


class Habilidade(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    level = models.IntegerField(default=1)
    
    def __str__(self):
        return self.nome


class Aptidao(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    pontos = models.IntegerField()
    
    def __str__(self):
        return self.nome


class Virtude(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    pontos = models.IntegerField()
    
    def __str__(self):
        return self.nome


class Ficha(models.Model):
    TIPOS = (
        ('player', 'jogador'),
        ('npc', 'npc')
    )
    nomePersonagem = models.CharField(max_length=20)
    tipo = models.CharField(max_length=15, choices=TIPOS, default=TIPOS[1])
    indole = models.CharField(max_length=20)
    presenca = models.CharField(max_length=20)
    raca = models.CharField(max_length=20)
    exp = models.IntegerField(default=0)
    classe = models.CharField(max_length=20)
    insolitus = models.CharField(max_length=20)
    forca = models.IntegerField(default=0)
    velocidade = models.IntegerField(default=0)
    resistencia = models.IntegerField(default=0)
    inteligencia = models.IntegerField(default=0)
    sabedoria = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)
    prospeccao = models.CharField(max_length=20)
    forcaestatica = models.IntegerField(default=0)
    Forcaespiritual = models.IntegerField(default=0)
    vida = models.IntegerField(default=0)
    bonusbba = models.IntegerField(default=0)
    bonusreflexo = models.IntegerField(default=0)
    bonusbloqueio = models.IntegerField(default=0)
    bonusbbm = models.IntegerField(default=0)
    bonusrment = models.IntegerField(default=0)
    bonusmanipulacao = models.IntegerField(default=0)
    create_data = models.DateTimeField(auto_now_add=True)
    vantagens = models.ManyToManyField(Vantagem)
    aptidao = models.ManyToManyField(Aptidao)
    virtude = models.ManyToManyField(Virtude)
    habilidades = models.ManyToManyField(Habilidade)
    
    def __str__(self):
        return self.nomePersonagem


class Up(models.Model):
    level = models.IntegerField(default=0)
    atributos = models.IntegerField(default=0)
    vantagem = models.IntegerField(default=0)
    aptidao = models.IntegerField(default=0)
    virtude = models.IntegerField(default=0)
    vida = models.IntegerField(default=0)
    habilidades = models.IntegerField(default=0)
