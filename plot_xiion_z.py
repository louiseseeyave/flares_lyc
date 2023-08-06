import numpy as np
import matplotlib.pyplot as plt

# Plot xi_ion as a function of redshift for different luminosity bins

fnames = ['flares_xiion_z_lum-28-28.5.txt', 'flares_xiion_z_lum-28.5-29.txt',
          'flares_xiion_z_lum-29-29.5.txt', 'flares_xiion_z_lum-29.5-gtr.txt']

lum_labels = [r'FLARES $28<\rm{log}_{10}(L_{\rm FUV,dust}/\rm{erg\;s^{-1}Hz^{-1}})<28.5}$',
              r'FLARES $28.5<\rm{log}_{10}(L_{\rm FUV,dust}/\rm{erg\;s^{-1}Hz^{-1}})<29}$',
              r'FLARES $29<\rm{log}_{10}(L_{\rm FUV,dust}/\rm{erg\;s^{-1}Hz^{-1}})<29.5}$',
              r'FLARES $29.5<\rm{log}_{10}(L_{\rm FUV,dust}/\rm{erg\;s^{-1}Hz^{-1}})$']

# begin plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

cmap = plt.get_cmap('viridis')

for i, (fname, lum_label) in enumerate(zip(fnames, lum_labels)):

    z, p16, median, p84, n = np.loadtxt(fname, unpack=True)

    mask = n < 10
    ok_z = np.ma.masked_where(mask, z)
    ok_median = np.ma.masked_where(mask, median)
    ok_p16 = np.ma.masked_where(mask, p16)
    ok_p84 = np.ma.masked_where(mask, p84)

    ax.plot(z, median, c=cmap(i/len(fnames)), ls=':')
    ax.plot(ok_z, ok_median, c=cmap(i/len(fnames)), label=lum_label)
    ax.fill_between(ok_z, ok_p16, ok_p84, alpha=0.15, color=cmap(i/len(fnames)),
                    edgecolor='none')

ax.grid(color='whitesmoke')
ax.set_axisbelow(True)
ax.legend(frameon=False)
ax.set_ylabel(r'$\log_{10}(\xi_{\rm ion}/\rm{erg^{-1}Hz})$')
ax.set_xlabel('z')
ax.set_xlim(4, 11)
ax.set_ylim(24.5, 26.5)

plt.savefig('figures/xiion_z_lum-bins', dpi=300, bbox_inches='tight')

plt.close()

# --------------------------------------------------------------------

# Plot xi_ion as a function of redshift for all FLARES galaxies

fname = 'flares_xiion_z_lum-all.txt'

z, p2, p16, median, p84, p98, n = np.loadtxt(fname, unpack=True)

# begin plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(z, median, c='k', ls='-', label='FLARES')
ax.fill_between(z, p16, p84, alpha=0.15, color='grey', edgecolor='none')
ax.fill_between(z, p2, p98, alpha=0.15, color='grey', edgecolor='none')

ax.grid(color='whitesmoke')
ax.set_axisbelow(True)
ax.legend(frameon=False)
ax.set_ylabel(r'$\log_{10}(\xi_{\rm ion}/\rm{erg^{-1}Hz})$')
ax.set_xlabel('z')
ax.set_xlim(4, 11)
ax.set_ylim(24.5, 26.5)

plt.savefig('figures/xiion_z_lum-all', dpi=300, bbox_inches='tight')

plt.close()
