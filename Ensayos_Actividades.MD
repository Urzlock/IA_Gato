#3.-Introducción a la Inteligencia Artificial: Intro-spección

##Introducción 
El ajedrez es un antiguo juego de estrategia que ha cautivado la mente de jugadores de todo el mundo durante siglos. Se cree que el juego se originó en la India en el siglo VI, y desde entonces ha evolucionado y se ha extendido por diversas culturas y civilizaciones. A lo largo de la historia, el ajedrez ha sido más que un simple juego; ha sido un campo de batalla mental, una forma de arte y un medio para explorar la complejidad de la toma de decisiones estratégicas.
El juego se juega en un tablero cuadrado dividido en 64 casillas, alternando colores oscuros y claros. Cada jugador comienza con 16 piezas: un rey, una reina, dos torres, dos caballos, dos alfiles y ocho peones. El objetivo es someter al rey del oponente a un jaque mate, lo que significa que el rey está amenazado y no puede escapar de la amenaza.
El ajedrez es conocido por su profunda complejidad estratégica y táctica. Requiere habilidades cognitivas como la planificación a largo plazo, el pensamiento analítico, la memoria y la capacidad de evaluar posiciones de juego. Además, el ajedrez ha sido objeto de estudio en campos como la psicología, la inteligencia artificial y la filosofía debido a la riqueza de desafíos que presenta.
La introspección en el contexto de la inteligencia artificial se refiere a la capacidad de un sistema para examinar y comprender sus propios procesos internos, tomando conciencia de su propio estado y funcionamiento. Aunque la introspección en la IA no se equipara exactamente a la introspección humana, que implica una reflexión consciente y subjetiva, en la IA se refiere al análisis y comprensión de las decisiones y procesos internos de un sistema.
La introspección en la IA es un área de investigación importante, ya que busca mejorar la transparencia y la interpretabilidad de los modelos de inteligencia artificial. Los sistemas de IA modernos, especialmente los basados en aprendizaje profundo, a menudo son considerados como cajas negras debido a la complejidad de sus estructuras y algoritmos. La introspección busca abrir estas cajas negras, permitiendo a los desarrolladores y usuarios comprender mejor cómo y por qué un modelo de IA toma ciertas decisiones.
La introspección puede lograrse a través de diversas técnicas, como la visualización de capas internas de una red neuronal, el análisis de la importancia de las características en un modelo o la interpretación de las decisiones basadas en la entrada de datos. La introspección no solo mejora la confianza en los modelos de IA, sino que también puede ayudar a identificar sesgos y mejorar la ética en la implementación de sistemas de inteligencia artificial en aplicaciones del mundo real.
Problema
Coloca ocho alfiles (cuatro negros y cuatro blancos) en un tablero de ajedrez reducido, tal como se ve en la figura. El problema consiste en hacer que los alfiles negros intercambien sus posiciones con los blancos, ningún alfil debe atacar en ningún momento otro del color opuesto. Se deben alternar los movimientos, primero uno blanco, luego uno negro, luego uno blanco y así sucesivamente. ¿Cuál es el mínimo número de movimientos en que se puede conseguir?

##Solución 
Recapitulando lo comentado en la sección anterior, se nos requiere obtener un resultado satisfactorio al problema de poder intercambiar de posición todos los alfiles de color blanco con sus contrapartes negras. Para esto es fundamental el entender de antemano cual es el comportamiento de los alfiles con lo que respecta a su movimiento en un tablero, este mismo siendo un movimiento en diagonal indiferente de la dirección con respecto a un color en específico, es decir, si el alfil se encuentra inicialmente en una casilla blanca, solo se podrá mover en diagonal a otras casillas que compartan este mismo color.
Tomando en cuenta esto también es importante comprender las limitaciones de espacio que se presentan en el planteamiento del problema, las cuales se presentan en la forma de un tablero con dimensiones de 4 casillas de ancho por 5 casillas de alto. Tomando en cuenta que ambos grupos de alfiles estarán posicionados a los respectivos extremos, nos deja un área de movimientos disponibles al centro del tablero de 4 casillas de ancho por 3 de alto. A continuación, se presenta una representación de grafica del tablero el cual cuenta con una identificación única para cada una de sus casillas para que sea más sencillo poder visualizar el recorrido de cada una de las piezas y corroborar que se obtiene un resultado satisfactorio,

