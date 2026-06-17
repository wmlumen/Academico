# Consolidacion de planilla de diagnostico i mm i 2026

Este archivo resume varias versiones con el mismo nombre y contenido distinto.

## Version 1
Fuente: `C:\Users\HP 250 G10\Documents\GITHUT\MEC\MEC\MANUEL MOLINAS\PLANILLA DE DIAGNOSTICO I MM I 2026.xlsx`

### Hoja: Hoja7
<openpyxl.worksheet.formula.ArrayFormula object at 0x00000218BE378590> | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | Ale-02. Presenta lagunas en conocimientos previos. | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 37 | 1 | 0 | A mejorar
Académica | Ale-04. Se limita a memorizar sin comprender. | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | 18 | 1 | 19 | A mejorar
Académica | Ale-06. Entrega tareas incompletas o descuidadas. | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 4 | 4 | 33 | Muy bueno
Académica | Ale-08. Se bloquea ante desafíos matemáticos. | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 18 | 1 | 19 | A mejorar
Académica | Ale-10. Tiene dificultades de expresión oral/escrita. | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 14 | 2 | 23 | A mejorar
Académica | Ale-12. Muestra rechazo o desinterés por la lectura. | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 11 | 3 | 26 | Bueno
Académica | Ale-14. Requiere supervisión constante para avanzar. | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | 19 | 1 | 18 | A mejorar
Académica | Ale-16. Muestra apatía por temas nuevos. | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 7 | 4 | 30 | Muy bueno
Conductual | Ale-18. Desafía activamente la autoridad. | 18. Desafía activamente la autoridad. | Alerta/Mejora | 16 | 1 | 21 | A mejorar
Conductual | Ale-20. Presenta retardos o inasistencias frecuentes. | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 2 | 5 | 35 | Muy bueno
Conductual | Ale-22. Daña el mobiliario o materiales escolares. | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 1 | 5 | 36 | Muy bueno
Conductual | Ale-24. Interrumpe constantemente el flujo de clase. | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 2 | 5 | 35 | Muy bueno
Conductual | Ale-26. Emplea lenguaje soez o despectivo. | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 11 | 3 | 26 | Bueno
Conductual | Ale-28. Miente o culpa a otros por sus actos. | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 19 | 1 | 18 | A mejorar

### Hoja: Hoja9
 |  |  |  |  |  |  |
 | GRADO | SEPTIMO |  |  |  |  |
 | TURNO | TM |  |  |  |  |
 |  |  |  |  |  |  |
 | Etiquetas de fila | Cuenta de NF | Promedio de NF2 | Cuenta de NF2 |  |  |
 | 1 | 34 | 0 | 34 |  |  |
 | 2 | 5 | 0 | 5 |  |  |
 | 3 | 4 | 0 | 4 |  |  |
 | 4 | 4 | 0 | 4 |  |  |
 | 5 | 3 | 0 | 3 |  |  |
 | Total general | 50 | 0 | 50 |  |  |
 |  |  |  |  |  |  |
 |  |  |  |  |  |  |
 |  |  |  |  |  |  |
 |  |  |  |  |  |  |

### Hoja: RESULTADO


