# Import & Setup
import numpy as np
import pandas as pd
import os
# Set seed untuk hasil konsisten
np.random.seed(42)

# NumPy – Data & Statistik
nilai_ujian = np.random.normal(75, 15, 10).astype(int)
rata_rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

# Pandas – DataFrame
data = {
    "Nama": ["Joce", "Kai", "Jack", "Jill", "Long", "Hui"],
    "NIM": ["A12345", "A12346", "A12347", "A12348", "A12349", "A12350"],
    "Nilai": nilai_ujian[4:10]  # Ambil dari arxay NumPy
}
df = pd.DataFrame(data)
df["Status"] = np.where(df["Nilai"] >= 70, "LULUS", "TIDAK LULUS")

# File I/O – Tulis Ringkasan ke .txt
with open("ringkasan_tugas6.txt", "w") as f:
    f.write("RINGKASAN STATISTIK NUMPY\n")
    f.write(f"Rata-rata: {rata_rata:.2f}\n")
    f.write(f"Median: {median:.2f}\n")
    f.write(f"Std Dev: {std_dev:.2f}\n")
    f.write(f"Min: {nilai_min}, Max: {nilai_max}\n\n")
    
    f.write("RINGKASAN DATAFRAME\n")
    f.write(f"Jumlah baris: {len(df)}\n")
    lulus = (df['Status'] == 'LULUS').sum()
    f.write(f"Jumlah LULUS: {lulus}\n")
    f.write(f"Jumlah TIDAK LULUS: {len(df)-lulus}\n\n")

print("\nRingkasan disimpan ke ringkasan_tugas6.txt")

# OOP Sederhana
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    def average(self) -> float:
        return self.df["Nilai"].mean()
    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = (self.df["Nilai"] >= threshold).sum()
        total = len(self.df)
        return (lulus / total) * 100
    def save_summary (self, path: str):
        avg = self.average()
        pass_rate = self.pass_rate()
        total = len(self.df)
        lulus = (self.df["Nilai"]>=70).sum()
        tidak_lulus = total - lulus

        with open(path, "a") as f:
            f.write("RINGKASAN GRADEBOOK\n")
            f.write(f"Total data: {total}\n")
            f.write(f"Rata-rata Nilai: {avg:.2f}\n")
            f.write(f"Jumlah lulus: {lulus}\n")
            f.write(f"Jumlah tidak lulus: {tidak_lulus}\n")
            f.write(f"Pass Rate: {pass_rate:.2f}%\n\n")

    def __str__(self) -> str:
        total = len(self.df)
        avg = self.average()
        return f"GradeBook: {total} data, rata-rata nilai = {avg:.2f}"
    
#Demo
if __name__ == "__main__":
    print("=== NUMPY ===")
    print(f"Array nilai ujian: {nilai_ujian}")
    print("Rata-rata:", rata_rata)
    print("Median:", median)
    print("Standar Deviasi:", std_dev)
    print("Min:", nilai_min, "Max:", nilai_max)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print(f"Average: {gb.average():.2f}")
    print(f"Pass Rate: {gb.pass_rate():.2f}%")

    gb.save_summary("ringkasan_tugas6.txt")
    
            
