# Cytopus :octopus:

## A language for single cell omics biology

![Image of Cytopus](https://github.com/wallet-maker/cytopus/blob/main/img/cytopus_v1.1_stable_graph.png)

currently version 1.2 (stable)

## Overview:

Package to query our single cell genomics KnowledgeBase.

KnowledgeBase is provided in graph format based on the networkx package. Central to the KnowledgeBase is a cell type hierarchy and **cellular processess** which correspond to these cell types. Cell types are supported by gene sets indicative of their **cellular identities**. 

The KnowledgeBase can be queried to retrieve gene sets for specific cell types and organize them in a dictionary format for downstream use with the **Soectra** package https://github.com/dpeerlab/spectra: 


## Installation:

install from source:

```
git clone https://github.com/wallet-maker/cytopus.git
cd cytopus
pip install .
```

**dependencies:**
"pandas>1.3"
"numpy>1.2"
"networkx>2.7"
"matplotlib>3.4"

## Tutorial

Retrieve default KnowledgeBase (human only):

```
import cytopus as cp
G = cp.kb.KnowledgeBase()
```
Retrieve custom KnowledgeBase (documentation to build KnowledgeBase object coming soon):
```
file_path = '~/dir1/dir2/knowledgebase_file.txt'
G = cp.kb.KnowledgeBase(file_path)
```
Access data in KnowledgeBase:
```
#list of all processes in KnowledgeBase
G.celltypes
#dictionary of all cellular processes in KnowledgeBase as a dictionary {'process_1':['gene_a','gene_e','gene_y',...],'process_2':['gene_b','gene_u',...],...}
G.processes
#dictionary of all cellular identities in KnowledgeBase as a dictionary {'process_1':['gene_j','gene_k','gene_z',...],'identity_2':['gene_y','gene_p',...],...}
G.identities
#dictionary with gene set properties (for cellular processes or identities)
G.graph.nodes['gene_set_name']
```

Plot the cell type hierarchy stored in the KnowledgeBase as a directed graph with edges pointing into the direction of the parents:
```
G.plot_celltypes()
```

Prepare a nested dictionary assigning cell types to their cellular processes and cellular processes to their corresponding genes. This dictionary can be used as an input for Spectra.
```
#First, select the cell types which you want to retrieve gene sets for. These cell types can be selected from the cell type hierarchy (see .plot_celltypes() method above)
celltype_of_interest = ['M','T','B','epi']

#Second, select the cell types which you want merge gene sets and set them as global gene sets for the Spectra package. These gene sets should be valid for all cell types in the data. 
##e.g. if you are working with different human cells
global_celltypes = ['all-cells']
##e.g. if you are working with human leukocytes
global_celltypes = ['all-cells','leukocyte']
##e.g. if you are working with B cells
global_celltypes = ['all-cells','leukocyte','B']

#Third retrieve dictionary of format {celltype_a:{process_a:[gene_a,gene_b,...],...},...}.
#Decide whether you want to merge gene sets for all children or all parents (unusual) of the selected cell types.
G.get_celltype_processes(celltype_of_interest,global_celltypes = global_celltypes,get_children=True,get_parents =False)

#Fourth, dictionary will be stored in the KnowledgeBase
G.celltype_process_dict
```


A full tutorial can be found under https://github.com/wallet-maker/cytopus/blob/main/notebooks/KnowledgeBase_queries.ipynb

## you can submit gene sets to be added to the KnowledgeBase here:

https://docs.google.com/forms/d/e/1FAIpQLSfWU7oTZH8jI7T8vFK0Nqq2rfz6_83aJIVamH5cogZQMlciFQ/viewform?usp=sf_link

All submissions will be reviewed by 2 (computational) biologists and if needed revised before they will be added to the database. This will ensure consistency of the annotations and avoid gene set duplication. Authorship will be acknowledged in the KnowledgeBase for all submitted gene sets added to the KnowledgeBase.
