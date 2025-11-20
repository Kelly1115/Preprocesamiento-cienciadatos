# ...existing code...
import subprocess
import time
import statistics
import json
import os
import sys
import pstats
import io
# ...existing code...

def profile_script(script_path, out_prof, out_txt, sort='cumtime', top=30):
    cmd = [sys.executable, "-m", "cProfile", "-o", out_prof, script_path]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ejecución fallida al perfilar {script_path}: {e}", file=sys.stderr)
        return None

    s = io.StringIO()
    ps = pstats.Stats(out_prof, stream=s).sort_stats(sort)
    ps.print_stats(top)
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(s.getvalue())
    # total_tt es el tiempo total medido por cProfile
    total = getattr(ps, "total_tt", None)
    return total

# ...existing code...

if __name__ == "__main__":
    base = os.path.abspath(os.path.dirname(__file__))

    orig_py = os.path.join(base, "codigo_original.py")
    opt_py = os.path.join(base, "codigo_optimizado.py")

    prof_orig = os.path.join(base, "codigo_original.prof")
    prof_opt = os.path.join(base, "codigo_optimizado.prof")
    txt_orig = os.path.join(base, "profiling_original.txt")
    txt_opt = os.path.join(base, "profiling_optimizado.txt")

    print("Perfilando código original...")
    t_orig = profile_script(orig_py, prof_orig, txt_orig, top=50)
    print("Perfilando código optimizado...")
    t_opt = profile_script(opt_py, prof_opt, txt_opt, top=50)

    summary = {
        "original": {"prof_file": prof_orig, "txt_file": txt_orig, "total_time": t_orig},
        "optimizado": {"prof_file": prof_opt, "txt_file": txt_opt, "total_time": t_opt},
    }

    # Imprime comparación rápida
    print("\nComparación de tiempos (total de cProfile):")
    print(f"Original:   {t_orig if t_orig is not None else 'error'} segundos")
    print(f"Optimizado: {t_opt if t_opt is not None else 'error'} segundos")

    # Recomendar funciones críticas (indicar al usuario revisar profiling_optimizado.txt)
    if t_opt is not None:
        print("\nFunciones que más tiempo consumen (ver profiling_optimizado.txt para detalles).")
    else:
        print("\nNo se generó profiling_optimizado.txt correctamente.")

    # guardar resumen
    with open(os.path.join(base, "perfil_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

# ...existing code...