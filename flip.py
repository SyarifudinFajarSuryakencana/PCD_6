import cv2
import matplotlib.pyplot as plt

# 1. Baca citra
img = cv2.imread("contoh.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
tinggi, lebar = img.shape[:2]
print(f"Ukuran citra asli: {lebar} x {tinggi}")

# 2. Horizontal Flip (cermin kiri-kanan): kode 1
flip_horizontal = cv2.flip(img, 1)

# 3. Vertical Flip (cermin atas-bawah): kode 0
flip_vertikal = cv2.flip(img, 0)

# 4. Simpan hasil sebagai file (untuk laporan)
cv2.imwrite("hasil_flip_horizontal.jpg",
            cv2.cvtColor(flip_horizontal, cv2.COLOR_RGB2BGR))
cv2.imwrite("hasil_flip_vertikal.jpg",
            cv2.cvtColor(flip_vertikal, cv2.COLOR_RGB2BGR))
print("Hasil tersimpan: hasil_flip_horizontal.jpg, hasil_flip_vertikal.jpg")

# 5. Tampilkan citra asli dan kedua hasil flip
fig, axes = plt.subplots(1, 3, figsize=(12, 5))
axes[0].imshow(img)
axes[0].set_title("Citra Asli")
axes[1].imshow(flip_horizontal)
axes[1].set_title("Flip Horizontal")
axes[2].imshow(flip_vertikal)
axes[2].set_title("Flip Vertikal")
for ax in axes:
    ax.axis("off")
plt.tight_layout()
plt.show()
