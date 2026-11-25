
import tkinter as tk
from tkinter import ttk

from src.api_client import IPApiClient, ApiError


class IPWhoisGUI:

    def __init__(self, root):
        self.root = root
        self.client = IPApiClient()

        self.root.title("IP WHOIS APP")
        self.root.geometry("850x600")
        self.root.resizable(False, False)

        self.create_interface()
        self.load_my_ips()

    def create_interface(self):

        # Titre principal
        title = tk.Label(
            self.root,
            text="IP WHOIS APPLICATION",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        # Section des adresses IP
        ip_frame = tk.LabelFrame(
            self.root,
            text="My IP Addresses",
            padx=20,
            pady=15
        )
        ip_frame.pack(fill="x", padx=30, pady=10)

        tk.Label(ip_frame, text="IPv4:").grid(
            row=0, column=0, sticky="w", padx=10, pady=5
        )

        self.ipv4_label = tk.Label(
            ip_frame,
            text="Not loaded"
        )
        self.ipv4_label.grid(row=0, column=1, sticky="w")

        tk.Label(ip_frame, text="IPv6:").grid(
            row=1, column=0, sticky="w", padx=10, pady=5
        )

        self.ipv6_label = tk.Label(
            ip_frame,
            text="Not loaded"
        )
        self.ipv6_label.grid(row=1, column=1, sticky="w")

        refresh_button = tk.Button(
            ip_frame,
            text="Refresh IP",
            command=self.load_my_ips
        )
        refresh_button.grid(
            row=2, column=0, columnspan=2, pady=10
        )

        # Section de recherche
        search_frame = tk.LabelFrame(
            self.root,
            text="IP Lookup",
            padx=20,
            pady=20
        )
        search_frame.pack(fill="x", padx=30, pady=10)

        self.ip_entry = tk.Entry(
            search_frame,
            width=40,
            font=("Arial", 11)
        )
        self.ip_entry.grid(row=0, column=0, padx=10)

        search_button = tk.Button(
            search_frame,
            text="Search",
            command=self.search_ip
        )
        search_button.grid(row=0, column=1)

        # Zone des rÃ©sultats
        result_frame = tk.LabelFrame(
            self.root,
            text="Search Results",
            padx=10,
            pady=10
        )
        result_frame.pack(fill="both", expand=True, padx=30, pady=10)

        self.result_text = tk.Text(
            result_frame,
            width=90,
            height=12,
            font=("Consolas", 10)
        )
        self.result_text.pack(fill="both", expand=True)

    def load_my_ips(self):

        self.ipv4_label.config(text="Loading...")
        self.ipv6_label.config(text="Loading...")
        self.root.update_idletasks()

        try:
            ips = self.client.get_my_ips()

            self.ipv4_label.config(
                text=ips["ipv4"] or "Not available"
            )

            self.ipv6_label.config(
                text=ips["ipv6"] or "Not available"
            )

        except ApiError as error:
            self.ipv4_label.config(text="Unavailable")
            self.ipv6_label.config(text="Unavailable")

            self.show_result(str(error))

    def search_ip(self):

        ip = self.ip_entry.get().strip()

        if not ip:
            self.show_result("Please enter an IP address.")
            return

        self.show_result("Searching...")

        self.root.update_idletasks()

        try:
            data = self.client.lookup(ip)

            connection = data.get("connection") or {}

            results = (
                f"IP Address: {data.get('ip', 'N/A')}\n"
                f"Country: {data.get('country', 'N/A')}\n"
                f"City: {data.get('city', 'N/A')}\n"
                f"Region: {data.get('region', 'N/A')}\n"
                f"Postal Code: {data.get('postal', 'N/A')}\n"
                f"Latitude: {data.get('latitude', 'N/A')}\n"
                f"Longitude: {data.get('longitude', 'N/A')}\n"
                f"ISP: {connection.get('isp', 'N/A')}\n"
                f"Organization: {connection.get('org', 'N/A')}\n"
            )

            self.show_result(results)

        except ApiError as error:
            self.show_result(f"Error: {error}")

    def show_result(self, message):

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, message)


if __name__ == "__main__":

    root = tk.Tk()
    app = IPWhoisGUI(root)
    root.mainloop()