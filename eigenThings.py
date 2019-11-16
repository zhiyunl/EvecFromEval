import cmath

import numpy as np


class evecfromeval():
    vals = 0
    vecs = 0

    def __init__(self):
        pass

    def evalue(self, mm):
        return np.linalg.eigvals(mm)

    def normalize(self, a, axis=-1, order=2):
        l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
        l2[l2 == 0] = 1
        return a / np.expand_dims(l2, axis)

    def evector(self, mm):
        self.vecs = []
        submm = np.array([np.delete(np.delete(mm, j, 1), j, 0) for j in range(mm.shape[0])])
        print(submm)
        subevals = np.array([self.evalue(submm[j]) for j in range(len(submm))])
        print(subevals)
        # total 3 matrix, each has 2 eigen value theta gamma
        # original matrix has 3 eigenvalue i,j,k
        # our vectors are 3 1x3 vector. v_a v_b v_c {i,j,k}
        for j in range(mm.shape[0]):
            # square of vector j
            v_a2 = [cmath.sqrt((self.vals[i] - subevals[j][0]) * (self.vals[i] - subevals[j][1]) / (
                        self.vals[i] - self.vals[(i + 1) % 3]) / (self.vals[i] - self.vals[(i + 2) % 3])) for i in
                    range(3)]
            # this formula can be simplified using trace and determinant as in the paper
            # numerator : using the sum and product of the eigenvalues
            #       eigenvalues of submatrix do not have to be explictly calculated
            self.vecs.append(v_a2)
        self.vecs = np.array(self.vecs)
        print(self.vecs)
        # compare
        _, real_vec = np.linalg.eig(mm)
        print(real_vec)
        # print(np.allclose(real_vec,self.vecs))
        # print(self.normalize(np.array(self.vecs)))


if __name__ == '__main__':
    sl = evecfromeval()
    X = np.array([[2, 3, 3, 4, 5, 7], [2, 4, 5, 5, 6, 8], [2, 3, 4, 5, 6, 7]])
    mm = X @ X.T
    print("Matrix xxT is\n", mm)
    sl.vals = sl.evalue(mm)
    print("eigenvalue of xxT is")
    print(sl.vals)
    vecs = sl.evector(mm)
