# Manual Técnico Programa Algoritmos de Busqueda
#### Proyecto Mate para computación 2

## Integrantes 
* **202300653** - Francisco Gerardo Castillo Sagastume
* **202300400**	- Iker Renato Barrios Portillo
* **202300778**	- Sharon Melissa Santa Cruz Huertas
* **202300652**	- Vasti Abigail González Pereira
* **202302190**	- Carlos Fernando Matta Peña

## Introduccion
Este manual técnico proporciona una guía detallada sobre el uso y funcionamiento de un programa desarrollado en Python para la aplicación de algoritmos de búsqueda en grafos. El programa incluye la implementación de dos algoritmos fundamentales en la teoría de grafos: la búsqueda en anchura (BFS) y la búsqueda en profundidad (DFS). El objetivo principal de este programa es proporcionar a los usuarios una herramienta eficiente y fácil de usar para realizar operaciones de búsqueda en grafos.


## Objetivos

#### Generales
 * Presentar detalladamente la configuración y razonamiento lógico del programa desde su código.

#### Especificos

* Establecer el alcance del sistema, incluyendo los requisitos para su funcionamiento óptimo.
* Explicar la lógica del código programado para la solución de los algoritmos de busqueda solicitados.

## Requisitos del Sistema

#### Hardware
*  Poseer procesador de doble núcleo o superior.
*  Se recomienda disponer de al menos 2 GB de RAM.
*  Sistema operativo compatible con Python (windows, linux, macOS)

#### Sofware
* **_Python:_** Desarrollo de un sistema gráfico a través de la programación orientada a objetos.
* **_IDE Visual Studio Code:_** Se requiere un IDE para el desarrollo del código.

## Descripción de la Solucion

La estructura de esta aplicación se desarrolló a partir de los códigos proporcionados, implementando dos diferentes algoritmos de búsqueda: búsqueda en anchura y en profundidad. Estos algoritmos fueron desarrollados utilizando múltiples librerías dentro de la aplicación.

Se utilizaron las siguientes librerias de Python:
* **Networkx**: Es una librería enfocada al análisis de datos, utilizada para el manejo de aristas y vértices del grafo en este proyecto.
* **Time**: Parte de la biblioteca estándar de Python, proporciona funcionalidades para el manejo del tiempo, utilizada en este caso para mostrar la explicación paso a paso de los algoritmos.
* **Tkinter**:  Librería orientada a la programación orientada a objetos, utilizada para proporcionar una interfaz gráfica al proyecto.
* **Matplotlib**: Es una librería orientada a la generación de gráficos, necesaria para representar de manera gráfica los grafos generados.
* **Queue**: Parte de la biblioteca estándar de Python, proporciona funcionalidades para el manejo de colas, utilizada para el manejo lógico de los vértices en el proyecto.

El proceso inicial comprendió la creación de una estructura de gráfica vacía para la manipulación de grafos. A través de funciones lambda vinculadas a los elementos de interfaz, se incorporaron nodos o aristas a la gráfica. La función _draw_graph_ fue responsable de la generación de grafos según los requerimientos específicos.

Los algoritmos se dividieron en dos métodos diferentes. En uno de ellos, se utilizó una estructura de datos tipo lista para simular el estado de visitado o no visitado de los nodos, agregándolos a la lista si no estaban presentes. El algoritmo de profundidad, por su parte, siguió un enfoque similar con la incorporación de un mecanismo de retorno para analizar los datos.

Para la representación gráfica de los resultados, se definieron los parámetros necesarios, incluyendo las estructuras de datos mencionadas anteriormente, para facilitar la visualización a través de las funciones de graficación pertinentes.

El desarrollo del código incluyó diversas estrategias lógicas y el uso de librerías especializadas. Estas incluyen herramientas para la representación gráfica de coordenadas, operaciones matemáticas complejas y la simulación temporal de los algoritmos.


## Estructura del Código  

 ##### Funciones Lambda 
 Funciones para agregar a la gráfica un...
 ###### **Nodo/Vertice**

```
.add_node(vertex_entry.get())
```
 ###### **Arista**

```
.add_edge(edge_entry_1.get(),edge_entry_2.get())
```
  
  ##### Método para dibujar el grafo en un canvas
 Recibe como parámetro una lista con los vértices y aristas para dibujar el grafo en el canvas.
  
```
draw_graph(bfs_edges=None):
    ax.clear()
    if bfs_edges:
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=ax, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, edgelist=bfs_edges, edge_color='b', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[vertex_entry.get()]+[v for u, v in bfs_edges], node_color='r', ax=ax)
    else:
        nx.draw(G, ax=ax, with_labels=True)
        canvas.draw()
```

  ##### Método de la busqueda por anchura
 Recibe como parámetro una lista con los vértices y aristas para dibujar el algoritmo de búsqueda por anchura.
 
  
```
def show_bfs():
    bfs_edges=list(nx.bfs_edges(G,source=vertex_entry.get()))
    draw_graph(bfs_edges)
    canvas.draw()
```

  ##### Método de la busqueda a lo largo
  Recibe como parámetro una lista con los vértices y aristas para dibujar el algoritmo de búsqueda a lo largo.
  
```
def show_dfs():
    dfs_edges=list(nx.dfs_edges(G,source=vertex_entry.get()))
    draw_graph(dfs_edges)
    canvas.draw()
```

  ##### Metodo a paso a paso busqueda por anchura
  Por medio de la lista con los vértices, se realiza el método de búsqueda por anchura.
  
```
def order_bfs(graph,start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order=[]

    while not q.empty():
        vertex = q.get()
        if vertex not in visited: 
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
    return order 
```

  ##### Metodo a paso a paso busqueda a lo largo
  Por medio de la lista con los vértices, se realiza el método de búsqueda a lo largo.
  
```
def order_dfs(graph, start_node, visited = None):
    if visited is None:
        visited=set()

    order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(order_dfs(graph, node, visited))   

    return order  
```

 ##### Metodo para mostrar el paso a paso de manera gráfica
  Mediante una lista con el algoritmo ya aplicado, muestra por intervalos los cambios gráficos que experimentaron cada nodo y arista.
  
```
def visualize_search(order, title,  G, pos):
    plt.figure
    plt.title(title)
    for i, node in enumerate(order, start = 1):
        plt.clf()
        plt.title(title)
        nx.draw(G,pos,with_labels=True,node_color=['r' if n==node else  'g' for  n in G.nodes])
        plt.draw()
        plt.pause(1)
    plt.show()
    time.sleep(1)    
```
## Link del video

 * ##### [Video explicativo del funcionamiento del programa](https://drive.google.com/file/d/1vjZ96zvVSnUyctjGDy9wX7biOyqNUSw4/view)  
 
 

 ## Referencias
 *  ##### [Graph Search Visualization in Python (BFS and DFS) ](https://www.youtube.com/watch?v=7XVTnCrWDPY&t=524s&ab_channel=NeuralNine)
 *  ##### Código proporcionado por el auxiliar.