![Tablero](src/tablero.png)

| Movimiento | Posición inicial | Posición final | Color  |
|------------|-------------------|-----------------|--------|
| 1          | XVIII             | XVII            | Blancas|
| 2          | III               | VI              | Negras |
| 3          | XVII              | XII             | Blancas|
| 4          | VII               | XIII            | Negras |
| 5          | XIX               | XVIII           | Blancas|
| 6          | II                | VII             | Negras |
| 7          | XVII              | XIII            | Blancas|
| 8          | VI                | XVII            | Negras |
| 9          | XII               | III             | Blancas|
| 10         | XIII              | XVIII           | Negras |
| 11         | XVIII             | XI              | Blancas|
| 12         | VII               | XVI             | Negras |
| 13         | XIII              | IX              | Blancas|
| 14         | XVI               | XI              | Negras |
| 15         | XI                | XIX             | Blancas|
| 16         | XIV               | V               | Negras |
| 17         | IX                | II              | Blancas|
| 18         | XI                | X               | Negras |
| 19         | XVIII             | IX              | Blancas|
| 20         | I                 | X               | Negras |
| 21         | III               | VII             | Blancas|
| 22         | XVII              | XVI             | Negras |
| 23         | IX                | XIII            | Blancas|
| 24         | X                | VIII             | Negras |
| 25         | XIX               | XVI             | Blancas|
| 26         | VI                | I               | Negras |
| 27         | XVI               | I               | Blancas|
| 28         | I                 | XIX             | Negras |
| 29         | VII               | II              | Blancas|
| 30         | XVI               | XV              | Negras |
| 31         | XIII              | VIII            | Blancas|
| 32         | IX               | XVII            | Negras |
| 33         | VI                | III             | Blancas|
| 34         | XV               | XVIII           | Negras |
| 35         | VIII              | VI              | Blancas|
| 36         | XVII              | XIX             | Negras |


##Conclusión

El problema planteado, que consiste en el intercambio de posiciones entre alfiles blancos y negros en un tablero de ajedrez de dimensiones reducidas, ha sido resuelto de manera óptima en 36 movimientos. La solución se fundamenta en la comprensión del movimiento diagonal inherente a los alfiles y la consideración de las restricciones espaciales presentes en el tablero. Este ejercicio subraya la importancia no solo de la familiaridad con las reglas y propiedades específicas de las piezas de ajedrez, sino también de la capacidad estratégica y analítica necesaria para abordar problemas de índole compleja. Asimismo, se puede establecer una analogía con el concepto de introspección en inteligencia artificial, donde la comprensión profunda de los procesos internos se erige como un pilar fundamental para la toma de decisiones efectivas y transparentes. En este contexto, la resolución del problema ejemplifica cómo el conocimiento detallado de las reglas y restricciones puede conducir a soluciones eficientes y bien fundadas.

