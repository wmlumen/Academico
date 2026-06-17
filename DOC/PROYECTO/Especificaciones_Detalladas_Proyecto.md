# Especificaciones Técnicas y Funcionales: MEC 2026 PRO

## 1. Visión General del Proyecto
**MEC 2026 PRO** es una plataforma digital de gestión pedagógica diseñada para empoderar a los docentes de la República del Paraguay (Educación Escolar Básica y Educación Media). El sistema centraliza la planificación, el seguimiento administrativo de rubros y la organización cronológica del aula, asegurando el cumplimiento estricto de las normativas del **Ministerio de Educación y Ciencias (MEC)**.

---

## 2. Objetivos del Proyecto
*   **Centralización**: Consolidar en una sola interfaz todos los planes anuales y diarios según la Reforma de la Educación Media.
*   **Eficiencia Administrativa**: Permitir que el docente organice su "Matriz de Rubros" entre múltiples instituciones y secciones.
*   **Asistencia en Tiempo Real**: Proporcionar un horario dinámico que indique qué planificar y desarrollar según el día y la hora.
*   **Acceso a Recursos**: Facilitar libros, guías y marcos legales vigentes del 2026.

---

## 3. Alcance Funcional (Módulos)

### 📊 Módulo A: Matriz de Rubros y Cátedras
*   **Wizard de Configuración**: Interfaz guiada para vincular asignaturas a instituciones específicas.
*   **Gestión Multinivel**: Soporte para Tercer Ciclo (Ética, Ciencias) y Bachilleratos Técnicos (BTCC).
*   **Persistencia Local**: Guardado de datos en el navegador del docente para uso sin conexión a internet constante.

### ⏱️ Módulo B: Horario Semanal Cronológico
*   **Ordenamiento Atómico**: Reordenamiento automático de la matriz de cátedras según la hora actual.
*   **Sistema de Notificaciones**: Avisos visuales 5 minutos antes de iniciar cada clase.
*   **Vista de Agenda**: Rejilla semanal para visualización de carga horaria completa.

### 📂 Módulo C: Repositorio Pedagógico (Biblioteca)
*   **Planes de 10 Puntos**: Generación de planes anuales con fundamentación, capacidades y cronograma.
*   **Secuencia Didáctica**: Planes diarios basados en los tres momentos (Inicio, Desarrollo, Cierre).
*   **Biblioteca Digital**: Enlaces directos a libros oficiales y guías docentes (Integración Google Drive).
*   **Marco Legal**: Compendio de resoluciones (989/22, 9588/19) para auditorías.

---

## 4. Requerimientos Técnicos
*   **Interfaz**: HTML5 / CSS3 (Aesthetic Premium / Responsivo).
*   **Lógica**: JavaScript Vanilla (Sin frameworks externos para máxima portabilidad).
*   **Renderizado**: `marked.js` para visualización fluida de documentos Markdown.
*   **Iconografía**: Lucide Icons para una UI moderna y clara.
*   **Almacenamiento**: Browser LocalStorage para datos de rubros y favoritos.

---

## 5. Hoja de Ruta (Próximas Fases)
1.  **Fase 1 (Completada)**: Dashboard, Matriz de Rubros, Horario y Biblioteca de Planes.
2.  **Fase 2 (En Desarrollo)**: Seguimiento de Alumnos (Asistencia y Notas).
3.  **Fase 3 (Planeada)**: Generador de Reportes RSA en PDF para supervisión.
4.  **Fase 4 (Planeada)**: Módulos específicos para Bachilleratos en Ciencias Sociales y Ambientales.

---
*Este documento define el norte estratégico y técnico para el desarrollo integral del ecosistema pedagógico MEC 2026.*
