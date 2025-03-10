def ededi_orta(siyahi):
    if not siyahi:
        return None  # Siyahi boşdursa, None qaytar
    return sum(siyahi) / len(siyahi)

# İstifadə nümunəsi
ededler = [10, 20, 30, 40, 50]
orta = ededi_orta(ededler)
print(f"Ədədi orta: {orta}")
