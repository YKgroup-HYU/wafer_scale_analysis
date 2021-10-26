import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

def IV(filename,save,show):

    tree = ET.parse(filename)
    b = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Voltage")
    c = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Current")
    x_2 = b.text.split(",")
    y_2 = c.text.split(",")
    x_list = list(map(float, x_2))
    y_list = list(map(float, y_2))
    y_list_1 = []
    for i in range(len(y_list)):
        g = abs(y_list[i])
        y_list_1.append(g)
    plt.plot(x_list, y_list_1, "ro", label='evaluated values')
    plt.yscale("log")
    plt.title("IV-analysis")
    plt.xlabel('Voltage [V]')
    plt.ylabel('Current [A]')

    polyfiti = np.polyfit(x_list, y_list_1, 12)
    fiti = np.poly1d(polyfiti)
    plt.plot(x_list, fiti(x_list), label='fitting')

    plt.xlabel('Voltage [V]')
    plt.ylabel('Current [A]')
    plt.title('IV-fitting')
    plt.legend()
    if save == 'T':
        plt.savefig('.\\res\\figure\\%s.png'%(filename.split("\\")[4]))
    if show == 'T':
        plt.show()
