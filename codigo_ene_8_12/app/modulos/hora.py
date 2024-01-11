
class TimeError(Exception):
    """
    Clase que gestiona los errores con el tiempo.
    """

    def __init__(self, mensaje=""):
        Exception.__init__(self, mensaje)


class Time:
    def __init__(self, hh=0, mm=0, ss=0):
        if not (0 <= hh <= 23):
            raise TimeError("Las horas deben estar entre 0 y 23")

        if not (0 <= mm <= 59):
            raise TimeError("Los minutos deben estar entre 0 y 59")

        if not (0 <= ss <= 59):
            raise TimeError("Los segundos deben estar entre 0 y 59")

        # definir los att con acceso privado
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    def ajustar(self):
        minutos = self.__ss // 60
        self.__ss %= 60
        self.__mm += minutos

        horas = self.__mm // 60
        self.__hh += horas
        self.__mm %= 60

    def __add__(self, other):
        resul = Time(
            self.__hh + other.__hh, self.__mm + other.__mm, self.__ss + other.__ss
        )
        resul.ajustar()
        return resul

    def __str__(self):
        # Resultado: 15:02:06
        return "%02d:%02d:%02d" % (self.__hh, self.__mm, self.__ss)