### Hoja: 7mo. TM
Categoría | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | =+CONCATENATE(LEFT(D2,3),"-",C2) | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 37 | =IF(D2="Alerta/Mejora",
  IF(E2<=3, 5, IF(E2<=7, 4, IF(E2<=11, 3, IF(E2<=15, 2, 1)))),
  IF(E2>=34, 5, IF(E2>=30, 4, IF(E2>=26, 3, IF(E2>=22, 2, 1))))
) | =+L$1-E2 | =VLOOKUP(F2, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D3,3),"-",C3) | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | =37-19 | =IF(D3="Alerta/Mejora",
  IF(E3<=3, 5, IF(E3<=7, 4, IF(E3<=11, 3, IF(E3<=15, 2, 1)))),
  IF(E3>=34, 5, IF(E3>=30, 4, IF(E3>=26, 3, IF(E3>=22, 2, 1))))
) | =+L$1-E3 | =VLOOKUP(F3, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D4,3),"-",C4) | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 4 | =IF(D4="Alerta/Mejora",
IF(E4<=3, 5, IF(E4<=7, 4, IF(E4<=11, 3, IF(E4<=15, 2, 1)))),
IF(E4>=34, 5, IF(E4>=30, 4, IF(E4>=26, 3, IF(E4>=22, 2, 1))))
) | =+L$1-E4 | =VLOOKUP(F4, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D5,3),"-",C5) | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 18 | =IF(D5="Alerta/Mejora",
IF(E5<=3, 5, IF(E5<=7, 4, IF(E5<=11, 3, IF(E5<=15, 2, 1)))),
IF(E5>=34, 5, IF(E5>=30, 4, IF(E5>=26, 3, IF(E5>=22, 2, 1))))
) | =+L$1-E5 | =VLOOKUP(F5, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D6,3),"-",C6) | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 14 | =IF(D6="Alerta/Mejora",
IF(E6<=3, 5, IF(E6<=7, 4, IF(E6<=11, 3, IF(E6<=15, 2, 1)))),
IF(E6>=34, 5, IF(E6>=30, 4, IF(E6>=26, 3, IF(E6>=22, 2, 1))))
) | =+L$1-E6 | =VLOOKUP(F6, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D7,3),"-",C7) | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 11 | =IF(D7="Alerta/Mejora",
IF(E7<=3, 5, IF(E7<=7, 4, IF(E7<=11, 3, IF(E7<=15, 2, 1)))),
IF(E7>=34, 5, IF(E7>=30, 4, IF(E7>=26, 3, IF(E7>=22, 2, 1))))
) | =+L$1-E7 | =VLOOKUP(F7, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D8,3),"-",C8) | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | =37-18 | =IF(D8="Alerta/Mejora",
IF(E8<=3, 5, IF(E8<=7, 4, IF(E8<=11, 3, IF(E8<=15, 2, 1)))),
IF(E8>=34, 5, IF(E8>=30, 4, IF(E8>=26, 3, IF(E8>=22, 2, 1))))
) | =+L$1-E8 | =VLOOKUP(F8, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D9,3),"-",C9) | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 7 | =IF(D9="Alerta/Mejora",
IF(E9<=3, 5, IF(E9<=7, 4, IF(E9<=11, 3, IF(E9<=15, 2, 1)))),
IF(E9>=34, 5, IF(E9>=30, 4, IF(E9>=26, 3, IF(E9>=22, 2, 1))))
) | =+L$1-E9 | =VLOOKUP(F9, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D10,3),"-",C10) | 18. Desafía activamente la autoridad. | Alerta/Mejora | 16 | =IF(D10="Alerta/Mejora",
IF(E10<=3, 5, IF(E10<=7, 4, IF(E10<=11, 3, IF(E10<=15, 2, 1)))),
IF(E10>=34, 5, IF(E10>=30, 4, IF(E10>=26, 3, IF(E10>=22, 2, 1))))
) | =+L$1-E10 | =VLOOKUP(F10, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D11,3),"-",C11) | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 2 | =IF(D11="Alerta/Mejora",
IF(E11<=3, 5, IF(E11<=7, 4, IF(E11<=11, 3, IF(E11<=15, 2, 1)))),
IF(E11>=34, 5, IF(E11>=30, 4, IF(E11>=26, 3, IF(E11>=22, 2, 1))))
) | =+L$1-E11 | =VLOOKUP(F11, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D12,3),"-",C12) | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 1 | =IF(D12="Alerta/Mejora",
IF(E12<=3, 5, IF(E12<=7, 4, IF(E12<=11, 3, IF(E12<=15, 2, 1)))),
IF(E12>=34, 5, IF(E12>=30, 4, IF(E12>=26, 3, IF(E12>=22, 2, 1))))
) | =+L$1-E12 | =VLOOKUP(F12, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D13,3),"-",C13) | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 2 | =IF(D13="Alerta/Mejora",
IF(E13<=3, 5, IF(E13<=7, 4, IF(E13<=11, 3, IF(E13<=15, 2, 1)))),
IF(E13>=34, 5, IF(E13>=30, 4, IF(E13>=26, 3, IF(E13>=22, 2, 1))))
) | =+L$1-E13 | =VLOOKUP(F13, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D14,3),"-",C14) | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 11 | =IF(D14="Alerta/Mejora",
IF(E14<=3, 5, IF(E14<=7, 4, IF(E14<=11, 3, IF(E14<=15, 2, 1)))),
IF(E14>=34, 5, IF(E14>=30, 4, IF(E14>=26, 3, IF(E14>=22, 2, 1))))
) | =+L$1-E14 | =VLOOKUP(F14, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D15,3),"-",C15) | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 19 | =IF(D15="Alerta/Mejora",
IF(E15<=3, 5, IF(E15<=7, 4, IF(E15<=11, 3, IF(E15<=15, 2, 1)))),
IF(E15>=34, 5, IF(E15>=30, 4, IF(E15>=26, 3, IF(E15>=22, 2, 1))))
) | =+L$1-E15 | =VLOOKUP(F15, REGLA1, 2, FALSE)

### Hoja: 7mo. TT
Categoría | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | =+CONCATENATE(LEFT(D2,3),"-",C2) | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 12 | =VLOOKUP(G2, $L$3:$N$7, 3, 1) | =+L$1-E2 | =VLOOKUP(F2, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D3,3),"-",C3) | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | 8 | =VLOOKUP(G3, $L$3:$N$7, 3, 1) | =+L$1-E3 | =VLOOKUP(F3, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D4,3),"-",C4) | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 3 | =VLOOKUP(G4, $L$3:$N$7, 3, 1) | =+L$1-E4 | =VLOOKUP(F4, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D5,3),"-",C5) | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 7 | =VLOOKUP(G5, $L$3:$N$7, 3, 1) | =+L$1-E5 | =VLOOKUP(F5, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D6,3),"-",C6) | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 2 | =VLOOKUP(G6, $L$3:$N$7, 3, 1) | =+L$1-E6 | =VLOOKUP(F6, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D7,3),"-",C7) | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 3 | =VLOOKUP(G7, $L$3:$N$7, 3, 1) | =+L$1-E7 | =VLOOKUP(F7, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D8,3),"-",C8) | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | 3 | =VLOOKUP(G8, $L$3:$N$7, 3, 1) | =+L$1-E8 | =VLOOKUP(F8, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D9,3),"-",C9) | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 0 | =VLOOKUP(G9, $L$3:$N$7, 3, 1) | =+L$1-E9 | =VLOOKUP(F9, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D10,3),"-",C10) | 18. Desafía activamente la autoridad. | Alerta/Mejora | 0 | =VLOOKUP(G10, $L$3:$N$7, 3, 1) | =+L$1-E10 | =VLOOKUP(F10, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D11,3),"-",C11) | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 2 | =VLOOKUP(G11, $L$3:$N$7, 3, 1) | =+L$1-E11 | =VLOOKUP(F11, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D12,3),"-",C12) | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 0 | =VLOOKUP(G12, $L$3:$N$7, 3, 1) | =+L$1-E12 | =VLOOKUP(F12, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D13,3),"-",C13) | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 2 | =VLOOKUP(G13, $L$3:$N$7, 3, 1) | =+L$1-E13 | =VLOOKUP(F13, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D14,3),"-",C14) | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 0 | =VLOOKUP(G14, $L$3:$N$7, 3, 1) | =+L$1-E14 | =VLOOKUP(F14, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D15,3),"-",C15) | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 0 | =VLOOKUP(G15, $L$3:$N$7, 3, 1) | =+L$1-E15 | =VLOOKUP(F15, REGLA1, 2, FALSE)

