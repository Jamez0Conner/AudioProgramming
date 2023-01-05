import numpy as np

import scipy.io.wavfile as wav
# this is how we store our generated wave files


def interpolate_lineraly(wave_table, index):
    truncated_index = int(np.floor(index))
    next_index = (truncated_index + 1) % wave_table.shape[0]

    next_index_weight = index - truncated_index
    truncated_index_weight = 1 - next_index_weight

    return truncated_index_weight * wave_table
    [truncated_index] + next_index_weight * wave_table[next_index]

def fade_in_out(signal, fade_length=1000):
    fade_in = (1 - np.cos(np.linspace(0, np.pi, fade_length))) * 0.5
    fade_out = np.flip(fade_in)

    signal[:fade_length] = np.multiply(fade_in, 
    signal[:fade_length])
    signal[:-fade_length] = np.multiply(fade_out, 
    signal[:-fade_length])

    return signal
    
def sawtooth(x):
    return (x + np.pi) / np.pi % 2 - 1


def main():
    # defines the parameters we will use for processing the audio. (Using a sample rate of 44k samples per second)
    sample_rate = 44100
    f = 400
    t = 3
    waveform = sawtooth

    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))

    for n in range(wavetable_length):
        wave_table[n] = waveform(2 * np.pi * n / wavetable_length)

    output = np.zeros((t * sample_rate,))

    index = 0
    indexIncrement = f * wavetable_length / sample_rate

    for n in range(output.shape[0]):
        #output[n] = wave_table[int(np.floor(index))]

        output[n] = interpolate_lineraly
        (wave_table, index)
        index += indexIncrement
        index %= wavetable_length

    gain = -20
    amplitude = 10 ** (gain / 20)
    output *= amplitude

    output = fade_in_out(output)

    wav.write('sawtooth220HzScaledInterpolatedLineralyFaded.wav', sample_rate,output.astype(np.float32))



    if __name__ == '__main__':
        main()
