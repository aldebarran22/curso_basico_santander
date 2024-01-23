"""
Crear un histograma de países. 
Cuantas veces aparece cada país
"""

txt = """Finlandia
Alemania
Brasil
Francia
Belgica
Brasil
Suiza
Suiza
Brasil
Venezuela
Austria
Mexico
Alemania
Brasil
Estados Unidos
Austria
Suecia
Francia
Finlandia
Alemania
Venezuela
Estados Unidos
Finlandia
Estados Unidos
Estados Unidos
Alemania
Francia
Italia
Mexico
Alemania
Suecia
Alemania
Suecia
Espanya
Espanya
Venezuela
Alemania
Alemania
Alemania
Brasil
Italia
Reino Unido
Brasil
Brasil
Brasil
Mexico
Estados Unidos
Francia
Venezuela
Francia
Irlanda
Brasil
Italia
Alemania
Belgica
Espanya
Mexico
Estados Unidos
Espanya
Estados Unidos
Mexico
Irlanda
Estados Unidos
Francia
Alemania
Alemania
Estados Unidos
Reino Unido
Estados Unidos
Estados Unidos
Reino Unido
Mexico
Finlandia
Reino Unido
Mexico
Alemania
Estados Unidos
Alemania
Espanya
Suecia
Portugal
Estados Unidos
Venezuela
Francia
Canada
Finlandia
Francia
Irlanda
Portugal
Alemania
Estados Unidos
Canada
Francia
Dinamarca
Alemania
Alemania
Estados Unidos
Alemania
Estados Unidos
Brasil
Alemania
Estados Unidos
Francia
Austria
Portugal
Austria
Mexico
Reino Unido
Alemania
Venezuela
Francia
Reino Unido
Francia
Alemania
Francia
Alemania
Reino Unido
Mexico
Espanya
Dinamarca
Austria
Estados Unidos
Suiza
Francia
Brasil
Irlanda
Polonia
Estados Unidos
Canada
Reino Unido
Suecia
Brasil
Irlanda
Venezuela
Austria
Reino Unido
Suecia
Estados Unidos
Brasil
Noruega
Reino Unido
Canada
Austria
Alemania
Austria
Estados Unidos
Estados Unidos
Venezuela
Alemania
Portugal
Estados Unidos
Dinamarca
Reino Unido
Estados Unidos
Austria
Austria
Italia
Venezuela
Brasil
Alemania
Francia
Argentina
Canada
Canada
Finlandia
Francia
Brasil
Estados Unidos
Finlandia
Dinamarca
Alemania
Suiza
Brasil
Brasil
Italia
Brasil
Canada
Francia
Espanya
Austria
Italia
Irlanda
Austria
Canada
Estados Unidos
Portugal
Suecia
Reino Unido
Francia
Finlandia
Alemania
Canada
Estados Unidos
Estados Unidos
Austria
Italia
Suecia
Suecia
Alemania
Brasil
Argentina
Francia
Francia
Alemania
Estados Unidos
Reino Unido
Francia
Finlandia
Alemania
Alemania
Belgica
Francia
Suecia
Venezuela
Reino Unido
Belgica
Portugal
Dinamarca
Brasil
Italia
Alemania
Estados Unidos
Francia
Reino Unido
Reino Unido
Reino Unido
Mexico
Belgica
Venezuela
Portugal
Francia
Estados Unidos
Francia
Brasil
Estados Unidos
Estados Unidos
Reino Unido
Venezuela
Venezuela
Brasil
Alemania
Austria
Venezuela
Portugal
Canada
Francia
Brasil
Canada
Brasil
Alemania
Venezuela
Venezuela
Francia
Alemania
Mexico
Irlanda
Estados Unidos
Canada
Alemania
Mexico
Alemania
Alemania
Estados Unidos
Francia
Brasil
Alemania
Austria
Alemania
Irlanda
Reino Unido
Mexico
Suiza
Noruega
Argentina
Alemania
Reino Unido
Suecia
Francia
Finlandia
Alemania
Estados Unidos
Belgica
Austria
Argentina
Reino Unido
Suecia
Alemania
Mexico
Alemania
Suiza
Reino Unido
Reino Unido
Alemania
Brasil
Alemania
Venezuela
Estados Unidos
Estados Unidos
Francia
Reino Unido
Alemania
Alemania
Espanya
Portugal
Venezuela
Finlandia
Alemania
Estados Unidos
Dinamarca
Alemania
Reino Unido
Francia
Alemania
Suecia
Italia
Brasil
Estados Unidos
Canada
Francia
Irlanda
Espanya
Estados Unidos
Canada
Austria
Suecia
Mexico
Estados Unidos
Alemania
Mexico
Estados Unidos
Reino Unido
Estados Unidos
Alemania
Brasil
Alemania
Finlandia
Francia
Brasil
Italia
Brasil
Alemania
Estados Unidos
Canada
Dinamarca
Alemania
Alemania
Estados Unidos
Austria
Estados Unidos
Austria
Estados Unidos
Reino Unido
Estados Unidos
Venezuela
Dinamarca
Estados Unidos
Portugal
Canada
Brasil
Estados Unidos
Alemania
Francia
Francia
Polonia
Estados Unidos
Venezuela
Alemania
Finlandia
Estados Unidos
Estados Unidos
Canada
Canada
Canada
Reino Unido
Brasil
Alemania
Estados Unidos
Mexico
Suecia
Estados Unidos
Francia
Espanya
Alemania
Francia
Alemania
Austria
Francia
Italia
Finlandia
Brasil
Venezuela
Noruega
Alemania
Venezuela
Dinamarca
Alemania
Brasil
Brasil
Irlanda
Brasil
Brasil
Belgica
Brasil
Alemania
Brasil
Alemania
Suecia
Italia
Estados Unidos
Estados Unidos
Alemania
Brasil
Estados Unidos
Irlanda
Estados Unidos
Francia
Portugal
Estados Unidos
Suiza
Austria
Alemania
Dinamarca
Alemania
Francia
Suecia
Finlandia
Reino Unido
Alemania
Mexico
Mexico
Estados Unidos
Francia
Estados Unidos
Estados Unidos
Mexico
Francia
Alemania
Brasil
Austria
Irlanda
Dinamarca
Suecia
Brasil
Alemania
Alemania
Estados Unidos
Alemania
Finlandia
Estados Unidos
Venezuela
Austria
Alemania
Estados Unidos
Irlanda
Alemania
Suecia
Brasil
Venezuela
Estados Unidos
Reino Unido
Estados Unidos
Brasil
Italia
Estados Unidos
Irlanda
Estados Unidos
Estados Unidos
Francia
Argentina
Alemania
Alemania
Estados Unidos
Brasil
Alemania
Estados Unidos
Estados Unidos
Canada
Brasil
Reino Unido
Italia
Brasil
Venezuela
Francia
Suiza
Francia
Suecia
Brasil
Estados Unidos
Irlanda
Francia
Francia
Francia
Estados Unidos
Suecia
Canada
Reino Unido
Dinamarca
Alemania
Suiza
Austria
Estados Unidos
Reino Unido
Finlandia
Suiza
Reino Unido
Italia
Italia
Francia
Estados Unidos
Estados Unidos
Suiza
Mexico
Belgica
Estados Unidos
Suecia
Francia
Austria
Alemania
Alemania
Belgica
Reino Unido
Dinamarca
Brasil
Austria
Alemania
Austria
Suecia
Estados Unidos
Austria
Brasil
Suecia
Alemania
Venezuela
Finlandia
Argentina
Brasil
Italia
Venezuela
Brasil
Francia
Alemania
Francia
Brasil
Alemania
Polonia
Reino Unido
Brasil
Austria
Venezuela
Alemania
Reino Unido
Alemania
Reino Unido
Espanya
Dinamarca
Brasil
Reino Unido
Estados Unidos
Francia
Italia
Estados Unidos
Brasil
Canada
Venezuela
Italia
Brasil
Francia
Estados Unidos
Estados Unidos
Alemania
Italia
Argentina
Estados Unidos
Estados Unidos
Estados Unidos
Venezuela
Suecia
Alemania
Francia
Francia
Argentina
Reino Unido
Brasil
Noruega
Francia
Alemania
Brasil
Alemania
Austria
Suecia
Venezuela
Brasil
Venezuela
Belgica
Mexico
Francia
Austria
Alemania
Belgica
Estados Unidos
Reino Unido
Alemania
Francia
Brasil
Estados Unidos
Alemania
Austria
Estados Unidos
Mexico
Suecia
Francia
Alemania
Francia
Estados Unidos
Alemania
Venezuela
Reino Unido
Alemania
Suecia
Estados Unidos
Brasil
Reino Unido
Estados Unidos
Francia
Espanya
Finlandia
Espanya
Suecia
Francia
Brasil
Alemania
Finlandia
Suecia
Argentina
Estados Unidos
Estados Unidos
Estados Unidos
Belgica
Brasil
Espanya
Espanya
Estados Unidos
Francia
Alemania
Belgica
Alemania
Estados Unidos
Austria
Belgica
Irlanda
Argentina
Venezuela
Brasil
Venezuela
Suecia
Brasil
Estados Unidos
Brasil
Polonia
Francia
Italia
Noruega
Finlandia
Espanya
Irlanda
Brasil
Brasil
Mexico
Argentina
Espanya
Canada
Venezuela
Reino Unido
Dinamarca
Brasil
Francia
Suecia
Brasil
Mexico
Francia
Espanya
Alemania
Belgica
Suiza
Francia
Reino Unido
Alemania
Brasil
Estados Unidos
Argentina
Alemania
Italia
Francia
Estados Unidos
Italia
Reino Unido
Canada
Alemania
Dinamarca
Reino Unido
Espanya
Canada
Italia
Suiza
Alemania
Reino Unido
Venezuela
Suecia
Alemania
Venezuela
Argentina
Brasil
Venezuela
Brasil
Alemania
Portugal
Francia
Estados Unidos
Suiza
Alemania
Austria
Brasil
Espanya
Francia
Francia
Francia
Estados Unidos
Canada
Venezuela
Suecia
Belgica
Austria
Suecia
Brasil
Canada
Estados Unidos
Estados Unidos
Irlanda
Argentina
Reino Unido
Estados Unidos
Brasil
Austria
Alemania
Estados Unidos
Suecia
Dinamarca
Mexico
Alemania
Venezuela
Polonia
Alemania
Estados Unidos
Suecia
Estados Unidos
Estados Unidos
Belgica
Finlandia
Estados Unidos
Portugal
Austria
Espanya
Italia
Alemania
Alemania
Espanya
Venezuela
Noruega
Reino Unido
Austria
Estados Unidos
Argentina
Alemania
Alemania
Brasil
Reino Unido
Reino Unido
Finlandia
Italia
Canada
Alemania
Suiza
Estados Unidos
Estados Unidos
Estados Unidos
Suiza
Estados Unidos
Belgica
Alemania
Espanya
Belgica
Venezuela
Estados Unidos
Suiza
Brasil
Francia
Polonia
Canada
Alemania
Reino Unido
Canada
Brasil
Suecia
Francia
Brasil
Austria
Argentina
Venezuela
Reino Unido
Reino Unido
Alemania
Brasil
Italia
Estados Unidos
Italia
Irlanda
Estados Unidos
Venezuela
Estados Unidos
Alemania
Brasil
Mexico
Alemania
Venezuela
Austria
Mexico
Dinamarca
Suiza
Francia
Estados Unidos
"""
