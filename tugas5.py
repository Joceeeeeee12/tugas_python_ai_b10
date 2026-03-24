# =========================
# FUNCTIONS
# =========================

def greet(nama: str) -> str:
    return f"Halo, {nama}!"
def tambah(a: float, b: float = 0.0) -> float:
    return float(a + b)
def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka),2)

# =========================
# CLASS
# =========================
class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []
    
    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)
    
    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)
    
    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"
    
    def __str__(self) -> str:
        rata = self.rata_nilai()
        stat = self.status()
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={rata}, status={stat})"

# =========================
# DEMO
# =========================
if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    
    print(greet("Arifian"))
    print(tambah(5, 7))
    print(tambah(10))
    print(rata_rata([80, 90, 100]))
    print(rata_rata([]))

    print("\n=== CLASS STUDENT ===")
    
    s1 = Student("Jackson", "A123")
    s1.tambah_nilai(85)
    s1.tambah_nilai(90)
    s1.tambah_nilai(88)
    print(s1)            # Student(nama='Jackson', nim='A123', rata=87.67, status=LULUS)
    print(s1.rata_nilai())  # 87.67
    print(s1.status())      # LULUS
    s2 = Student("Kay", "A456")
    s2.tambah_nilai(60)
    s2.tambah_nilai(65)
    s2.tambah_nilai(70)
    print(s2)            # Student(nama='Kay', nim='A456', rata=65.0, status=TIDAK LULUS)
    print(s2.rata_nilai())  # 65.0
    print(s2.status())      # TIDAK LULUS