---
#4.- Introducción a la Inteligencia Artificial: Intro-spección
##Introducción 
La introspección, una expresión derivada del latín "introspicere" que se traduce como "mirar en el interior," nos invita a sumergirnos en la capacidad humana de adquirir conocimiento sobre los propios estados mentales. Este acto de observarse y analizarse a uno mismo plantea similitudes metafóricas con el intrigante desafío de contar el número de elementos en una matriz, donde cada "isla" está compuesta por celdas del mismo valor. Este ensayo explora la resolución de esta problemática mediante enfoques tanto iterativos como recursivos.
Planteamiento del Problema
Enfrentamos la tarea de desarrollar un método capaz de contar el número de elementos que comparten el mismo valor en una matriz dada. Este enigma nos lleva a pensar en la introspección, ya que el programa debe ejercer una suerte de "observación" y "análisis" de la matriz, identificando agrupaciones de celdas del mismo valor como entidades diferenciadas.
Enfoque Iterativo
El método iterativo aborda este desafío paso a paso. Inicia con una celda y explora sus vecinos, marcando aquellos del mismo valor como parte de la misma isla. Este proceso se repite hasta que no haya más celdas por explorar. En este contexto, el enfoque iterativo permite una descomposición detallada de la matriz, similar a cómo la introspección fragmenta la conciencia en pensamientos y emociones individuales.
Enfoque Recursivo
En contraste, el enfoque recursivo se sumerge en la matriz de manera más profunda y reflexiva. Explora cada celda y se expande a través de sus vecinos del mismo valor. Esta aproximación reflexiva refleja la naturaleza introspectiva al buscar comprender los procesos mentales a un nivel más profundo. La recursividad facilita una comprensión más holística de la matriz, identificando y contando las islas de manera eficiente.
Reflexiones sobre la Implementación Práctica
Ambos enfoques, iterativo y recursivo, pueden ser implementados utilizando un lenguaje de programación. En el enfoque iterativo, se emplea un bucle para explorar la matriz celda por celda, mientras que, en el enfoque recursivo, una función se llama a sí misma para explorar los vecinos de una celda.

##Solución Iterativa
Una vez tomamos en cuenta todo lo anterior podemos proponer una solución usando el paradigma iterativo de la siguiente forma
```python
def contar_islas_iterativo(imagen):
    if not imagen or not imagen[0]:
        return 0
    
    filas = len(imagen)
    columnas = len(imagen[0])
    visitado = [[False] * columnas for _ in range(filas)]
    contador_islas = 0

    for i in range(filas):
        for j in range(columnas):
            if imagen[i][j] == 1 and not visitado[i][j]:
                dfs_iterativo(imagen, i, j, visitado)
                contador_islas += 1

    return contador_islas

def dfs_iterativo(imagen, x, y, visitado):
    filas, columnas = len(imagen), len(imagen[0])
    stack = [(x, y)]
    
    while stack:
        i, j = stack.pop()
        if 0 <= i < filas and 0 <= j < columnas and imagen[i][j] == 1 and not visitado[i][j]:
            visitado[i][j] = True
            stack.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

```
##Solución Recursiva
La función contar_elementos_iterativo toma una matriz como argumento y comprueba si está vacía. Si la matriz está vacía, la función devuelve 0. Luego, calcula el número de filas y columnas de la matriz y crea una matriz llamada visitado para realizar un seguimiento de los elementos ya visitados.
La función interna explorar se define para explorar recursivamente una "isla" de elementos del mismo color. Toma las coordenadas (x, y) de un elemento, el valor color que se está explorando, y marca los elementos del mismo color como visitados.
La sección principal del código utiliza dos bucles anidados para recorrer cada elemento de la matriz. Si un elemento no ha sido visitado, invoca la función explorar para marcar todos los elementos de la "isla" a la que pertenece. Incrementa el contador de islas por cada nueva "isla" encontrada.
Finalmente, la función devuelve el número total de "islas" encontradas en la matriz. Un ejemplo de uso se proporciona con una matriz de ejemplo, y se imprime el resultado del conteo de islas utilizando la función contar_elementos_iterativo. Este código puede ser útil para casos en los que se desee identificar agrupaciones de elementos del mismo valor en una matriz bidimensional.
De igual forma podemos determinar una solución utilizando la recursividad de la siguiente forma

```python
def contar_islas_recursivo(imagen):
    if not imagen or not imagen[0]:
        return 0
    
    filas = len(imagen)
    columnas = len(imagen[0])
    visitado = [[False] * columnas for _ in range(filas)]
    contador_islas = 0

    for i in range(filas):
        for j in range(columnas):
            if imagen[i][j] == 1 and not visitado[i][j]:
                dfs_recursivo(imagen, i, j, visitado)
                contador_islas += 1

    return contador_islas

def dfs_recursivo(imagen, x, y, visitado):
    filas, columnas = len(imagen), len(imagen[0])
    
    if 0 <= x < filas and 0 <= y < columnas and imagen[x][y] == 1 and not visitado[x][y]:
        visitado[x][y] = True
        dfs_recursivo(imagen, x+1, y, visitado)
        dfs_recursivo(imagen, x-1, y, visitado)
        dfs_recursivo(imagen, x, y+1, visitado)
        dfs_recursivo(imagen, x, y-1, visitado)
```

