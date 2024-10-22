from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
import matplotlib.pyplot as plt
from io import BytesIO
from kivy.core.image import Image as CoreImage


def create_savings_graph(current, target):
    # Përdorim Matplotlib për të krijuar një grafik të thjeshtë të progresit të kursimeve
    fig, ax = plt.subplots()
    ax.bar(["Kursime Aktualisht", "Synim"], [
           current, target], color=['blue', 'green'])
    ax.set_ylabel("Shuma ($)")
    ax.set_title("Progresi i Kursimeve")

    # Ruaj grafikën në një imazh në memorien e përkohshme
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close(fig)

    # Kthe imazhin si një CoreImage që mund të shfaqet në Kivy
    return CoreImage(buffer, ext='png').texture
