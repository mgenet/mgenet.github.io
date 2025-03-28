---
title: "New paper with MSU and ETHZ on Mechanical Regularization for Medical Image Registration"
date: "2018-08-22"
categories: 
  - "News"
image: "images/GraphicalAbstract.png"
---

Title: Equilibrated warping: Finite element image registration with finite strain equilibrium gap regularization

Authors: [Martin Genet](https://m3disim.saclay.inria.fr/people/martin-genet), Christian T. Stoeck, Constantin von Deuster, Lik Chuan Lee, Sebastian Kozerke

Abstract: In this paper, we propose a novel continuum finite strain formulation of the equilibrium gap regularization for image registration. The equilibrium gap regularization essentially penalizes any deviation from the solution of a hyperelastic body in equilibrium with arbitrary loads prescribed at the boundary. It thus represents a regularization with strong mechanical basis, especially suited for cardiac image analysis. We describe the consistent linearization and discretization of the regularized image registration problem, in the framework of the finite elements method. The method is implemented using FEniCS & VTK, and distributed as a freely available python library. We show that the equilibrated warping method is effective and robust: regularization strength and image noise have minimal impact on motion tracking, especially when compared to strain-based regularization methods such as hyperelastic warping. We also show that equilibrated warping is able to extract main deformation features on both tagged and untagged cardiac magnetic resonance images.