La función comienza verificando si la matriz de entrada está vacía. En caso afirmativo, devuelve 0, ya que no hay elementos para contar. Luego, se determinan las dimensiones de la matriz mediante la obtención de la cantidad de filas y columnas.
A continuación, se inicializa una matriz llamada visitado, que se utiliza para realizar un seguimiento de los elementos que ya han sido visitados durante el proceso de exploración de las "islas". Esta matriz se crea con las mismas dimensiones que la matriz de entrada y se llena con valores booleanos, todos inicialmente establecidos en False.
La función interna explorar se define para llevar a cabo la exploración recursiva de una "isla". Recibe las coordenadas (x, y) de un elemento, así como el valor color del elemento que se está explorando. La exploración se realiza verificando las coordenadas, el color del elemento y si ya ha sido visitado. Si se cumplen estas condiciones, el elemento se marca como visitado y se exploran recursivamente sus vecinos en las cuatro direcciones: arriba, abajo, izquierda y derecha.
El proceso principal del código utiliza dos bucles anidados para recorrer cada elemento de la matriz. Si el elemento no ha sido visitado, se invoca la función explorar para marcar todos los elementos de la "isla" a la que pertenece. Además, se incrementa un contador llamado islas por cada nueva "isla" encontrada.
Finalmente, la función devuelve el número total de "islas" encontradas en la matriz. El código incluye un ejemplo de uso con una matriz de ejemplo, donde se imprime el resultado del conteo de "islas" utilizando la función contar_elementos_recursivo.
Este código es una implementación recursiva que busca identificar agrupaciones de elementos del mismo valor en una matriz bidimensional, proporcionando un enfoque alternativo al enfoque iterativo previamente discutido.

##Conclusión
En conclusión, exploramos la analogía entre la introspección y el desafío de contar elementos en una matriz, utilizando enfoques iterativos y recursivos. El enfoque iterativo se asemeja a un análisis paso a paso, mientras que el recursivo se sumerge reflexivamente. Ambos métodos, implementados en un lenguaje de programación, ofrecen soluciones efectivas. Esta reflexión destaca la versatilidad de estos enfoques, no solo en programación, sino también en nuestra capacidad para comprender la complejidad de la mente. La elección entre iteración y recursión depende del problema, proporcionando flexibilidad para abordar desafíos diversos.

---


##Introducción
La introspección, derivada del latín "introspicere", que significa "mirar hacia dentro", es una práctica antigua que permite a los humanos adquirir conocimientos sobre sus propios estados mentales. Este proceso implica observación y análisis interno, en el que el sujeto se sumerge en la interpretación y representación de sus propios procesos cognitivos y afectivos. En el contexto de la inteligencia artificial, esta introspección se convierte en un elemento clave para comprender cómo las máquinas abordan los problemas y desarrollan soluciones de manera similar a la mente humana.
##Problema:
Realizar un algoritmo que permita contar elementos que que estén compuestos del color rojo en la siguiente imagen:
Basado en lo visto en el ensayo anterior, podemos reestructurar el código realizado previamente para poder reaprovecharlo para contar pixeles de una tonalidad RGB deseada (en este caso, roja). Esto mismo nos permite obtener como resultado el siguiente código:

