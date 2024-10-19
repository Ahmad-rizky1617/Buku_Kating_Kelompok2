import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "MedKraf"
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill"

        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nrkqHjYXezmjvPqWMoW3zlKpvaoFZnSj",
            "https://drive.google.com/uc?export=view&id=1ncxpNR-SCF9FKEeY4JInjEBmDvY1b-VA",
            "https://drive.google.com/uc?export=view&id=1nPBOX0ccPNoJ8JXr4L6H4iE_f6-HZ0rs",
            "https://drive.google.com/uc?export=view&id=1njQ07oHo4zKhKA3IoZNuud5W5kHBKH8i",
            "https://drive.google.com/uc?export=view&id=1nszby9pGxEtRoDBcaHfJodIvhg8QdeEw",
            "https://drive.google.com/uc?export=view&id=1nV-oCnARcdI6RtdQOt7JtxDlmzf3yulC",
        ]
        data_list = [
    
                {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Denger Musik",
                "sosmed": "@gumilangtkharisma",
                "kesan": "Keren banget bang suka sama pengalamannya",
                "pesan": "Sehat sehat bang",
                "jabatan" : "Ketua himpunan",  # 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Imut banget kak, kayak masih angkatan 23",
                "pesan": "Semangat kak kuliahnya, jangan lupa tersenyum",  
                "jabatan" : " Sekretaris Umum" # 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Denger Musik",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya ramah dan kalem",
                "pesan": "Semangat terus kak, bahagia selalu",
                "jabatan" : "Bendahara umum",  # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": " 121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@nadillaandr26",
                "kesan": "Abangnya keren saat berbicara",
                "pesan": "semangat bang kuliahnya, tetap keren selalu", 
                "jabatan" : "Sekretaris Jendral", # 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh, Sumatra Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak menunjukkan sikap ramah yang membuat kami nyaman bertanya",
                "pesan": "Sukses selalu kak", 
                "jabatan" : "Sekretaris 1", # 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "1214500030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Baca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak sangat ramah dan menyenangkan diajak bicara",
                "pesan": "Tetap bersinar dan menginspirasi untuk kami",  
                "jabatan" : "Bendahara 1", # 1
            },


        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jpoiGEBUMYphrldRzDERfX8rLFWU08F2",
            "https://drive.google.com/uc?export=view&id=1kDsaXk0KWuwHoVT_6Cfh0b0dUcAlQyCF",
            "https://drive.google.com/uc?export=view&id=1kI7C-zH5M1u3UjPvd1WivOyGwKanFDfZ",
            "https://drive.google.com/uc?export=view&id=1ju5DoIJjrlX7sQGrn0xjYs7JvFFIHSzk",
            "https://drive.google.com/uc?export=view&id=1jyiMTZNg_Y6Dtw2_qgjNoMaaw35B2QvT",
            "https://drive.google.com/uc?export=view&id=1k4A9781pbIwrEdboNplbbwnH5LwVX1mk",
            "https://drive.google.com/uc?export=view&id=1kMuJaugiqO0BsyE0T_8xy4hS4Y28wEuA",
            "https://drive.google.com/uc?export=view&id=1kmtIn59WJw_wmAnU4v3p5pC-4hKobWxP",
            "https://drive.google.com/uc?export=view&id=1k_z0ZUk2gwXjk3y5vlyWbQlv7gYjVe0n",
            "https://drive.google.com/uc?export=view&id=1kBZEqjxWlVDiH4RieL8VG7v6oCfflq8K",
            "https://drive.google.com/uc?export=view&id=1kcOoz8WKaIghWx41bkSLfeYfU-BLWzWg",
            "https://drive.google.com/uc?export=view&id=1kK9Fy-LCG6hz8_GDRiV_B0xevs8j9U9C",
            "https://drive.google.com/uc?export=view&id=1k7sCG_pKjGMX-aH-MxV_qOdfOhc1S_yk",
            
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Tanya sama GPT",
                "sosmed": "@trimurniaa",
                "kesan": "Kakak punya energi positif yang menular",
                "pesan": "Terima kasih atas bimbingannya semoga kakak slalu sukses",
                "jabatan" : "Ketua Badan Legislatif", #1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Puasa Senin Kamis",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ramah banget dan inspiratif",
                "pesan": "Tetaplah menjadi inspirasi bagi kami", 
                "jabatan" : "Sekretaris", # 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "wlsbn0",
                "kesan": "Kakak sangat profesional dalam mencari solusi ",
                "pesan": "semangat ya kak terus berkembang di baleg", 
                "jabatan" : "Bendahara", # 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450021",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": " @anisadini10",
                "kesan": "Kakaknya menginspirasi kami dengan sikap pantang menyerah",
                "pesan": "Jangan pernah berhenti memotivasi adik adik", 
                "jabatan" : "Kepala Komisi 1 Legislatif", # 1
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": " @dylebee",
                "kesan": "Kakak selalu menjaga suasana agar tetap positif",
                "pesan": "Teruslah membimbing kami dengan keteladanan yang kakak miliki", 
                "jabatan" : "Kepala Komisi 2 Aspirasi dan Pengawasan", # 1
            },
            {
                "nama": "Muhammad Fachrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Sholat Malam",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang selalu penuh perhatian dan peduli terhadap kami",
                "pesan": "Semoga abang diberi kemudahan dalam mencapai tujuan hidup", 
                "jabatan" : "Kepala Komisi 3 Media Legislatif", # 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kalianda",
                "hobbi": "Membaca Al waqiah setiap magrib",
                "sosmed": " @ansftynn_",
                "kesan": "Kakak selalu sabar meski ditengah tekanan tugas",
                "pesan": "Terima kasih atas pengertian dan perhatian yang kakak tunjukkan", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 1
            },
            {
                "nama": "Feryadi Yulius ",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abang berpikir kritis dan logis dalam memberikan solusi ",
                "pesan": "Semoga abang dijauhkan dari kesulitan", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-Qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak membagikan pengalaman yang bermanfaat",
                "pesan": "Teruslah menjadi sosok yang peduli dan penuh perhatian", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang memberikan arahan dan penuh perhatian",
                "pesan": "Semoga abang terus berkembang", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", # 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20 tahun",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": " @_.dheamelia",
                "kesan": "Kakak sangat inspiratif",
                "pesan": "Semoga kakak bisa tetap menjaga semangat dalam belajar", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", # 1
            },
            {
                "nama": " Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak kelihatan ramah sekali",
                "pesan": "Semangat terus kak, pertahankan akademiknya", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Bilabong",
                "hobbi": "Cerita",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang selalu ceria dan selalu membawa suasana positif",
                "pesan": "Semoga abang selalu berhasil atas semua usaha yang dilakukan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ijyLBfY5zE2WVcCCKZflm2MNT0yeQ1n1", 
            "https://drive.google.com/uc?export=view&id=1j2s0YviSCBSRNpJF6gL0ghwAH-TFeg4V",
            "https://drive.google.com/uc?export=view&id=1jjd9_I6b9LOLheujKSTV3Rc4TnJnbF9i",
            "https://drive.google.com/uc?export=view&id=1ighpvp0iNL22Pg_UqdgL73Cf0JjLcrFf",
            "https://drive.google.com/uc?export=view&id=1jTmZbzJfyfBqZ2uQM4LLTlOFx023hI0q",
            "https://drive.google.com/uc?export=view&id=1j0UZU_x7QW1ega8KE3HfH-4xDQS6bti9",
            "https://drive.google.com/uc?export=view&id=1jMvyg9nv4fmCuq5vY-4Gl3hmT-aeIIvs",
            "https://drive.google.com/uc?export=view&id=1ivbUVA8oC7WwrVpWFhEB1g0bxez41A9o", 
            "https://drive.google.com/uc?export=view&id=1jmty7KBM45FQFjvWD7Cof90pZxzCtjKy",
            "https://drive.google.com/uc?export=view&id=1jJJ3fswMBIdzbCffV_WvehYuBhxcZ9nT",
            "https://drive.google.com/uc?export=view&id=1ioTn3_lvodQ5BGl1fcrsWFPOJcdMegfs",
            "https://drive.google.com/uc?export=view&id=1ioPmWvmnFHPbhD1VuRHyz8E9t9AYikWz", 
            "https://drive.google.com/uc?export=view&id=1iilyLK_YNWLrkXJkdWRd-kllDQjFpMql",
            "https://drive.google.com/uc?export=view&id=1ilSlIjEmorKaXGoCv8_Z6CccooNBauOI", 
            "https://drive.google.com/uc?export=view&id=1ikFCGgSmPA-6M0FGA5M5tCKnwpKsOyxG",
            "https://drive.google.com/uc?export=view&id=1iu3JMoZi34jfDi9_VdLDncER6jb5_5nV",
            "https://drive.google.com/uc?export=view&id=1jOSxiOvVc0fz5ZbIw0KiS6lVLJLpdJT",
            "https://drive.google.com/uc?export=view&id=1igeUrag7PeE7vZd6xds36s0NYWMPFPr2",
            "https://drive.google.com/uc?export=view&id=1jnmvcaSHXHq_LvpMTFjo09HPB1kTc6xa",
            
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "",
                "kesan": "Kakak sangat terbuka dalam menerima kritik dan saran",
                "pesan": "Semangat terus bang dalam menjalani hari",
                "jabatan" : "Kepala Departemen", #1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakaknya manis banget ada lesung pipi",
                "pesan": "Semangat kak tetap ramah dan baik hatinya", 
                "jabatan" : "Sekretaris", # 1
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakaknya baik, semua pertanyaan terjawab dengan baik",
                "pesan": "Bahagia terus kak, semoga cepat lulus", 
                "jabatan" : "Kepala Divisi Media & Konten", # 1
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": " 121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": " @dino_kiper",
                "kesan": "Abangnya asik ketika diajak berbicara",
                "pesan": "Tetap semangat dalam menjalani hari bang", 
                "jabatan" : "Kepala Divisi PDD", # 1
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Abangnya selalu menjawab pertanyaanku dengan baik",
                "pesan": "Tetap semangat dan bahagia selalu bang", 
                "jabatan" : "Kepala Divisi Visual Desain", # 1
            },
            {
                "nama": "Cintya  Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Cantik banget dan inspiratif banget kakaknya",
                "pesan": "Selalu menjadi orang yang inspiratif kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " 122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakaknya asik diajak ngobrol",
                "pesan": "Tetap semangat dan selalu menginspirasi adik adik", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakak memotivasi aku untuk menjadi orang yang lebih baik",
                "pesan": "Terus memotivasi kami kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Patricia Leondra Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya keren banget jadi pj datafact",
                "pesan": "Tetap semangat menjalani hari hari", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakak selalu menjawab dengan baik selama kami bertanya tentang pengalaman kakak",
                "pesan": "Tetaplah menjadi sosok yang rendah hati", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak berwawasan luas ",
                "pesan": "Jangan pernah lelah dalam membagi ilmu kepada kami ", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak hebat bangett dan cantikk",
                "pesan": "Senyum selalu kakakku", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Abang konsisten dalam memberikan arahan dan nasihat",
                "pesan": "Abangnya semoga diberi kesehatan dan kekuatan ", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
            {
                "nama": "Nasywa Nur Afifah ",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kakak selalu hadir dengan solusi yang kreatif",
                "pesan": "Tetaplah rendah hati meskipun sudah sukses", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "kami kagum dengan kemampuan abang dalam mengatur waktu dengan baik",
                "pesan": "Semoga abang tetap membantu dan memotivasi semua orang", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Sikap abang yang sabar membuat kami merasa percaya diri",
                "pesan": "Semoga apa yang abang cita citakan segera tercapai", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Hermawan Manurung ",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani) ",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang baik dalam memberikan panduan",
                "pesan": "Jangan berhenti berbagi ilmu dan pengalaman ya bang", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakak menginspirasi dan sikap yang tangguh",
                "pesan": "Tetaplah menjadi kakak yang ceria", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakak selalu mendukung kami untuk berfikir kritis",
                "pesan": "Tetaplah tegar dan semangat menjalani setiap tantangan", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    medkraf()

elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oUzY4PA4L2_o5drOmXLLNH6osN47zvoV",
            "https://drive.google.com/uc?export=view&id=1oWRyJ_rM9YciqSm4flXIF57LT9uk2kQ7",
            "https://drive.google.com/uc?export=view&id=1o0CKVH7Pk1yh8dVVe_KIVaRYa1fYh56E",
            "https://drive.google.com/uc?export=view&id=1oV14YaO1DwN_csZRA56cuU3MqXPtPxe1",
            "https://drive.google.com/uc?export=view&id=1oEMhBFTXY7fYebLDNs2pUfkKfi6M-BRa",
            "https://drive.google.com/uc?export=view&id=1nyl5ZPfYtNS4U6hGHGwky2RKxqzzGqqx",
            "https://drive.google.com/uc?export=view&id=1oWnXdcVzv33IYPgeJSIrRhCgcxk-6BJg",
            "https://drive.google.com/uc?export=view&id=1oRiZc9fjtk8jLOQDivoOnSUcJIm8WsRL",
            "https://drive.google.com/uc?export=view&id=1oZg4T6GRazY0Mdbgu0oK2fZz1egWZwTa",
            "https://drive.google.com/uc?export=view&id=1oP9EcYyK04sxqEtYmuRkHHYmglsbT-dm",
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumbangaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abangnya keren banget",
                "pesan": "Tetaplah menginspirasi kami bang",
                "jabatan" : "Kepala Departemen SSD", #1
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak selalu menunjukkan semangat yang tinggi",
                "pesan": "Semoga kakak diberkahi keberhasilan dalam segala hal", 
                "jabatan" : "Sekretaris Departemen SSD", # 1
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kakak selalu menjaga suasana agar tetap positif",
                "pesan": "Semoga kakak sukses di masa depan", 
                "jabatan" : "Kepala Divisi KWU", # 1
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Abang sangat konsisten dalam memberikan arahan dan nasihat",
                "pesan": "Semoga abang dikelilingi oleh orang-orang yang mendukung", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": " 122450110",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Abang disiplin dan memotivasi kami untuk disiplin juga",
                "pesan": "Semoga abang terus sukses di masa depan", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukitting",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang selalu berusaha membuat suasana nyaman dan kondusif",
                "pesan": "Jangan pernah ragu untuk terus belajar dan berbgi ilmu", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak sangat kreatif dan imut",
                "pesan": "Jangan lupa ibadah ya kak", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak selalu membagikan pengalaman yang bermanfaat",
                "pesan": "Terimakasih atas bimbingan dan motivasinya", 
                "jabatan" : "Kepala Divisi Sponsor", # 1
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kakak sangat bijak dalam menghadapi situasi sulit",
                "pesan": "Jangan pernah berhenti memberikan contoh yang baik", 
                "jabatan" : "Staff sponsor", # 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": " Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang sangat peduli terhadap kami sebagai adik tingkat",
                "pesan": "Semoga abang diberi kemudahan dalam mencapai tujuan hidup", 
                "jabatan" : "Staff sponsor", # 1
            },
           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()

elif menu == "Departemen PSDA":

    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ujbL5d0Ad3qhbG1M5YplaJMBWBSJL3ZJ",
            "https://drive.google.com/uc?export=view&id=1tcsx7sXsQ6nOekF4u4z25kkpbM9ysLDs",
            "https://drive.google.com/uc?export=view&id=1utfER2Un8QhXlzVcbb2mKqzgiIPy1o7V",
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": " Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abang sangat tegas namun tetap bersahabat",
                "pesan": "Terimakasih atas kesabaran dan pengertian yang abang tunjukkan",
                "jabatan" : "Kepala Departemen PSDA", #1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya cantik dan auranya positif",
                "pesan": "Semoga kakak selalu berhasil dalam setiap kesempatan", 
                "jabatan" : "Sekretaris Departemen PSDA", # 1
            },
            {
                "nama": "Deyvan Loxefal ",
                "nim": "121450148",
                "umur": "21",
                "asal": "Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang sangat peduli kepada kami",
                "pesan": "Semoga abang dapat meraih kesuksesan", 
                "jabatan" : "Kepala Divisi Manjakat", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    PSDA()



# Tambahkan menu lainnya sesuai kebutuhan
