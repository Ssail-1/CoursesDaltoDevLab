
# 🧪 Proyecto:

Un sistema de consola para **gestionar talleres** (cursos cortos), **inscripciones de usuarios**, **cupos**, **recomendaciones por intereses** y **estadísticas**.

## 🎯 Objetivos (mínimos)

1. **Usuarios**

   * Alta de usuario con validación:

     * `username` (str, único, alfanumérico, 3–15 chars)
     * `nombre` (str, capitalizado)
     * `edad` (int, 13–99)
     * `intereses` (set de tags, p.ej. `{python, web, datos}`)
   * Estructura sugerida (dic de dic):

     ```python
     usuarios = {
       "ssail": {
         "nombre": "Luis",
         "edad": 25,
         "intereses": {"python", "web", "datos"},
         "inscripciones": [("PY101", "2025-11-11")],  # lista de tuplas inmutables
       },
       ...
     }
     ```
2. **Talleres**

   * Alta de taller con validación:

     * `codigo` (ID único tipo “PY101”)
     * `titulo` (str)
     * `capacidad` (int > 0)
     * `tags` (set, p.ej. `{python, basico}`)
   * Estructura sugerida:

     ```python
     talleres = {
       "PY101": {
         "titulo": "Python desde Cero",
         "capacidad": 3,
         "tags": {"python", "basico"},
         "inscritos": set()  # conjunto de usernames
       },
       ...
     }
     ```
3. **Inscripciones**

   * Inscribir `username` en `codigo`:

     * Rechazar si no existe user/taller, si ya está inscrito, o si no hay cupo.
     * Registrar en **ambos** lados:

       * `talleres[codigo]["inscritos"].add(username)`
       * `usuarios[username]["inscripciones"].append((codigo, fecha_iso))`
   * Cancelación (opcional en mínimos, obligatoria en “extra”).
4. **Búsqueda & Recomendación**

   * Buscar talleres por **intersección** de tags con intereses del usuario:

     * score = tamaño de `intereses_usuario ∩ tags_taller`
     * Mostrar ordenado por score (desc), luego por cupo disponible.
5. **Reportes**

   * Top 3 talleres más poblados.
   * Usuarios **sin** inscripciones.
   * Tags globales:

     * `tags_presentes = union de todos los tags de talleres`
     * `tags_faltantes_usuario = tags_presentes - intereses_usuario`
   * % de ocupación por taller: `len(inscritos) / capacidad`.

---

## 🧩 Reglas y validaciones (obligatorias)

* `input()` siempre se valida: números con `isdigit()` o `try/except`.
* Claves inexistentes → nunca rompen el programa (usa `get` y condicionales).
* No se permite **duplicar** usuarios ni talleres.
* Usar **tuplas** para (codigo, fecha) en el historial de inscripciones.
* Usar **sets** para:

  * `intereses` (usuarios)
  * `tags` (talleres)
  * `inscritos` (talleres)
* Al menos **una** comparación encadenada (p.ej. `13 <= edad <= 99`).
* Menú principal con `while True` y opciones (`1…n`, `0 salir`).

---

## 🧱 Menú sugerido

```
[1] Alta usuario
[2] Alta taller
[3] Inscribir usuario en taller
[4] Recomendar talleres a un usuario
[5] Reportes
[0] Salir
```

### Reportes (mínimos)

* [5.1] Top 3 talleres por inscritos
* [5.2] Usuarios sin inscripciones
* [5.3] Ocupación por taller (ordenado desc)
* [5.4] Tags globales y faltantes por usuario (ingresando username)

---

## 🧠 Pistas técnicas (para hacerlo pro)

* **Desempaquetado** en bucles:

  ```python
  for codigo, data in talleres.items():
      titulo, capacidad = data["titulo"], data["capacidad"]
  ```
* **Sets** a full:

  ```python
  score = len(usuarios[u]["intereses"] & talleres[c]["tags"])
  cupo_disponible = talleres[c]["capacidad"] - len(talleres[c]["inscritos"])
  ```
