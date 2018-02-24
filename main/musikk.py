import pyaudio
import numpy as np
from math import log
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib import pyplot as plt

fig = plt.figure()
p = pyaudio.PyAudio()
A = 220  # kammertonen, oktav ned
halvtone = 2 ** (1 / 12)
scales = {"M": [0, 2, 2, 1, 2, 2, 2, 1],
          "m": [0, 2, 1, 2, 2, 1, 2, 2],
          "cro": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          "pent": [0, 3, 2, 2, 3, 2]}
sine = 0
scale = scales["M"]
tot = 0
graph = 0


def show_wave():
    x = np.arange(int(num_samples*0.05))
    y = samples[int(num_samples*0.95):]
    while len(x) > len(y):
        print("a")
    while len(x) < len(y):
        print("b")
        y.append(0)
        x = np.append(x, x[-1] + 1)
        print(x[len(x)-10:])
    plt.plot(x, y)
    plt.subplots_adjust(left=0.05, right=0.990, top=0.990, bottom=0.05)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show(block=False)
    plt.pause(1.5)
    plt.close()


def close():
    global stream
    stream.stop_stream()
    stream.close()
    p.terminate()


def play_melody(melody, durr):
    for i, note in enumerate(melody):
        if type(note) == list:
            play_tone(note, durr[i])
        else:
            play_tone([note], durr[i])


def play_tone(notes, duration, volume=0.3):
    global tot
    global stream
    global samples
    global sampling_rate
    global num_samples
    samples = 0
    sampling_rate = 44100
    volume = volume / len(notes)
    num_samples = sampling_rate * duration
    print(num_samples)

    for note in notes:
        frequency = find_fq(note)
        if frequency == "ghost":
            ghosting(duration)
            continue
        make_tone(frequency)
        get_step_from_fq(frequency)
        print(frequency)

        # for y in range(1,100):
        #    ghosting(1, y)

    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True)
    cut_click()
    stream.write(volume * samples)
    print(" ")
    if graph:
        show_wave()
    #tot = np.append(tot, [volume * sample for sample in samples]).astype(np.float32)


def cut_click():
    global samples
    end = samples[int(0.0 * num_samples):]
    fadeout = np.arange(1, 0, -1 / (len(end)))
    samples = np.append([samples[:int(0.0 * num_samples)]],
                        [fadeout * end]).astype(np.float32)


def make_tone(frequency):
    overtones = [1, 2, 4, 8], [1, 2/3, 1/2, 1/2]
    if sine:
        overtones = [1], [1]
    global samples
    for i, x in enumerate(overtones[0]):
        samples += overtones[1][i] * (np.sin(2 * np.pi * np.arange(num_samples)
                                            * x * frequency / sampling_rate)).astype(np.float32)


def get_step_from_fq(fq):
    try:
        print(format(log(fq / A) / log(halvtone), ".1f"))
    except:
        print("")


def ghosting(dur, y=1):
    global samples
    global stream
    samples = 0
    for x in range(10, 2000, 4*y):
        samples += (np.sin(2 * np.pi * np.arange(dur * 44100)
                           * x/10 / 44100)).astype(np.float32)


def find_fq(note, skala=scale):
    if not note:
        return note
    elif note == "ghost":
        return note
    antall = 0
    if note > 0:
        for i in range(note):
            antall += skala[i % len(skala)]
    else:
        note = note + 1
        for i in range(-note):
            antall -= skala[-(i + 1 % len(skala))]
    return A * halvtone ** antall


def scale_fq(scale, start_step):
    fqs = []
    for i in range(start_step, len(scale) + start_step):
        if i == 0:
            for j in range(i, len(scale)):
                fqs.append(format(find_fq(j+1, scale), ".2f"))
            return fqs
        fqs.append(format(find_fq(i, scale), ".2f"))
    return fqs


def transpose(halfsteps):
    global scale
    scale[0] = halfsteps


def sanger(sang):
    global scale

    if sang == "lisa":
        scale = scales["M"]
        return([[1, 3, 5], 2, 3, 4, [2, 5, 7], 5, [4, 6, 8], 6, 6, 6, [2, 5, 7], 0,
              [2, 4, 6], 4, 4, 4, [3, 5, 7], 3, [2, 4, 6], 2, 2, 2, [1, 3, 6], [1, 3, 7], [1, 3, 5]],
               [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 0.51, 4])

    elif sang == "baseball":
        scale = scales["cro"]
        return ([6, 1, 3, 5]*4 + [7, 2, 4, 6]*2 + [8, 3, 5, 7]*2 + [3, 7, 9, 12, 7, [12, 6, 9]],
                [1, 1, 1, 1]*8 +[1/2, 1/2, 1/2, 1, 1/2, 2])

    elif sang == "kirke":
        scale = scales["m"]
        return [[1, 4, 5], [1, 2, 5], [1, 3, 5]], [4, 4, 6]

    A_pow = [1, 5]
    D_pow = [4, 9]
    C_pow = [3, 8]
    F_pow = [6, 11]
    if sang == "smells":
        return ([A_pow, A_pow, A_pow, "ghost", "ghost", "ghost", "ghost", D_pow, D_pow, [1],
              C_pow, C_pow, C_pow, "ghost", "ghost", "ghost", "ghost", F_pow, F_pow, [1]],
                [1, 1/2, 1/2, 1/8, 1/8, 1/8, 1/8, 1, 1, 1/2,
                 1, 1/2, 1/2, 1/8, 1/8, 1/8, 1/8, 1, 1, 1/2])

    if sang == "akkorder":
        return ([1, [1, 2, 5], [1, 4, 5, 7], [1, 3, 5, 8], [7, 9%7, 11%7],
                 [6, 8%7, 10%7], [5, 7%7, 9%7], [1, 3, 5, 7], [1, 3, 5, 8]],
                [2 for x in range(len([1, [1, 2, 5], [1, 4, 5, 7], [1, 3, 5, 8], [7, 9%7, 11%7],
                 [6, 8%7, 10%7], [5, 7%7, 9%7], [1, 3, 5, 7], [1, 3, 5, 8]]))])

"""
def find_fqs_from_notes(notes, skala=scale):
    fqs = []
    for note in notes:
        if not note:
            return note
        elif note == "ghost":
            return note
        antall = 0
        if note > 0:
            for i in range(note):
                antall += skala[i % len(skala)]
        else:
            note = note + 1
            print(note, "!")
            for i in range(-note):
                antall -= skala[-(i + 1 % len(skala))]
                print(i)
                print(antall, "!")
        fqs.append(A * halvtone ** antall)
    return fqs
"""

if __name__ == "__main__":
    play_melody(*sanger("lisa"))
    
close()