### Hoja: 8vo. TM
Categoría | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | =+CONCATENATE(LEFT(D2,3),"-",C2) | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 8 | =VLOOKUP(G2, $L$3:$N$7, 3, 1) | =+L$1-E2 | =VLOOKUP(F2, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D3,3),"-",C3) | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | 6 | =VLOOKUP(G3, $L$3:$N$7, 3, 1) | =+L$1-E3 | =VLOOKUP(F3, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D4,3),"-",C4) | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 4 | =VLOOKUP(G4, $L$3:$N$7, 3, 1) | =+L$1-E4 | =VLOOKUP(F4, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D5,3),"-",C5) | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 7 | =VLOOKUP(G5, $L$3:$N$7, 3, 1) | =+L$1-E5 | =VLOOKUP(F5, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D6,3),"-",C6) | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 5 | =VLOOKUP(G6, $L$3:$N$7, 3, 1) | =+L$1-E6 | =VLOOKUP(F6, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D7,3),"-",C7) | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 6 | =VLOOKUP(G7, $L$3:$N$7, 3, 1) | =+L$1-E7 | =VLOOKUP(F7, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D8,3),"-",C8) | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | 7 | =VLOOKUP(G8, $L$3:$N$7, 3, 1) | =+L$1-E8 | =VLOOKUP(F8, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D9,3),"-",C9) | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 2 | =VLOOKUP(G9, $L$3:$N$7, 3, 1) | =+L$1-E9 | =VLOOKUP(F9, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D10,3),"-",C10) | 18. Desafía activamente la autoridad. | Alerta/Mejora | 1 | =VLOOKUP(G10, $L$3:$N$7, 3, 1) | =+L$1-E10 | =VLOOKUP(F10, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D11,3),"-",C11) | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 4 | =VLOOKUP(G11, $L$3:$N$7, 3, 1) | =+L$1-E11 | =VLOOKUP(F11, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D12,3),"-",C12) | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 1 | =VLOOKUP(G12, $L$3:$N$7, 3, 1) | =+L$1-E12 | =VLOOKUP(F12, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D13,3),"-",C13) | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 9 | =VLOOKUP(G13, $L$3:$N$7, 3, 1) | =+L$1-E13 | =VLOOKUP(F13, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D14,3),"-",C14) | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 2 | =VLOOKUP(G14, $L$3:$N$7, 3, 1) | =+L$1-E14 | =VLOOKUP(F14, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D15,3),"-",C15) | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 2 | =VLOOKUP(G15, $L$3:$N$7, 3, 1) | =+L$1-E15 | =VLOOKUP(F15, REGLA1, 2, FALSE)

### Hoja: 9no. TM
Categoría | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | =+CONCATENATE(LEFT(D2,3),"-",C2) | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 14 | =VLOOKUP(G2, $L$3:$N$7, 3, 1) | =+L$1-E2 | =VLOOKUP(F2, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D3,3),"-",C3) | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | 12 | =VLOOKUP(G3, $L$3:$N$7, 3, 1) | =+L$1-E3 | =VLOOKUP(F3, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D4,3),"-",C4) | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 9 | =VLOOKUP(G4, $L$3:$N$7, 3, 1) | =+L$1-E4 | =VLOOKUP(F4, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D5,3),"-",C5) | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 15 | =VLOOKUP(G5, $L$3:$N$7, 3, 1) | =+L$1-E5 | =VLOOKUP(F5, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D6,3),"-",C6) | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 8 | =VLOOKUP(G6, $L$3:$N$7, 3, 1) | =+L$1-E6 | =VLOOKUP(F6, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D7,3),"-",C7) | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 3 | =VLOOKUP(G7, $L$3:$N$7, 3, 1) | =+L$1-E7 | =VLOOKUP(F7, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D8,3),"-",C8) | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | 7 | =VLOOKUP(G8, $L$3:$N$7, 3, 1) | =+L$1-E8 | =VLOOKUP(F8, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D9,3),"-",C9) | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 5 | =VLOOKUP(G9, $L$3:$N$7, 3, 1) | =+L$1-E9 | =VLOOKUP(F9, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D10,3),"-",C10) | 18. Desafía activamente la autoridad. | Alerta/Mejora | 2 | =VLOOKUP(G10, $L$3:$N$7, 3, 1) | =+L$1-E10 | =VLOOKUP(F10, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D11,3),"-",C11) | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 4 | =VLOOKUP(G11, $L$3:$N$7, 3, 1) | =+L$1-E11 | =VLOOKUP(F11, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D12,3),"-",C12) | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 0 | =VLOOKUP(G12, $L$3:$N$7, 3, 1) | =+L$1-E12 | =VLOOKUP(F12, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D13,3),"-",C13) | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 26 | =VLOOKUP(G13, $L$3:$N$7, 3, 1) | =+L$1-E13 | =VLOOKUP(F13, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D14,3),"-",C14) | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 0 | =VLOOKUP(G14, $L$3:$N$7, 3, 1) | =+L$1-E14 | =VLOOKUP(F14, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D15,3),"-",C15) | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 4 | =VLOOKUP(G15, $L$3:$N$7, 3, 1) | =+L$1-E15 | =VLOOKUP(F15, REGLA1, 2, FALSE)

