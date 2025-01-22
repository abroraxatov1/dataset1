import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Ma'lumotlar (x: dars tayyorlash soatlari, y: imtihon natijalari)
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Kirish (soat)
y = np.array([50, 55, 65, 70, 75])  # Chiqish (natijalar)

# Modelni yaratish
model = LinearRegression()

# Modelni o'rgatish
model.fit(x, y)

# Tenglama koeffitsientlari
beta_1 = model.coef_[0]  # Eğim (slope)
beta_0 = model.intercept_  # To'xtash nuqtasi (intercept)

print(f"Regressiya tenglamasi: y = {beta_0:.2f} + {beta_1:.2f}x")

# Prognoz qilish (masalan, 6 soat uchun)
x_new = np.array([[6]])
y_pred = model.predict(x_new)
print(f"6 soat tayyorlangan talabaning prognoz qilingan natijasi: {y_pred[0]:.2f}%")

# Grafik chizish
plt.scatter(x, y, color='blue', label="Haqiqiy ma'lumotlar")  # Haqiqiy ma'lumotlar
y_line = model.predict(x)  # Chiziqli regressiya chizig'i
plt.plot(x, y_line, color='red', label="Regressiya chizig'i")
plt.scatter(x_new, y_pred, color='green', label=f'Prognoz (6 soat: {y_pred[0]:.2f}%)')

plt.xlabel('Dars tayyorlash soatlari')
plt.ylabel('Imtihon natijalari (%)')
plt.title('Oddiy chiziqli regressiya')
plt.legend()
plt.show()