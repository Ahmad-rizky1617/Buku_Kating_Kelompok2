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
            st.write("  ")
    st.write("Semua gambar telah dimuat!")


menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":

    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1srIhnLGLnoCzJDfrFOSIvYGLmoTb1N0N",
            "https://drive.google.com/uc?export=view&id=1hh4eLuXHajIDqPYB4Xg9T_uRA0yyNNJQ",
            "https://drive.google.com/uc?export=view&id=1G3V6WLQor-wTPjIiu98adBSbx5P8Hmn9",
            "https://drive.google.com/uc?export=view&id=1PKii0kMkRVpSiYcmcAsdrvVQlsWdKjzQ",
            "https://drive.google.com/uc?export=view&id=1RRjn3p7obs4yOGGXKDNgUB8_tqeQ3IYB",
            "https://drive.google.com/uc?export=view&id=1UuxrTMYjtH_augK2B6w5dKSHYQ_HQjam",
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
                "kesan": "Cara komunikasi abangnya keren",
                "pesan": "Semoga cepat lulus bang",
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
                "kesan": "Kakaknya lucu bangettt",
                "pesan": "semangat kuliahnya semoga cepat lulus kak",  
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
                "kesan": "Kakaknya pendiam dan kalem",
                "pesan": "Jangan patah semangat kakak",
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
                "kesan": "Abangnya keren public speakingnya",
                "pesan": "semangat bang kuliahnya, jangan patah semangat", 
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
                "kesan": "Kakaknya keliatan pintar",
                "pesan": "semangat kak kuliahnya, dan tidak mudah menyerah", 
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
                "kesan": "Sama sama asal metro hihihi",
                "pesan": "semangat kak kuliahnya, sukses selalu",  
                "jabatan" : "Bendahara 1", # 1
            },




        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1u2LnV0mTQogIYs4y9nftJceib_8rjSrt",
            "https://drive.google.com/uc?export=view&id=1Mjv7Hga6C_GT-S1tJWjZhrGg12Ze4ntE",
            "https://drive.google.com/uc?export=view&id=1wkpz2p_sipQPYPdGS5hwhWRe-tSAoNNF",
            "https://drive.google.com/uc?export=view&id=1xRy_zNrdLppEq6BUKeBSLo04S0HPtxKV",
            "https://drive.google.com/uc?export=view&id=1I7mV2KgTNE6InLtXJwCxTaBogJNxxYiS",
            "https://drive.google.com/uc?export=view&id=1jJnU3nibKggPNHJfRqPIbAsULvgzpfEe",
            "https://drive.google.com/uc?export=view&id=1oEAaXpKZw4xNByqG1NwP520JezNQoU8w",
            "https://drive.google.com/uc?export=view&id=1y2H_EdRfGoBF5dhMKM3HFcLseHVBd-T0",
            "https://drive.google.com/uc?export=view&id=1igUoJXdyDoLnEIP4Y8u31g-LR-7vZuCK",
            "https://drive.google.com/uc?export=view&id=1lMXPna-siKEj7pU3JzAGKgFsPZqfOUKk",
            "https://drive.google.com/uc?export=view&id=1rzVo9Ah-7RBOM5YYZVoXSFg4mlUoK44t",
            "https://drive.google.com/uc?export=view&id=1uID-TsF0YGU6TZEofMUZPaJUG36bB6O3",
            "https://drive.google.com/uc?export=view&id=1kDwjHSnxHMgcCd1PM9K3eIsG1XMTBuRk",
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
                "kesan": "Kakaknya cantik, ramah, baik",
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
                "kesan": "Baik banget kakaknya, sgt humble",
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
                "kesan": "Ramah banget kakanya, baikk pula",
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
                "kesan": "Abangnya sepertinya famous yah",
                "pesan": "semangat kuliahnya kak, semoga lulus tepat waktu", 
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
                "hobbi": "Nyari Sinyal di Gedung F",
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
                "kesan": "Baik kakanya",
                "pesan": "semangat kuliahnya kak, tetap pertahankan jadi orang baik", 
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
                "kesan": "Abangnya keliatan seperti orang pintar, memang pintar",
                "pesan": "semangat kuliahnya kak, tetap pertahankan akademiknya", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dLevJN__yKeNDLhxMh3WdDAss98PBgnD",
            "https://drive.google.com/uc?export=view&id=1t10zFtR3pAukNaSYcpS3wRws-64Dxxj3",
            "https://drive.google.com/uc?export=view&id=1scrWn9MzuC2gCkt99tMdRtlVuQh7wl25",
            "https://drive.google.com/uc?export=view&id=1_FidCGCCXGLgFbY8gDY4170STjrFFlXl",
            "https://drive.google.com/uc?export=view&id=1mdvkfsYJ8WLZ6QSfP2ZfBIAo4FJiD8hf",
            "https://drive.google.com/uc?export=view&id=1L_-NCwykbCnGE64ycYlxXYpLGeQF91m9",
            "https://drive.google.com/uc?export=view&id=1FPcW3xij4NQdMnQSk5NRarz-9sQogcg1",
            "https://drive.google.com/uc?export=view&id=12fQY3aieQJFXhQlN9ryJg4-0IQlGwyTH",
            "https://drive.google.com/uc?export=view&id=1zG9d9PrnMvMcpKsBH8vQxHxL5MOsdHh",
            "https://drive.google.com/uc?export=view&id=1POdKZLiuP3MEPtIsGHd3x8mBZ-GWrVLt",
            "https://drive.google.com/uc?export=view&id=1XSvnTFVBD0k5IjFT2sD-ObQRDaEpB_LQ",
            "https://drive.google.com/uc?export=view&id=13QUBn-PBhnCqX9kzAuhTWxgS_CdcUjOi",
            "https://drive.google.com/uc?export=view&id=1l_3a7dIzcaDnfZUqdEdJW_EXApuSWgCy",
            "https://drive.google.com/uc?export=view&id=1nED8Efxr47wOyxQMQArv0DPyExuaZBJn",
            "https://drive.google.com/uc?export=view&id=1gBTwdeOa8BB94BAcqpy8FdC8Mag7pvdY",
            "https://drive.google.com/uc?export=view&id=1vwfdR3MBxM0neon0ZFWZpxmpIsSqSZUC",
            "https://drive.google.com/uc?export=view&id=1XaCYi_G8nbdNPd6ItNpnIEQbSq4pDzac",
            "https://drive.google.com/uc?export=view&id=1aPkfEWqZvt6J8_SwFWNoRyrso1O8_J-O",
            "https://drive.google.com/uc?export=view&id=13ENqy-WDdx7_WTBMn2vGKikJsd3zXXLD",
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
                "kesan": "Abangnya asik dana kece",
                "pesan": "Semangat kuliahnya bang, tetap fokus",
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
                "kesan": "Manis bangett kakk, NIM nya sama kayak aku hihi",
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
                "kesan": "Kakaknya baik, pertanyaanku semua terjawab",
                "pesan": "Sehat selalu kak", 
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
                "kesan": "Abangnya asik dan kece",
                "pesan": "Keren banget bang", 
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
                "kesan": "Keren abangnya pasti jago ngoding",
                "pesan": "Semangat bang ngodingnya", 
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
                "pesan": "Lancar terus kuliahnya kak", 
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
                "kesan": "Kakaknya keliatan rajin organisasi",
                "pesan": "Jangan lupa istirahat kak", 
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
                "kesan": "Keren banget kakaknya",
                "pesan": "Jangan lupa istirahat kak", 
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
                "kesan": "Lucu asik banget kakaknya",
                "pesan": "Jaga kesehatan kak", 
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
                "kesan": "Keren banget kak, pasti jago ngoding",
                "pesan": "Ajarin aku ngoding dong kak", 
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
                "kesan": "Baik banget kakaknya",
                "pesan": "Ayo kak nonton bareng", 
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
                "kesan": "Kakaknya kalem banget dan baik hati ",
                "pesan": "Semangat kak dan bahagia terus ya", 
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
                "kesan": "Baik abangnya",
                "pesan": "Ajarin aku foto foto dong kak", 
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
                "kesan": "kakaknya baik dan ramah",
                "pesan": "semangat kuliahnya kak, tetap pertahankan jadi orang baiknya", 
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
                "kesan": "Abangnya asik banget",
                "pesan": "Semangat kuliahnya bang", 
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
                "kesan": "Abangnya keren dan asik",
                "pesan": "Semangat bang, jaga kesehatan", 
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
                "kesan": "Rajin banget abangnya hobi membaca buku",
                "pesan": "Semangat kuliahnya bang, tetap baik hati", 
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
                "kesan": "Kakaknya kelihatan rajin dan sekaliii",
                "pesan": "Sehat selalu kak", 
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
                "kesan": "Kakaknya asik banget",
                "pesan": "Jangan lupa bahagia kak", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    medkraf()

elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mMb9JSDLeze6qudPfMWPW-NV9msWGsqJ",
            "https://drive.google.com/uc?export=view&id=1upOiVJBc1rED7sEfG1D4F11HfMWngLYt",
            "https://drive.google.com/uc?export=view&id=16wNCsus9_2NvnVPrVMbhKiW28JeOIeMJ",
            "https://drive.google.com/uc?export=view&id=1K0Rf227mUJSPTQHEAQQ0v_dfT8BQQ4LG",
            "https://drive.google.com/uc?export=view&id=1V26dD6Iu9vIUI7Z7hHsJruGQ6_jDOTMi",
            "https://drive.google.com/uc?export=view&id=1HwfBhKOuUAEM6FXpFlw3L5lGxOhltl0I",
            "https://drive.google.com/uc?export=view&id=1wgJcptKnbItQU-yTBKr5htnR2Gvxn3bv",
            "https://drive.google.com/uc?export=view&id=17os67zDHkdGPiJcB-Tyxp9TV-w9wapXs",
            "https://drive.google.com/uc?export=view&id=1sW_X0feS-ma29FaXvDCgP21MwbQTjSMY",
            "https://drive.google.com/uc?export=view&id=1e40AFoEiOV_eMRiTWk2feDqbJBJGLHWF",
            
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
                "kesan": "Keren banget abangnya sangat berambisi mencari uang",
                "pesan": "Semoga makin banyak uang bang",
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
                "kesan": "Kakaknya asal dari Metro sama kayak aku",
                "pesan": "Semangat kak, semoga makin banyak uang", 
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
                "kesan": "Keren banget kakaknya jago ngitung uang",
                "pesan": "Semangat kak menghitung uangnya", 
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
                "kesan": "Sering ketemu abangnya, produktif banget ya bang",
                "pesan": "Semangat bang walaupun produktif jangan lupa jaga kesehatan", 
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
                "kesan": "Keren abangnya asik juga",
                "pesan": "Semangat bang", 
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
                "kesan": "Abangnya rapih banget, suka",
                "pesan": "Semangat terus bang kuliahnya", 
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
                "kesan": "Kakaknya manis banget dan juga humble",
                "pesan": "Semangat kak kuliahnya, tetap semangatt", 
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
                "kesan": "Keren kak jadi kepala sponsor",
                "pesan": "Semoga kerennya nular ke aku ya kak", 
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
                "kesan": "Kakaknya manis banget dan asikk",
                "pesan": "Semangat kuliahnya kak, tetap jadi orang baik", 
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
                "kesan": "Abangnya kalem banget",
                "pesan": "Semangat bang kuliahnya", 
                "jabatan" : "Staff sponsor", # 1
            },
           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()

