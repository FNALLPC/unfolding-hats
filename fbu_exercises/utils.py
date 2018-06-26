"""
Unfolding HATS 2018

Collection functions for making plots and 
simple analysis

For use with jupyter notebooks and 
%matplotlib inline 
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def printPosteriors(posteriors):
    """Print the FBU posteriors in each bin"""
    for i,p in enumerate(posteriors):
        print(u" > Bin {0}: {1:.2f} \u00B1 {2:.2f}".format(i,np.mean(p),np.std(p)))
        # \u00B1 is the same as $\pm$ in unicode

    return


def plotPosteriors(posteriors):
    """Plot the FBU posteriors"""
    for i,p in enumerate(posteriors):
        plt.hist(p,bins=20,histtype='stepfilled',alpha=0.5,
                 density=True,label='Bin {0}'.format(i))
    plt.legend()
    plt.ylabel("Probability")
    plt.xlabel("Posterior")

    return


def plotTrace(trace):
    """Draw the FBU trace as a function of step"""
    for t in trace:
        plt.plot(range(len(t)),t,alpha=0.5)
    plt.ylabel("Trace")
    plt.xlabel("Step")

    return


def nuisancePriorPosterior(nuis,name):
    """Plot the prior and posterior of a nuisance parameter in FBU"""
    n,bins,patched = plt.hist(nuis,bins=40,alpha=0.5,color='g',lw=0,
                              density=True, histtype='stepfilled')

    gbins = np.arange(-4,4,0.1)
    gaus  = norm.pdf(gbins,0.,1.)
    line  = plt.plot(gbins,gaus,'r',lw=2)

    (mm,ss) = norm.fit(nuis)

    plt.xlabel("Nuisance Parameter "+name)
    plt.text(0.1,0.8,'mean=%1.2f'%mm,transform=plt.gca().transAxes)
    plt.text(0.1,0.65,'RMS=%1.2f'%ss,transform=plt.gca().transAxes)
    plt.legend((line[0],patched[0]),('prior','posterior'))

    return mm,ss


def plotPulls(means,stddevs):
    """Plot pulls for nuisance parameters in FBU"""
    plt.axvspan(-2.,2.,color='#FFFF00',alpha=0.5)
    plt.axvspan(-1.,1.,color='#00FF00',alpha=0.5)
    plt.axvline(x=0.0, color='black',  linestyle='--')
    listOfNuisances = means.keys()
    y = np.arange(len(listOfNuisances))

    for i,name in enumerate(listOfNuisances):
        plt.errorbar(means[name],y[i],xerr=stddevs[name],fmt='o',
                     color='k',capsize=0,label=name)

    plt.gca().set_ylim(-0.5,len(listOfNuisances)+0.5)
    plt.gca().set_xlim(-3,3)
    plt.yticks(y,listOfNuisances,fontsize=14)
    plt.gca().yaxis.tick_right()
    plt.xlabel(r'$\theta\pm\Delta\theta$',fontsize=14)

    return


def plotResponseMatrix(resmat,bins=[]):
    """Plot the response matrix
        - Assume the response matrix is 2d array (truth,reco) dimensions
          Reco is plotted as the x-axis
        - Make histogram in matplotlib using 'weights' argument
          to handle the bin content, and dummy values for the x/y
    """
    try:
        shape = resmat.shape
    except AttributeError:
        resmat = np.array(resmat)
        shape  = resmat.shape

    # use data from the histogram as 'weights'
    # use 'dummy' values for the center of the bin 
    if not bins:
        nbinsx = shape[1]
        nbinsy = shape[0]
        dummy_xbins = [ 0.5*i for _ in range(nbinsy) for i in range(nbinsx) ]
        dummy_ybins = [ 0.5*j for j in range(nbinsy) for _ in range(nbinsx) ]
    else:
        nbinsx  = bins[0]
        nbinsy  = bins[1]
        xcenter = [ 0.5*(b+bins[0][i+1]) for i,b in enumerate(bins[0]) if i<len(bins[0])-1]
        ycenter = [ 0.5*(b+bins[1][i+1]) for i,b in enumerate(bins[1]) if i<len(bins[1])-1]
        dummy_xbins = [ i for _ in ycenter for i in xcenter ]
        dummy_ybins = [ j for j in ycenter for _ in xcenter ]

    # make histogram with dummy values and bin contents as weights
    plt.hist2d(dummy_xbins,dummy_ybins,bins=(nbinsx,nbinsy),weights=resmat.flatten())
    plt.colorbar()
    plt.xlabel("Reconstructed Bin")
    plt.ylabel("Generator Bin")

    return


def plotYields(data,signal=None,backgrounds=[],bins=[]):
    """Plot event yields
        - Assume we are given TH1s from uproot
        - Convert to arrays for plotting in matplotlib
    """
    print 
    if not bins:
        center = [i+0.5 for i,d in enumerate(data)]  # pseudo-data points for making histogram
        bins   = [i for i in range( len(data)+1 )]   # pseudo-binning
    else:
        center = [ 0.5*(b+bins[i+1]) for i,b in enumerate(bins) if i<len(bins)-1]
    data = np.array(data)

    # stack the backgrounds on top of each other in the plot
    nbckgs  = len(backgrounds)
    labels  = ['background {0}'.format(i) for i in range(nbckgs)]
    weights = list(backgrounds)
    bincenters = [ list(center) for _ in range(nbckgs)]

    # stack the signal on top of the backgrounds
    if signal is not None:
        # 'signal' is what we want to unfold, e.g., ttbar
        labels  += ['signal']
        weights += [list(signal)]
        bincenters += [list(center)]

    # plot backgrounds & signal
    d,bb,pp = plt.hist(bincenters,weights=weights,stacked=True,
                       histtype='stepfilled',label=labels,
                       edgecolor='k',bins=bins)

    # plot the data as error bars
    plt.errorbar(center,data,color='k',
                 fmt='o',yerr=np.sqrt(data),
                 label='Data')

    plt.ylim(ymin=0,ymax=plt.ylim()[1]*1.6) # scale the y-axis to accommodate the legend
    plt.legend()
    plt.xlabel("Distribution")
    plt.ylabel("Events")

    return

## THE END ##
