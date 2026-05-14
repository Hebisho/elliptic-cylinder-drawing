import numpy as np
import matplotlib.pyplot as plt

def ve_mat_tru_ellipse():
    try:
        a = float(input("Nhập chiều dài bán trục a (a khác 0): "))
        b = float(input("Nhập chiều dài bán trục b (b khác 0): "))
        if a == 0 or b == 0:
            print("Lỗi: Các bán trục a và b phải là số dương.")
            return 
    except ValueError:
        print("Lỗi: Giá trị nhập vào không hợp lệ.")
        return

    u = np.linspace(0, 2 * np.pi, 100)   # 100 điểm trên góc [0, 2π]
    v = np.linspace(-5, 5, 100)          # 100 điểm trên chiều cao [-5, 5]
    U, V = np.meshgrid(u, v)             # tạo lưới 2D (100x100)
    
    X = a * np.cos(U)
    Y = b * np.sin(U)
    Z = V

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.8, edgecolor='none')
    
    ax.set_xlabel('Trục X')
    ax.set_ylabel('Trục Y')
    ax.set_zlabel('Trục Z')
    ax.set_title(f'Mặt Trụ Ellipse\n$x^2/({a})^2 + y^2/({b})^2 = 1$', fontsize=12)
    ax.set_box_aspect([1, b/a, 1]) 
    
    plt.show()

if __name__ == "__main__":
    ve_mat_tru_ellipse()
