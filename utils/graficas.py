import matplotlib 
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def grafica_genero(hombres, mujeres, titulo):

    etiquetas = ["Hombres", "Mujeres"]
    valores = [hombres, mujeres]

    plt.figure()

    plt.pie(
        valores,
        labels=etiquetas,
        autopct="%1.1f%%"
    )

    plt.title(titulo)

    archivo = "grafica_genero.png"

    plt.savefig(archivo)
    plt.close()

    return archivo

def grafica_comparativa(anios, valores, titulo):

    plt.figure()

    plt.bar(anios, valores)

    plt.title(titulo)
    plt.xlabel("Año")
    plt.ylabel("Cantidad")

    archivo = "grafica_comparativa.png"

    plt.savefig(archivo)
    plt.close()

    return archivo