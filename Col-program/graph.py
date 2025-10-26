import matplotlib.pyplot as plt

# Sample data
forward_voltage = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
forward_current = [0, 0, 0.01, 0.02, 0.06, 0.65, 5.50, 20.0]

reverse_voltage = [-0.5, -1, -1.5, -2, -2.5, -3, -3.5, -4]
reverse_current = [-0.02, -0.02, -0.03, -0.03, -0.03, -0.03, -0.03, -0.03]

plt.plot(forward_voltage, forward_current, label='Forward Bias', marker='o')
plt.plot(reverse_voltage, reverse_current, label='Reverse Bias', marker='x')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA / µA)')
plt.title('V-I Characteristics of PN Junction Diode')
plt.axvline(x=0.6, color='r', linestyle='--', label='Knee Voltage (~0.6V)')
plt.legend()
plt.grid(True)
plt.show()
