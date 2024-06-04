import numpy as np
import pickle
from flask import Flask, request, jsonify


def calculate_quality_of_sleep(answers):
    """
    Menghitung kualitas tidur berdasarkan jawaban yang diberikan.

    Args:
    answers (list of int): Jawaban dari pengguna untuk setiap pertanyaan dalam skala 1-10.

    Returns:
    float: Skor kualitas tidur dalam skala 1-10.
    """
    if len(answers) != 7:
        raise ValueError(
            "Harus ada 7 jawaban untuk setiap aspek kualitas tidur.")

    # Hitung rata-rata dari jawaban
    quality_of_sleep_score = sum(answers) / len(answers)
    return quality_of_sleep_score


# Contoh jawaban untuk setiap aspek kualitas tidur dalam skala 1-10
# [Subjective Sleep Quality, Sleep Latency, Sleep Duration, Sleep Disturbances, Habitual Sleep Efficiency, Use of Sleeping Medication, Daytime Dysfunction]
# answers = [8, 7, 9, 8, 9, 10, 8]  # Contoh jawaban pengguna

# # Hitung skor kualitas tidur
# quality_of_sleep_score = calculate_quality_of_sleep(answers)
# print(f"Skor Kualitas Tidur: {quality_of_sleep_score:.2f}")

# # Interpretasi skor
# if quality_of_sleep_score >= 8:
#     print("Kualitas tidur: Sangat Baik")
# elif quality_of_sleep_score >= 6:
#     print("Kualitas tidur: Baik")
# elif quality_of_sleep_score >= 4:
#     print("Kualitas tidur: Cukup")
# else:
#     print("Kualitas tidur: Buruk")


def calculate_stress_level(answers):
    """
    Menghitung tingkat stres berdasarkan jawaban yang diberikan.

    Args:
    answers (list of int): Jawaban dari pengguna untuk setiap pertanyaan dalam skala 1-10.

    Returns:
    float: Skor tingkat stres dalam skala 1-10.
    """
    if len(answers) != 7:
        raise ValueError(
            "Harus ada 7 jawaban untuk setiap aspek tingkat stres.")

    # Hitung rata-rata dari jawaban
    stress_level_score = sum(answers) / len(answers)
    return stress_level_score


# Contoh jawaban untuk setiap aspek tingkat stres dalam skala 1-10
# [Kesehatan Fisik, Kesehatan Mental, Beban Kerja, Hubungan Sosial, Keuangan, Tidur, Keseimbangan Hidup]
# answers = [7, 8, 6, 5, 7, 8, 6]  # Contoh jawaban pengguna

# # Hitung skor tingkat stres
# stress_level_score = calculate_stress_level(answers)
# print(f"Skor Tingkat Stres: {stress_level_score:.2f}")

# # Interpretasi skor
# if stress_level_score >= 8:
#     print("Tingkat stres: Sangat Tinggi")
# elif stress_level_score >= 6:
#     print("Tingkat stres: Tinggi")
# elif stress_level_score >= 4:
#     print("Tingkat stres: Sedang")
# else:
#     print("Tingkat stres: Rendah")


def calculate_bmi(weight, height):
    """
    Menghitung BMI berdasarkan berat dan tinggi badan.

    Args:
    weight (float): Berat badan dalam kilogram.
    height (float): Tinggi badan dalam meter.

    Returns:
    float: Nilai BMI.
    """
    if height <= 0:
        raise ValueError("Tinggi badan harus lebih besar dari nol.")

    bmi = weight / (height ** 2)
    return bmi


def categorize_bmi(bmi):
    """
    Mengkategorikan BMI berdasarkan nilai BMI.

    Args:
    bmi (float): Nilai BMI.

    Returns:
    str: Kategori BMI.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


# # Contoh penggunaan
# weight = 70  # Berat badan dalam kilogram
# height = 1.75  # Tinggi badan dalam meter

# bmi = calculate_bmi(weight, height)
# category = categorize_bmi(bmi)

# print(f"BMI: {bmi:.2f}")
# print(f"Kategori BMI: {category}")

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    # data = request.json

    # buatkan dummy data
    # data = {
    #     'features': [8, 7, 9, 8, 9, 10, 8]
    # }
    # prediction = model.predict([np.array(data['features'])])
    # return jsonify({'prediction': int(prediction[0])})

    try:
        # data = request.json
        data = {  # dummy data
            'features': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        }

        prediction = model.predict([np.array(data['features'])])
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
