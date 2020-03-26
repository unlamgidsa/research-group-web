---
title: Telemetría de alta performance

notitle: true

description: |
  Telemetría de alta performance sobre motores de bases de datos hibridos

people:
  - Pablo
  - Jorge
  
  
layout: project
image: "/img/timescale2.png"
#
last-updated: 2020-03-01
---

Telemetría de alta performance sobre bases de datos hibridas

## Telemetría de alta performance sobre base de datos hibridas

El UGS(UNLaM Ground Segment) utiliza un RDBMS desde su primera versión. Estos sistemas permiten un almacenamiento seguro, de acceso estandarizado y concurrente, una alta fiabilidad y mecanismos que garantizan la integridad. Todas estas características tienen un costo asociado y en grandes volúmenes de datos la eficiencia del sistema puede resentirse. El UGS accede a la base de datos mediante un ORM produciendo un diseño relacional altamente normalizado, condición que limita la eficiencia en el acceso a los datos. En función de los objetivos de mediano plazo de alojar grandes volumenes de datos de varias misiones se opta por continuar trabajando sobre un motor relacional pero transformando en hipertablas aquellas entidades vinculadas con series de datos evitando desnormalizaciones y manteniendo la solución costo-efectiva.

