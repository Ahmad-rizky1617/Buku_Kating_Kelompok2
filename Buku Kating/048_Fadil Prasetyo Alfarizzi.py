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
            "Departemen MedKraf",
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
            "people-fill",
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
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":

    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mr_OnoWrb33rxMPJoPu1HWX5yFhetFWQ",
            "https://drive.google.com/uc?export=view&id=1iPDBlMyuALLAajTsCKzqv5HYOQMp_Q0h",
            "https://drive.google.com/uc?export=view&id=1iVjayLW1HGFIHJN7DjxycVHxQ035upoF",
            "https://drive.google.com/uc?export=view&id=1iPY4z7FG9km0985uLa1OLgPTyLhYrV3f",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
            "https://drive.google.com/uc?export=view&id=1mmbjC7BFnSlVGTD2G3074LvseENZvdMy",
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
                "kesan": "aura pemimpinnya terlihat",
                "pesan": "Semoga cita-citanya dihimpunan segera tercapai",
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
                "pesan": "semangat bang nyanyinya", 
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
                "kesan": "Kakaknya keliatan pintar dan baik",
                "pesan": "semangat kak dengerin bang pandra nyanyi", 
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
                "kesan": "sangat baik",
                "pesan": "semangat kak kuliahnya, sukses selalu",  
                "jabatan" : "Bendahara 1", # 1
            },




        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dU_MgfZ0HQ5Rtw-NYQ9_B-SsbWkgyNMF",
            "https://drive.google.com/uc?export=view&id=1dphzB3Tr7sr-agBGsbyBmKIC3UXc0z6T",
            "https://drive.google.com/uc?export=view&id=1e6XTHHnRNmo16N9uWnEAvlayUOvGNgW1",
            "https://drive.google.com/uc?export=view&id=1dqDxzH304tVv2YKlpESLz8FpILimETxO",
            "https://drive.google.com/uc?export=view&id=1dgjZjdbP8lfb_eS1w2UqNiIvQxPdS3bM",
            "https://drive.google.com/uc?export=view&id=1dv8wg95nUVcE70bdPvh8ekUOettGiw2E",
            "https://drive.google.com/uc?export=view&id=1e6KQoYFmfCS6JuJseenF-wuVkj0J1hAC",
            "https://drive.google.com/uc?export=view&id=1dqcyuS6aGroVlYzv40rlPuu_KDUzE4M8",
            "https://drive.google.com/uc?export=view&id=1dqABMV2zsvihgS5zZawQg9TF-goUnlp8",
            "https://drive.google.com/uc?export=view&id=1e1kmkI4_iR03ZtFMf0DD22Dcmin58c9p",
            "https://drive.google.com/uc?export=view&id=1e36MRRiA9ycTJYU4JduL_wbOZ0sMxrf_",
            "https://drive.google.com/uc?export=view&id=1dU09lHrd1KgaHv8IZzdKTyuG1oR1FDiT",
            "https://drive.google.com/uc?export=view&id=1dqX-ZWEWrb-w7uNuFM7nF1_tYyd1d78a",
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
                "kesan": "Kakaknya cantik",
                "pesan": "semangat kuliahnya kakak, tetap jadi pemimpin baik",
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
                "kesan": "Baik banget kakaknya, lucu",
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
                "kesan": "Abangnya sepertinya terkenal yah",
                "pesan": "semangat kuliahnya kak,  ngaspraknya juga", 
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
                "kesan": "Sangat mendengarkan keluh kesah",
                "pesan": "semangat kuliahnya kak, semangat ngaspraknya", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "Departemen MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OjvMBpOyWEAn5u1_4YU4VRe6YZcqp-Hk",
            "https://drive.google.com/uc?export=view&id=1Ov7_TWnFDszB_OONu734ZCH6kA7roPpb",
            "https://drive.google.com/uc?export=view&id=1P4mWYbl7_-9RGiZ7LxG_io_dWVVtlnkF",
            "https://drive.google.com/uc?export=view&id=1PYIu_PnCVy_b22L5p2UsvWq09WYLw-eo",
            "https://drive.google.com/uc?export=view&id=1OgTq1Vg-TpNXKKlt_tC6kJPHeRdCW5Z8",
            "https://drive.google.com/uc?export=view&id=1QBwFpnvNqQVnU0tq4JznWY_1hPwO92VC",
            "https://drive.google.com/uc?export=view&id=1PC5Xw-QlkgdqHXFiAf2RdUh6zFqJx_SI",
            "https://drive.google.com/uc?export=view&id=1OmKpr7OhQ_sGA3oauXSVtSaz0D2yFV4E",
            "https://drive.google.com/uc?export=view&id=1PjrSrxa-q-JyZoPRwh5JL2U9lNcehCNO",
            "https://drive.google.com/uc?export=view&id=1PvZN8vj2OJ2ftaMd-4cdY4xIbnbgzd1w",
            "https://drive.google.com/uc?export=view&id=1Q5mA77ce4bYcCMgu4LKd68CBmWhV4Vl6",
            "https://drive.google.com/uc?export=view&id=1PEZxR4PN3OXMzwO7tQ8LiHdvWl8xctIA",
            "https://drive.google.com/uc?export=view&id=1Q2nr3gsSQAcOZ74BOhgmHeAry3zZ9H2-",
            "https://drive.google.com/uc?export=view&id=1PQz2kSdn_KYeZwZUK0CEHopCyMlIf4YG",
            "https://drive.google.com/uc?export=view&id=1Ovz-ydkkB5UOr-oG0tbSWXoXdrg2MWlC",
            "https://drive.google.com/uc?export=view&id=1PUMy8XwKswr_u6mCKeTBIJsWY5aKrXLF",
            "https://drive.google.com/uc?export=view&id=1PHmLbV3NYvxXNsKFScHTLp2iBHvh83qZ",
            "https://drive.google.com/uc?export=view&id=1PlTWuLucVeXqsOWtlIDzkf-j_G4aeiuH",
            "https://drive.google.com/uc?export=view&id=1QBooOvoKpho0Urc4r1Di2xeYtVzbXoTR",
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
                "kesan": "abangnya terlihat sangat berpengalaman",
                "pesan": "Semangat kerjanya bang",
                "jabatan" : "Kepala Departemen Medkraf", #1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "baik kak",
                "pesan": "tetap ramah", 
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
                "kesan": "baik banget kak",
                "pesan": "Semangat kuliahnya", 
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
                "kesan": "kece banget",
                "pesan": "Semangat bang kerjanya", 
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
                "kesan": "keren banget kak",
                "pesan": "Semangat ngodingnya", 
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
                "kesan": "Konten banget",
                "pesan": "semangat bikin ide kontennya", 
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
                "kesan": "kece",
                "pesan": "Semangat kak", 
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
                "kesan": "keren",
                "pesan": "Semangat ngontennya", 
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
                "kesan": "akamsi pride",
                "pesan": "Semangat ldrnya kak", 
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
                "kesan": "Lucu",
                "pesan": "Selalu jadi daplok yang baik bagi markov ya kak", 
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
                "kesan": "keren",
                "pesan": "Semangat kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Sangat berpengetahuan",
                "pesan": "Semangat bang nugasnya", 
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
                "kesan": "Keren knowledge abangnya",
                "pesan": "Semangat desainnya bang", 
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
                "kesan": "Asprakku",
                "pesan": "Semangat ngaspraknya bang", 
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
                "kesan": "Merangkul banget",
                "pesan": "Maaf ya bang ga masuk desain :)", 
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
                "kesan": "Terlihat profesional",
                "pesan": "semangat figmanya", 
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
                "kesan": "terlihat berpengalaman",
                "pesan": "Semangat dokumnya", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1d4grR40vmMn7ZRHE8auzm6SPGqWVcxiP",
            "https://drive.google.com/uc?export=view&id=1dWKDv_8D9KY7TqGhNUXqrPNucbA9QK6J",
            "https://drive.google.com/uc?export=view&id=1dm13UDzD9Smp5TABbxQbKR-UlivIxnk8",
            "https://drive.google.com/uc?export=view&id=1drqQONYm8CAlYASPCc02wmoHnl0uAN_4",
            "https://drive.google.com/uc?export=view&id=1dYE1asg8G3wm5EvQsAo3XZM9CdVm3I5H",
            "https://drive.google.com/uc?export=view&id=1dN5VMyCM0hgSQTJx7ZnvRcMdZ4jd3vFC",
            "https://drive.google.com/uc?export=view&id=1dMlEOZ8-cp7NGldIa9muABZcNm91Q1gw",
            "https://drive.google.com/uc?export=view&id=1cxRSgcNqBZiYddzeBYqVP64EaBkCHgW7",
            "https://drive.google.com/uc?export=view&id=1d2lGAFOTMlb9-Uyc_QDu9EofQSrKs89-",
            "https://drive.google.com/uc?export=view&id=1d51uiWKxv-zur9b3_Hu1TqraWk3wo7Q7",
            
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
                "kesan": "Bisnismen banget",
                "pesan": "Sukses terus bang pitchingnya",
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
                "kesan": "Lucuu pake topi",
                "pesan": "Semangat kaka usahanya", 
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
                "kesan": "Asprak awak",
                "pesan": "Semangat ngaspraknya bang, bismillah nilai A", 
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
                "kesan": "keren parah ngerangkulnya",
                "pesan": "Semangat capoku", 
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
                "kesan": "Namanya sama kek cakahim",
                "pesan": "Semangat abang", 
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
                "pesan": "Semangat pitchingnya", 
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
                "kesan": "keren",
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
            "https://drive.google.com/uc?export=view&id=1WeC0SNDTXWca0InAUbzxEeYPTvCN9OO5",
            "https://drive.google.com/uc?export=view&id=1JRCroxXa9pjfKejhAI-wziuHOwfNF_ql",
            "https://drive.google.com/uc?export=view&id=1KANJmnLqhZZBaPl6lxI-UlbVTNqtKueD",
            "https://drive.google.com/uc?export=view&id=1K8qMVQr9IxdXw4Clhd9_8XEjgqc0rf4V",
            "https://drive.google.com/uc?export=view&id=1JVEuxFKoXEJDWliOJbrN1bOi9TooA7p1",
            "https://drive.google.com/uc?export=view&id=1Jk0P5WzVzkMBBW2jrnPBKJVmSKpqmB0O",
            "https://drive.google.com/uc?export=view&id=1JvDoDzxaMtGm15jp5HkYFo8vlKYw0aN_",
            "https://drive.google.com/uc?export=view&id=1Jhq5BKkpZaLb9X7JJhGtBXidoeKhPyCR",
            "https://drive.google.com/uc?export=view&id=1KBuYzfWSFn7LNuJR6_pbXfrsOf2Etf8z",
            "https://drive.google.com/uc?export=view&id=1K102B3i12I0qwzMoRY-KPRNM-2LHq260",
            "https://drive.google.com/uc?export=view&id=1JjfETiDqx7-5qctLZAVeU1VPDHiin0PE",
            "https://drive.google.com/uc?export=view&id=1JS5Wux9zoaHXq57884ueZGRlqs-ELsP-",
            "https://drive.google.com/uc?export=view&id=1KForphp_FwCv4y8kVmjFPGZBb-mF5znD",
            "https://drive.google.com/uc?export=view&id=1JlJQH0T4NgeIyEnciWCd_XwG-vQAbikf",
            "https://drive.google.com/uc?export=view&id=1K8HNR4KHUqEF7dOIPHqhSHvhkMgpxcRq",
            "https://drive.google.com/uc?export=view&id=1KCpY4Xz_AeGyb4eIeyXEJLZ2Bv221vdI",
            "https://drive.google.com/uc?export=view&id=1KFC4eIF5HjSkhasIZAB8-uRQNTEBdav6",
            "https://drive.google.com/uc?export=view&id=1JYV9EnpgZ8xZBjUiCyJ8_yr2t__WbU9v",
            "https://drive.google.com/uc?export=view&id=1JbSPd8pLTMIJVM4y15q0aYSXVfjB6UNY",
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
                "kesan": "Keren banget pengalamannya banyak",
                "pesan": "Lanjutkan organisasinya",
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
                "kesan": "Asik banget",
                "pesan": "Langgeng terus kak", 
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
                "kesan": "Abangda basketku",
                "pesan": "Selalu rangkul kami ya bang", 
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
                "kesan": "Kakaknya tegas",
                "pesan": "Lancar terus kak acaranya", 
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
                "kesan": "keren banget perencanaannya",
                "pesan": "Selalu wadahi kami ya bang", 
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
                "kesan": "Abangda basketku #2",
                "pesan": "Gass terus basketnya bang", 
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
                "kesan": "Abangnya keliatan gamers",
                "pesan": "Semangat terus bang ngodingnya", 
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
                "kesan": "so pretty",
                "pesan": "Semangat ya kak ngaspraknya", 
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
                "kesan": "kakaknya softspoken",
                "pesan": "Semangat kaka", 
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
                "kesan": "Abangnya terlihat interested",
                "pesan": "Next time saya ajak abang ya kalo ada debat inggris hehe", 
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
                "kesan": "Kece abizz",
                "pesan": "Menangin basketnya ka Vanessss", 
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
                "kesan": "Kakak tegas dan perhatian",
                "pesan": "Stay strong kak", 
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
                "kesan": "Kakaknya jenius",
                "pesan": "semangat kak ngaspraknya", 
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
                "kesan": "akhirnya ada yang sama akamsi",
                "pesan": "Ayo makan bareng di pu bang", 
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
                "kesan": "Abangnya ramah",
                "pesan": "Semangat kuliahnya bang", 
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
                "kesan": "Pernah liat kembarannya",
                "pesan": "Gimana rasanya kembar kak?", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    PSDA()