### Hoja: Hoja10
 |
 | Este ajuste es fundamental. Para un **Master en Programación y Arquitecto de Software** como tú, la eficiencia es un requisito no negociable. [cite_start]El objetivo es **refactorizar** el tiempo que ya pasas en el aula, no añadir "líneas de código" (actividades) innecesarias. [cite: 7]

Aquí tienes el **Prompt Maestro Final "Zero-Overload"**, diseñado para que la IA optimice tu plan de estudios actual de **Formación Ética y Ciudadana** redistribuyendo el esfuerzo existente.

---

## Prompt Maestro: Optimización de Plan sin Carga Adicional

> **Rol:** Actúa como un **Especialista en Eficiencia Pedagógica y Currículum de la EEB (Paraguay)**.
>
> **Entrada de Datos:**
> * **Resultados Diagnósticos por Ítem:** [PEGA AQUÍ LOS TOTALES DE LA ENCUESTA]
> * **Plan de Estudios Actual:** [PEGA AQUÍ TU LISTA DE TEMAS/ACTIVIDADES PROGRAMADAS]
>
> **Objetivo 1: Diagnóstico de Eficiencia Grupal**
> [cite_start]* Analiza las frecuencias de respuesta para identificar qué contenidos del plan ya domina el **92% del grupo (nivel Muy Bueno)**. [cite: 10]
> [cite_start]* Detecta qué temas programados están en riesgo de fallar debido a la **memorización mecánica** o la **distracción con TIC** identificada. [cite: 42, 53]
>
> **Objetivo 2: Refactorización del Plan de Estudios (Sin Actividades Extra)**
> [cite_start]* **Sustitución, no Adición:** En lugar de crear actividades nuevas, indica cómo modificar la metodología de las actividades **ya programadas** para que ataquen las debilidades (ej. si tenías una lectura, conviértela en un debate de 5 minutos para mejorar la expresión oral). [cite: 94, 95]
> [cite_start]* **Delegación (Tutoría entre Pares):** Diseña un sistema donde los alumnos destacados lideren las partes teóricas de las actividades existentes, liberando tu tiempo para monitorear al **5% que necesita mejora**. [cite: 10, 75]
> [cite_start]* **Optimización de Recursos:** Propón cómo usar los dispositivos que ya causan distracción como la herramienta principal para una actividad que ya tenías planeada, eliminando la fricción. [cite: 88]
>
> **Objetivo 3: Informe Ejecutivo y Plan Optimizado**
> [cite_start]* Genera un informe de seguimiento que valide que se están cumpliendo las **Acciones Pedagógicas** (como el ABP o el pensamiento crítico) dentro del horario y plan original. [cite: 66, 71]
> [cite_start]* Entrega un cronograma ajustado que mantenga los mismos temas pero con un enfoque de **0% de error** en la comprensión. [cite: 7]
>
> **Restricción Estricta:** No propongas ninguna tarea, proyecto o recurso que requiera tiempo extra de planificación o ejecución fuera de lo que ya está estipulado en el calendario escolar.

---

### Por qué este enfoque respeta tu tiempo:

1.  **Aprovecha el "Muy Bueno" (92%):** El informe del **Lic. [cite_start]Christhian Keim** muestra que la gran mayoría de tus alumnos ya tiene autonomía y dominio conceptual. [cite: 7, 10, 14, 18] [cite_start]Al convertirlos en monitores de las actividades que ya tienes, reduces tu carga de supervisión constante. [cite: 47]
2.  [cite_start]**Ataca la Raíz:** El problema no es la falta de actividades, sino que las actuales pueden estar fomentando la **memorización sin comprensión**. [cite: 84] El prompt obliga a la IA a cambiar el *cómo* lo das, no el *qué* das.
3.  **Coherencia con Villa Hayes:** Mantiene el enfoque territorial y los estándares de la **Escuela Exc. [cite_start]Manual Molinas**, asegurando que el informe sea útil para tu contexto específico en Paraguay. [cite: 1, 2]

¿Quieres que apliquemos este prompt ahora mismo con los temas que tienes programados para la siguiente unidad de **7mo u 8vo grado**?

### Hoja: REGLAS
REGLAS |  |  |  |  |  |  |
 |  |  |  |  | GRADO | TURNO | CANTIDAD
Nota  | VALORACION |  |  |  | SEPTIMO  | TM | 37
1 | A mejorar |  |  |  | SEPTIMO  | TT | 14
2 | A mejorar |  |  |  | OCTAVO | TM | 42
3 | Bueno |  |  |  | NOVENO | TM | 42
4 | Muy bueno  |  |  |  |  |  |
5 | =+B7 |  |  |  |  |  |

## Version 2
Fuente: `C:\Users\HP 250 G10\Documents\GITHUT\MEC\MEC\VH ESC MANUEL MOLINAS DIAGNOSTICO\Data\PLANILLA DE DIAGNOSTICO I MM I 2026.xlsx`

