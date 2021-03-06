import numpy as np
import inspect
import os
LOCATION = "/".join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))).split("/")[:-1])
# from nose.tools import raises
import sys
sys.path.insert(0, LOCATION)
from hmf import functional as tf
from hmf import MassFunction

def test_order():
    order = [
    "sigma.8: 0.7, ST, z: 0",
    "sigma.8: 0.8, ST, z: 0",
    "sigma.8: 0.7, ST, z: 1",
    "sigma.8: 0.8, ST, z: 1",
    "sigma.8: 0.7, ST, z: 2",
    "sigma.8: 0.8, ST, z: 2",
    "sigma.8: 0.7, PS, z: 0",
    "sigma.8: 0.8, PS, z: 0",
    "sigma.8: 0.7, PS, z: 1",
    "sigma.8: 0.8, PS, z: 1",
    "sigma.8: 0.7, PS, z: 2",
    "sigma.8: 0.8, PS, z: 2"]

    for i,(quants, mf, label) in enumerate(tf.get_hmf(['dndm','ngtm'],z=range(3),hmf_model=["ST","PS"],sigma_8=[0.7,0.8])):
        assert label==order[i]
        assert isinstance(mf,MassFunction)
        assert np.allclose(quants[0],mf.dndm)
        assert np.allclose(quants[1],mf.ngtm)
