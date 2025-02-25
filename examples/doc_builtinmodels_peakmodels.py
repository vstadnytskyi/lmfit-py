# <examples/doc_builtinmodels_peakmodels.py>
import matplotlib.pyplot as plt
from numpy import loadtxt

from lmfit.models import GaussianModel, LorentzianModel, VoigtModel

data = loadtxt('test_peak.dat')
x = data[:, 0]
y = data[:, 1]


# Gaussian model
mod = GaussianModel()
pars = mod.guess(y, x=x)
out = mod.fit(y, pars, x=x)

print(out.fit_report(min_correl=0.25))

plt.plot(x, y, 'b-')
plt.plot(x, out.best_fit, 'r-', label='Gaussian Model')
plt.legend(loc='best')
plt.show()


# Lorentzian model
mod = LorentzianModel()
pars = mod.guess(y, x=x)
out = mod.fit(y, pars, x=x)

print(out.fit_report(min_correl=0.25))

plt.plot(x, y, 'b-')
plt.plot(x, out.best_fit, 'r-', label='Lorentzian Model')
plt.legend(loc='best')
plt.show()


# Voigt model
mod = VoigtModel()
pars = mod.guess(y, x=x)
out = mod.fit(y, pars, x=x)

print(out.fit_report(min_correl=0.25))

fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8))

axes[0].plot(x, y, 'b-')
axes[0].plot(x, out.best_fit, 'r-', label='Voigt Model\ngamma constrained')
axes[0].legend(loc='best')

# free gamma parameter
pars['gamma'].set(value=0.7, vary=True, expr='')
out_gamma = mod.fit(y, pars, x=x)
axes[1].plot(x, y, 'b-')
axes[1].plot(x, out_gamma.best_fit, 'r-', label='Voigt Model\ngamma unconstrained')
axes[1].legend(loc='best')

plt.show()
# <end examples/doc_builtinmodels_peakmodels.py>
