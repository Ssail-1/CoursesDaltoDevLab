
# Un sistema de consola para gestionar talleres
# - Inscripciones de usuarios}
# - Cupos
# - Recomendaciones por intereses
# - Estadisticas

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