### Hoja: Hoja7
<openpyxl.worksheet.formula.ArrayFormula object at 0x00000218BE53C8A0> | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | Ale-02. Presenta lagunas en conocimientos previos. | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 37 | 1 | 0 | A mejorar
Académica | Ale-04. Se limita a memorizar sin comprender. | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | 18 | 1 | 19 | A mejorar
Académica | Ale-06. Entrega tareas incompletas o descuidadas. | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 4 | 4 | 33 | Muy bueno
Académica | Ale-08. Se bloquea ante desafíos matemáticos. | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 18 | 1 | 19 | A mejorar
Académica | Ale-10. Tiene dificultades de expresión oral/escrita. | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 14 | 2 | 23 | A mejorar
Académica | Ale-12. Muestra rechazo o desinterés por la lectura. | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 11 | 3 | 26 | Bueno
Académica | Ale-14. Requiere supervisión constante para avanzar. | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | 19 | 1 | 18 | A mejorar
Académica | Ale-16. Muestra apatía por temas nuevos. | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 7 | 4 | 30 | Muy bueno
Conductual | Ale-18. Desafía activamente la autoridad. | 18. Desafía activamente la autoridad. | Alerta/Mejora | 16 | 1 | 21 | A mejorar
Conductual | Ale-20. Presenta retardos o inasistencias frecuentes. | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 2 | 5 | 35 | Muy bueno
Conductual | Ale-22. Daña el mobiliario o materiales escolares. | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 1 | 5 | 36 | Muy bueno
Conductual | Ale-24. Interrumpe constantemente el flujo de clase. | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 2 | 5 | 35 | Muy bueno
Conductual | Ale-26. Emplea lenguaje soez o despectivo. | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 11 | 3 | 26 | Bueno
Conductual | Ale-28. Miente o culpa a otros por sus actos. | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 19 | 1 | 18 | A mejorar

### Hoja: Hoja9
 |  |  |  |  |  |  |
 | GRADO | SEPTIMO |  |  |  |  |
 | TURNO | TM |  |  |  |  |
 |  |  |  |  |  |  |
 | Etiquetas de fila | Cuenta de NF | Promedio de NF2 | Cuenta de NF2 |  |  |
 | 1 | 34 | 0 | 34 |  |  |
 | 2 | 5 | 0 | 5 |  |  |
 | 3 | 4 | 0 | 4 |  |  |
 | 4 | 4 | 0 | 4 |  |  |
 | 5 | 3 | 0 | 3 |  |  |
 | Total general | 50 | 0 | 50 |  |  |
 |  |  |  |  |  |  |
 |  |  |  |  |  |  |
 |  |  |  |  |  |  |
 |  |  |  |  |  |  |

### Hoja: RESULTADO


### Hoja: 7mo. TM
Categoría | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | =+CONCATENATE(LEFT(D2,3),"-",C2) | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 37 | =IF(D2="Alerta/Mejora",
  IF(E2<=3, 5, IF(E2<=7, 4, IF(E2<=11, 3, IF(E2<=15, 2, 1)))),
  IF(E2>=34, 5, IF(E2>=30, 4, IF(E2>=26, 3, IF(E2>=22, 2, 1))))
) | =+L$1-E2 | =VLOOKUP(F2, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D3,3),"-",C3) | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | =37-19 | =IF(D3="Alerta/Mejora",
  IF(E3<=3, 5, IF(E3<=7, 4, IF(E3<=11, 3, IF(E3<=15, 2, 1)))),
  IF(E3>=34, 5, IF(E3>=30, 4, IF(E3>=26, 3, IF(E3>=22, 2, 1))))
) | =+L$1-E3 | =VLOOKUP(F3, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D4,3),"-",C4) | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 4 | =IF(D4="Alerta/Mejora",
IF(E4<=3, 5, IF(E4<=7, 4, IF(E4<=11, 3, IF(E4<=15, 2, 1)))),
IF(E4>=34, 5, IF(E4>=30, 4, IF(E4>=26, 3, IF(E4>=22, 2, 1))))
) | =+L$1-E4 | =VLOOKUP(F4, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D5,3),"-",C5) | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 18 | =IF(D5="Alerta/Mejora",
IF(E5<=3, 5, IF(E5<=7, 4, IF(E5<=11, 3, IF(E5<=15, 2, 1)))),
IF(E5>=34, 5, IF(E5>=30, 4, IF(E5>=26, 3, IF(E5>=22, 2, 1))))
) | =+L$1-E5 | =VLOOKUP(F5, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D6,3),"-",C6) | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 14 | =IF(D6="Alerta/Mejora",
IF(E6<=3, 5, IF(E6<=7, 4, IF(E6<=11, 3, IF(E6<=15, 2, 1)))),
IF(E6>=34, 5, IF(E6>=30, 4, IF(E6>=26, 3, IF(E6>=22, 2, 1))))
) | =+L$1-E6 | =VLOOKUP(F6, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D7,3),"-",C7) | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 11 | =IF(D7="Alerta/Mejora",
IF(E7<=3, 5, IF(E7<=7, 4, IF(E7<=11, 3, IF(E7<=15, 2, 1)))),
IF(E7>=34, 5, IF(E7>=30, 4, IF(E7>=26, 3, IF(E7>=22, 2, 1))))
) | =+L$1-E7 | =VLOOKUP(F7, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D8,3),"-",C8) | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | =37-18 | =IF(D8="Alerta/Mejora",
IF(E8<=3, 5, IF(E8<=7, 4, IF(E8<=11, 3, IF(E8<=15, 2, 1)))),
IF(E8>=34, 5, IF(E8>=30, 4, IF(E8>=26, 3, IF(E8>=22, 2, 1))))
) | =+L$1-E8 | =VLOOKUP(F8, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D9,3),"-",C9) | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 7 | =IF(D9="Alerta/Mejora",
IF(E9<=3, 5, IF(E9<=7, 4, IF(E9<=11, 3, IF(E9<=15, 2, 1)))),
IF(E9>=34, 5, IF(E9>=30, 4, IF(E9>=26, 3, IF(E9>=22, 2, 1))))
) | =+L$1-E9 | =VLOOKUP(F9, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D10,3),"-",C10) | 18. Desafía activamente la autoridad. | Alerta/Mejora | 16 | =IF(D10="Alerta/Mejora",
IF(E10<=3, 5, IF(E10<=7, 4, IF(E10<=11, 3, IF(E10<=15, 2, 1)))),
IF(E10>=34, 5, IF(E10>=30, 4, IF(E10>=26, 3, IF(E10>=22, 2, 1))))
) | =+L$1-E10 | =VLOOKUP(F10, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D11,3),"-",C11) | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 2 | =IF(D11="Alerta/Mejora",
IF(E11<=3, 5, IF(E11<=7, 4, IF(E11<=11, 3, IF(E11<=15, 2, 1)))),
IF(E11>=34, 5, IF(E11>=30, 4, IF(E11>=26, 3, IF(E11>=22, 2, 1))))
) | =+L$1-E11 | =VLOOKUP(F11, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D12,3),"-",C12) | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 1 | =IF(D12="Alerta/Mejora",
IF(E12<=3, 5, IF(E12<=7, 4, IF(E12<=11, 3, IF(E12<=15, 2, 1)))),
IF(E12>=34, 5, IF(E12>=30, 4, IF(E12>=26, 3, IF(E12>=22, 2, 1))))
) | =+L$1-E12 | =VLOOKUP(F12, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D13,3),"-",C13) | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 2 | =IF(D13="Alerta/Mejora",
IF(E13<=3, 5, IF(E13<=7, 4, IF(E13<=11, 3, IF(E13<=15, 2, 1)))),
IF(E13>=34, 5, IF(E13>=30, 4, IF(E13>=26, 3, IF(E13>=22, 2, 1))))
) | =+L$1-E13 | =VLOOKUP(F13, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D14,3),"-",C14) | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 11 | =IF(D14="Alerta/Mejora",
IF(E14<=3, 5, IF(E14<=7, 4, IF(E14<=11, 3, IF(E14<=15, 2, 1)))),
IF(E14>=34, 5, IF(E14>=30, 4, IF(E14>=26, 3, IF(E14>=22, 2, 1))))
) | =+L$1-E14 | =VLOOKUP(F14, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D15,3),"-",C15) | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 19 | =IF(D15="Alerta/Mejora",
IF(E15<=3, 5, IF(E15<=7, 4, IF(E15<=11, 3, IF(E15<=15, 2, 1)))),
IF(E15>=34, 5, IF(E15>=30, 4, IF(E15>=26, 3, IF(E15>=22, 2, 1))))
) | =+L$1-E15 | =VLOOKUP(F15, REGLA1, 2, FALSE)

