import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True
#Mencegah datanya berubah menjadi default

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)
#homepage itu adalah variabel
#st.page adalah komponen di streamlit untuk membuat halaman
#st.page ini butuh argumen; Halaman Utama/halaman_utama.py (path directory); 

Mahasiswa1 = st.Page(
    "Buku Kating/051_Fiodora Alysa Juandi.py",
    title="051 - Fiodora Alysa Juandi",
    icon=":material/person:",
)
#Mahasiswa1 akan mengakses data yang bernama Kemas Veriandra yang foldernya disimpan di Buku Kating

Mahasiswa2 = st.Page(
    "Buku Kating/020_Keren Marito Lumban Gaol.py",
    title="020 - 020_Keren Marito Lumban Gaol.py",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/102_Rahmah Gustriana Deka.py",
    title="102 - Rahmah Gustriana Deka",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/081_Intan Nursyabani.py",
    title="081 - Intan Nursyabani",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/045_Ken Gracya Waoma.py",
    title="045 - Ken Gracya Waoma",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/090_Malika Azzahra Salsabila.py",
    title="090 - Malika Azzahra Salsabila",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/050_Ahmad Rizky.py",
    title="050-Ahmad Rizky",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/007_Devyna Sonya Palupi Sanjaya.py",
    title="007-Devyna Sonya Palupi Sanjaya",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/029_Vania Claresta.py",
    title="029_Vania Claresta",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/048_Fadil Prasetyo Alfarizzi.py",
    title="048_Fadil Prasetyo ALfarizzi",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/003_Rahma Oktavia Albar.py",
    title="003_Rahma Oktavia Albar",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/116_Muhammad Naufal Al Ghani.py",
    title="116_Muhammad Naufal Al Ghani",
    icon=":material/person:",
)

#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12] ,
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()
#if state adalah logic di mana kita bisa berpindah-pindah page tanpa data-data kita ini hilang atau berubah
#Halaman utama akan menampung homepage
#Buku Kating akan menampung Nama mahasiswa
#try me akan menampung kreasI dan kreasII
