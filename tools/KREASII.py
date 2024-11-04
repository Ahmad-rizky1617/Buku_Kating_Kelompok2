import streamlit as st
import pandas as pd

st.title("Data Analyst With Python")

import streamlit as st

st.header("Data Magang CEO HMSD Adyatama")
st.write("Dataset ini berisi informasi mengenai peserta magang di sebuah program, "
         "dengan beberapa atribut penting terkait pengalaman magang mereka. "
         "Berikut adalah analisis umum terhadap dataset ini dan langkah-langkah yang dapat dilakukan "
         "untuk menggali wawasan lebih lanjut.")

st.write("Dataset ini memiliki 112 baris (peserta) dan 11 kolom, yang masing-masing berisi informasi sebagai berikut:")
st.write("1. Nama Lengkap: Nama lengkap peserta.")
st.write("2. NIM: Nomor Induk Mahasiswa sebagai identitas unik peserta.")
st.write("3. Asal Provinsi: Provinsi asal peserta, yang dapat memberikan informasi demografis.")
st.write("4. Divisi Magang: Divisi tempat peserta menjalani magang, seperti Badan Legislatif.")
st.write("5. Rating Kesulitan Magang (1-5): Skor kesulitan magang yang dirasakan, dari 1 hingga 5, "
         "di mana 5 berarti semakin sulit.")
st.write("6. Gender: Jenis kelamin peserta (Laki-laki atau Perempuan).")
st.write("7. Rating Kepuasan saat diterima Magang (1-5): Tingkat kepuasan peserta saat diterima magang, "
         "dari 1 hingga 5, dengan 5 sebagai tingkat kepuasan tertinggi.")
st.write("8. Perasaan Selama Magang: Deskripsi singkat mengenai perasaan peserta selama magang.")
st.write("9. Minat & Hobi: Hobi dan minat peserta, yang bisa membantu memahami profil minat mereka.")
st.write("10. Rating Kesibukan Saat Magang (1-5): Skor kesibukan semua"
### Analisis Potensial

#### 1. Analisis Demografis
   - "Asal" Provinsi: Analisis ini dapat membantu mengetahui distribusi geografis peserta magang, apakah mayoritas berasal dari wilayah tertentu atau tersebar di berbagai provinsi.
   - Gender: Menghitung distribusi gender bisa memberi gambaran tentang keseimbangan gender di program ini.

#### 2. Analisis Divisi dan Kesulitan Magang
   - Divisi Magang: Mengevaluasi distribusi peserta di tiap divisi dan membandingkannya dengan tingkat kesulitan yang dirasakan. Misalnya, apakah divisi tertentu cenderung lebih menantang dibandingkan divisi lain?
   - Rating Kesulitan Magang: Melihat rata-rata kesulitan di masing-masing divisi dapat membantu perusahaan menilai area mana yang mungkin memerlukan dukungan tambahan.

#### 3. *Analisis Kepuasan dan Perasaan Selama Magang*
   - Rating Kepuasan saat diterima Magang: Mengukur seberapa puas peserta saat diterima magang dan apakah ada korelasi antara kepuasan awal dengan pengalaman keseluruhan.
   - Perasaan Selama Magang: Menyusun analisis kualitatif terhadap perasaan peserta menggunakan kata-kata yang sering muncul dapat membantu mengetahui pengalaman magang secara umum.

#### 4. Kesibukan dan Jam Kerja
   - Rating Kesibukan: Meninja skor kesibukan di tiap divisi, apakah ada divisi yang cenderung lebih sibuk dibandingkan yang lain.
   - Jam Kerja Magang per Minggu: Membandingkan jam kerja mingguan dengan tingkat kesibukan untuk memahami apakah jam kerja yang lebih panjang selalu berkaitan dengan perasaan kesibukan yang lebih tinggi.

### Langkah-Langkah Lanjutan

"1. Visualisasi Data: Menggunakan grafik batang atau pie chart untuk menunjukkan distribusi peserta berdasarkan provinsi, gender, dan divisi magang.
2. Korelasi Antar Variabel: Menggunakan analisis korelasi antara kesulitan, kepuasan, dan kesibukan dengan variabel lain untuk melihat pola atau hubungan tertentu yang signifikan.
3. Analisis Teks pada Kolom “Perasaan Selama Magang”: Menganalisis kata-kata yang sering digunakan untuk mendeskripsikan perasaan, guna menangkap perasaan umum dari para peserta.

### Kesimpula
("Analisis dataset ini dapat memberikan pemahaman yang mendalam mengenai pengalaman peserta magang. Informasi seperti tingkat kesulitan, kepuasan, dan kesibukan bisa digunakan sebagai dasar untuk meningkatkan program magang di masa mendatang, memastikan bahwa peserta mendapatkan pengalaman yang bermanfaat sekaligus sesuai dengan kapasitas mereka."))