elif menu == "Departemen PSDA":

    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WRelsiMEzrHw-12Ruo8ApWSbgGaF05Fy",
            "https://drive.google.com/uc?export=view&id=1jM3cwRrMCBS1c6O4BCyrugmewztRrqgi",
            "https://drive.google.com/uc?export=view&id=1kud2i-6AKaGdbYw_lElBzBfdtAjO16RS",
            "https://drive.google.com/uc?export=view&id=16uaiM0jfZpx06pGuq1JUKNQST_JcLnQc",
            "https://drive.google.com/uc?export=view&id=1lBEIamTTHG2GY45lqj6mNq9YfqXJ6b7Y",
            "https://drive.google.com/uc?export=view&id=1J5XWzh33YrzqzCdgbSUlzQcCf-Y9jCtY",
            "https://drive.google.com/uc?export=view&id=10r0sLEc5B2t6HjnqN0fDuIPujF6cca6A",
            "https://drive.google.com/uc?export=view&id=1UMR_czxiGzkYOfnBnPfXu4J2C7EyDzH3",
            "https://drive.google.com/uc?export=view&id=1pz2UvwB1rqpY72aPFfM8nUYCM9t7Bv3A",
            "https://drive.google.com/uc?export=view&id=1n87dFA5L7mop7sLPqTHokyz7RArDEBsA",
            "https://drive.google.com/uc?export=view&id=1gPEvbc4Ku4nBtorPh7EghJqlyt6OPt_F",
            "https://drive.google.com/uc?export=view&id=1EfNi0R319oU8_vq1hc4-PpVuuCQtewMu",
            "https://drive.google.com/uc?export=view&id=103i8b_Um5N9S2rjsaBhKIWaugRm2MpQy",
            "https://drive.google.com/uc?export=view&id=1ZYP4IM3gagjC4wX0a5aUOHI__GVE0ZEI",
            "https://drive.google.com/uc?export=view&id=1W0IkE6ph2NO7VatJPiuM12Cp_IGcTtqU",
            "https://drive.google.com/uc?export=view&id=1Rf7Igxy4OQmPUqWn8BumGMgpXYBoDiew",
            "https://drive.google.com/uc?export=view&id=1bprZ4ziytKKFYLJTF9q6WbO-Cr3dlFxp",
            "https://drive.google.com/uc?export=view&id=1u7IhpuLq11ra8eJ66OM0O0QFz5Luiv4T",
            "https://drive.google.com/uc?export=view&id=1zVMkAiHw0hoHp9-tW2Y6nVFkVx88fK8d",
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
                "kesan": "Keren banget bang",
                "pesan": "Semangat bang, semoga aku bisa keren kayak abang",
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
                "kesan": "Asik banget kakanya, lucu juga",
                "pesan": "Semangat kuliahnya kak, jangan lupa istirahat", 
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
                "kesan": "Abangnya kelihatan berbakat sekali",
                "pesan": "Semangat bang jangan lupa istirahat", 
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
                "kesan": "Kakaknya cantik dan tegas",
                "pesan": "Jangan lupa istirahat kak, jaga kesehatan", 
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
                "pesan": "Selalu jadi orang baik yang rajin menolong", 
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
                "pesan": "Semoga semakin rajin ngaspraknya bang", 
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
                "kesan": "Abangnya keliatan gamers ternyata memang hobi main game",
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
                "kesan": "Music taste nya bagus kak",
                "pesan": "Semangat belajarnya kak, semoga akademiknya emakin meningkat ", 
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
                "kesan": "Baik kakaknya, ramah jugaa",
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
                "kesan": "Kakak kerenn sangattt, sukanya sama stylenya",
                "pesan": "Keren selalu kakk", 
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
                "kesan": "Kakak tegas dan berwibawa",
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
                "kesan": "Kakaknya baik dan ramah",
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
                "kesan": "Abangnya humble dan asik",
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
            "https://drive.google.com/uc?export=view&id=18W1dNVSnHKimBT6QsrDEiKDU5BDaFRKM",
            "https://drive.google.com/uc?export=view&id=18L4Hr0OZAinhXmtN9S1K-k2euGZVlEXn",
            "https://drive.google.com/uc?export=view&id=1Pnuzz0xJGwS0KEQG4umEkU2fzRnUyGwA",
            "https://drive.google.com/uc?export=view&id=1mVFzWZSsV80XybgO6TYVV8tJPDDxWtdE",
            "https://drive.google.com/uc?export=view&id=1ALJ3mUe9RoTLopOzf4IzcGzryDBuL0nl",
            "https://drive.google.com/uc?export=view&id=1k7nOJiJtSNhTZwggtHwMfiDSans4t-4i",
            "https://drive.google.com/uc?export=view&id=1DEaOtJIDkJaEO4qgAaYJLOUpa0xMxeZu",
            "https://drive.google.com/uc?export=view&id=1LoPuUW7dnifk7rUESlcvXFDlH7MhNE8J",
            "https://drive.google.com/uc?export=view&id=12oGKmOWntKalGr1PKyRLhLME4b__aeQY",
            "https://drive.google.com/uc?export=view&id=1L5byKSeM6SC2URb1DIX6vm276JooOY84",
            "https://drive.google.com/uc?export=view&id=1MLXXV_XlQJCxgN9Zg3U7AqdVy9yvURZ7",
            "https://drive.google.com/uc?export=view&id=1rJ3-wktVYZRJXgbwLO2xq2CvNYwNshKI",
            "https://drive.google.com/uc?export=view&id=1leNbOv0dg4YP_uoj3RTjdGpiZQWJzk4_",
            "https://drive.google.com/uc?export=view&id=1GqLONvnN1bVlK9P-W4wLWQwuFpnsYEUL", 
            "https://drive.google.com/uc?export=view&id=1Il67H2c0HHM9TA8EE-a0UQTlaUT_sI6J",
            "https://drive.google.com/uc?export=view&id=1e0K7hYXDbh3sSqNjwf734qB6FwzLAKgG",
            "https://drive.google.com/uc?export=view&id=1hWqVGqfxJi2cOQt6g7nrmFBlmcOgJ5rm",
            "https://drive.google.com/uc?export=view&id=1xKugy1HwL-egysjK_mU6KLMMZ4g5xu2j",
           
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
                "kesan": "Abangnya keren, sangat memotivasi",
                "pesan": "Jangan lupa semangat bang",
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
                "kesan": "Kakaknya baik dan ramah sekali",
                "pesan": "Semangat dan sukses selalu kak", 
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
                "kesan": "Keren abangnya jago olahraga",
                "pesan": "Semangat terus bang olahraganya semoga semakin rajin", 
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
                "kesan": "Baik dan memotivasi kami abangnya",
                "pesan": "Sukses selalu bang, jangan lupa semangat", 
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
                "kesan": "Ramah dan baik hati abangnya",
                "pesan": "Selalu memotivasi kami ya bang", 
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
                "kesan": "Keren kakaknya sepertinya aktif sekali di organisasi",
                "pesan": "Semangat kak semoga akademiknya semakin meningkat", 
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
                "kesan": "Pintar dan baik hati abangnya",
                "pesan": "Semoga kesuksesan selalu menyertai abang", 
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
                "kesan": "Baik dan solutif abangnya",
                "pesan": "Semangat abang pj materi kelompok kami cosval", 
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
                "kesan": "Ramah dan baik banget kak",
                "pesan": "Sukses selalu kak dalam berbagai hal", 
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
                "kesan": "Keren kakaknyaa",
                "pesan": "Semangat menjalani hri-hari kak", 
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
                "kesan": "Pinter kak marletta, kenal dari pas TPB jadi tutor matdas TPB 2",
                "pesan": "Semangat terus kak, semoga akademiknya semakin meningkat", 
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
                "kesan": "Kakaknya baik hati dna tidak sombong",
                "pesan": "Bahagia terus ya kakak", 
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
                "kesan": "Keren bang hobi membaca",
                "pesan": "Sukses selalu bang, terus memberi motivasi kepada kami", 
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
                "kesan": "abangnya baik banget, membantu banget di magang SNR",
                "pesan": "Sukses selalu bang, tetap memotivasi kami ya", 
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
                "kesan": "Keren banget bang ",
                "pesan": "Selalu membimbing kami ya bang", 
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
                "kesan": "Baik kakaknya dan cantik",
                "pesan": "Jangan pernah bosan ngajarin kami ya kak", 
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
                "kesan": "Baik dan ramah abangnya",
                "pesan": "Sukses selalu bang", 
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
                "kesan": "Keren dan baik abangnya",
                "pesan": "Jangan lupa semangat bang", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    mikfes()
