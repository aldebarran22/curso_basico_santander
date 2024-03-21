"""Clase Time"""

class Time:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __add__(self, other):
        resul = Time(self.h + other.h, self.m + other.m, self.s + other.s)
        resul.ajustar()
        return resul

    def ajustar(self):
        minutos = self.s // 60
        self.s %= 60
        self.m += minutos
        horas = self.m // 60
        self.m %= 60
        self.h += horas

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)