##Solución
```python
from PIL import Image

def contar_pixeles_rojos(imagen):
    if not imagen:
        return 0
    
    ancho, alto = imagen.size
    pixeles = imagen.load()
    
    visitado = [[False] * alto for _ in range(ancho)]
    
    def explorar(x, y, color):
        contador = 0
        if 0 <= x < ancho and 0 <= y < alto and pixeles[x, y][0] == color and not visitado[x][y]:
            visitado[x][y] = True
            contador += 1
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                contador += explorar(x + dx, y + dy, color)
        return contador
    
    grupos_pixeles_rojos = 0
    for i in range(ancho):
        for j in range(alto):
            if not visitado[i][j]:
                contador_actual = explorar(i, j, pixeles[i, j][0])
                if contador_actual >= 4:
                    grupos_pixeles_rojos += 1
    
    return grupos_pixeles_rojos


imagen_ejemplo = Image.open("D:/test.jpg")  
print("Número de grupos de 4 píxeles rojos o más:", contar_pixeles_rojos(imagen_ejemplo))

```
Este código en Python emplea la biblioteca PIL (Python Imaging Library) para realizar un análisis de imágenes, específicamente para determinar el número de grupos de píxeles rojos, cada uno compuesto por al menos cuatro píxeles adyacentes de color rojo. La función principal, denominada `contar_pixeles_rojos`, acepta una imagen como parámetro y devuelve el recuento de tales grupos presentes en la imagen suministrada
En un primer paso, se realiza una comprobación para verificar la existencia de una imagen. En caso de que no se haya proporcionado una imagen, la función retorna 0. Posteriormente, se extraen las dimensiones de la imagen (ancho y alto), y se carga la información de píxeles en la variable `pixeles`.
Se crea una matriz denominada `visitado` para llevar un registro de los píxeles que han sido visitados durante el proceso de exploración. Inicialmente, todos los elementos de esta matriz se establecen en `False`.
A continuación, se define la función interna `explorar`. Esta función emplea un enfoque de búsqueda recursiva para explorar los píxeles adyacentes al píxel actual. Si un píxel cumple con ciertos criterios (se encuentra dentro de los límites de la imagen, es de color rojo y no ha sido visitado), se marca como visitado y se incrementa el contador. La exploración prosigue en las direcciones arriba, abajo, izquierda y derecha desde el píxel actual.
Una vez definida la función de exploración, se inicializa la variable `grupos_pixeles_rojos` en 0. Luego, mediante un bucle anidado, se recorren todos los píxeles de la imagen. Si un píxel no ha sido visitado, se inicia la exploración desde ese píxel y se obtiene el número de píxeles rojos en el grupo actual. Si este número es igual o mayor a 4, se incrementa el contador de grupos de píxeles rojos.
Finalmente, la función devuelve el total de grupos de píxeles rojos identificados en la imagen.
En el ejemplo de uso al final del código, se carga una imagen denominada "test.jpg" (es necesario reemplazar la ruta con la ubicación de la imagen deseada) mediante la función `Image.open` de la biblioteca PIL. Posteriormente, se imprime el resultado de aplicar la función `contar_pixeles_rojos` a dicha imagen, representando el número de grupos de 4 píxeles rojos o más presentes en la misma.
##Conclusión
En conclusión, el código en Python utilizando la biblioteca PIL realiza un análisis de imágenes para determinar el número de grupos de píxeles rojos, donde cada grupo consta de al menos cuatro píxeles adyacentes de color rojo. La función principal, `contar_pixeles_rojos`, verifica la existencia de la imagen, extrae sus dimensiones y realiza un recorrido de píxeles para identificar y contar los grupos deseados. La exploración se lleva a cabo mediante una búsqueda recursiva, marcando los píxeles visitados y contando los grupos que cumplen con los criterios establecidos. El ejemplo de uso demuestra cómo aplicar la función a una imagen específica, proporcionando el número total de grupos de píxeles rojos identificados.
 

---
#6- Introducción a la Inteligencia Artificial: El pro-ceso de razonamiento según la lógica

##Introducción
En el contexto de la guerra judeo-romana, surge un dilema matemático y computacional conocido como el "Problema de Josephus". En este escenario, Josephus y otros 40 soldados se encuentran atrapados en una cueva, enfrentándose a la decisión de determinar el orden en que se suicidarán según un método específico.
La dinámica del juego implica que los soldados se ubiquen en un círculo numerado del 1 al 41. Comenzando con el soldado en la posición 1, este elimina al siguiente soldado (posición 2), y así sucesivamente. Este patrón de eliminación se repite, eliminando a los soldados en las posiciones pares, hasta que solo queda un sobreviviente. Según las reglas del juego, este último soldado también debe suicidarse.
La singularidad del problema radica en que este último sobreviviente ocupa una posición estratégica específica en el círculo, siendo Josephus quien, con perspicacia, elige conscientemente esa posición para garantizar que será el último en permanecer con vida y, por ende, el último en cumplir con las reglas del juego.
Para poder llegar a determinar un modelo en cual basarnos para saber dónde es el lugar correcto para ubicarse, es necesario tomar en cuenta lo siguiente:
El Problema de Josephus es un problema teórico que involucra a un grupo de personas numeradas de manera consecutiva alrededor de un círculo. La idea es que cada k-ésima persona es eliminada hasta que solo queda una. La tarea es determinar la posición en la que deberías colocarte para ser la última persona restante.