### Hoja: 7mo. TT
Categoría | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | =+CONCATENATE(LEFT(D2,3),"-",C2) | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 12 | =VLOOKUP(G2, $L$3:$N$7, 3, 1) | =+L$1-E2 | =VLOOKUP(F2, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D3,3),"-",C3) | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | 8 | =VLOOKUP(G3, $L$3:$N$7, 3, 1) | =+L$1-E3 | =VLOOKUP(F3, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D4,3),"-",C4) | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 3 | =VLOOKUP(G4, $L$3:$N$7, 3, 1) | =+L$1-E4 | =VLOOKUP(F4, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D5,3),"-",C5) | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 7 | =VLOOKUP(G5, $L$3:$N$7, 3, 1) | =+L$1-E5 | =VLOOKUP(F5, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D6,3),"-",C6) | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 2 | =VLOOKUP(G6, $L$3:$N$7, 3, 1) | =+L$1-E6 | =VLOOKUP(F6, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D7,3),"-",C7) | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 3 | =VLOOKUP(G7, $L$3:$N$7, 3, 1) | =+L$1-E7 | =VLOOKUP(F7, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D8,3),"-",C8) | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | 3 | =VLOOKUP(G8, $L$3:$N$7, 3, 1) | =+L$1-E8 | =VLOOKUP(F8, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D9,3),"-",C9) | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 0 | =VLOOKUP(G9, $L$3:$N$7, 3, 1) | =+L$1-E9 | =VLOOKUP(F9, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D10,3),"-",C10) | 18. Desafía activamente la autoridad. | Alerta/Mejora | 0 | =VLOOKUP(G10, $L$3:$N$7, 3, 1) | =+L$1-E10 | =VLOOKUP(F10, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D11,3),"-",C11) | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 2 | =VLOOKUP(G11, $L$3:$N$7, 3, 1) | =+L$1-E11 | =VLOOKUP(F11, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D12,3),"-",C12) | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 0 | =VLOOKUP(G12, $L$3:$N$7, 3, 1) | =+L$1-E12 | =VLOOKUP(F12, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D13,3),"-",C13) | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 2 | =VLOOKUP(G13, $L$3:$N$7, 3, 1) | =+L$1-E13 | =VLOOKUP(F13, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D14,3),"-",C14) | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 0 | =VLOOKUP(G14, $L$3:$N$7, 3, 1) | =+L$1-E14 | =VLOOKUP(F14, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D15,3),"-",C15) | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 0 | =VLOOKUP(G15, $L$3:$N$7, 3, 1) | =+L$1-E15 | =VLOOKUP(F15, REGLA1, 2, FALSE)

