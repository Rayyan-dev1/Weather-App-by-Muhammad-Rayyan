"""
🌦 Weather App - Mobile & PC Version (Tkinter + OpenWeatherMap API)
By Rayyan (Final Polished Version)
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

# ---------------- CONFIG ----------------
API_KEY = "361bf9e926b0f29711293965c2e66562"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Paths (update with your images)
MOBILE_BG_PATH = r"C:\Users\Muhammd Reyyan\Desktop\Python\daniel-olah-HNkgPFBShSw-unsplash.jpg"
PC_BG_PATH = r"C:\Users\Muhammd Reyyan\Desktop\Python\actionvance-t7EL2iG3jMc-unsplash.jpg"
# ---------------------------------------


def fetch_weather(city: str):
    """Fetch weather data from API"""
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "en"}
        resp = requests.get(API_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if data.get("cod") != 200:
            return None, data.get("message", "Error occurred")

        return data, None
    except requests.exceptions.RequestException as e:
        return None, str(e)


# ---------------- MOBILE VERSION ----------------
def mobile_ui():
    def show_weather():
        city = city_entry.get().strip()
        if not city or city == "🔍 Enter city name":
            messagebox.showwarning("Input Error", "Please enter a city name")
            return
        data, error = fetch_weather(city)
        if error:
            messagebox.showerror("Error", f"Could not fetch weather:\n{error}")
            return

        for widget in result_frame.winfo_children():
            widget.destroy()

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        desc = data["weather"][0]["description"].capitalize()
        name = data["name"]
        country = data["sys"]["country"]

        tk.Label(result_frame, text=f"{temp}°C", font=("Segoe UI", 42, "bold"),
                 bg="#121212", fg="white").pack(pady=(10, 0))
        tk.Label(result_frame, text=f"{name}, {country}", font=("Segoe UI", 18, "bold"),
                 bg="#121212", fg="#90caf9").pack(pady=5)
        tk.Label(result_frame, text=desc, font=("Segoe UI", 16, "italic"),
                 bg="#121212", fg="white").pack(pady=(0, 15))

        details = [
            ("🌡", "Feels Like", f"{feels}°C"),
            ("💧", "Humidity", f"{humidity}%"),
            ("💨", "Wind", f"{wind_speed} m/s")
        ]

        detail_frame = tk.Frame(result_frame, bg="#1E1E1E")
        detail_frame.pack(pady=10, fill="x", padx=15)

        for i, (emoji, label, value) in enumerate(details):
            box = tk.Frame(detail_frame, bg="#1E1E1E", padx=10, pady=10)
            box.grid(row=0, column=i, padx=10)
            tk.Label(box, text=emoji, font=("Segoe UI Emoji", 20),
                     bg="#1E1E1E", fg="white").pack()
            tk.Label(box, text=label, font=("Segoe UI", 12, "bold"),
                     bg="#1E1E1E", fg="#90caf9").pack()
            tk.Label(box, text=value, font=("Segoe UI", 12),
                     bg="#1E1E1E", fg="white").pack()

    root = tk.Tk()
    root.geometry("500x700")
    root.resizable(False, False)
    root.title("Weather App - Mobile")

    # Background
    bg_image = Image.open(MOBILE_BG_PATH).resize((500, 700))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title
    title_label = tk.Label(root, text="🌦 Weather Now", font=("Segoe UI", 20, "bold"),
                           bg="#0d47a1", fg="white", pady=14)
    title_label.pack(fill="x")
    title_label.lift()

    # Search
    search_frame = tk.Frame(root, bg="#121212")
    search_frame.pack(pady=20)
    search_frame.lift()

    city_entry = tk.Entry(search_frame, font=("Segoe UI", 14), justify="center",
                          relief="flat", bd=5, fg="grey", bg="#1E1E1E",
                          insertbackground="white", width=20)
    city_entry.insert(0, "🔍 Enter city name")
    city_entry.pack(ipady=10, padx=20)

    # Stylish Buttons
    get_btn = tk.Button(root, text="Get Weather", command=show_weather,
                        font=("Segoe UI", 12, "bold"), bg="#0d47a1", fg="white",
                        activebackground="#1565c0", activeforeground="white",
                        relief="flat", padx=90, pady=10)
    get_btn.pack(pady=10)
    get_btn.lift()

    # Results
    result_frame = tk.Frame(root, bg="#131313", bd=0)
    result_frame.pack(pady=25, expand=True, padx=20)
    result_frame.lift()

    footer_label = tk.Label(root, text="Designed and Developed by Rayyan",
                            font=("Segoe UI", 10, "italic"), bg="black", fg="white", pady=6)
    footer_label.pack(side="bottom", fill="x")
    footer_label.lift()

    root.mainloop()


# ---------------- PC VERSION ----------------
def pc_ui():
    def show_weather():
        city = city_entry.get().strip()
        if not city or city == "Enter city name":
            messagebox.showwarning("Input Error", "Please enter a city name")
            return
        data, error = fetch_weather(city)
        if error:
            messagebox.showerror("Error", f"Could not fetch weather:\n{error}")
            return

        for w in result_frame.winfo_children():
            w.destroy()

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        desc = data["weather"][0]["description"].capitalize()
        name = data["name"]
        country = data["sys"]["country"]

        tk.Label(result_frame, text=f"{temp}°C", font=("Segoe UI", 60, "bold"),
                 bg="#000000", fg="white").pack(pady=20)
        tk.Label(result_frame, text=f"{name}, {country}", font=("Segoe UI", 24, "bold"),
                 bg="#000000", fg="#90caf9").pack()
        tk.Label(result_frame, text=desc, font=("Segoe UI", 20, "italic"),
                 bg="#000000", fg="white").pack(pady=10)

        details = [
            ("🌡 Feels Like", f"{feels}°C"),
            ("💧 Humidity", f"{humidity}%"),
            ("💨 Wind", f"{wind_speed} m/s")
        ]
        details_frame = tk.Frame(result_frame, bg="#000000", padx=20, pady=20)
        details_frame.pack(pady=20)

        for text, val in details:
            box = tk.Frame(details_frame, bg="#1E1E1E", padx=20, pady=20)
            box.pack(side="left", padx=15)
            tk.Label(box, text=text, font=("Segoe UI", 14, "bold"),
                     bg="#1E1E1E", fg="#90caf9").pack()
            tk.Label(box, text=val, font=("Segoe UI", 16),
                     bg="#1E1E1E", fg="white").pack()

    root = tk.Tk()
    root.title("Weather App - PC")
    root.state("zoomed")

    # Background image
    screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
    bg_image = Image.open(PC_BG_PATH).resize((screen_w, screen_h))
    bg_photo = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(root, image=bg_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Overlay content (placed above background)
    title = tk.Label(root, text="🌍 Weather Dashboard", font=("Segoe UI", 24, "bold"),
                     bg="#0d47a1", fg="white", pady=20, padx=700)
    title.place(relx=0.5, y=20, anchor="n")
    title.lift()

    search_frame = tk.Frame(root, bg="#000000")
    search_frame.place(relx=0.5, rely=0.15, anchor="n")
    search_frame.lift()

    city_entry = tk.Entry(search_frame, font=("Segoe UI", 16), width=30, bg="#1E1E1E", fg="white",
                          insertbackground="white", relief="flat")
    city_entry.insert(0, "Enter city name")
    city_entry.pack(side="left", padx=10, ipady=5)

    search_btn = tk.Button(search_frame, text="Search", command=show_weather,
                           font=("Segoe UI", 12, "bold"), bg="#0d47a1", fg="white",
                           activebackground="#1565c0", relief="flat", padx=15, pady=8)
    search_btn.pack(side="left")
    search_btn.lift()

    result_frame = tk.Frame(root, bg="#000000")
    result_frame.place(relx=0.5, rely=0.3, anchor="n")
    result_frame.lift()

    footer = tk.Label(root, text="Weather App PC Edition | Designed by Rayyan",
                      font=("Segoe UI", 11, "italic"), bg="#0d47a1", fg="white", pady=10)
    footer.pack(side="bottom", fill="x")
    footer.lift()

    root.mainloop()


# ---------------- LAUNCHER ----------------
def launcher():
    root = tk.Tk()
    root.title("Weather App Launcher")
    root.geometry("400x300")
    root.configure(bg="#121212")

    tk.Label(root, text="🌦 Choose App Version", font=("Segoe UI", 18, "bold"),
             bg="#121212", fg="white").pack(pady=40)

    tk.Button(root, text="📱 Mobile Version", command=lambda: [root.destroy(), mobile_ui()],
              font=("Segoe UI", 12, "bold"), bg="#0d47a1", fg="white",
              activebackground="#1565c0", relief="flat", padx=20, pady=10).pack(pady=15)

    tk.Button(root, text="💻 PC Version", command=lambda: [root.destroy(), pc_ui()],
              font=("Segoe UI", 12, "bold"), bg="#388e3c", fg="white",
              activebackground="#2e7d32", relief="flat", padx=20, pady=10).pack(pady=15)

    root.mainloop()


# ---------------- RUN ----------------
if __name__ == "__main__":
    launcher()