elif menu == "Departemen Eksternal":

    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15GZ0Yvs92OSOR0iKVwKYTBIQjNBwX6wY",
            "https://drive.google.com/uc?export=view&id=1igOFURNxowDcGCQua58cAj7q7P8AM9c2",
            "https://drive.google.com/uc?export=view&id=1iZ30T-vRdcAh0f05KBxV0MuuVSVlZ9pR",
            "https://drive.google.com/uc?export=view&id=1y89YBiEQT_Q2nh9g57D_ehyFOTEyn4Hx",
            "https://drive.google.com/uc?export=view&id=1V6TkepkVWodtbEOBAIR-EUtYiG_DLM8r",
            "https://drive.google.com/uc?export=view&id=1b83H4yUz41tKqT2a4ZsbKbA2gjsVB5Fv",
            "https://drive.google.com/uc?export=view&id=1pKyKCGTkuLx_WUjZnztYEF4IoUmLtmGZ",
            "https://drive.google.com/uc?export=view&id=18DP9CBU3hNnk1iDuBUjqmSEKGf_rZqLZ",
            "https://drive.google.com/uc?export=view&id=14MmecgWS8K9LXmnegD-lVo3QpMww-ugK",
            "https://drive.google.com/uc?export=view&id=1T449s-D9yMDSR5WwU6Gdooq6bMNXk-rT",
            "https://drive.google.com/uc?export=view&id=1kWDKN134o1XY3eWEdF8cSD6MPVgHKIde",
            "https://drive.google.com/uc?export=view&id=177FH9CzVDLfXejRvPkQC0Akpus1SoTcm",
            "https://drive.google.com/uc?export=view&id=1QReNJbCCbEyx9mqy1EQoq094EjwskYyU",
            "https://drive.google.com/uc?export=view&id=1pdbDGCwVzRuPxw3uZsHWVEh9wymZgl63",
            "https://drive.google.com/uc?export=view&id=1aQNgUn6ihpR9cDDQLiMkoUYbLQYow8pw",
            "https://drive.google.com/uc?export=view&id=1GO_FFSCvStabdREsq9Tnj8xFRnAs8Rn2",
            "https://drive.google.com/uc?export=view&id=1RQkBtyLKKGfEoEy9KwZ92YCmQ16xotyH",
            "https://drive.google.com/uc?export=view&id=1qCR0vVqpBjOwYpvd9sjFIFeT_-_ojF3c",
            "https://drive.google.com/uc?export=view&id=1OZDxyBQhj1vBI6d9XE9Yh7UD5MI7PjvZ",
            "https://drive.google.com/uc?export=view&id=1A8vCohD6KV_66htONNiBCt4DtpUAtDKy",
            
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
                "kesan": "Abangnya solutif, selalu menjawa pertanyaan kami dengan baik",
                "pesan": "Semakin sukses ya bang dalam hal apapun itu",
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
                "kesan": "Keren banget kak, selalu aktif organisasi",
                "pesan": "Jangan lupa istirahat dan semangat selalu kak", 
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
                "kesan": "Lucu kakaknya, ketawa terus gemas",
                "pesan": "Bahagia selalu kak", 
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
                "kesan": "Keren banget bang",
                "pesan": "Semangat selalu kuliahnya bang", 
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
                "kesan": "Cantik sekali dan ramah banget daplokku",
                "pesan": "Semangat selalu kak Dea baik hati dan cantik", 
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
                "kesan": "Asik banget dan lucu kakk",
                "pesan": "Semangat terus kak, seneng terus yaa", 
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
                "kesan": "Keren kakaknya, aktif sekali di organisasi",
                "pesan": "Semangat kak, terus mempertahankan akademiknya ya", 
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
                "kesan": "Cantik dan ramah sekali kakaknya",
                "pesan": "Jangan lupa semangat dalam menjalani hari kak", 
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
                "kesan": "Kakaknya baik dan rajin sekali",
                "pesan": "Bahagia terus kak, jangan lupa istirahat", 
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
                "kesan": "Keren banget bang, aktif sekali dalam berkegiatan",
                "pesan": "Jangan lupa istirahat bang, semoga semangatnya selalu membara", 
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
                "kesan": "Kakaknya baik dan tegas",
                "pesan": "Sukses selalu kak di dalam hal apapun", 
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
                "kesan": "Keren dan baik hati abangnya",
                "pesan": "Selalu memotivasi kami ya bang", 
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
                "kesan": "Asik banget abangnya",
                "pesan": "Tetap jadi orang baik bang", 
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
                "kesan": "Kakaknya ramah dan cocok sekali di pengmas",
                "pesan": "Tetap jadi orang yang ramah kak", 
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
                "kesan": "Baik sekali kakaknya",
                "pesan": "Tetap pertahankan semangat yang berkobar itu kak", 
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
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Baik dan sangat memberi motivasi bang",
                "pesan": "Bahagia selalu bang", 
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
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },

           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    eksternal()