### Hoja: 8vo. TM
Categoría | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | =+CONCATENATE(LEFT(D2,3),"-",C2) | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 8 | =VLOOKUP(G2, $L$3:$N$7, 3, 1) | =+L$1-E2 | =VLOOKUP(F2, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D3,3),"-",C3) | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | 6 | =VLOOKUP(G3, $L$3:$N$7, 3, 1) | =+L$1-E3 | =VLOOKUP(F3, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D4,3),"-",C4) | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 4 | =VLOOKUP(G4, $L$3:$N$7, 3, 1) | =+L$1-E4 | =VLOOKUP(F4, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D5,3),"-",C5) | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 7 | =VLOOKUP(G5, $L$3:$N$7, 3, 1) | =+L$1-E5 | =VLOOKUP(F5, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D6,3),"-",C6) | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 5 | =VLOOKUP(G6, $L$3:$N$7, 3, 1) | =+L$1-E6 | =VLOOKUP(F6, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D7,3),"-",C7) | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 6 | =VLOOKUP(G7, $L$3:$N$7, 3, 1) | =+L$1-E7 | =VLOOKUP(F7, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D8,3),"-",C8) | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | 7 | =VLOOKUP(G8, $L$3:$N$7, 3, 1) | =+L$1-E8 | =VLOOKUP(F8, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D9,3),"-",C9) | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 2 | =VLOOKUP(G9, $L$3:$N$7, 3, 1) | =+L$1-E9 | =VLOOKUP(F9, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D10,3),"-",C10) | 18. Desafía activamente la autoridad. | Alerta/Mejora | 1 | =VLOOKUP(G10, $L$3:$N$7, 3, 1) | =+L$1-E10 | =VLOOKUP(F10, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D11,3),"-",C11) | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 4 | =VLOOKUP(G11, $L$3:$N$7, 3, 1) | =+L$1-E11 | =VLOOKUP(F11, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D12,3),"-",C12) | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 1 | =VLOOKUP(G12, $L$3:$N$7, 3, 1) | =+L$1-E12 | =VLOOKUP(F12, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D13,3),"-",C13) | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 9 | =VLOOKUP(G13, $L$3:$N$7, 3, 1) | =+L$1-E13 | =VLOOKUP(F13, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D14,3),"-",C14) | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 2 | =VLOOKUP(G14, $L$3:$N$7, 3, 1) | =+L$1-E14 | =VLOOKUP(F14, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D15,3),"-",C15) | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 2 | =VLOOKUP(G15, $L$3:$N$7, 3, 1) | =+L$1-E15 | =VLOOKUP(F15, REGLA1, 2, FALSE)

### Hoja: 9no. TM
Categoría | Indicador  | Indicador  | Tipo de Indicador | Cantidad de veces | NOTA | PR | VALORACION
Académica | =+CONCATENATE(LEFT(D2,3),"-",C2) | 02. Presenta lagunas en conocimientos previos. | Alerta/Mejora | 14 | =VLOOKUP(G2, $L$3:$N$7, 3, 1) | =+L$1-E2 | =VLOOKUP(F2, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D3,3),"-",C3) | 04. Se limita a memorizar sin comprender. | Alerta/Mejora | 12 | =VLOOKUP(G3, $L$3:$N$7, 3, 1) | =+L$1-E3 | =VLOOKUP(F3, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D4,3),"-",C4) | 06. Entrega tareas incompletas o descuidadas. | Alerta/Mejora | 9 | =VLOOKUP(G4, $L$3:$N$7, 3, 1) | =+L$1-E4 | =VLOOKUP(F4, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D5,3),"-",C5) | 08. Se bloquea ante desafíos matemáticos. | Alerta/Mejora | 15 | =VLOOKUP(G5, $L$3:$N$7, 3, 1) | =+L$1-E5 | =VLOOKUP(F5, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D6,3),"-",C6) | 10. Tiene dificultades de expresión oral/escrita. | Alerta/Mejora | 8 | =VLOOKUP(G6, $L$3:$N$7, 3, 1) | =+L$1-E6 | =VLOOKUP(F6, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D7,3),"-",C7) | 12. Muestra rechazo o desinterés por la lectura. | Alerta/Mejora | 3 | =VLOOKUP(G7, $L$3:$N$7, 3, 1) | =+L$1-E7 | =VLOOKUP(F7, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D8,3),"-",C8) | 14. Requiere supervisión constante para avanzar. | Alerta/Mejora | 7 | =VLOOKUP(G8, $L$3:$N$7, 3, 1) | =+L$1-E8 | =VLOOKUP(F8, REGLA1, 2, FALSE)
Académica | =+CONCATENATE(LEFT(D9,3),"-",C9) | 16. Muestra apatía por temas nuevos. | Alerta/Mejora | 5 | =VLOOKUP(G9, $L$3:$N$7, 3, 1) | =+L$1-E9 | =VLOOKUP(F9, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D10,3),"-",C10) | 18. Desafía activamente la autoridad. | Alerta/Mejora | 2 | =VLOOKUP(G10, $L$3:$N$7, 3, 1) | =+L$1-E10 | =VLOOKUP(F10, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D11,3),"-",C11) | 20. Presenta retardos o inasistencias frecuentes. | Alerta/Mejora | 4 | =VLOOKUP(G11, $L$3:$N$7, 3, 1) | =+L$1-E11 | =VLOOKUP(F11, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D12,3),"-",C12) | 22. Daña el mobiliario o materiales escolares. | Alerta/Mejora | 0 | =VLOOKUP(G12, $L$3:$N$7, 3, 1) | =+L$1-E12 | =VLOOKUP(F12, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D13,3),"-",C13) | 24. Interrumpe constantemente el flujo de clase. | Alerta/Mejora | 26 | =VLOOKUP(G13, $L$3:$N$7, 3, 1) | =+L$1-E13 | =VLOOKUP(F13, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D14,3),"-",C14) | 26. Emplea lenguaje soez o despectivo. | Alerta/Mejora | 0 | =VLOOKUP(G14, $L$3:$N$7, 3, 1) | =+L$1-E14 | =VLOOKUP(F14, REGLA1, 2, FALSE)
Conductual | =+CONCATENATE(LEFT(D15,3),"-",C15) | 28. Miente o culpa a otros por sus actos. | Alerta/Mejora | 4 | =VLOOKUP(G15, $L$3:$N$7, 3, 1) | =+L$1-E15 | =VLOOKUP(F15, REGLA1, 2, FALSE)

