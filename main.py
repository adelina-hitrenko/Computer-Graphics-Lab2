import matplotlib.pyplot as plt

def visualize_dataset(input_file, output_file, width_px=960, height_px=540):
    x_coords = []
    y_coords = []

    # зчитує датасету з файлу
    try:
        with open(input_file, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    try:
                        x = int(parts[0])
                        y = int(parts[1])
                        x_coords.append(x)
                        y_coords.append(y)
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Помилка: Файл {input_file} не знайдено.")
        return

    # встановлення розмірів полотна
    # matplotlib задає розмір у дюймах, приймемо dpi=100 для зручності.
    my_dpi = 100
    fig = plt.figure(figsize=(width_px / my_dpi, height_px / my_dpi), dpi=my_dpi)

    # відображення точок
    # scatter підходить для відображення окремих точок
    plt.scatter(x_coords, y_coords, s=10, c='blue', marker='.')
    
    # налаштування осей
    plt.xlim(0, width_px)
    plt.ylim(0, height_px)
    
    # додавання сітки та підписів
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Візуалізація датасету {input_file}")

    # збереження результату у графічний формат png
    plt.savefig(output_file, dpi=my_dpi)
    print(f"Зображення збережено у файл {output_file}")
    
    # закриваємо фігуру, щоб звільнити пам'ять
    plt.close()

if __name__ == "__main__":
    visualize_dataset('DS6.txt', 'result.png')
    
    
    