elif menu == "Departemen Internal":

    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1z4KNhrONhRjOW0O7NkV0G5ciFa6L4KfH",
            "https://drive.google.com/uc?export=view&id=186UwsiwWUsJB70dOD83yudRAHnKXJ5lC",
            "https://drive.google.com/uc?export=view&id=1-LZ4ILmLr9y2TFTAgiajNkh_OlQhN0L-",
            "https://drive.google.com/uc?export=view&id=15lFgjKPhdFyyZlhKPTEvhgZm6eHij6r6",
            "https://drive.google.com/uc?export=view&id=1Y3wxWspI5TCJCT1-vjLAWllziuxdIpgm",
            "https://drive.google.com/uc?export=view&id=1tCCvfMKRl83FJMngHHyNL_H_hhlOKLEo",
            "https://drive.google.com/uc?export=view&id=1AuU4DZ9RRIWYQgo52orpZ12dApvceQI0",
            "https://drive.google.com/uc?export=view&id=1qhTWCJucvbCMt4g06eP18Lx_ctXKx8CM",
            "https://drive.google.com/uc?export=view&id=1C72Of0jPKjpvVKL0gfRR1rL5XDIxPeyt",
            "https://drive.google.com/uc?expor t=view&id=1NbT2wquNDCI3rCgk6W9YLfflVRmg4TCs",
            "https://drive.google.com/uc?export=view&id=1YQbi0yksyVIJKkHuBc2xMFzGgPamXlxA",
            "https://drive.google.com/uc?expor t=view&id=1aWoW8foWIV2Q3GZEB3TVMTHPD_-6tvay",
            
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
                "kesan": "Baik sekali kakanya ramah banget juga",
                "pesan": "Tetap jadi orang yang baik ya kak", 
                "jabatan" : "Sekretaris Departemen Internal", # 1
            },
            {
                "nama": "Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Ramah banget bang",
                "pesan": "Boleh minta satu gak bang dinonya", 
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
                "pesan": "Ajakin aku dong kak kalo mancing, tapi aku bisanya mancing amarah", 
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
                "kesan": "Ramah kakaknya, cocok banget di keharmonisasian",
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
                "kesan": "Keren banget bang, selalu menjawa pertanyaan kami dengan baik",
                "pesan": "Jangan lupa semangat bang", 
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
                "sosmed": "@meiralsty_",
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
                "kesan": "Asik dan baik sekalii abang daplokku satu ini",
                "pesan": "Semangat terus bang Rendi, jangan lupa bahagia", 
                "jabatan" : "Staff Kerohanian", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    internal()
elif menu == "Senator":

    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=15Zh8bPqjQH_2Z-_WbUoGrM7uKqoprZGS",
            "https://drive.google.com/uc?export=14ZWF1_ZWUNrC_NcW9WxXB1FJh0j_jk3M",
            
            
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
                "kesan": "Keren banget kakk, cara jawab pertanyaannya bagus sekali ",
                "pesan": "Semangat kakk, semoga segera lulus ya kakk",
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
                "kesan": "WOW keren banget bang, aktif sekali di kepanitiaan dan organisasi",
                "pesan": "Tetap semangat dan tetap mempertahankan akademiknya ya", 
                "jabatan" : "Tim Senator", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    senator()



    



# Tambahkan menu lainnya sesuai kebutuhan