### Hoja: Hoja10
 |
 | Este ajuste es fundamental. Para un **Master en Programación y Arquitecto de Software** como tú, la eficiencia es un requisito no negociable. [cite_start]El objetivo es **refactorizar** el tiempo que ya pasas en el aula, no añadir "líneas de código" (actividades) innecesarias. [cite: 7]

Aquí tienes el **Prompt Maestro Final "Zero-Overload"**, diseñado para que la IA optimice tu plan de estudios actual de **Formación Ética y Ciudadana** redistribuyendo el esfuerzo existente.

---

## Prompt Maestro: Optimización de Plan sin Carga Adicional

> **Rol:** Actúa como un **Especialista en Eficiencia Pedagógica y Currículum de la EEB (Paraguay)**.
>
> **Entrada de Datos:**
> * **Resultados Diagnósticos por Ítem:** [PEGA AQUÍ LOS TOTALES DE LA ENCUESTA]
> * **Plan de Estudios Actual:** [PEGA AQUÍ TU LISTA DE TEMAS/ACTIVIDADES PROGRAMADAS]
>
> **Objetivo 1: Diagnóstico de Eficiencia Grupal**
> [cite_start]* Analiza las frecuencias de respuesta para identificar qué contenidos del plan ya domina el **92% del grupo (nivel Muy Bueno)**. [cite: 10]
> [cite_start]* Detecta qué temas programados están en riesgo de fallar debido a la **memorización mecánica** o la **distracción con TIC** identificada. [cite: 42, 53]
>
> **Objetivo 2: Refactorización del Plan de Estudios (Sin Actividades Extra)**
> [cite_start]* **Sustitución, no Adición:** En lugar de crear actividades nuevas, indica cómo modificar la metodología de las actividades **ya programadas** para que ataquen las debilidades (ej. si tenías una lectura, conviértela en un debate de 5 minutos para mejorar la expresión oral). [cite: 94, 95]
> [cite_start]* **Delegación (Tutoría entre Pares):** Diseña un sistema donde los alumnos destacados lideren las partes teóricas de las actividades existentes, liberando tu tiempo para monitorear al **5% que necesita mejora**. [cite: 10, 75]
> [cite_start]* **Optimización de Recursos:** Propón cómo usar los dispositivos que ya causan distracción como la herramienta principal para una actividad que ya tenías planeada, eliminando la fricción. [cite: 88]
>
> **Objetivo 3: Informe Ejecutivo y Plan Optimizado**
> [cite_start]* Genera un informe de seguimiento que valide que se están cumpliendo las **Acciones Pedagógicas** (como el ABP o el pensamiento crítico) dentro del horario y plan original. [cite: 66, 71]
> [cite_start]* Entrega un cronograma ajustado que mantenga los mismos temas pero con un enfoque de **0% de error** en la comprensión. [cite: 7]
>
> **Restricción Estricta:** No propongas ninguna tarea, proyecto o recurso que requiera tiempo extra de planificación o ejecución fuera de lo que ya está estipulado en el calendario escolar.

---

### Por qué este enfoque respeta tu tiempo:

1.  **Aprovecha el "Muy Bueno" (92%):** El informe del **Lic. [cite_start]Christhian Keim** muestra que la gran mayoría de tus alumnos ya tiene autonomía y dominio conceptual. [cite: 7, 10, 14, 18] [cite_start]Al convertirlos en monitores de las actividades que ya tienes, reduces tu carga de supervisión constante. [cite: 47]
2.  [cite_start]**Ataca la Raíz:** El problema no es la falta de actividades, sino que las actuales pueden estar fomentando la **memorización sin comprensión**. [cite: 84] El prompt obliga a la IA a cambiar el *cómo* lo das, no el *qué* das.
3.  **Coherencia con Villa Hayes:** Mantiene el enfoque territorial y los estándares de la **Escuela Exc. [cite_start]Manual Molinas**, asegurando que el informe sea útil para tu contexto específico en Paraguay. [cite: 1, 2]

¿Quieres que apliquemos este prompt ahora mismo con los temas que tienes programados para la siguiente unidad de **7mo u 8vo grado**?

### Hoja: REGLAS
REGLAS |  |  |  |  |  |  |
 |  |  |  |  | GRADO | TURNO | CANTIDAD
Nota  | VALORACION |  |  |  | SEPTIMO  | TM | 37
1 | A mejorar |  |  |  | SEPTIMO  | TT | 14
2 | A mejorar |  |  |  | OCTAVO | TM | 42
3 | Bueno |  |  |  | NOVENO | TM | 42
4 | Muy bueno  |  |  |  |  |  |
5 | =+B7 |  |  |  |  |  |