* **Tuplas** para historial:

  ```python
  usuarios[u]["inscripciones"].append((codigo, fecha_iso))
  ```
* **Dicts** con `fromkeys` (para plantillas rápidas):

  ```python
  plantilla_user = dict.fromkeys(["nombre","edad","intereses","inscripciones"])
  ```
* **Funciones** pequeñas y puras (cuando avances):

  * `validar_username(s:str)->bool`
  * `alta_usuario(usuarios:dict)->None`
  * `recomendar(usuarios,talleres,u)->list[tuple[str,int,int]]`  # (codigo, score, cupo)
* **Pretty print**:

  ```python
  print(f"{codigo:6} | {titulo:25} | {len(inscritos):2}/{capacidad:2} | {', '.join(tags)}")
  ```

---

## 🧨 Casos límite que debes manejar

* Intentar inscribir dos veces al mismo taller.
* Taller lleno.
* Usuario o taller inexistente.
* Intereses vacíos → recomendaciones vacías.
* Borrar/interrumpir flujo y volver al menú sin crashear.

---

## 🧗 Retos Extra (para encenderlo más)

1. **Cancelaciones** con regla: si cancelas, se elimina de ambos lados.
2. **Lista de espera** (cola con `collections.deque`) cuando no haya cupo; al cancelar alguien, corre la lista.
3. **Compatibilidad de intereses**:

   * Para un usuario `u`, sugiere 3 usuarios “afinidad”:

     * afinidad(u, v) = `|intereses_u ∩ intereses_v| / |intereses_u ∪ intereses_v|`
4. **Recomendación negativa**:

   * Filtra talleres cuyos `tags` sean **disjuntos** de los intereses del usuario (`isdisjoint`).
5. **Snapshot de datos**:

   * Exporta un **resumen** en texto (sin archivos todavía) al finalizar cada operación (solo `print` bonito).
6. **Ranking por multi-criterio**:

   * Ordena recomendaciones por: `score desc`, luego `cupo desc`, luego `titulo asc`.

---

## 🧰 Esqueleto inicial (starter)

Crea `hybridge_workshop_manager.py` y empieza con esto:

```python
from datetime import date

usuarios = {}
talleres = {}

def pedir_tags(msg):
    bruto = input(msg).strip()
    if not bruto:
        return set()
    return set(x.strip().lower() for x in bruto.split(",") if x.strip())

def alta_usuario():
    username = input("Username (3-15 alfanumérico): ").strip().lower()
    if not (username.isalnum() and 3 <= len(username) <= 15):
        print("✗ Username inválido.")
        return
    if username in usuarios:
        print("✗ Ya existe ese usuario.")
        return
    nombre = input("Nombre: ").strip().title()
    edad_s = input("Edad (13-99): ").strip()
    if not edad_s.isdigit():
        print("✗ Edad inválida.")
        return
    edad = int(edad_s)
    if not (13 <= edad <= 99):
        print("✗ Edad fuera de rango.")
        return
    intereses = pedir_tags("Intereses (coma-separados): ")
    usuarios[username] = {
        "nombre": nombre,
        "edad": edad,
        "intereses": intereses,
        "inscripciones": []
    }
    print("✓ Usuario creado.")

def alta_taller():
    codigo = input("Código (p.ej. PY101): ").strip().upper()
    if codigo in talleres:
        print("✗ Ya existe ese taller.")
        return
    titulo = input("Título: ").strip().title()
    cap_s = input("Capacidad (>0): ").strip()
    if not cap_s.isdigit() or int(cap_s) <= 0:
        print("✗ Capacidad inválida.")
        return
    capacidad = int(cap_s)
    tags = pedir_tags("Tags del taller: ")
    talleres[codigo] = {
        "titulo": titulo,
        "capacidad": capacidad,
        "tags": tags,
        "inscritos": set()
    }
    print("✓ Taller creado.")

def inscribir():
    u = input("Username: ").strip().lower()
    c = input("Código taller: ").strip().upper()
    if u not in usuarios or c not in talleres:
        print("✗ Usuario o taller inexistente.")
        return
    if u in talleres[c]["inscritos"]:
        print("✗ Ya inscrito.")
        return
    cupo = talleres[c]["capacidad"] - len(talleres[c]["inscritos"])
    if cupo <= 0:
        print("✗ Sin cupo.")
        return
    talleres[c]["inscritos"].add(u)
    usuarios[u]["inscripciones"].append((c, date.today().isoformat()))
    print("✓ Inscripción realizada.")

def recomendar():
    u = input("Username para recomendar: ").strip().lower()
    if u not in usuarios:
        print("✗ Usuario no existe.")
        return
    intereses = usuarios[u]["intereses"]
    ranking = []
    for codigo, t in talleres.items():
        score = len(intereses & t["tags"])
        cupo = t["capacidad"] - len(t["inscritos"])
        ranking.append((codigo, score, cupo, t["titulo"]))
    ranking.sort(key=lambda x: (-x[1], -x[2], x[3]))
    print("\n— Recomendaciones —")
    for codigo, score, cupo, titulo in ranking:
        if score == 0:  # omite irrelevantes
            continue
        print(f"{codigo:6} | {titulo:25} | score={score} | cupo={cupo}")

def reportes():
    print("\n[1] Top 3 talleres por inscritos")
    print("[2] Usuarios sin inscripciones")
    print("[3] Ocupación por taller (desc)")
    print("[4] Tags globales y faltantes por usuario")
    op = input("Opción: ").strip()
    if op == "1":
        top = sorted(talleres.items(), key=lambda kv: len(kv[1]["inscritos"]), reverse=True)[:3]
        for cod, t in top:
            print(f"{cod:6} | {t['titulo'][:25]:25} | {len(t['inscritos'])}/{t['capacidad']}")
    elif op == "2":
        vacios = [u for u, d in usuarios.items() if not d["inscripciones"]]
        print("Sin inscripciones:", ", ".join(vacios) or "—")
    elif op == "3":
        orden = sorted(
            talleres.items(),
            key=lambda kv: len(kv[1]["inscritos"]) / kv[1]["capacidad"] if kv[1]["capacidad"] else 0,
            reverse=True
        )
        for cod, t in orden:
            occ = len(t["inscritos"]) / t["capacidad"] if t["capacidad"] else 0
            print(f"{cod:6} | {t['titulo'][:25]:25} | {occ:.0%}")
    elif op == "4":
        u = input("Username: ").strip().lower()
        if u not in usuarios:
            print("✗ Usuario no existe.")
            return
        tags_global = set().union(*(t["tags"] for t in talleres.values())) if talleres else set()
        faltantes = tags_global - usuarios[u]["intereses"]
        print("Tags globales:", ", ".join(sorted(tags_global)) or "—")
        print("Faltantes para", u + ":", ", ".join(sorted(faltantes)) or "—")

def menu():
    while True:
        print("\n— Hybridge Workshop Manager —")
        print("[1] Alta usuario")
        print("[2] Alta taller")
        print("[3] Inscribir usuario en taller")
        print("[4] Recomendar talleres")
        print("[5] Reportes")
        print("[0] Salir")
        op = input("Opción: ").strip()
        if op == "1": alta_usuario()
        elif op == "2": alta_taller()
        elif op == "3": inscribir()
        elif op == "4": recomendar()
        elif op == "5": reportes()
        elif op == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
```

> Con esto tienes **esqueleto + lógica base**. De aquí, puedes atacar los **Retos Extra** para subir la dificultad.

---

## 🧨 Cómo te evaluaría (rubrica rápida)

* **Correctitud** (no se rompe, valida bien): 40%
* **Uso de estructuras adecuadas** (set/dict/tuple/list): 25%
* **Legibilidad** (nombres, prints claros, funciones pequeñas): 20%
* **Extras implementados** (listas de espera, afinidad, ranking multi-criterio): 15%

---
