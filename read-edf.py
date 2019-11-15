import pyedflib
import numpy as np
import os

current_dir = os.getcwd()
print(current_dir)
subject = "S026"
sub_edf = "S026R01.edf"
file_name = os.path.join(current_dir, subject, sub_edf)
f = pyedflib.EdfReader(file_name)
n = f.signals_in_file
signal_labels = f.getSignalLabels()
sigbufs = np.zeros((n, f.getNSamples()[0]))
for i in np.arange(n):
    sigbufs[i, :] = f.readSignal(i)
print("Ok")
