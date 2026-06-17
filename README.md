# Academico

Sistema documental académico para la gestión educativa de Bachillerato Técnico en Construcciones Civiles (BTCC). Incluye planillas de evaluación, registro de clases, asistencias, panel institucional y planificación curricular.

## Acceso

Publicado en GitHub Pages:  
[https://wmlumen.github.io/Academico/](https://wmlumen.github.io/Academico/)

## Estructura del repositorio

```
BT/BTCC/                     → Sistema principal BTCC (2.do Curso)
  ├── index.html             → Portal de acceso
  ├── panel_institucional.html
  ├── sistema_institucional_asistencia.html
  ├── calendario_escolar_2026.html
  ├── perfil_docente.html
  ├── 2_Curso/
  │   ├── Tecnicas_Instrumentales_II/   → Planillas, RSA, exámenes, competencias
  │   └── Resistencia_Materiales/       → Planillas, RSA, exámenes, competencias
  ├── 1_Curso/
  ├── 3_Curso/
  ├── data/                  → Datos en JSON/JS (alumnos, indicadores, calendario)
  └── nav/                   → Sidebar de navegación

CURRICULO_BASE/              → Planes anuales, mapas documentales, fichas
INSTITUCIONES/               → Contenidos por institución educativa
SISTEMA_PANELES/             → Dashboards (central, dirección, docente)
DOC/                         → Documentación, guías, plantillas MEC
```

## Funcionalidades principales

### BTCC — 2.do Curso
- **Panel Institucional**: gestión de docentes, asignaturas, horarios, calendario académico
- **Registro de Asistencia**: carga con detección de feriados, vista planilla/calendario/resumen
- **RSA Individual**: registro de secuencia de aprendizaje con 3-4 revisiones
- **Planilla de Proceso**: 70% RSA + 30% Proyectos Institucionales
- **Exámenes Sumativos**: carga de puntajes con nota 1-5
- **Planilla Integrada**: RSA + Proyectos + Exámenes + Competencias Transversales con pesos configurables
- **Competencias Transversales**: 28 criterios por alumno
- **Registro de Clases**: asistencia y temas por bloque horario
- **Calendario Escolar**: vista grilla/lista, eventos sincronizados
- **Perfil Docente**: protegido, con gestión de tareas, horarios, exámenes
- **Perfil Estudiante**: autenticación con credenciales, tareas, RSA, competencias
- **Sidebar universal**: navegación auto-ocultable con detección de rol y materia

### Currículo Base
- Planes anuales completos para 1.er, 2.do y 3.er Curso BTCC
- Materiales complementarios, ejercitarios, guías de estudiante
- Planes para EEB (7°-9°) y EM (1°-3°) en Ciencias, Ética, Educación Ambiental

### Dashboards
- Panel Central
- Panel de Dirección
- Panel de Supervisión
- Panel MEC PRO

## Stack

- HTML5 + CSS3 + JavaScript (vanilla, sin frameworks)
- Datos en localStorage + archivos JSON estáticos
- Ejecución desde `file://` o servidor HTTP estático
- Compatible con Chrome, Edge, Firefox

## Licencia

Uso educativo exclusivo.
