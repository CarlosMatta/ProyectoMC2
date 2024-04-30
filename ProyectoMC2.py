import networkx as nx 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import time 
import queue

G = nx.Graph()
root = tk.Tk()
root.title("Algoritmos de búsqueda proyecto MC2")
vertex_entry = tk.Entry(root)
vertex_entry.pack()
add_vertex_button=tk.Button(root, text="Agregar vertice", command=lambda:G.add_node(vertex_entry.get()))
add_vertex_button.pack()

edge_entry_1=tk.Entry(root)
edge_entry_1.pack()
edge_entry_2=tk.Entry(root)
edge_entry_2.pack()
add_edge_button = tk.Button(root, text="Agregar arista", command=lambda:G.add_edge(edge_entry_1.get(),edge_entry_2.get()))
add_edge_button.pack()



figure = Figure(figsize=(5,5))
ax = figure.add_subplot(111)
canvas=FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack()

#Método para dibujar el grafo
def draw_graph(bfs_edges=None):
    ax.clear()
    if bfs_edges:
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=ax, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, edgelist=bfs_edges, edge_color='b', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[vertex_entry.get()]+[v for u, v in bfs_edges], node_color='r', ax=ax)
    else:
        nx.draw(G, ax=ax, with_labels=True)
        canvas.draw()

draw_button = tk.Button(root, text="Dibujar grafo", command=draw_graph)
draw_button.pack()
#Metodo de la busqueda por anchura
def show_bfs():
    bfs_edges=list(nx.bfs_edges(G,source=vertex_entry.get()))
    draw_graph(bfs_edges)
    canvas.draw()

#Metodo de la busqueda a lo largo
def show_dfs():
    dfs_edges=list(nx.dfs_edges(G,source=vertex_entry.get()))
    draw_graph(dfs_edges)
    canvas.draw()

#Metodo a paso a paso busqueda por anchura
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

#Metodo a paso a paso busqueda a lo largo
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

#Metodo para mostrar el paso a paso de manera gráfica
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

       
    
bfs_button = tk.Button(root, text="Busqueda a lo ancho", command=show_bfs)
bfs_button.pack()
bfs_button2 = tk.Button(root, text="Busqueda en profundidad (A lo largo)", command=show_dfs)
bfs_button2.pack()
bfs_button3 = tk.Button(root, text="Proceso a lo ancho", command=lambda: (visualize_search(order_bfs(G,'A'),'Visualización búsqueda a lo ancho',G, nx.spring_layout(G))))
bfs_button3.pack()
bfs_button4 = tk.Button(root, text="Proceso en profundidad (A lo largo)", command=lambda: (visualize_search(order_dfs(G,'A'),'Visualización búsqueda a lo largo',G, nx.spring_layout(G))))
bfs_button4.pack()


root.mainloop()