elif menu == "Departemen MIKFES":

    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oB7Ccag_S__S5-RstN8tqYhdNP7krmzC",
            "https://drive.google.com/uc?export=view&id=1njePqL9bioNnkO5kEJUbnoS8sNVdIOHl",
            "https://drive.google.com/uc?export=view&id=1oCWTrardrwkZgpv4zmqJwE6y0Ktv7S5G",
            "https://drive.google.com/uc?export=view&id=1o4UrciQdTWV65Jkl-maqefIKnDhme0HI",
            "https://drive.google.com/uc?export=view&id=1oCZKMnbdR3FaomjhCrh8KElsmxyUjbkB",
            "https://drive.google.com/uc?export=view&id=1nlVT-9jbBgslxHFyg9GNworjpdH7utGF",
            "https://drive.google.com/uc?export=view&id=1o7EMyCh2P8j8MAtaL2zu6gcFxYzpqcKv",
            "https://drive.google.com/uc?export=view&id=1oDFJ7YyBgLL3sHNaiVddrO4Nh-gsRHZf",
            "https://drive.google.com/uc?export=view&id=1njjkExqZLixR19yBtEv4yhme0gLOqF_2",
            "https://drive.google.com/uc?export=view&id=1njgioWkZXAak61PWYeuWhl0NNmPj2v28",
            "https://drive.google.com/uc?export=view&id=1oI4Ov9nZT7n-s21VKsW_CzY8MCwPeNSV",
            "https://drive.google.com/uc?export=view&id=1oELhaNGpzLDex7djTYGc0d6l53ACY5FM",
            "https://drive.google.com/uc?export=view&id=1o38Dv_50LqOBq5SrBhl7fj7S8_TheUji",
            "https://drive.google.com/uc?export=view&id=1nrZF7h7Y1wP8dgdLp8p_LH2W9FRsTCCF"
            "https://drive.google.com/uc?export=view&id=1o00WV_7w-c3p2XkTWXT6rPwrWPbVIW1j",
            "https://drive.google.com/uc?export=view&id=1oKBQG1uFMHbj3SkeIlQCCyP9jzf4o-yu",
            "https://drive.google.com/uc?export=view&id=1o1zCSmr6E39UASLD-B21_ikUqtHGJwOx",
            "https://drive.google.com/uc?export=view&id=1nmYYUq64Ow2WqYS_7mBA5OwF10OXJAJe",
           
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
                "kesan": "Sangat santai dan memotivasi",
                "pesan": "Terus pantau perkembangan akademik kami bang",
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
                "kesan": "Wih kembar",
                "pesan": "Semangat kaka dan kembarannya", 
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
                "kesan": "Sangat merangkul",
                "pesan": "Next time cariin saya partner debat lagi ya bang hehe", 
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
                "kesan": "asprakk dan pj tugasku",
                "pesan": "Semangat ngaspraknya bang, ajarin ya bang hehe", 
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
                "kesan": "pinter banget kakanya",
                "pesan": "semangat ngaspraknya kak", 
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
                "kesan": "penutor matdas tpb 2",
                "pesan": "long time no see kak", 
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
                  "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20 Tahun",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr ",
                "kesan": "ketemu lagi bang hehe",
                "pesan": "next time panitia bareng lagi ya bang",
                "jabatan": "Staff Divisi Survei dan Riset",
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
                "kesan": "Baik dan pendiem abangnya",
                "pesan": "next time panitia bareng lagi ya bang", 
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
            "https://drive.google.com/uc?export=view&id=1kDhvI4FygZCzI1CcGiX2OjGxYOfl1DaK",
            "https://drive.google.com/uc?export=view&id=1kLH4FW8n0N2dmhY_R6FXIasVibBg0DkJ",
            "https://drive.google.com/uc?export=view&id=1kg1UfnJMDe11JJcC7PAqLYyZgunBFj0p",
            "https://drive.google.com/uc?export=view&id=1lyDC21c_Ba9lDWBNfY3Q-TzNPyWk05f5",
            "https://drive.google.com/uc?export=view&id=1xuPf6PDdTn2aKXmNGn5pM5y8VU9QHhn_",
            "https://drive.google.com/uc?export=view&id=1kUSHT738WMqiQ2yv15exdoHxpw2PehY1",
            "https://drive.google.com/uc?export=view&id=1kaPUaFrquqVkesOAzg8l7fknicDIrxkj",
            "https://drive.google.com/uc?export=view&id=1E47KBuQr_yVnRdN9XUV9JkZi8PUqi7so",
            "https://drive.google.com/uc?export=view&id=1kTdjN5zsODuuO2i7_78RhWd5Z0CRIU_I",
            "https://drive.google.com/uc?export=view&id=1kSi9Qf3oh1FricueE9XJdCTwGINRu-zY",
            "https://drive.google.com/uc?export=view&id=1kZmDQg7dhvdgQphTxH0FwhOB5gxjuc_L",
            "https://drive.google.com/uc?export=view&id=1lwu0BDGw1S5zIug25qVST17lMevmJC3k",
            "https://drive.google.com/uc?export=view&id=1kC_2MkqZNUAFqlIKBth8wr-Sj9qEW0Zi",
            "https://drive.google.com/uc?export=view&id=1k53n-DzsQE2kwjnHGMjWQCe5ORMyJ0qf",
            "https://drive.google.com/uc?export=view&id=1lx06ozyJVDQK577MTi05n79c9hxoayka",
            "https://drive.google.com/uc?export=view&id=1kwR5wKOVVv_4SFaJ-gH6EPIfVQoE2Htl",
            "https://drive.google.com/uc?export=view&id=1bCvsAxeNgW-GUbgXLADyJ-gvYUf6mGcL",
            "https://drive.google.com/uc?export=view&id=1bGU2BDbpHuTZzSP9FfmWSi22geTIgD-7",
            "https://drive.google.com/uc?export=view&id=1l-LXZsnc6ECRMOE-g769MsVgTwmwvxhg",
            "https://drive.google.com/uc?export=view&id=1k1Kfa4kjRH3iJcVgbmEwOOKIqrhMs56l",
            
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
                "kesan": "Abangnya solutif, selalu menjawab pertanyaan kami dengan baik",
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
                "kesan": "abang basket ku",
                "pesan": "ajarin basket lagi ya bang", 
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
                "nama": "Raid Muhammad Naufa",
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
            "https://drive.google.com/uc?export=view&id=1SpAbMWNAPpbgHs4WZB8AWzTNs28eoeM-",
            "https://drive.google.com/uc?export=view&id=1ScTDpJxwb4wLXaDG3tCzATVbH0uLbKJv",
            "https://drive.google.com/uc?export=view&id=1SViPEu60uBbJ7y6g9VM6OOqMjlXutFTy",
            "https://drive.google.com/uc?export=view&id=1St89jog7IcptOPqp9wvD5Sd3-M3125kf",
            "https://drive.google.com/uc?export=view&id=1Sh2UsKZ2NA5WBRT563zWVVJDoF9xTJwr",
            "https://drive.google.com/uc?export=view&id=1Szm19LsiqqhaEYn2boTYBAafedvJtxaB",
            "https://drive.google.com/uc?export=view&id=1SoFyXbX_mu1cgcJw66kiGjhYZfWIpug6",
            "https://drive.google.com/uc?export=view&id=1SbbAvUsR5aLDLA3QX7kQoHe1BSiyE_4t",
            "https://drive.google.com/uc?export=view&id=1SUhy2UR5Fp_D_d-VKkdPhuNHM0HT7B6Q",
            "https://drive.google.com/uc?expor t=view&id=1Scgets7laqQYzMVSh6pnSd81RVCUAZ67",
            "https://drive.google.com/uc?export=view&id=1ShsRcE93jy-pcx_bVAlOZtuOjFdFbUE8",
            "https://drive.google.com/uc?expor t=view&id=1SlwNCnl_R17LhZw2WQJ7iubdE197-t4n",
            
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
                "kesan": "keren pengalaman dan cita-citanya",
                "pesan": "Selalu naikan nama HMSD bang",
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
                "nama": "M. Akbar Restika",
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
            "https://drive.google.com/uc?export=1Xa-vrffToS8ato-ZCQObD_XwHNYwq84Q",
            "https://drive.google.com/uc?export=1Bl0apqUyqMcveR78KNK-tlL1c6Ev6oYN",
            
            
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


