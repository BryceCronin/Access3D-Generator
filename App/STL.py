import numpy
from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import LightSource
from mpl_toolkits import mplot3d
from stl import mesh

# Setup Plot
figure = pyplot.figure()
axes = figure.add_subplot(projection='3d')
DPI = figure.get_dpi()
figure.set_size_inches(500 / float(DPI), 400 / float(DPI))
axes.margins=(0)

def prepare_STL(file):
    global figure
    global axes
    
    # Load the STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(file) # todo: load and update actual STL file
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
    polymesh = mplot3d.art3d.Poly3DCollection(your_mesh.vectors)

    # Auto scale to the mesh size
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale,scale,scale)

    ls = LightSource(azdeg=225, altdeg=45)
    # Darkest shadowed surface, in rgba
    dk = numpy.array([1/255, 87/255, 155/255, 1]) # rgb(1, 87, 155)
    # Brightest lit surface, in rgba
    lt = numpy.array([144/255, 202/255, 249/255, 1])  # rgb(144, 202, 249)
    # Interpolate between the two, based on face normal
    shade = lambda s: (lt-dk) * s + dk

    # Set face colors 
    sns = ls.shade_normals(your_mesh.get_unit_normals(), fraction=1.0)
    rgba = numpy.array([shade(s) for s in sns])
    polymesh.set_facecolor(rgba)

    # turn off axis display
    axes.axis('off')

    axes.set_facecolor((1, 1 , 1, 1)) 

    axes.add_collection3d(polymesh)

    return figure

def update_STL(file):
    global figure
    global axes

    axes.cla()

    # Load the STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(file)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
    
    polymesh = mplot3d.art3d.Poly3DCollection(your_mesh.vectors)

    # Auto scale to the mesh size
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale,scale,scale)

    ls = LightSource(azdeg=225, altdeg=45)
    # Darkest shadowed surface, in rgba
    dk = numpy.array([1/255, 87/255, 155/255, 1]) # rgb(1, 87, 155)
    # Brightest lit surface, in rgba
    lt = numpy.array([144/255, 202/255, 249/255, 1])  # rgb(144, 202, 249)
    # Interpolate between the two, based on face normal
    shade = lambda s: (lt-dk) * s + dk

    # Set face colors 
    sns = ls.shade_normals(your_mesh.get_unit_normals(), fraction=1.0)
    rgba = numpy.array([shade(s) for s in sns])
    polymesh.set_facecolor(rgba)

    # turn off axis display
    axes.axis('off')   

    axes.set_facecolor((1,1,1,1))

    axes.add_collection3d(polymesh)

    return figure

def draw_STL(canvas, fig):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)