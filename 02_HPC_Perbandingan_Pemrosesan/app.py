from time import perf_counter
from multiprocessing import Pool, cpu_count
import os

def sum_squares_range(bounds):
    start, end = bounds
    return sum(i*i for i in range(start, end))

def run_serial(n):
    return sum_squares_range((0, n))

def run_parallel(n, workers):
    step = (n + workers - 1) // workers
    chunks = [(i, min(i + step, n)) for i in range(0, n, step)]
    with Pool(processes=workers) as pool:
        return sum(pool.map(sum_squares_range, chunks))

if __name__ == "__main__":
    n = int(input("Jumlah bilangan yang dihitung (contoh 2000000): ") or "2000000")
    workers = max(2, min(cpu_count(), 4))
    t0 = perf_counter(); serial = run_serial(n); serial_time = perf_counter()-t0
    t0 = perf_counter(); parallel = run_parallel(n, workers); parallel_time = perf_counter()-t0
    print(f"Jumlah data: {n:,}")
    print(f"Serial: {serial:,} | waktu: {serial_time:.3f} detik")
    print(f"Paralel ({workers} proses): {parallel:,} | waktu: {parallel_time:.3f} detik")
    print("Hasil sama:", serial == parallel)
    if parallel_time > 0:
        print(f"Speedup: {serial_time/parallel_time:.2f}x")
    print("Catatan: pada beban kecil, paralel bisa lebih lambat karena overhead.")
