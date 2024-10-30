import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown(
    """<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True
)
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
            st.write(f"Jabatah: {data_list[i]['jabatan']}")
            st.write(f"Jabatan: {data_list[i]['jabatan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")


menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":

    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iDw2-D_7WeLM40zVsarzWu1FeKwrTUcr",
            "https://drive.google.com/uc?export=view&id=1iHiCgoiZj-1kWI-gPuizyIUiXvEQGYtW",
            "https://drive.google.com/uc?export=view&id=1iM8QZVqq-FALVLYFYwZOZ97dsBbduxCP",
            "https://drive.google.com/uc?export=view&id=1iGwZPaeRNRY86UHdglqh-jmW7NuFg-JB",
            "https://drive.google.com/uc?export=view&id=1iHZDb4mLiZFgZ6mA7BICOolAqrZ62wFU",
            "https://drive.google.com/uc?export=view&id=1iGorfahlDUagrjffANonVuo_p-etWw8k",
        
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
                "kesan": "best sihh bang gumii",
                "pesan": "Semangat bang gumiii",
                "jabatan" : "Ketua himpunan",  # 1
            },
            {
            
                "nama": "Pandra Insani Putra Azwar",
                "nim": " 121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@npndrinsni27",
                "kesan": "asik bang pandraa",
                "pesan": "semangat banggg", 
                "jabatan" : "Sekretaris Jendral", # 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kak lizaa lucu bangettt",
                "pesan": "doain saya sekum 2025 yaa kak",  
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
                "kesan": "Kakaknya kalem",
                "pesan": "semangat kuliahnya kakk",
                "jabatan" : "Bendahara umum",  # 1
            },
        
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh, Sumatra Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kak putri keren sih",
                "pesan": "semangat kak kuliahnyaa", 
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
                "kesan": "lucuuu",
                "pesan": "semangat kak kuliahnya",  
                "jabatan" : "Bendahara 1", # 1
            },




        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dLp6NuNORbbo_DAsQkyMmFgQ-X0VxwzB",
            "https://drive.google.com/uc?export=view&id=1dAEN_5lquiBVX9VrZUGlC40JKKUSaeDt",
            "https://drive.google.com/uc?export=view&id=1dA1bbomhJHeqntJ9TxEZH5KrIxUF98vf",
            "https://drive.google.com/uc?export=view&id=1d8o73-wKvxzAAqzH3cvnH1ixQfVDau1I",
            "https://drive.google.com/uc?export=view&id=1oaR_27ezt2qm6PK2q0fgiI2hCRaC60R7",
            "https://drive.google.com/uc?export=view&id=1dGNkcQ1twmGFpSECrHQsmkKwQUWyYWZd",
            "https://drive.google.com/uc?export=view&id=1dATFoW8hV1h1-w2hsGngFlTC1bjg-0_d",
            "https://drive.google.com/uc?export=view&id=1dGCt6Yfj09jZx2foOWwk2wb9QnbR0-g8",
            "https://drive.google.com/uc?export=view&id=1d62zk9foJodVO474_DbFMCzjFK5zgLCO",
            "https://drive.google.com/uc?export=view&id=1dHMh8H_p3BmB48otCPmaPnh9urofT0Gj",
            "https://drive.google.com/uc?export=view&id=1dSf71gmRwspe09u1MlRgYVRRJlaaBHAh",
            "https://drive.google.com/uc?export=view&id=1d5Ftnc77LM3FI3p1vg3fFlAnSHubk9tv",
            "https://drive.google.com/uc?export=view&id=1dAZFR2JmNgq7ZYPYgx_7M8P_sUjcVI-K",
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
                "kesan": "Kakaknya cantikkk, humble pula",
                "pesan": "semangat kuliahnya kakak, tetap jadi orang baik",
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
                "kesan": "keren kakaknya",
                "pesan": "Semangat kuliahnya kak", 
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
                "kesan": "Ramah banget kakanya, murah senyum",
                "pesan": "semangat ya kak, tetap ramahh", 
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
                "kesan": "Kakaknya ramahh, asik,baik",
                "pesan": "semangat terus kuliahnya kakak, jangan mudah menyerah", 
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
                "kesan": "Bagus sekali kak namanya, orangnya juga cantik",
                "pesan": "semangat ya kuliahnya jangan putus asa kak", 
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
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
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
                "kesan": "Manis banget kakaknya, ramah juga",
                "pesan": "semangat kuliahnya kak, tetap baik hati kak", 
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
                "kesan": "Abang asprak alpro rb nihh",
                "pesan": "semangat kuliahnya bang, info nilai A", 
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
                "kesan": "MasyaAllah kak pertahankan hobinya",
                "pesan": "Semangat kuliahnya, semoga semakin rajin mengerjakan tugas", 
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
                "kesan": "Abangnya baik, kalem, dan ramah",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", # 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20 tahun",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": " @_.dheamelia",
                "kesan": "Kakaknya kelihatan aktif organisasi bangettt",
                "pesan": "Ramahh banget kak Dheaa", 
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
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
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
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1U5xNc9NBDGwBBmuMrlSacFgbTC_cAIaW",
            "https://drive.google.com/uc?export=view&id=1UvIxovrGWbAKABGwy91G8tnRNosg7p3G",
            "https://drive.google.com/uc?export=view&id=1UOwudL882u2trXykJ8lX3v9kmycNDhf3",
            "https://drive.google.com/uc?export=view&id=1V_dUbAsTjKP0381cPVlKcxhsOnmwRkoj",
            "https://drive.google.com/uc?export=view&id=1UMuPeiuhG7tLATIh-4jc1nUyvkzHl1gV",
            "https://drive.google.com/uc?export=view&id=1UwNBTkipIRuTFrcuusd9fys187-r9iAM",
            "https://drive.google.com/uc?export=view&id=1Ug0kQnx39gtLJjRBB7tYRqybGg2VTw8Y",
            "https://drive.google.com/uc?export=view&id=1UyVaV2siSb5726XGO8lOxAJYI2MDs7Wt",
            "https://drive.google.com/uc?export=view&id=1UMXPhtX1VXRwSexnu-9lMjruisfdx24b",
            "https://drive.google.com/uc?export=view&id=1UgQbT9JWDLmoCuV2tYFdeP4J3uB7UAhK",
            "https://drive.google.com/uc?export=view&id=1VD3Mr2oXgo613QF-IpP6JoWiOFABqKqc",
            "https://drive.google.com/uc?export=view&id=1VQ8dUqi5qNelTXs4rVM0NQ_rsvIMmtNi",
            "https://drive.google.com/uc?export=view&id=1UX4CBmz9wEN0kAZVtr224bO_IU5qnXKB",
            "https://drive.google.com/uc?export=view&id=1VQlgGxKTxIgP3Aej0GrmP_ICovI564yj",
            "https://drive.google.com/uc?export=view&id=1Vbj1UR4DkvlmRmjbBBzz1wBt1qItUchI",
            "https://drive.google.com/uc?export=view&id=1VVf0D9TWCWPO51gRg3MXyaruL3CIDmRI",
            "https://drive.google.com/uc?export=view&id=1Ufg2Jmu6I5vj1DfyAitBgR7CFfc-n-f3",
            "https://drive.google.com/uc?export=view&id=1VPcApBYPkHgazBZ02p0xfFfR7RTTx7Iy",
            "https://drive.google.com/uc?export=view&id=1VLNvY3BZViX_pZqOlXA1H3T-7noWi76X",
          
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
                "kesan": "tegas ya abangnya",
                "pesan": "Sehat-sehat bang",
                "jabatan" : "Kepala departemen", #1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Manis bangett kakk elokk",
                "pesan": "Semangat ya kak, tetap ramah", 
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
                "kesan": "impresif",
                "pesan": "semangatt kakk", 
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
                "kesan": "impresif",
                "pesan": "semangat kuliahnya bangg", 
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
                "kesan": "lucu bang arsal",
                "pesan": "semangat bang kuliahnyaa", 
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
                "kesan": "Suka banget sama outfit kakak, cocok banget di divisi media & konten",
                "pesan": "semangat terus yaa kak", 
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
                "kesan": "kak eka aktif banget dimanapunn",
                "pesan": "semoga sehat selalu yaa kak eka,", 
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
                "kesan": "cantik kakaknya",
                "pesan": "mangat kak", 
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
                "kesan": "cantik pake banget, cheerful",
                "pesan": "tips menjadi orang dengan positive vibes kak", 
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
                "kesan": "ramah sekali daplok kel sebelah ini",
                "pesan": "semangat kak nelii", 
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
                "kesan": "cantik gemas",
                "pesan": "mangat kak dalam hal apapun", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5",
                "hobi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "keren kakaknya",
                "pesan": "Ramahh banget kak", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "keren nama bang gym",
                "pesan": "Ramahh banget bang gym", 
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
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
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
                "kesan": "",
                "pesan": "", 
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
                "kesan": "",
                "pesan": "", 
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
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "",
                "pesan": "", 
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
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
        ]
        
        display_images_with_data(gambar_urls, data_list)

    medkraf()
elif menu == "Departemen_Eksternal":

    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZPy-cZgP8R3PYJTkdUVtQDo7FV06rW5O",
            "https://drive.google.com/uc?export=view&id=1Z6QQaeAdCuBb7ewOm1K-_SZqRrv6TSuW",
            "https://drive.google.com/uc?export=view&id=1ZdlrFQdyBlW8hhOL6GSw5dsI3RB57WkH",
            "https://drive.google.com/uc?export=view&id=1lq3pxgLapsciJ-rcwTsrm4ycUbdoGlIV",
            "https://drive.google.com/uc?export=view&id=1Zq6YrL4BucXR-wG78mhbmPP6b8j9HGte",
            "https://drive.google.com/uc?export=view&id=1ZSaSjIO1FmY1XaNQtiiiLZWLXkE8kP-i",
            "https://drive.google.com/uc?export=view&id=1ZiNM6nbVCwe81WYV3C3-RwZVbDRCKJkB",
            "https://drive.google.com/uc?export=view&id=1iyJT9h3UVcV6TXr3eC3_wSpj3Uep0Cre",
            "https://drive.google.com/uc?export=view&id=1ZeUDL0k5S1Igz7pVEJqYlUi2HvzSCBSU",
            "https://drive.google.com/uc?export=view&id=1ZeqCx-xr6b52yngd3tWfd6scLX7kJumR",
            "https://drive.google.com/uc?export=view&id=1ZjVyNs62huzYOZihUSfoDdRjVxiQqd9T",
            "https://drive.google.com/uc?export=view&id=1gZQE69ZiqrRf0W9Q5spTb8NVLjhbFBVz",
            "https://drive.google.com/uc?export=view&id=1YuxNAgBtafPXABIq5VK9RuBU5i0V6iw6",
            "https://drive.google.com/uc?export=view&id=1YrMPEz70WgldaTyBv7CVofcHJdei6jS4",
            "https://drive.google.com/uc?export=view&id=1lC8Z-45Ku1_9zi9gTpIpuzkbJHIfGtHD",
            "https://drive.google.com/uc?export=view&id=1YreO14zRWqA-tTZlL9kr9ZFV7n-YsVCO",
            "https://drive.google.com/uc?export=view&id=1ZxLytk8eW-BpbsSHu8T9WyPEjqYvV4FC",
            "https://drive.google.com/uc?export=view&id=1ZurnLCfam2QPINAWYgpA8EjJaDqvM0To",
            "https://drive.google.com/uc?export=view&id=1YwfavSaUiCwpiaApv8QzZhVN64PV4qjy",
            "https://drive.google.com/uc?export=view&id=1Z5klKBcfpPSGR4_Ci2MXDzK3ziBWR75s",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "BAB setiap jam 07.00 pagi",
                "sosmed": "@yogyst",
                "kesan": "Abangnya kocag, seru, baik",
                "pesan": "semangat kuliahnya bang, tetap jadi orang baik",
                "jabatan" : "Kepala Departemen Eksternal", #1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakaknya humble",
                "pesan": "Semangat kuliahnya kak", 
                "jabatan" : "Sekretaris Departemen", # 1
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "nazwanbilla",
                "kesan": "Ramah banget kakanya, banyak ketawa, seru",
                "pesan": "semangat ya kak, tetaplah tertawa sebelum tertawa itu dilarang", 
                "jabatan" : "Kepala Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "abangnya ramahh, asik,baik",
                "pesan": "semangat terus kuliahnya bang bass, jangan mudah menyerah", 
                "jabatan" : "", # 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": " @deaa.rsn",
                "kesan": "Kakaknya ramah, orangnya juga cantik, ariess prideee",
                "pesan": "semangat ya kuliahnya jangan putus asa orang sibuk", 
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
                "kesan": "kakaknya pasti jago main golf",
                "pesan": "semangat kuliahnya kak, tetap pertahankan main golfnya", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "surfing",
                "sosmed": " @nateee__15",
                "kesan": "Manis banget kakaknya, ramah juga",
                "pesan": "semangat kuliahnya kak, tetap baik hati kak", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Novelia Adinda ",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya bener-bener cantik banget!",
                "pesan": "semangat kuliahnya kak, semoga makin cantik", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main Sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "MasyaAllah kak pertahankan hobinya",
                "pesan": "Semangat kuliahnya, semoga semakin rajin mengerjakan tugas", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatra Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya baik, kalem, dan ramah",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19 tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobi": "Main Bowling",
                "sosmed": " @yo_annamnk",
                "kesan": "Kakaknya kelihatan aktif organisasi bangettt",
                "pesan": "semangat kak", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": " Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
                "jabatan" : " Kepala Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Abangnya baik sekaliii",
                "pesan": "semangat kuliahnya bang, tetap pertahankan rajin sholat malamnya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya baik",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Quality Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya baik, dulu kakak asprak fisdas 1 aku juga",
                "pesan": "semangat kuliahnya kak ochaa", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatra Barat",
                "alamat": "WSukarame",
                "hobbi": "Nonton Youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik",
                "pesan": "semangat kuliahnya bang, tetap pertahankan rajin sholat malamnya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfiaa",
                "kesan": "kakaknya baik, aktif berorganisasi sekalii",
                "pesan": "semangat kuliahnya kak, tetap pertahankan aktifnya",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Khaalishah Zuhrah Alyss Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanefi",
                "kesan": "kakaknya baik",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin mengajinya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayth_",
                "kesan": "Abangnya baik",
                "pesan": "semangat kuliahnya bang", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": "kakaknya baik",
                "pesan": "semangat kuliahnya kak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
         ]
        display_images_with_data(gambar_urls, data_list)

    Departemen_Eksternal()         

elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZxYjSxJvXaQpJCSOrrj9l5R4fNFq1NyB",
            "https://drive.google.com/uc?export=view&id=1Z1UwUYXccDNvJcIhy3gWxHETD8XIXN2N",
            "https://drive.google.com/uc?export=view&id=1Z6Cj0lFQlJvMnhGwKDC84Ds4ZLnPI7nt",
            "https://drive.google.com/uc?export=view&id=1Zp-bYYcW8QQFQyc9AgYM5TiHgWShC_oo",
            "https://drive.google.com/uc?export=view&id=1ZmNdIBZ-Ga0pjcRlFbH_KTB71UHohjZx",
            "https://drive.google.com/uc?export=view&id=1ZTZEk0YYG4FmPBRt-oIQb8pXxIDX_Ddz",
            "https://drive.google.com/uc?export=view&id=1Z3DNupoW8NwXqMtZMqgXEhi6pJM0gA7t",
            "https://drive.google.com/uc?export=view&id=1_-83adfhy_2eFtczX6bkBkUgXWus1lz9",
            "https://drive.google.com/uc?export=view&id=1KqZulVVX0uh4ObESl9NDh6jEhvvhMOvQ",
            "https://drive.google.com/uc?export=view&id=1ZyeAVuletDxCJ3i__HponLunbMc7H_VY",
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
                "kesan": "Abangnya keren banget suka cari uwank",
                "pesan": "Bang infokan cara mencari uwang dengan cepat tanpa jaga lilin hehehe",
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
                "kesan": "Kakaknya lucu",
                "pesan": "Semoga kakak sukses selaluuu", 
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
                "kesan": "Kakak lucu pake kacamata",
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
                "kesan": "Kakak kelas smandap",
                "pesan": "Semoga tercapai bang jadi kadep ssd hihihi", 
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
                "kesan": "Bang farel keren sih ",
                "pesan": "Semoga abang terus sukses di masa depan", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittingi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang selalu berusaha membuat suasana nyaman dan kondusif",
                "pesan": "Jangan pernah ragu untuk terus belajar dan berbagi ilmu", 
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
                "pesan": "Jangan lupa ibadah ya kak, semangat kak tesaaa", 
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
                "kesan": "Kakaknya gemessss",
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
                "kesan": "Bang dhafin kalo senyum matanya hilang",
                "pesan": "Semoga abang diberi kemudahan dalam mencapai tujuan hidup", 
                "jabatan" : "Staff sponsor", # 1
            },
           

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()

elif menu == "Departemen PSDA":

    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KmDh9Jy2JQeOTcDl-uamOjNDepbn3uvT",
            "https://drive.google.com/uc?export=view&id=1GgMo6T-UJLjHqlO8XyKpYkkEkSPXiVCW",
            "https://drive.google.com/uc?export=view&id=1Fr9A82iOgKV19z6HD_4nrZQfFKgTDme9",
            "https://drive.google.com/uc?export=view&id=1Fabopo00M9QcbHHhFP9N4oXVUVExKC2-",
            "https://drive.google.com/uc?export=view&id=1GQBJzRsWFbv53j5Hsyca9eki4cw9Wi7s",
            "https://drive.google.com/uc?export=view&id=1E52EJ_DYarPgfFsAY5gO1Xe1863UgDOn",
            "https://drive.google.com/uc?export=view&id=1FosrmFZ07dibrMEkqRPGYGvbzYhOmbs6",
            "https://drive.google.com/uc?export=view&id=1G-2YAz_sWiOZMrn1PWReges4G-pubqkn",
            "https://drive.google.com/uc?export=view&id=1FGGT4t4a5h1MJ6Y6VFBxpidfwwW14OKb",
            "https://drive.google.com/uc?export=view&id=1FQriRUNLdUHrs9miU9Isl982zisxyMS3",
            "https://drive.google.com/uc?export=view&id=1FFtlcHU7tZKyFMAkGt0zZSTQHRVE4nwl",
            "https://drive.google.com/uc?export=view&id=1Em6Lfx62JPF88Mx2LIgx8py4slcODgRq",
            "https://drive.google.com/uc?export=view&id=1FZO5VKQD5W6QVdQ8ykkBNcG_u6U3TVHE",
            "https://drive.google.com/uc?export=view&id=1FhFoR5rPqVr7FadKpPM_JbF_NbdlFrEZ",
            "https://drive.google.com/uc?export=view&id=1FN6NAu7EMIkv7VKHNQ_Mtnx2paLnN31J",
            "https://drive.google.com/uc?export=view&id=1F3xMcmAmEYkAweNybWCrE1vno1m9XEW3",
            "https://drive.google.com/uc?export=view&id=1ErXeVWcL3SA2LK6st1_wQ90QlYuRbUDw",
            "https://drive.google.com/uc?export=view&id=1GIYcSm95Na8hyQq2wSAFSSUfc_fiO7Tk",
            "https://drive.google.com/uc?export=view&id=1GDhCR3GiMnnM0HFjhuK3eEGDDdf6V9GS",
            
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
                "kesan": "Bang econ keren banget mindsetnya",
                "pesan": "Makasi bang untuk ilmu-ilmunya, sehagt selalu",
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
                "kesan": "Kak abet lucuu",
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
                "kesan": "bang depan jujur lucu banget orangnya",
                "pesan": "Semoga bang depan sehat terus", 
                "jabatan" : "Kepala Divisi Manjakat", # 1
            },
             {
                "nama": " Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak pipah cantik dan tegas",
                "pesan": "Jangan lupa istirahat kak, jaga kesehatan <3", 
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
                "kesan": "Keren bang sangat memotivasi kami",
                "pesan": "Selalu jadi orang baik yang sangat gemar menolong", 
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
                "kesan": "Keren bang",
                "pesan": "Sehat-sehat bang asprak", 
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
                "kesan": "Bang kemas ini jago ngoding",
                "pesan": "Semakin rajin ya bang belajarnya", 
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
                "kesan": "Kakaknya lucu imut",
                "pesan": "Semangat belajarnya kak, semoga akademiknya emakin meningkat, semoga nilai strukdat saya aman yaa kak hehehe ", 
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
                "kesan": "Baik kakaknya, ramah juga cantikk",
                "pesan": "Semangat kak kuliahnya, sukses selalu", 
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
                "kesan": "Abangnya baik ramah suaranya bagus",
                "pesan": "Semangat kuliahnya bang,bahagia dan sukses selalu", 
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
                "kesan": "Kakak cantikk, sukanya sama stylenya",
                "pesan": "semangatt selalu kakk", 
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
                "kesan": "Kak pashaa ini kating sd pertama yang bisa kenal heheh",
                "pesan": "Semangat kuliahnya kak, semoga segala kebaikan menyertai kakak", 
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
                "kesan": "Kakaknya baik dulu pas asprak baik banget kasih nilainyaa",
                "pesan": "Terus memotivasi kami kak, semangat terus", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Bang riko asik banget",
                "pesan": "Semangat mengejar akademiknya bang", 
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
                "kesan": "Kakaknya baik dan asik",
                "pesan": "Sukses selalu kak dalam segala hal", 
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
                "kesan": "Abangnya ramah dan tidakk sombong",
                "pesan": "Semangat dalam menjalani hari-hari bang", 
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
                "kesan": "Kakak baik, ramah dan rajin olahraga",
                "pesan": "Semoga semakin jago kak renangnya", 
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
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Sehat dan bahagia selalu bang", 
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
                "kesan": "Kakaknya pintar dan baik hati",
                "pesan": "Sukses selalu kak dalam berbagai bidang", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)


    PSDA()
elif menu == "Departemen MIKFES":

    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CD7M8bWFXNnMme4PGQkpUadEm2JwbfIP",
            "https://drive.google.com/uc?export=view&id=1CuJy8LBAO6KR-vEzhrDHNgyfLKy1hp9h",
            "https://drive.google.com/uc?export=view&id=1CPiZlYFndSo9otU0wDhhQaTdpsoyyD27",
            "https://drive.google.com/uc?export=view&id=1C3xkYMJTdErdXhorUvzPhDcrcGTby1a3",
            "https://drive.google.com/uc?export=view&id=1CLwYDmPyjfg756RnhzjY48NfImMpmd_k",
            "https://drive.google.com/uc?export=view&id=1CYc1YEJjrAeopDYb9TRwV8Agwfw9Q1od",
            "https://drive.google.com/uc?export=view&id=1CKcbcXm9odFpM0532j0PYxdgRZNsXx4f",
            "https://drive.google.com/uc?export=view&id=1CNdoBEFDT2_D1pmKTJzFerHV5Zv6BcOt",
            "https://drive.google.com/uc?export=view&id=1C06VdwCVuGq8mDIubMi4TC6z5JmYwgqG",
            "https://drive.google.com/uc?export=view&id=1CmlQ0AXQC336crsMqNd00ulThvi0PgOR",
            "https://drive.google.com/uc?export=view&id=1KrMZKLYSUcE_OBmvyZHdAjK9IBXYqL4c",
            "https://drive.google.com/uc?export=view&id=1CPnET9e4A1W1GuBHZ6JYghfoupdzpWJq",
            "https://drive.google.com/uc?export=view&id=1CzdQMIgKpLlb0qQ1156QQSZZDCdjDBKO",
            "https://drive.google.com/uc?export=view&id=1DFEg1ytsTRCDbXGEg-684sId9vNqsPfL",
            "https://drive.google.com/uc?export=view&id=1CwcyxKEliyj-EKaS2gTuMvtuP444DlJK",
            "https://drive.google.com/uc?export=view&id=1D83jWWJJRZw3WbAKxNCSxU7f_yORwRT0",
            "https://drive.google.com/uc?export=view&id=1DFjpV9X1EiLji4zRl5_dGTEmFnUuwHW_",
           
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
                "kesan": "Penjelasan abang jelas dan inspiratif, kami jadi lebih paham tentang mikfess",
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
                "kesan": "nama kakak kalo disingkat lucu, jadi anova",
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
                "kesan": "Abang auranya emang mikfes banget sihh",
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
                "kesan": "keren sekali mindset abangnyaa",
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
                "kesan": "Kakaknya lucu",
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
                "kesan": "Keren loh bang nathan ini",
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
                "kesan": "bang anwar baik banget udah bantu cosval as pj tugas",
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
                "kesan": "Kakaknya baik dan cantik",
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
                "kesan": "Kak dinda ramah sekali",
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
                "kesan": "Selain cantik, kak marleta juga murah senyum",
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
                "kesan": "Salut banget!",
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
                "kesan": "keren bangg",
                "pesan": "Sehat terus ya abang, semoga apa yang abang inginkan segera tercapai", 
                "jabatan" : "Kepala Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "bang adit ini lucu",
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
                "kesan": "cantik bgt?!",
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
                "kesan": "nama abangnya keren banget",
                "pesan": "be happy bang happy!", 
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
                "kesan": "Abang keren banget, astut tpb 1 duluu",
                "pesan": "Semoga abang terus berkarya dan sukses dalam segala hal, jangan lupa berdoa!", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()

elif menu == "Departemen PSDA":

    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16njtyY_udcs-P-o7CBz6-5lhwhBKC52W",
            "https://drive.google.com/uc?export=view&id=1GgMo6T-UJLjHqlO8XyKpYkkEkSPXiVCW",
            "https://drive.google.com/uc?export=view&id=1Fr9A82iOgKV19z6HD_4nrZQfFKgTDme9",
            "https://drive.google.com/uc?export=view&id=1Fabopo00M9QcbHHhFP9N4oXVUVExKC2-",
            "https://drive.google.com/uc?export=view&id=1GQBJzRsWFbv53j5Hsyca9eki4cw9Wi7s",
            "https://drive.google.com/uc?export=view&id=1E52EJ_DYarPgfFsAY5gO1Xe1863UgDOn",
            "https://drive.google.com/uc?export=view&id=1FosrmFZ07dibrMEkqRPGYGvbzYhOmbs6",
            "https://drive.google.com/uc?export=view&id=1G-2YAz_sWiOZMrn1PWReges4G-pubqkn",
            "https://drive.google.com/uc?export=view&id=1FGGT4t4a5h1MJ6Y6VFBxpidfwwW14OKb",
            "https://drive.google.com/uc?export=view&id=1FQriRUNLdUHrs9miU9Isl982zisxyMS3",
            "https://drive.google.com/uc?export=view&id=1FFtlcHU7tZKyFMAkGt0zZSTQHRVE4nwl",
            "https://drive.google.com/uc?export=view&id=1Em6Lfx62JPF88Mx2LIgx8py4slcODgRq",
            "https://drive.google.com/uc?export=view&id=1FZO5VKQD5W6QVdQ8ykkBNcG_u6U3TVHE",
            "https://drive.google.com/uc?export=view&id=1FhFoR5rPqVr7FadKpPM_JbF_NbdlFrEZ",
            "https://drive.google.com/uc?export=view&id=1FN6NAu7EMIkv7VKHNQ_Mtnx2paLnN31J",
            "https://drive.google.com/uc?export=view&id=1F3xMcmAmEYkAweNybWCrE1vno1m9XEW3",
            "https://drive.google.com/uc?export=view&id=1ErXeVWcL3SA2LK6st1_wQ90QlYuRbUDw",
            "https://drive.google.com/uc?export=view&id=1GIYcSm95Na8hyQq2wSAFSSUfc_fiO7Tk",
            "https://drive.google.com/uc?export=view&id=1GDhCR3GiMnnM0HFjhuK3eEGDDdf6V9GS",
            
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
                "kesan": "Bang econ keren banget mindsetnya",
                "pesan": "Makasi bang untuk ilmu-ilmunya, sehagt selalu",
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
                "kesan": "Kak abet lucuu",
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
                "kesan": "bang depan jujur lucu banget orangnya",
                "pesan": "Semoga bang depan sehat terus", 
                "jabatan" : "Kepala Divisi Manjakat", # 1
            },
             {
                "nama": " Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak pipah cantik dan tegas",
                "pesan": "Jangan lupa istirahat kak, jaga kesehatan <3", 
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
                "kesan": "Keren bang sangat memotivasi kami",
                "pesan": "Selalu jadi orang baik yang sangat gemar menolong", 
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
                "kesan": "Keren bang",
                "pesan": "Sehat-sehat bang asprak", 
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
                "kesan": "Bang kemas ini jago ngoding",
                "pesan": "Semakin rajin ya bang belajarnya", 
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
                "kesan": "Kakaknya lucu imut",
                "pesan": "Semangat belajarnya kak, semoga akademiknya emakin meningkat, semoga nilai strukdat saya aman yaa kak hehehe ", 
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
                "kesan": "Baik kakaknya, ramah juga cantikk",
                "pesan": "Semangat kak kuliahnya, sukses selalu", 
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
                "kesan": "Abangnya baik ramah suaranya bagus",
                "pesan": "Semangat kuliahnya bang,bahagia dan sukses selalu", 
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
                "kesan": "Kakak cantikk, sukanya sama stylenya",
                "pesan": "semangatt selalu kakk", 
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
                "kesan": "Kak pashaa ini kating sd pertama yang bisa kenal heheh",
                "pesan": "Semangat kuliahnya kak, semoga segala kebaikan menyertai kakak", 
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
                "kesan": "Kakaknya baik dulu pas asprak baik banget kasih nilainyaa",
                "pesan": "Terus memotivasi kami kak, semangat terus", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Bang riko asik banget",
                "pesan": "Semangat mengejar akademiknya bang", 
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
                "kesan": "Kakaknya baik dan asik",
                "pesan": "Sukses selalu kak dalam segala hal", 
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
                "kesan": "Abangnya ramah dan tidakk sombong",
                "pesan": "Semangat dalam menjalani hari-hari bang", 
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
                "kesan": "Kakak baik, ramah dan rajin olahraga",
                "pesan": "Semoga semakin jago kak renangnya", 
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
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Sehat dan bahagia selalu bang", 
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
                "kesan": "Kakaknya pintar dan baik hati",
                "pesan": "Sukses selalu kak dalam berbagai bidang", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)


    PSDA()
elif menu == "Departemen MIKFES":

    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CD7M8bWFXNnMme4PGQkpUadEm2JwbfIP",
            "https://drive.google.com/uc?export=view&id=1CuJy8LBAO6KR-vEzhrDHNgyfLKy1hp9h",
            "https://drive.google.com/uc?export=view&id=1CPiZlYFndSo9otU0wDhhQaTdpsoyyD27",
            "https://drive.google.com/uc?export=view&id=1C3xkYMJTdErdXhorUvzPhDcrcGTby1a3",
            "https://drive.google.com/uc?export=view&id=1CLwYDmPyjfg756RnhzjY48NfImMpmd_k",
            "https://drive.google.com/uc?export=view&id=1CYc1YEJjrAeopDYb9TRwV8Agwfw9Q1od",
            "https://drive.google.com/uc?export=view&id=1CKcbcXm9odFpM0532j0PYxdgRZNsXx4f",
            "https://drive.google.com/uc?export=view&id=1CNdoBEFDT2_D1pmKTJzFerHV5Zv6BcOt",
            "https://drive.google.com/uc?export=view&id=1C06VdwCVuGq8mDIubMi4TC6z5JmYwgqG",
            "https://drive.google.com/uc?export=view&id=1CmlQ0AXQC336crsMqNd00ulThvi0PgOR",
            "https://drive.google.com/uc?export=view&id=C0Wlr-KEFj28xLmVC6Pg-z5tI2aVGks5",
            "https://drive.google.com/uc?export=view&id=1CPnET9e4A1W1GuBHZ6JYghfoupdzpWJq",
            "https://drive.google.com/uc?export=view&id=1CzdQMIgKpLlb0qQ1156QQSZZDCdjDBKO",
            "https://drive.google.com/uc?export=view&id=1DFEg1ytsTRCDbXGEg-684sId9vNqsPfL",
            "https://drive.google.com/uc?export=view&id=1CwcyxKEliyj-EKaS2gTuMvtuP444DlJK",
            "https://drive.google.com/uc?export=view&id=1D83jWWJJRZw3WbAKxNCSxU7f_yORwRT0",
            "https://drive.google.com/uc?export=view&id=1DFjpV9X1EiLji4zRl5_dGTEmFnUuwHW_",
           
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
                "kesan": "Penjelasan abang jelas dan inspiratif, kami jadi lebih paham tentang mikfess",
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
                "kesan": "nama kakak kalo disingkat lucu, jadi anova",
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
                "kesan": "Abang auranya emang mikfes banget sihh",
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
                "kesan": "keren sekali mindset abangnyaa",
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
                "kesan": "Kakaknya lucu",
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
                "kesan": "Keren loh bang nathan ini",
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
                "kesan": "bang anwar baik banget udah bantu cosval as pj tugas",
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
                "kesan": "Kakaknya baik dan cantik",
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
                "kesan": "Kak dinda ramah sekali",
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
                "kesan": "Selain cantik, kak marleta juga murah senyum",
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
                "kesan": "Salut banget!",
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
                "kesan": "keren bangg",
                "pesan": "Sehat terus ya abang, semoga apa yang abang inginkan segera tercapai", 
                "jabatan" : "Kepala Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "bang adit ini lucu",
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
                "kesan": "cantik bgt?!",
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
                "kesan": "nama abangnya keren banget",
                "pesan": "be happy bang happy!", 
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
                "kesan": "Abang keren banget, astut tpb 1 duluu",
                "pesan": "Semoga abang terus berkarya dan sukses dalam segala hal, jangan lupa berdoa!", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    mikfes()

elif menu == "Departemen Internal":

    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SPayuX5ufTaESVcDCKvog6tEIC2zGQ9T",
            "https://drive.google.com/uc?export=view&id=1Rwc5rpd_S_XU8a9PKwLG9RU_aeMiGcFv",
            "https://drive.google.com/uc?export=view&id=1KrzKL7jVTmFHxCHHPcdnFiVNrv3wC0Sg",
            "https://drive.google.com/uc?export=view&id=1S9iFwYMVjQkLTUqsNsw1bQ-Ah5sPbMM-",
            "https://drive.google.com/uc?export=view&id=1SFbNbCMa44TMrktTM_Uj375gGqvRUc7d",
            "https://drive.google.com/uc?export=view&id=1SI1v1ny3FnhQJZTgNZMVxtw1yzfTimDJ",
            "https://drive.google.com/uc?export=view&id=1RyK9Fzr2KMTiU94233oFPpProW3D-4z4",
            "https://drive.google.com/uc?export=view&id=1SUSFApIDs9aAH6np1UKpdgpW3giCD-zZ",
            "https://drive.google.com/uc?export=view&id=1RxbdQliWDHjPS0WIBXukS9121tW-rRKM",
            "https://drive.google.com/uc?export=view&id=1SChLm7crK17Pfja4A7ZNGGZXuETQR1z-",
            "https://drive.google.com/uc?export=view&id=1SFlU55o3gEMHCFsh8Z2Lfimkk3K-gX2A",
            "https://drive.google.com/uc?export=view&id=1SOuR1aGEiJ7i3Zj5Os1VN_2TOuFYq5fA",
            "https://drive.google.com/uc?export=view&id=1SPXWcwR7wXeRDUxhhLvSd8IsDU7QcIcA",
            
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
                "kesan": "Keren banget bang, hobinya juga uniq skali",
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
                "kesan": "Baik, cantik sekali kakaknya ramah juga",
                "pesan": "Tetap jadi orang yang baik ya kak", 
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
                "kesan": "Ramah banget bang",
                "pesan": "semoga makin rajin mengoleksi dino ya bang", 
                "jabatan" : "Kepala Divisi Keharmonisasian", # 1
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Baik dan kalem sekali kakanya",
                "pesan": "sehat-sehat kakk", 
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
                "kesan": "Ramah kakaknya",
                "pesan": "Sukses selalu dalam segala hal kak", 
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
                "kesan": "Pinter abangnya",
                "pesan": "Tetap pertahankan akademiknya bang", 
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
                "kesan": "Keren banget bang, selalu menjawab pertanyaan kami dengan baik",
                "pesan": "Jangan lupa makan bang, nungguin ayam betina berkokok juga butuh energi", 
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
                "kesan": "Keren banget bang pasti jago main futsal",
                "pesan": "Semangat bang menjalani hari-harinya yang walau terkadang berat", 
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
                "kesan": "Baik dan ramah abangnya",
                "pesan": "Beri aku satu jokes bang, aku ingin tertawa", 
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
                "kesan": "Asik dan kalem kakaknya",
                "pesan": "Bahagia selalu kak", 
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
                "kesan": "Kakaknya kalem dan baik",
                "pesan": "Semoga kakak selalu diberi kesehatan", 
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
                "kesan": "peduli & baik sekalii abang daplokku satu ini",
                "pesan": "Semangat terus bang Rendi, jangan lupa bahagia, smileee", 
                "jabatan" : "Staff Kerohanian", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    internal()
elif menu == "Senator":

    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=1jSz2gl5JrOt2taQoQEtFSK0_CTt2Ye8I",
            "https://drive.google.com/uc?export=1OZJd2IlXJ9lPE3tnMg403NrVOlYG_yNf",
            "https://drive.google.com/uc?export=view&id=1KkeXlOBxC_IyBguE9ECGQfnsUuLEUfMg",
            "https://drive.google.com/uc?export=view&id=1KYCxigbzhNNq3jkcfwblAXPCBFxoIVhg",
            
            
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
                "kesan": "Waktu pertama kali denger kak annisa speaking, aku langsung jatuh cinta sama cara kakaknya public speaking!! ",
                "pesan": "SEMANGATTT KAK ANNISAAA, doain aku bisa se keren kakak yaaa",
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
                "kesan": "Bang Bintang aktif banget di kepanitiaan dan organisasi, kerenn",
                "pesan": "Semangaaat ya bang, jangan lupa berdoaa", 
                "jabatan" : "Tim Senator", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    senator()

