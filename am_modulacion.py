# -*- coding: utf-8 -*-
"""
Actividad: Implementación y análisis de un sistema de modulación AM
Autor: Rafael Ricardo Fuantos Gutierrez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# -----------------------
# 1. Parámetros de la señal
# -----------------------
Fs = 5000              # Frecuencia de muestreo
t = np.arange(0, 1, 1/Fs)  # Vector de tiempo

# Señal de mensaje
fm = 5                 # Frecuencia del mensaje
Am = 1                 # Amplitud del mensaje
mensaje = Am * np.sin(2 * np.pi * fm * t)

# Señal portadora
fc = 100               # Frecuencia de la portadora
Ac = 1                 # Amplitud de la portadora
portadora = Ac * np.cos(2 * np.pi * fc * t)

# -----------------------
# 2. Graficar mensaje y portadora
# -----------------------
plt.figure(figsize=(10,4))
plt.plot(t, mensaje, label='Mensaje')
plt.title('Señal de Mensaje (Tiempo)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t, portadora, label='Portadora', color='orange')
plt.title('Portadora (Tiempo)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

# -----------------------
# 3. Señal modulada AM
# -----------------------
modulada = (1 + mensaje) * portadora

plt.figure(figsize=(10,4))
plt.plot(t, modulada, label='Señal AM', color='green')
plt.title('Señal Modulada AM (Tiempo)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

# -----------------------
# 4. Espectro de la señal AM
# -----------------------
N = len(modulada)
frecuencia = fftfreq(N, 1/Fs)
modulada_fft = fft(modulada)

plt.figure(figsize=(10,4))
plt.plot(frecuencia[:N//2], np.abs(modulada_fft[:N//2]))
plt.title('Espectro de la Señal AM')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.grid(True)
plt.show()

# -----------------------
# 5. Señal AM con ruido
# -----------------------
ruido = 0.5 * np.random.randn(len(modulada))
modulada_ruidosa = modulada + ruido

plt.figure(figsize=(10,4))
plt.plot(t, modulada_ruidosa, color='red')
plt.title('Señal AM con Ruido')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()