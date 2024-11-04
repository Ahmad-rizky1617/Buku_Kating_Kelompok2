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
                "kesan": "Suasana wawancara terasa chill dan banyak pelajaran yang bisa diambil, abang keren bangett!",
                "pesan": "Keep up the good work, abangg! Semoga selalu berhasil dalam apapun yang dikerjakan",
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
                "pesan": "semangat bang kuliahnya, semoga abang dan keluarga diberi kesehatann", 
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
            "https://drive.google.com/uc?export=view&id=1jOSxiOvVc0fz5ZbIw0KiS6lVLJLpdJT-",
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
                "kesan": "Abang sangat profesional dalam menjawab pertanyaan, kami belajar banyak dari itu",
                "pesan": "Semoga semangat abang terus menular ke orang-orang sekitar, sukses selalu!",
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
                "kesan": "Kakak memberikan wawasan yang menarik mengenai SSD, kerennnn",
                "pesan": "Semoga kakak selalu sukses dan menggapai impian", 
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
            "https://drive.google.com/uc?export=view&id=1uIYnLAPLpoIMU4BlD8M16EirqNoNYuCb",
            "https://drive.google.com/uc?export=view&id=1tp2pviTBGQZPh_rYT3Cdlq68OoDfSQ7x",
            "https://drive.google.com/uc?export=view&id=1uK36HMYsuK9ZatbJUzgJbhh2-5IWzypN",
            "https://drive.google.com/uc?export=view&id=1u8kNlV-jQfOLehRpKHyY51Uwa-z--oNp",
            "https://drive.google.com/uc?export=view&id=1uQgBbFOAXRonvdW1RKN5JxHIJIk52ib3",
            "https://drive.google.com/uc?export=view&id=1uMyzGq66Ts9lqioUZNfqHF-r20eNalow",
            "https://drive.google.com/uc?export=view&id=1uNK0wWHTdx8f77m0-nRxSORT20rQbjm9",
            "https://drive.google.com/uc?export=view&id=1uCmZljm8iuB8YPG86jAUdmiZb6cGCagg",
            "https://drive.google.com/uc?export=view&id=1u8RRPYrCQlWlTVSJ0z5Acim8-5UUvGI3",
            "https://drive.google.com/uc?export=view&id=1uAl9IhFopxn75TP1L2QpZGXX6NoSz9LS",
            "https://drive.google.com/uc?export=view&id=1ukNFVwtZpUSQibvJKLS-nnY84TXBC5y4",
            "https://drive.google.com/uc?export=view&id=1uYDOFu3S86t4bqyrkKFVIYqIG177JxMh",
            "https://drive.google.com/uc?export=view&id=1tfCQHYgWYeP5-MLnsl7C_rxE6N6C_QxU",
            "https://drive.google.com/uc?export=view&id=1tsr_Fgo1GxxSHUM_HmPo-kDA6kMcUwRU",
            "https://drive.google.com/uc?export=view&id=1uUeKFpryY-_FNDrkn8UzUohGlrAY0Tpn",
            "https://drive.google.com/uc?export=view&id=1trxAIDmrWRc02CXdxwrMrsPwUQ0lYd48",
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
            {
                "nama": " Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya cantik dan cocok jadi panutan",
                "pesan": "Semoga kakak sehat selalu", 
                "jabatan" : "Kepala Divisi Kaderisasi", # 1
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang keren dan mampu memotivasi kami",
                "pesan": "Semoga abang selalu sukses dan bahagia dimasa depan", 
                "jabatan" : "Kepala Divisi Olahraga dan Perlombaan", # 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "JL. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abang menjawab pertanyaan dengan gaya yang asik, bikin senang bertanya",
                "pesan": "Semoga harapan dan impian abang segera tercepai", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main game",
                "sosmed": "@kemasverii",
                "kesan": "Abangnya membawa energi positif selama wawancara, sehingga jadi penuh motivasi dan insight baru",
                "pesan": "Makasih banyak bang, semoga makin sukses dimasa depan", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "Kakak kok bisa cantik bangett",
                "pesan": "Jaga kesehatan ya kak, semoga menjadi orang sukses dimasa depan", 
                "jabatan" : " Bendahara Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak selalu menunjukkan semangat yang tinggi",
                "pesan": "Semoga kakak diberkahi keberhasilan dalam segala hal", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Abangnya keren dan asik diajak ngobrol",
                "pesan": "Semangat terus ya bang, semoga langkah kedepannya makin gemilang", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kakak sangat baik dan cantik, memberikan ruang bagi kami untuk berbicara dan mengekspresikan pendapat",
                "pesan": "Semoga kakak terus berkarya dan sukses dalam setiap hal yang ditekuni", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak tampak tegas namun tetap terlihat sosok yang baik dan easy-going",
                "pesan": "Makasih ya kak, teruslah semangat dan menjadi sosok yang inspiratiff, sukses selalu kakk", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": " 122450001",
                "umur": "20",
                "asal": " Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "Wawancaranya terasa fun dan informatif, kakak bisa ngejelasin dengan cara yang terbaik",
                "pesan": "Semoga kakak dan keluarga tetap sehat selalu, jangan lupa ya tersenyum kak jadi bikin terlihat banget cantiknya", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Abangnya menghargai setiap pertanyaan kami dan memberikan jawaban yang membantu",
                "pesan": "Terimakasih bang atas insight yang berharga, semoga selalu diberi kemudahan dan kesuksesan", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "1224500418",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "Kakaknya cantik, tegas, memberikan kami wawasan yang luas",
                "pesan": "Semangat kak, semoga segala yang dicita-citakan tercapai", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "Gede Moena",
                "nim": " 121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abangnya memberikan kesan yang positif dan supportif selama wawancara",
                "pesan": "Terimakasih ya bangg, semoga kesuksesan selalu menyertai abang", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
             {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": " Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakaknya hebat ya, cantik dan jago dalam bidang olahraga",
                "pesan": "Semoga kakak terus berkembang dan sukses disemua bidang yang ditekuni", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
             {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abangnya baik dan bikin wawancara jadi fun dan banyak yang dapat dipelajari",
                "pesan": "Makasih banng atas waktunya, semoga menjadi orang yang sukses dan berguna dimasa depan", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
             {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakaknya baik dan ramahh",
                "pesan": "Semoga terus menginspirasi ya kak dan meraih kesuksesan dimasa depan", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ] 

        display_images_with_data(gambar_urls, data_list)

    PSDA()
elif menu == "Departemen MIKFES":

    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lV-RdEOoOJYvekVHjJjL2snLN9LaI8gO",
            "https://drive.google.com/uc?export=view&id=1l1RMq7-rJCZEX1fkhekIlptiimL2181D",
            "https://drive.google.com/uc?export=view&id=1lSgUfHB8Zwce_UDLT1FBJYACZFUgfv1G",
            "https://drive.google.com/uc?export=view&id=1lVnx6KdQ89ASX5dxOlDjFApy5qE6eApV",
            "https://drive.google.com/uc?export=view&id=1lK1AjUWM-Qr9IgagHAGyGnnrYnXgHaLp",
            "https://drive.google.com/uc?export=view&id=1krHCCFIFSy1iDaWXKl771aQLt7ItuFJg",
            "https://drive.google.com/uc?export=view&id=1lUMjvMXVVuHK6ZO7UP3ccG6dR8ZPh6pW",
            "https://drive.google.com/uc?export=view&id=1l9aHR9aDB0TrEBdI5TXwDX0LDUxcOEE0",
            "https://drive.google.com/uc?export=view&id=1l5dYNponkiVPGTFcL3T31EU8pFhuJ9NQ",
            "https://drive.google.com/uc?export=view&id=1ko_xa22CQeFIGQAUYaCBFeX4OrfXol-y",
            "https://drive.google.com/uc?export=view&id=1lA7qRtXA0H0-TapcxGk8HsxzC0j20t_f",
            "https://drive.google.com/uc?export=view&id=1l2XCQaOrqQXTuLRJWdhvI9kXAGgmtCSE",
            "https://drive.google.com/uc?export=view&id=1l_lrGK-atn1eph5qddkxvzqrgEcEA5u2",
            "https://drive.google.com/uc?export=view&id=1lv1-5Jo3uoQaECjwZaudC1Yo4kJMxRdS",
            "https://drive.google.com/uc?export=view&id=1lfn0hLtnjfWl4-pmWSXkLVILJlGriOmD",
            "https://drive.google.com/uc?export=view&id=1l1ov9aNjESpFGPDIizFDiMl_mEufFukk",
            "https://drive.google.com/uc?export=view&id=1lshn0H45NPkzxood-9KFixXMtgYjJ4W9",
            "https://drive.google.com/uc?export=view&id=1le2d-NTsmjEuABKI9pwCsWnIb-xVTy4n",
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "Penjelasan abang jelas dan inspiratif, kami jadi lebih paham tentang peran di organisasi",
                "pesan": "Terima kasih atas waktu abang! Semoga selalu sukses dan bahagia",
                "jabatan" : "Kepala Departemen Mikfes", #1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakaknya sangat profesional dalam menjawab pertanyaan kami, memberikan inspirasi yang berarti",
                "pesan": "Terima kasih atas wawancara yang menyenangkan, sukses selalu kakak di langkaah berikutnya", 
                "jabatan" : "Sekretaris Departement", # 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang memberikan banyak insight baru dan sudut pandang yang berguna untuk ke depan",
                "pesan": "Semoga karier abang kedepannya terus cemerlang!", 
                "jabatan" : " Staff Divisi Club dan Komunitas", # 1
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abang memberikan wawasan yang menarik mengenai organisasi",
                "pesan": "Terima kasih atas sharing-nya, semoga semua rencana abang tercapai", 
                "jabatan" : "Staff Divisi Club dan Komunitas", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame ",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Abang memberikan perspektif yang sangat fresh dan membantu kami memandang sesuatu dari sudut pandang baru.",
                "pesan": "Terima kasih atas wawancaranya yang bermanfaat, semoga sukses selalu abang", 
                "jabatan" : "Staff Divisi Club dan Komuitas", # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakaknya terlihat baik dan ramah",
                "pesan": "Semoga kakak terus sukses dan dapat menggapai semua tujuan dengan lancar", 
                "jabatan" : "Staff Divisi Club dan Komunitas", # 1
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Abang mampu membuat suasana wawancara menjadi lebih santai tapi tetap serius",
                "pesan": "Terima kasih abang, semoga terus sukses dan menginspirasi banyak orang", 
                "jabatan" : "Kepala Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abang menunjukkan sikap profesional yang patut kami contoh dalam wawancara ini",
                "pesan": "Terimakasih abang atas waktunya, semangat terus ya bangg", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakaknya baik dan bisa memberikan tanggapan yang relevan",
                "pesan": "Sukses selalu kakak! Semoga terus menjadi sosok yang menginspirasi", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "-",
                "sosmed": "@dindanababan_",
                "kesan": "Waww.. kakaknya cantik dan ramah",
                "pesan": "Semoga kakak selalu sukses dan bahagia dalam segala aspek kehidupan", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurna",
                "sosmed": "@marletacornelia",
                "kesan": "Selain cantik, kak Marleta juga pinterrr.. kami kenal kakak dari saat jadi tutor matdas TPB 2",
                "pesan": "Semoga kakak terus berkembang dan sukses dibidng yang ditekuni", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak bisa ngejaga suasana wawancara tetap asik dan seru. Salut banget!",
                "pesan": "Makasih banyak kakak, semoga terus sukses dan bahagia!", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " 121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Ngobrol sama abang bikin wawancara jadi fun tapi tetap dapet banyak pelajaran",
                "pesan": "Sukses terus ya abang, semoga apa yang abang inginkan segera tercapai", 
                "jabatan" : "Kepala Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "abangnya baik dan ramah",
                "pesan": "semoga selalu sukses dan inspiratif bang! Tetap memotivasi kami ya", 
                "jabatan" : "@egistr", # 1
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Wawancara sama abang rasanya kayak ngobrol santai tapi penuh makna, top deh!",
                "pesan": "Semoga abang terus diberikan kemudahan dan sukses dalam setiap langkahnya", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kehadiran kakak memberi kesan tenang dan mendengarkan kami dengan baik",
                "pesan": "Terima kasih banyak, kakak! Semoga sukses selalu dan tetap menjadi sosok yang inpiratif", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
             {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Serasa ngobrol santai, tapi jawaban abang tetap berbobot dan inspiratif!",
                "pesan": "Semoga abang terus sukses dan bisa menggapai semua mimpinya, cheers!", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
             {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abang keren banget, setiap jawaban bikin kita makin ngerti dan termotivasi",
                "pesan": "Semoga abang terus berkarya dan sukses dalam setiap hal yang ditekuni!", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    mikfes()
elif menu == "Departemen Eksternal":

    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fIX1l144eQOFxCpD7OzMY-5c_GBLZhjr",
            "https://drive.google.com/uc?export=view&id=1fHzStOB95NVDZ_8PoMBan6asxk6xW17P",
            "https://drive.google.com/uc?export=view&id=1g3Ie7kaCqPXb9y-UFYA9WpNv6460eT08",
            "https://drive.google.com/uc?export=view&id=1sCvDnmjoO-JH4Y6FSpO3RSRPpAKgMYw6",
            "https://drive.google.com/uc?export=view&id=1ftTqVMoAtzLnwm5Yz4xk_5yTBhSHvnV7",
            "https://drive.google.com/uc?export=view&id=1fnO8Zz7wSymUWS7UJRqqeD1UUoe9aXeH",
            "https://drive.google.com/uc?export=view&id=1sOxLWAIfk936PRsgXxHG7V8Q-F2xpp9a",
            "https://drive.google.com/uc?export=view&id=1n4FYwyr7sf81G2BX68-Xtfq7v0vHpNH2",
            "https://drive.google.com/uc?export=view&id=1fkznAIZ6zSq198w4dewh5X_oBX5kq3k3",
            "https://drive.google.com/uc?export=view&id=1fvxakO8zI6qnmzdKSmQxzUqeHCopcNhx",
            "https://drive.google.com/uc?export=view&id=1sHwmaY_xlU_Vyi7JEOHqKcab7dgzON7a",
            "https://drive.google.com/uc?export=view&id=1mxT_RdQ0465EZoQb7qhx-0vLYNxGO0Lf",
            "https://drive.google.com/uc?export=view&id=1fBJPg8g7aZa5ipLnLj27WLXLTElLaPjA",
            "https://drive.google.com/uc?export=view&id=1sOurhvA8S8Ddj6NFPL68drUb7Pfkg3SG",
            "https://drive.google.com/uc?export=view&id=1s4IBY0sUG1mjQ1hTmrDi6WF62jyxqbvj",
            "https://drive.google.com/uc?export=view&id=1fD01spP_l5st1sxig9YZBAzr_XqJ5O6_",
            "https://drive.google.com/uc?export=view&id=1mz6kTyChoOdZyJmJW7mLV-g4a_Dib18k",
            "https://drive.google.com/uc?export=view&id=1n0O60Mhmtb3R7kV5EqIzFMWYaUmsgY_N",
            "https://drive.google.com/uc?export=view&id=1f5gzCe8Fl0JyVjD03MMbQh1aj0n20k1L",
            "https://drive.google.com/uc?export=view&id=1f1N5JlTFUowAAXUWdkkSXjR7LEJDP1n2",
            
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "BAB setiap jam 7 pagi",
                "sosmed": "@yogyst",
                "kesan": "Sumpah, abang humble banget pas wawancara. Seru tapi tetap insightful!",
                "pesan": "Thanks abang, sukses terus ya, semoga makin banyak inspirasi yang abang sebarkan!",
                "jabatan" : "Kepala Departemen Eksternal", #1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakak selalu fokus mendengarkan, membuat kami merasa dihargai",
                "pesan": "Semoga kakak selalu sukses dan terus berkembang dalam segala hal!", 
                "jabatan" : "Sekretaris Departement", # 1
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya asikk bangett",
                "pesan": "Semangat dalam berkarya kakk", 
                "jabatan" : "Kepala Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Jawaban abang relate banget sama pengalaman kita, bikin wawancara jadi lebih nyambung",
                "pesan": "Makasih banyak abang, semoga selalu sukses dan inspiratif!", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak Dea daplokku yang terbaikkkk",
                "pesan": "Keep up the good work, kakak! Semoga selalu berhasil dalam apapun yang dikerjakan", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kakak easy-going banget pas wawancara, bikin kita nyaman buat nanya-nanya lebih banyak",
                "pesan": "Thanks a lot kakak, semoga makin sukses dan bahagia di masa depan!", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Jawaban kakak bikin wawancaea ini jadi pengalaman yang seruu",
                "pesan": "Makasih banget kakak cantik, sukses terus kedepannya", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Wawancara bareng kakak seru banget! Jawabannya bikin kita makin semangat buat belajar",
                "pesan": "Makasih banyak kakak, semoga sukses terus dan makin kece di segala hal!", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Seru banger ngobrol sama kakak, bawaannya santai tapi sarat makna!",
                "pesan": "Semoga terus sukses dan makin bersinar dimasa depan kak!", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya asik, jawabannya jelas dan bikin suasana wawancara jadi enjoy",
                "pesan": "Semoga lancar terus dan makin sukses dijalan yang ditempuh!", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
             {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakaknya tegas dan kerenn",
                "pesan": "Terima kasih atas waktunya, semoga hidup dan karier kakak kedepannya makin cemerlang", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
             {
                "nama": "Rizky Adrian Bennovry",
                "nim": "1214500731",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Wawancara seru banget, abang bikin suasana jadi cair dan informatif!",
                "pesan": "Semoga abang terus sukses dan selalu memberikan yang terbaik di setiap kesempatan", 
                "jabatan" : "Kepala Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Energi positif dari abang bikin wawancara jadi penuh motivasi dan insight baru",
                "pesan": "Semoga terus sukses dan selalu membawa vibe positif ke mana pun pergi!", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Jawabannya kakak jelas tapi bikin suasana wawancara jadi enjoy",
                "kesan": "Jawabannya kakak jelas dan bikin suasana wawancara jadi enjoy",
                "pesan": "Tetap inspiratif dan terus berkembang kakk", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "",
                "pesan": "Tetap pertahankan semangat yang berkobar itu kak", 
                "kesan": "Kakaknya terlihat baik dan ramah",
                "pesan": "Semoga kakak terus sukses dan dapat menggapai semua tujuan dengan lancar", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan", 
                "kesan": "Keren banget bang dan baik hati",
                "pesan": "Jangan lupa istirahat dan semangat bang", 
                "kesan": "Abang keren banget bang dan sangat ramah",
                "pesan": "Sehat selalu bang", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Baik, humble sekali kakk",
                "pesan": "Tetap pertahankan akademiknya kakakk", 
                "kesan": "Baik, kemudian kakaknya asikk",
                "pesan": "Sukses selalu ya kak, semangattt", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": " Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Baik hati dan namanya bagus sekali kak",
                "pesan": "Sukses selalu kakk", 
                "kesan": "Kakaknya cantik dan baikk",
                "pesan": "Semoga semua impiannya tercapai kakk", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Raid Muhammad Naufa",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Baik dan sangat memberi motivasi bang",
                "pesan": "Bahagia selalu bang", 
                "kesan": "Energi positif dari abang bikin wawancara jadi penuh motivasi",
                "pesan": "Semoga abang dan keluarga sehat selalu", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": " @tria_y062",
                "kesan": "Baik dan ramahh",
                "pesan": "Semangat kak dalam menjalani seluruh kegiatan ", 
                "kesan": "Kakaknya cantik bangett ",
                "pesan": "Semangat ya kakak, semoga tetap sehat selalu", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    eksternal()
elif menu == "Departemen Internal":

    def internal():
        gambar_urls = [

            "https://drive.google.com/uc?export=view&id=1ojoInjvKyT3i9s7EydPC_bRlO7V2w3at",
            "https://drive.google.com/uc?export=view&id=1pK4p48mPu6UH77c2Z6wR2Yfquv_PLxL4",
            "https://drive.google.com/uc?export=view&id=1ojw6xvPR12m27LZBaQy0lizKsZ-UFZEJ",
            "https://drive.google.com/uc?export=view&id=1pJIfLwNNmMVa5ZZgdNQhmyIOBBYiPwB3",
            "https://drive.google.com/uc?export=view&id=1pXeMvn5ySwHNbe9j-9JMnh3u62RO6t76",
            "https://drive.google.com/uc?export=view&id=1ovlPGJ8yiX5xfg021v_-h3NBFCUvQOTi",
            "https://drive.google.com/uc?export=view&id=1orGbJ6qdGcxCv35Ke5X27bjfS5q_MnIa",
            "https://drive.google.com/uc?export=view&id=1p5M-eLTH-UtfaZP3eS9mfgQCLMvQH6rY",
            "https://drive.google.com/uc?export=view&id=1p068oSqiKHAIfaokQxp2-Hf5wmRKIdyD",
            "https://drive.google.com/uc?export=view&id=1pOnM9zYgjfAa_AMOPqHLAhT9Y-8h_vjs",
            "https://drive.google.com/uc?export=view&id=1pP4ZNsMRNY3BUedcW_OMmRPqGVQN8WWs",
            "https://drive.google.com/uc?export=view&id=1p_WzCByxNaxDIouBnGs9CJRB5lFFLkD3",
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "menunggu ayam jantan bertelur",
                "sosmed": "@dimzrky_",
                "kesan": "Keren banget bang, cara menjawab pertanyaanya bagus banget",
                "pesan": "Selalu jadi orang yang rendah hati bang walaupun ntar udah sukses",
                "jabatan" : "Kepala Departemen Internal", #1
            },
            {
                "nama": "Cathrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": " Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Baik sekali kakaknya dan jugaa ramah, oh iyaa kakaknya juga cantikkk",
                "pesan": "Semoga semua impian dan harapan kakak segera tercapai", 
                "jabatan" : "Sekretaris Departemen Internal", # 1
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Abangnya ramah dan kerenn",
                "pesan": "Teruslah menjadi inspirasi buat orang-orang disekitar abangg", 
                "jabatan" : "Kepala Divisi Keharmonisasian", # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakak cantik dan terlihat kalem, cakeppp",
                "pesan": "Sukses terus ya kakk", 
                "jabatan" : "Staff Keharmonisasian", # 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakak bikin suasana wawancara jadi asikk",
                "pesan": "Semoga kakak dan keluarga sehat-sehat selalu yaa", 
                "jabatan" : "Staff Keharmonisasian", # 1
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abang asik banget waktu memberi jawaban, nggak kaku dan bikin wawancara jadi enjoy",
                "pesan": "Semoga abang makin sukses dan bahagia di masa depan", 
                "jabatan" : "Staff Keharmonisasian", # 1
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Abangnya keren dan bikin wawancara ini jadi pengalaman yang seruu",
                "pesan": "Sehat selalu bangg", 
                "jabatan" : "Staff Keharmonisasian", # 1
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abangnya keren dan pastinya jago futsal yaa, kerenn!",
                "pesan": "Semangat terus ya bangg", 
                "jabatan" : "Kepala Divisi Kerohanian", # 1
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Abangnya baik dan ramah, top deh!",
                "pesan": "Semoga selalu sukses dan menjadi inspiratif abangg", 
                "jabatan" : "Staff Kerohanian", # 1
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Energi positif dari kakak bikin wawancara jadi penuh motivasi",
                "pesan": "Semoga hidup dan karier kakak kedepannya makin cemerlangg", 
                "jabatan" : "Staff Kerohanian", # 1
            },
             {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kakaknya kalem udah gitu cantikkk jugaa",
                "pesan": "Sehat selalu yaa kakak cantikk", 
                "jabatan" : "Staff Kerohanian", # 1
            },
             {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Abang daplok yang baikkk, toppppppp bangett hehe",
                "pesan": "Semangat terus ya bangg, semoga impiannya segera tercapai!", 
                "jabatan" : "Staff Kerohanian", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    internal()
elif menu == "Senator":

    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nxO4F6LZ4RRvVevZbefJGpqJxx3OSD4U",
            "https://drive.google.com/uc?export=view&id=1ntgjq9vNFy5GoDJ0v3W6mBv_Y5-Oj9Yi",          
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": " 121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "Keren banget kakk, wawancaranya jadi seruu",
                "pesan": "Semangat kakk, semoga kakak dan keluarga bahagia teruss",
                "jabatan" : "Senator", #1
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "12245009",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang bisa ngejaga suasana wawancara tetap asik dan seru. Salut banget!",
                "pesan": "Makasih banyak abang, tetap keren dan sukses terus kedepannya!", 
                "jabatan" : "Tim Senator", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    senator()



# Tambahkan menu lainnya sesuai kebutuhan
