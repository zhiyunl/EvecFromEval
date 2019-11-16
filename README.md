<!--
 * @Author: zhiyunl
 * @Date: 2019-11-16 16:10:47
 * @LastEditors: zhiyunl
 * @LastEditTime: 2019-11-16 16:23:28
 * @Description: 
 -->
# EvecFromEval
---
A implementation of new method for calculating eigenvector from eigenvalue, inspired by the papers below:

- [Eigenvectors from Eigenvalues](https://arxiv.org/pdf/1908.03795.pdf)
- [Eigenvalues: the Rosetta Stone for Neutrino Oscillations in Matter](https://arxiv.org/pdf/1907.02534.pdf)

# Description

Quote from Papers:
> We present a new method of succinctly determining eigenvectors from eigenvalues. Specifically, we relate the norm squared of the elements of eigenvectors to the eigenvalues and the submatrix eigenvalues.

![The idea is straight forward](/quanta.jpg)

A detailed desp is available from 
- QuantaMagazine: [EN](https://www.quantamagazine.org/neutrinos-lead-to-unexpected-discovery-in-basic-math-20191113/)
- [Tao's Blog](https://terrytao.wordpress.com/2019/08/13/eigenvectors-from-eigenvalues/)
- 量子位：[CN](https://www.qbitai.com/2019/11/8982.html)
### Something to continue:

+ @*TODO* Expanding the matrix into larger size, only support 3x3 matrix now

+ @*TODO* Implement eigenvalue calculating strategy without *numpy*
