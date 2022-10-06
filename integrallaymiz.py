from Boshqa_domenlarga_nisbatan_birlashtirilgan_kop_olchovli import domain_unit_circle
from Bir_ozgaruvchan import mc_integrate
import numpy as np
import scipy.stats as st

class func_mvn:
    # ko'p o'zgaruvchan normal berilgan o'rtacha va kovariatsiya
    def __init__(self, mu, cov):
        self.mu = mu
        self.cov = cov
        self.func = st.multivariate_normal(mu, cov)

    def calc_pdf(self, x):
        return self.func.pdf(x)


mean = np.array([0, 0.5, 1])
cov = np.array([[1, 0.8, 0.5], [0.8, 1, 0.8], [0.5, 0.8, 1]])

f = func_mvn(mean, cov)
fmvn = f.calc_pdf

print("For multivariate normal, integrated over unit circle")
r, x_list, inside_domain = mc_integrate(fmvn, domain_unit_circle, -1, 1, 3, 2000000)
print(f"Monte Carlo solution: {r: .4f}")
print(f"Solution from pmvnEll (shotGroups pkg in R): {0.2018934: .4f}")
