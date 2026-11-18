def read_log(path):
    """Lit un fichier de log et renvoie la liste de ses lignes."""
    lines = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)
    return lines
