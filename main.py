import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Load the exchange rate data from the cleaned dataset
exchange_data = {
    "AUD (Dolar Australia)": {"Kurs Jual": 10124.81, "Kurs Beli": 10022.45},
    "BND (Dolar Brunei)": {"Kurs Jual": 11986.47, "Kurs Beli": 11861.97},
    "CAD (Dolar Kanada)": {"Kurs Jual": 11329.01, "Kurs Beli": 11212.40},
    "CHF (Franc Swiss )": {"Kurs Jual": 18040.00, "Kurs Beli": 17850.63},
    # Add other currencies as needed
}

# Initialize the main GUI application
class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Labels and input fields
        self.amount_label = tk.Label(root, text="Amount (in IDR):")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.currency_label = tk.Label(root, text="Select Currency:")
        self.currency_label.grid(row=1, column=0, padx=10, pady=10)

        self.currency_combo = ttk.Combobox(root, values=list(exchange_data.keys()))
        self.currency_combo.grid(row=1, column=1, padx=10, pady=10)
        self.currency_combo.set("AUD (Dolar Australia)")

        # Buttons
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Result display
        self.result_label = tk.Label(root, text="Converted Amount:")
        self.result_label.grid(row=3, column=0, padx=10, pady=10)

        self.result_value = tk.Label(root, text="-", fg="blue")
        self.result_value.grid(row=3, column=1, padx=10, pady=10)

    def convert_currency(self):
        try:
            # Get input values
            amount = float(self.amount_entry.get())
            currency = self.currency_combo.get()

            # Get the exchange rate
            if currency in exchange_data:
                rate = exchange_data[currency]["Kurs Beli"]
                converted_amount = amount / rate

                # Update result label
                self.result_value.config(text=f"{converted_amount:.2f} {currency}")
            else:
                messagebox.showerror("Error", "Selected currency is not available.")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
