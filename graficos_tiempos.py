# ...existing code...
"""
Genera dos gráficos usando matplotlib:
 1) Histograma comparado (distribución de tiempos).
 2) Barra de comparación (media ± std) entre original y optimizado.

Uso (desde PowerShell en la carpeta del proyecto):
  py -3 .\graficos_tiempos.py
Opciones: --original, --optimizado, --runs, --outdir
"""
import argparse
import json
import os
import subprocess
import sys
import time
import statistics

def run_multiple(script_path, runs=30):
    times = []
    cmd = [sys.executable, script_path]
    for i in range(runs):
        t0 = time.perf_counter()
        try:
            subprocess.run(cmd, check=True)
            t1 = time.perf_counter()
            times.append(t1 - t0)
        except subprocess.CalledProcessError as e:
            print(f"Ejecución fallida ({os.path.basename(script_path)}) run {i+1}/{runs}: {e}", file=sys.stderr)
    return times

def plot_times(dist_orig, dist_opt, out_dir, prefix="times"):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except Exception:
        print("Instala dependencias: pip install matplotlib numpy", file=sys.stderr)
        return None, None

    os.makedirs(out_dir, exist_ok=True)

    # Histograma comparado
    plt.figure(figsize=(10,4))
    all_vals = (dist_orig or []) + (dist_opt or [])
    bins = np.histogram_bin_edges(all_vals, bins='auto') if all_vals else 20
    plt.hist(dist_orig, bins=bins, alpha=0.6, label='original', color='C0')
    plt.hist(dist_opt, bins=bins, alpha=0.6, label='optimizado', color='C1')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de tiempos de ejecución')
    plt.legend()
    hist_path = os.path.join(out_dir, f"{prefix}_distribution.png")
    plt.tight_layout()
    plt.savefig(hist_path)
    plt.close()

    # Comparativa media ± std
    labels = []
    means = []
    stds = []
    if dist_orig:
        labels.append("original"); means.append(statistics.mean(dist_orig)); stds.append(statistics.stdev(dist_orig) if len(dist_orig)>1 else 0)
    if dist_opt:
        labels.append("optimizado"); means.append(statistics.mean(dist_opt)); stds.append(statistics.stdev(dist_opt) if len(dist_opt)>1 else 0)

    comp_path = None
    if means:
        import numpy as np
        x = np.arange(len(means))
        plt.figure(figsize=(6,4))
        plt.bar(x, means, yerr=stds, capsize=6, color=['C0','C1'][:len(means)])
        plt.xticks(x, labels)
        plt.ylabel('Tiempo medio (s)')
        plt.title('Comparativa de tiempos (media ± std)')
        comp_path = os.path.join(out_dir, f"{prefix}_comparison.png")
        plt.tight_layout()
        plt.savefig(comp_path)
        plt.close()

    return hist_path, comp_path

def save_times_json(outpath, orig_times, opt_times):
    data = {
        "original": {"times": orig_times},
        "optimizado": {"times": opt_times}
    }
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def main():
    p = argparse.ArgumentParser(description="Generar gráficos de tiempos para original vs optimizado")
    p.add_argument("--original", default="codigo_original.py", help="ruta al script original")
    p.add_argument("--optimizado", default="codigo_optimizado.py", help="ruta al script optimizado")
    p.add_argument("--runs", type=int, default=30, help="número de ejecuciones por script")
    p.add_argument("--outdir", default=".", help="directorio de salida para imágenes y json")
    args = p.parse_args()

    base = os.path.abspath(os.path.dirname(__file__))
    orig_path = os.path.join(base, args.original) if not os.path.isabs(args.original) else args.original
    opt_path = os.path.join(base, args.optimizado) if not os.path.isabs(args.optimizado) else args.optimizado

    if not os.path.exists(orig_path):
        print(f"No se encuentra {orig_path}", file=sys.stderr); return
    if not os.path.exists(opt_path):
        print(f"No se encuentra {opt_path}", file=sys.stderr); return

    print(f"Ejecutando {args.runs} veces: {os.path.basename(orig_path)}")
    orig_times = run_multiple(orig_path, runs=args.runs)
    print(f"Ejecutando {args.runs} veces: {os.path.basename(opt_path)}")
    opt_times = run_multiple(opt_path, runs=args.runs)

    outdir = os.path.abspath(args.outdir)
    times_json = os.path.join(outdir, "tiempos_generados.json")
    save_times_json(times_json, orig_times, opt_times)
    print(f"Tiempos guardados en {times_json}")

    hist, comp = plot_times(orig_times, opt_times, outdir, prefix="times")
    if hist: print(f"Histograma: {hist}")
    if comp: print(f"Comparativa: {comp}")
    if not hist and not comp:
        print("No se generaron gráficos. Comprueba instalación de matplotlib/numpy o que hubo ejecuciones exitosas.", file=sys.stderr)

if __name__ == "__main__":
    main()
# ...existing code...