La fórmula matemática para resolver el Problema de Josephus se basa en una secuencia recursiva. La notación J(n, k) se utiliza para representar la posición de la última persona en un grupo de n personas cuando se elimina cada k-ésima persona.

1.	Cuando hay una sola persona (n = 1), esa persona será la última en pie (posición 1).
2.	Para grupos más grandes (n > 1), piensa en el hecho de que después de eliminar la k-ésima persona, el problema se reduce a un grupo más pequeño de tamaño (n-1). Entonces, la posición final en este grupo más pequeño es J(n-1, k).
3.	Sin embargo, hay que tener en cuenta que la eliminación ocurre cada k personas y el índice se reinicia en cada eliminación. Por lo tanto, necesitas ajustar la posición final del grupo más pequeño. Esto se logra sumando (k - 1) y tomando el módulo n.
4.	Finalmente, el resultado se ajusta sumando 1 y tomando el módulo n para asegurarse de que esté dentro de los límites del círculo.

 Por lo tanto, podemos determinar las siguientes soluciones para los casos posibles

 ## si $ n = 1$ entonces $ f(n,k) = 1$
 ## si $ n > 1$ entonces $ f(n,k) = ((f(n-1,k)+k-1)mod(n))+1$
 


Si aplicamos esta ecuación en un caso con 10 personas y se elimina cada 3 personas, obtenemos que la posición con la que podra sobrevivir es la 4 siguiendo la siguiente secuencia:

    3, 6, 9, 2, 7, 1, 8, 5, 10, 4

---
#7.- Introducción a la Inteligencia Artificial: El papelde la heurística
##Introducción
La heurística es un enfoque o método general que se utiliza para resolver problemas o tomar decisiones de manera rápida y eficiente, aunque no garantiza una solución óptima. Se basa en reglas generales, estrategias intuitivas o experiencias pasadas para abordar situaciones complejas, especialmente cuando la información es limitada o el tiempo es escaso.
El papel de la heurística en la resolución de problemas es facilitar el proceso de toma de decisiones al proporcionar atajos mentales y enfoques simplificados. Estas reglas o estrategias heurísticas son reglas prácticas que ayudan a reducir la complejidad de un problema, permitiendo tomar decisiones más rápidas y eficientes. Sin embargo, estas soluciones pueden no ser la mejor opción o la más óptima en términos de resultados, ya que se basan en aproximaciones y simplificaciones.
Algunos ejemplos comunes de heurísticas incluyen:

1.	Heurística de representatividad: Hacer juicios basados en la similitud percibida con prototipos, lo que puede llevar a sesgos cognitivos.
2.	Heurística de disponibilidad: Basar la toma de decisiones en la disponibilidad y accesibilidad de la información, lo que puede llevar a la sobrevaloración de información fácilmente recordada.
3.	Heurística de anclaje y ajuste: Tomar decisiones basadas en un valor inicial (ancla) y ajustar desde ese punto, lo que puede influir en la estimación final.
4.	Heurística de satisfacción: Elegir la primera solución que cumple con ciertos criterios mínimos en lugar de evaluar todas las posibles alternativas.
5.	Heurística de búsqueda del mejor primero: Centrarse en las opciones que parecen ser las mejores en un momento dado, sin explorar exhaustivamente todas las posibilidades.
Aunque las heurísticas pueden ser útiles y eficientes, también pueden dar lugar a errores sistemáticos o sesgos cognitivos. En ciertos casos, es importante equilibrar el uso de heurísticas con un análisis más exhaustivo y reflexivo para evitar decisiones subóptimas.

