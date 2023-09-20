import numpy as np
import matplotlib.pyplot as plt


def build_graph(type_signal, graph_number, t, signal, frequencies, signal_spectrum):
    plt.subplot(2, 2, graph_number)
    plt.plot(t, signal)
    plt.title(type_signal + ' сигнал')
    plt.xlabel('Время, с')
    plt.ylabel('Амплитуда')

    signal_spectrum[0] = 0
    title_spectrum_graph = 'Спектр ' + type_signal[0].lower() + type_signal[1: -2] + 'ого сигнала'

    plt.subplot(2, 2, graph_number + 1)
    plt.plot(frequencies[:len(frequencies) // 2], np.abs(signal_spectrum[:len(signal_spectrum) // 2]))
    plt.title(title_spectrum_graph)
    plt.xlabel('Частота, Гц')
    plt.xlim(0, 50)
    plt.ylabel('Амплитуда')


def calculate_spectra_and_build_graphs(frequency):
    duration = 1
    sampling_rate = 1000

    t = np.linspace(0, duration, sampling_rate * duration)

    harmonic_signal = np.sin(2 * np.pi * frequency * t)
    digital_signal = np.where(harmonic_signal > 0, 1, 0)

    harmonic_signal_spectrum = np.fft.fft(harmonic_signal)
    frequencies_for_harmonic_signal_spectrum = np.fft.fftfreq(len(harmonic_signal_spectrum), 1 / sampling_rate)

    digital_signal_spectrum = np.fft.fft(digital_signal)
    frequencies_for_digital_signal_spectrum = np.fft.fftfreq(len(digital_signal_spectrum), 1 / sampling_rate)

    plt.figure(figsize=(12, 6))
    plt.suptitle('Сигнал с частотой ' + str(frequency) + " Гц")

    build_graph('Гармонический', 1, t, harmonic_signal,
                frequencies_for_harmonic_signal_spectrum, harmonic_signal_spectrum)

    build_graph('Цифровой', 3, t, digital_signal,
                frequencies_for_digital_signal_spectrum, digital_signal_spectrum)

    plt.tight_layout()

    name_signal_graph = 'graphs/signal_with_frequency_' + str(frequency) + '_hz.png'
    plt.savefig(name_signal_graph)


def main():
    signal_frequencies = (1, 2, 4, 8)

    for frequency in signal_frequencies:
        calculate_spectra_and_build_graphs(frequency)


main()
