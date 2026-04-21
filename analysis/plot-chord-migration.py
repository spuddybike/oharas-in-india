from pycirclize import Circos
from pycirclize.parser import Matrix
import pandas as pd

# Create from-to table dataframe & convert to matrix
fromto_table_df = pd.DataFrame(
    [
        ["Africa", "India", 2],
        ["Burma", "Australia", 112],
        ["Burma", "Australia", 13],
        ["Burma", "Europe", 1],
        ["Burma", "India", 5],
        ["Burma", "N America", 3],
        ["Burma", "SE Asia", 1],
        ["Burma", "UK", 28],
        ["Europe", "Australia", 1],
        ["Europe", "N America", 1],
        ["India", "Africa", 3],
        ["India", "Australia", 28],
        ["India", "Burma", 10],
        ["India", "Europe", 1],
        ["India", "N America", 7],
        ["India", "SE Asia", 1],
        ["India", "UK", 101],
        ["N America", "Australia", 8],
        ["SE Asia", "Australia", 8],
        ["SE Asia", "Europe", 5],
        ["SE Asia", "India", 2],
        ["SE Asia", "N America", 2],
        ["UK", "Australia", 3],
        ["UK", "N America", 1],
    ],
    columns=["from", "to", "value"], # Column name is optional
)
matrix = Matrix.parse_fromto_table(fromto_table_df)

# Initialize Circos instance for chord diagram plot
circos = Circos.chord_diagram(
    matrix,
    space=10,
    cmap="viridis",
    ticks_interval=20,
    label_kws=dict(size=12, r=110),
    link_kws=dict(direction=1, ec="black", lw=0.5),
)

# print(fromto_table_df.to_string(index=False))
fig = circos.plotfig()
fig.savefig("images/chord.png")

# Create from-to table dataframe & convert to matrix
fromto_table_dfa = pd.DataFrame(
    [
        ["Burma", "UK", 2],
        ["Europe", "N America", 2],
        ["India", "N America", 2],
        ["India", "UK", 9],
        ["SE Asia", "Australia", 6],
        ["SE Asia", "Europe", 5],
        ["SE Asia", "India", 2],
        ["SE Asia", "N America", 2],
        ["SE Asia", "UK", 7],
        ["UK", "Australia", 1],
    ],
    columns=["from", "to", "value"], # Column name is optional
)
matrixa = Matrix.parse_fromto_table(fromto_table_dfa)

# Initialize Circos instance for chord diagram plot
circos = Circos.chord_diagram(
    matrixa,
    space=10,
    cmap="viridis",
    ticks_interval=20,
    label_kws=dict(size=12, r=110),
    link_kws=dict(direction=1, ec="black", lw=0.5),
)

# print(fromto_table_dfa.to_string(index=False))
figa = circos.plotfig()
figa.savefig("images/chord-amelia.png")

# Create from-to table dataframe & convert to matrix
fromto_table_dfe = pd.DataFrame(
    [
        ["Burma", "India", 3],
        ["India", "Australia", 13],
        ["India", "UK", 18],
        ["SE Asia","Australia", 2],
    ],
    columns=["from", "to", "value"], # Column name is optional
)
matrixe = Matrix.parse_fromto_table(fromto_table_dfe)

# Initialize Circos instance for chord diagram plot
circos = Circos.chord_diagram(
    matrixe,
    space=10,
    cmap="viridis",
    ticks_interval=20,
    label_kws=dict(size=12, r=110),
    link_kws=dict(direction=1, ec="black", lw=0.5),
)

# print(fromto_table_dfe.to_string(index=False))
fige = circos.plotfig()
fige.savefig("images/chord-elizabeth.png")


# Create from-to table dataframe & convert to matrix
fromto_table_dfg = pd.DataFrame(
    [
        ["Africa", "India", 1],
        ["Burma", "Australia", 1],
        ["Burma", "Europe", 1],
        ["Burma", "N America", 1],
        ["Burma", "UK", 4],
        ["India", "Africa", 1],
        ["India", "Australia", 2],
        ["India", "Burma", 4],
        ["India", "Europe", 1],
        ["India", "UK", 7],
    ],
    columns=["from", "to", "value"], # Column name is optional
)
matrixg = Matrix.parse_fromto_table(fromto_table_dfg)

# Initialize Circos instance for chord diagram plot
circos = Circos.chord_diagram(
    matrixg,
    space=10,
    cmap="viridis",
    ticks_interval=20,
    label_kws=dict(size=12, r=110),
    link_kws=dict(direction=1, ec="black", lw=0.5),
)

# print(fromto_table_df.to_string(index=False))
figg = circos.plotfig()
figg.savefig("images/chord-george.png")

# Create from-to table dataframe & convert to matrix
fromto_table_dfj = pd.DataFrame(
    [
        ["Africa", "India", 1],
        ["Burma", "Australia", 12],
        ["Burma", "India", 2],
        ["Burma", "N America", 2],
        ["Burma", "SE Asia", 1],
        ["Burma", "UK", 22],
        ["Europe", "Australia", 1],
        ["Europe", "UK", 1],
        ["India", "Africa", 2],
        ["India", "Australia", 13],
        ["India", "Burma", 6],
        ["India", "Europe", 2],
        ["India", "N America", 4],
        ["India", "UK", 67],
        ["SE Asia", "Australia", 2],
        ["UK", "Australia", 2],
        ["UK", "N America", 1],
    ],
    columns=["from", "to", "value"], # Column name is optional
)
matrixj = Matrix.parse_fromto_table(fromto_table_dfj)

# Initialize Circos instance for chord diagram plot
circos = Circos.chord_diagram(
    matrixj,
    space=10,
    cmap="viridis",
    ticks_interval=20,
    label_kws=dict(size=12, r=110),
    link_kws=dict(direction=1, ec="black", lw=0.5),
)

# print(fromto_table_df.to_string(index=False))
figj = circos.plotfig()
figj.savefig("images/chord-john.png")