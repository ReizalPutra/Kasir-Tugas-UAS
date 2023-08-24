import tkinter as tk
import os
import tkinter.messagebox as messagebox
from tkinter import ttk
from PIL import ImageTk, Image

spinboxes = {} 
produk = [
    {"nama": "Buku", "harga": 10000, "stok": 5, "gambar": "./assets/buku.png"},
    {"nama": "Penghapus", "harga": 20000, "stok": 3, "gambar": "./assets/penghapus.png"},
    {"nama": "Pencil", "harga": 15000, "stok": 6, "gambar": "./assets/pensil.png"},
    {"nama": "Pulpen", "harga": 12000, "stok": 4, "gambar": "./assets/pulpen.png"},
    {"nama": "Kerayon", "harga": 18000, "stok": 5, "gambar": "./assets/kerayon.png"},
    {"nama": "Spidol", "harga": 15000, "stok": 5, "gambar": "./assets/spidol.png"},
    {"nama": "Kertas", "harga": 12000, "stok": 8, "gambar": "./assets/kertas.png"},
    {"nama": "WhiteBoard", "harga": 18000, "stok": 2, "gambar": "./assets/whiteboard.png"},
    {"nama": "BlackBoard", "harga": 15000, "stok": 2, "gambar": "./assets/blackboard.png"},
    {"nama": "Kotak Pencil", "harga": 12000, "stok": 9, "gambar": "./assets/kotakpensil.png"},
    {"nama": "Kapur Tulis", "harga": 18000, "stok": 5, "gambar": "./assets/kapur.png"}
]

window = tk.Tk()
window.title('Toko Peralatan Sekolah')
window.iconbitmap("./assets/icon.ico")


def create_product(root, products):
    frame = ttk.Frame(root)
    frame.pack()
    row = 0
    column = 0
    new_row = 1
    for product in products:
        product_frame = ttk.LabelFrame(frame, text=product["nama"], relief=tk.RAISED, borderwidth=1)
        product_frame.grid(row=row, column=column, padx=10, pady=10, sticky='nsew')
        
        #gambar
        image_path = os.path.join(os.path.dirname(__file__), product["gambar"])
        image = Image.open(image_path)

        #konversi gambar 
        image_tk = ImageTk.PhotoImage(image)
        resized_image = image.resize((100, 100))  # Ubah ukuran sesuai kebutuhan
        image_tk = ImageTk.PhotoImage(resized_image)
        
        #menampilkan gambar di jendela
        label_image = tk.Label(product_frame, image=image_tk)
        label_image.image = image_tk
        label_image.grid(row=0, column=column, columnspan=2)  # Mengatur kolom dan lebar gambar
        
        harga = tk.Label(product_frame, text="Harga: RP " + str(product["harga"]))
        harga.grid(row=1, column=column, pady=5)
        
        label_stok = tk.Label(product_frame, text="Stok: " + str(product["stok"]))
        label_stok.grid(row=2, column=column)
        
        spinbox_jumlah = ttk.Spinbox(product_frame, from_=0, to=product["stok"])
        spinbox_jumlah.grid(row=3, column=column, pady=5)
        spinboxes[product["nama"]] = spinbox_jumlah
        
        #agar box nya bisa kebawah
        column += 1
        if column >= 4:  
            column = 0
            row += new_row
        if row >= 4:  
            new_row = 3

    frame.pack()

def calculate_total():
    total = 0
    out_of_stock_products = []
    
    for product in produk:
        price = product["harga"]
        quantity = spinboxes[product["nama"]].get()
        
        # Memeriksa apakah nilai quantity kosong atau tidak
        if not quantity:
            continue
        
        quantity = int(quantity)
        
        # Memeriksa apakah quantity melebihi stok produk
        if quantity > product["stok"]:
            out_of_stock_products.append(product["nama"])
        else:
            subtotal = price * quantity
            total += subtotal
    
    # Menampilkan pesan error jika ada produk yang kuantitasnya melebihi stok
    if out_of_stock_products:
        error_message = f"Kuantitas produk berikut melebihi stok yang tersedia: {', '.join(out_of_stock_products)}"
        messagebox.showerror("Error", error_message)
        return
    
    # Update total bayar
    total_label["text"] = f"Total: RP {total}"


create_product(window, produk)
calculate_button = ttk.Button(window, text="Hitung Total Belanja", command=calculate_total)
calculate_button.pack()

# Label untuk menampilkan total tagihan
total_label = ttk.Label(window, text="Total: Rp 0")
total_label.pack()

window.mainloop()
