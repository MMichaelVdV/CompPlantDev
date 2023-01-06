### A stroll through the developmental landscape of plants: trajectory inference from single-cell transcriptomics data

#### Project summary: 
Single-cell omics data (e.g. transcriptomics data) provide the opportunity to study cellular dynamic processes that are important for plant development such as cell differentiation along developmental trajectories. One popular method for the computational modelling of such processes is called trajectory inference (also known as pseudotime analysis), where the goal is to order individual cells along a developmental trajectory (e.g. based on similarities in expression patterns between cells). In this project you will foremost be able to familiarize yourselves with the basics of trajectory inference from single-cell transcriptomics data through a standard workflow. More than 70 trajectory inference tools have already been developed based on different underlying principles that allow inference from very basic linear trajectories to more complex topologies; we will look into a few of these methods and assess their advantages and disadvantages. Once the individual cells have been ordered along a developmental trajectory many interesting downstream analyses can be performed that potentially lead to more insight in the underlying biology of the developmental process under study. We will look for example into differential expression of genes along the trajectory to uncover those genes for which the temporal profile changes significantly during development (and if time permits, we might also look into dynamic gene regulatory network inference). An example of trajectory inference from single-cell transcriptomics on a developing Arabidopsis root can be found in the following paper by Wendrich et al. (2020): DOI: 10.1126/science.aay4970.

#### Techniques and methods: 
-	Exploratory data analysis and preprocessing (gene filtering, normalization, clustering) 
-	Dimensionality reduction using both linear (PCA) and non-linear methods (t-SNE, UMAP),
-	Trajectory inference with various methods (SCORPIUS, SlingShot, probabilistic methods, …)
-	Downstream analysis (e.g. differential expression (tradeSeq) or dynamic gene regulatory network inference (depending on the timing and the interest of the students))
-	Visualization and biological interpretation of the results
-	Programming languages: R and Python
-	Scientific computing using a computer cluster (Linux shell commands/scripts, submitting jobs)
-	Version control (Git)

#### Datasets:
Two papers on trajectory inference on single-cells transcriptomes from Arabidopsis root: Denjer et al. (2019) (DOI: 10.1016/j.devcel.2019.02.022) and Wendrich et al. (2020) (DOI: 10.1126/science.aay4970). 
