import numpy as np
from wav_file_loader import read_wavefiles
import IPython.display as ipd

# Sett til True for å importere egne lydfiler
egne_lydfiler = False
antall_filer = 2

if egne_lydfiler:
    paths = ["audio/heimemekk_" + str(i) + ".wav" for i in range(antall_filer)]
    data, sampling_rate = read_wavefiles(paths)
    numSignals = data.shape[0]
    data = nomralize_audio(data)
    for file in data:
        ipd.display(ipd.Audio(file, rate=sampling_rate))
    
print(paths)