```python
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

tablero=[
    ['#','#','#','#','#','#','#','#','#'],
    [' ',' ',' ',' ',' ',' ','#',' ','#'],
    ['#','#','#',' ','#','#','#',' ','#'],
    ['#',' ',' ',' ','#',' ','#',' ','#'],
    ['#',' ','#','#','#',' ','#',' ','#'],
    ['#',' ',' ',' ',' ',' ',' ',' ','#'],
    ['#',' ','#','#','#',' ','#',' ','#'],
    ['X',' ','#',' ',' ',' ','#',' ','#'],
    ['#','#','#','#','#','#','#','#','#']
]


ruta=[]
passed=[]

class Laberinto:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.configure(background="#ffffff")
        self.ventana1.title("Laberinto")
        self.check=False
        self.tablero()
        self.boton1=ttk.Button(self.ventana1, text="Resolver", command=self.ruta)
        self.boton1.grid(column=0, row=10, columnspan=5, padx=20, pady=10)
        self.boton2=ttk.Button(self.ventana1, text="Volver a intentar", command=self.reconstruir)
        self.boton2.grid(column=5, row=10, columnspan=5, padx=10, pady=10)
        self.ventana1.mainloop()

    def tablero(self):  
        self.lista=[]   
        listafila=[]     
        self.altura=len(tablero)
        self.ancho=len(tablero[0])
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):   
                texto=tablero[fila][columna]
                label=ttk.Label(self.ventana1, text=texto, background="white") 
                label.grid(column=columna, row=fila, padx=20, pady=10) 
                if(tablero[fila][columna]=='X'): 
                    label.configure(background="green")
                elif (tablero[fila][columna]=='#'): 
                    label.configure(background="black")
                listafila.append(label)
            self.lista.append(listafila)   
            listafila=[]    

    def reconstruir(self):  
        print("Intentando de nuevo...")
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])): 
                self.lista[fila][columna].configure(background="white")
        self.tablero()

    def ruta(self):
        self.check=False
        self.resolver(1,0)
        if (self.check):
            print("¡Ha llegado a su destino!")
            print("Solución = ", end="")
            print(ruta)
            print()
            tk.messagebox.showinfo('Laberinto','Ha llegado a su destino')
        else:    
            print("No se pudo resolver")                    
            tk.messagebox.showinfo('Laberinto','No se pudo resolver')

    def resolver(self, fil, col):
        while(self.check==False):
            if(fil<0 or col<0 or fil>=self.altura or col>=self.ancho):
                pass
            elif(self.lista[fil][col]['text']=='*' or self.lista[fil][col]['text']=='#'):
                pass
            elif(self.lista[fil][col]['text']=='X'):
                self.check=True
            else:
                self.lista[fil][col].configure(text="*", background="yellow")
                ruta.append([fil,col])
                if(fil<self.altura-1 and self.lista[fil+1][col]['text']!='#' and self.lista[fil+1][col]['text']!='*' and ([fil+1, col] not in passed)):
                    fil+=1
                elif(col>0 and self.lista[fil][col-1]['text']!='#' and self.lista[fil][col-1]['text']!='*' and ([fil, col-1] not in passed)):
                    col-=1
                elif(fil>0 and self.lista[fil-1][col]['text']!='#' and self.lista[fil-1][col]['text']!='*' and ([fil-1, col] not in passed)):
                    fil-=1
                elif(col<self.ancho and self.lista[fil][col+1]['text']!='#' and self.lista[fil][col+1]['text']!='*' and ([fil, col+1] not in passed)):
                    col+=1
                else:
                    passed.append([fil,col])
                    ruta.remove([fil,col])
                    self.lista[fil][col].configure(text=" ", background="#ffffff")
                    fil=ruta[-1][0]
                    col=ruta[-1][1]
                    ruta.remove([fil,col])
                    self.lista[fil][col].configure(text=" ", background="#ffffff") 
            if(len(ruta)==0):
                print("No hay solucion")
                break
            if(self.check==True):
                print("Se ha completado")

Laberinto1=Laberinto()
```