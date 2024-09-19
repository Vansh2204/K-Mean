import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class KMeansApp:
    def __init__(self, root):
        self.root = root
        self.root.title("K-Means Clustering")

        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        style = ttk.Style()
        style.theme_use("vista")  

        # Create the main frame
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack()

        # File upload section
        self.upload_button_frame = ttk.Frame(self.frame)
        self.upload_button_frame.pack(pady=5)

        self.upload_button = ttk.Button(self.upload_button_frame, text="Upload CSV/Excel", command=self.upload_file, style="upload.TButton")
        self.upload_button.pack(side=tk.LEFT)

        # style.configure("upload.TButton", foreground="white", background="black", padding=(10, 5),relief="flat",state="disabled", cursor="arrow")
        # style.configure("upload.TButton", foreground="white", background="black", padding=(10, 5))
        style.configure("upload.TButton", padding=20, borderwidth=2, relief="groove", radius=10 ,)

        

        self.cluster_config_frame = ttk.Frame(self.frame)
        self.cluster_config_frame.pack(pady=10)

        self.cluster_label = ttk.Label(self.cluster_config_frame, text="Number of Clusters:", style="cluster.TLabel")
        self.cluster_label.pack(side=tk.LEFT)

        style.configure("cluster.TLabel", font=("Arial", 12), foreground="black")

        self.cluster_entry = ttk.Entry(self.cluster_config_frame, width=25, style="cluster.TEntry")
        self.cluster_entry.pack(side=tk.LEFT, padx=5)

        style.configure("cluster.TEntry", background="black")

        self.cluster_button = ttk.Button(self.cluster_config_frame, text="Perform K-Means", command=self.perform_kmeans, state=tk.DISABLED, style="cluster.TButton",width=20)
        self.cluster_button.pack(side=tk.RIGHT)

        style.configure("cluster.TButton", padding=5, borderwidth=2, relief="groove", radius=10)


        self.data = None

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if file_path:
            try:
                if file_path.endswith(".csv"):
                    self.data = pd.read_csv(file_path)
                else:
                    self.data = pd.read_excel(file_path)
                
                # Enable the K-Means button
                self.cluster_button.config(state=tk.NORMAL)
                messagebox.showinfo("Info", f"File Uploaded !!!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while loading the file: {e}")

    def perform_kmeans(self):
        if self.data is not None:
            try:
                num_clusters = int(self.cluster_entry.get())
                if num_clusters <= 0:
                    raise ValueError("Number of clusters must be a positive integer.")

                kmeans = KMeans(n_clusters=num_clusters)
                self.data['Cluster'] = kmeans.fit_predict(self.data)

                # Plotting
                plt.figure(figsize=(10, 6))
                scatter = plt.scatter(self.data.iloc[:, 0], self.data.iloc[:, 1], c=self.data['Cluster'], cmap='viridis', marker='o')
                plt.title("K-Means Clustering")
                plt.xlabel(self.data.columns[0])
                plt.ylabel(self.data.columns[1])
                plt.colorbar(scatter, label='Cluster')
                plt.show()

            except ValueError:
                messagebox.showerror("Error", "Please enter a positive integer to display Clusters.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "No data loaded. Please upload a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = KMeansApp(root)
    root.mainloop()
