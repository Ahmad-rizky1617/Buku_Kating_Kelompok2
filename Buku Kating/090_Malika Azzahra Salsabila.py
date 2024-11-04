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
            "https://drive.google.com/uc?export=view&id=1i6rbcXoN86IQHNuArUf__lBo4v4af1Pk",
            "https://drive.google.com/uc?export=view&id=1i8BSOuORT9BVUUQdgE12odjBD8BvT8Ce",
            "https://drive.google.com/uc?export=view&id=1iL0rv4ORMWLqTfwCNx9FCYE5Lahh3kxU",
            "https://drive.google.com/uc?export=view&id=1hvF1kUvyoHtB5zYZBTHI7gZy8xeHiSCm",
            "https://drive.google.com/uc?export=view&id=1i9wqwwGhcH7Pa0eknLrralx3iS33SBI3",
            "https://drive.google.com/uc?export=view&id=1i-yqM7HMJ4ifGfhCGUEWDx4SeB106dNZ"
        
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
                "kesan": "Sikap dan cara komunikasi abangnya kerenn",
                "pesan": "Semoga lancar kuliahnya dan cepet lulus bang",
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
                "kesan": "Abangnya humoris dan memberi banyak motivasi",
                "pesan": "semangat terus kuliahnya bang", 
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
                "kesan": "Kakaknya keren plus lucu bangettt",
                "pesan": "Semangat kuliahnya kakk, semoga cepat lulus kak",  
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
                "kesan": "Kakaknya kerennn",
                "pesan": "Semangat kuliahnya kakk semoga lancar terus",
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
                "kesan": "Kakaknya keren plus cantik",
                "pesan": "Semangat kuliahnya kakk", 
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
                "kesan": "Kakaknya kerenn",
                "pesan": "semangat kak kuliahnya, sukses selalu",  
                "jabatan" : "Bendahara 1", # 1
            },




        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14aWUXOQhawK30YrTOFfCxk6W7neeBrj6",
            "https://drive.google.com/uc?export=view&id=1-gPWRbhZsXQEQo0OezZ_WiAxiUickSq3",
            "https://drive.google.com/uc?export=view&id=1CLAFt9aAmepOXQY4LiY3qoPWPq0mC_hx",
            "https://drive.google.com/uc?export=view&id=1iFdg2D1mnLrkJiEmDdUPq-ht6SN4hwbM",
            "https://drive.google.com/uc?export=view&id=14ORAdig59jK1bgw7FfMod_FuYBBuFtyb",
            "https://drive.google.com/uc?export=view&id=1ojZb4KUxi195fpNYhdqfvs61J7M6tVrS",
            "https://drive.google.com/uc?export=view&id=1S-3mIWKFYFGkuF61tYCGShEIW4QLQnz7",
            "https://drive.google.com/uc?export=view&id=1-PiIt-vY6f7HtCRLgK-8UjBF5YWHNa0S",
            "https://drive.google.com/uc?export=view&id=14cimgZRX8x6JJanS6BWQSzojcORDbLMJ",
            "https://drive.google.com/uc?export=view&id=17AEzbMR15XV_qxEOncrLBc4ZtdzS3PQA",
            "https://drive.google.com/uc?export=view&id=19pgXjsyBhCN7C01SR4oausZj7XeBaH8B",
            "https://drive.google.com/uc?export=view&id=1u89Ten3mppCehekr68ZrM2-nAOQ_945o",
            "https://drive.google.com/uc?export=view&id=1R2QXxnRbmBsepjXGe8g11vHt8Go-jZgn",
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
                "kesan": "Kakaknya keren, cantik, ramah, dan baik",
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
                "kesan": "Nama kakaknya keren banget, orangnya juga cantik",
                "pesan": "Semangat terus kuliahnya kakk", 
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
                "pesan": "Semangat kuliahnya bang", 
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
                "pesan": "Semangat kuliahnya kak, tetap baik hati kak", 
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
                "kesan": "Abangnya kerenn ramah jugaa",
                "pesan": "Semangat terus kuliahnya bang, semoga lulus tepat waktu", 
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
                "kesan": "Kakaknya lucuu, keren jugaa",
                "pesan": "Semangat kuliahnya kakakk", 
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
                "pesan": "Semangat kuliahnya bang, semoga lancar sampai lulus", 
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
                "kesan": "Kakaknya kerenn ramah jugaa",
                "pesan": "Semangat kuliahnya kak, Semoga lancar sampai luluss", 
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
                "kesan": "Abangnya kerenn, wejangannya juga bermanfaat",
                "pesan": "semangat kuliahnya bangg, lancar terus kuliahnya", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "Senator":

    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uVBfu3GSOjl5Wp8hRof-KLYlfNIJaLlH",
            "https://drive.google.com/uc?export=view&id=1uQuKwN5XL9V8F6taP-sbQUGMIMOUV5c_",
            
            
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
                "kesan": "Kakaknya keren banget, public speakingnya juga bagus ",
                "pesan": "Semangat kakk semoga lancar kedepannya",
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
                "kesan": "Abangnya keren, public speakingnya juga bagus",
                "pesan": "Semangat terus untuk kedepannya bang semoga makin kerenn", 
                "jabatan" : "Tim Senator", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    senator()

elif menu == "Departemen PSDA":

    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tQeXf65cVW73xrcpObBaYW8fCa1_fspu",
            "https://drive.google.com/uc?export=view&id=1tXxr6d4QbSlt6a6vlgsfgnag7hPjTF5O",
            "https://drive.google.com/uc?export=view&id=1tMR6VCkyyErpzjhbxqEWWMZzeBfVp8FH",
            "https://drive.google.com/uc?export=view&id=1uFRgJKB8L-Z20_xwBHOyTALDknPcpY-u",
            "https://drive.google.com/uc?export=view&id=1u-VXBjlEep7wh-Snjd1W-_thbYkxrCoj",
            "https://drive.google.com/uc?export=view&id=1u2bXbvdXhThS_xFsLkaMpV209q2AtFo7",
            "https://drive.google.com/uc?export=view&id=1th5wfVLmp09hQPyBL9dezkG7Lj9OXUDd",
            "https://drive.google.com/uc?export=view&id=1tsNiM-mgJ8eEEsdNmN7y96qcAhOeb6op",
            "https://drive.google.com/uc?export=view&id=1tn0KPGKuKv5ocOylpvqzPb6oU6A3H4YR",
            "https://drive.google.com/uc?export=view&id=1tHAQqqQWgtugV5oG8IyYKX0TecuiPpyi",
            "https://drive.google.com/uc?export=view&id=1uBf1nHHPSreec_VKgw6921H7guQ0eqo0",
            "https://drive.google.com/uc?export=view&id=1uMpPqdrEBmDTpUgBis2BOJP0pwrfhu5Y",
            "https://drive.google.com/uc?export=view&id=1u425iviO9QZKM7r452sMettKZ6pj4qCi",
            "https://drive.google.com/uc?export=view&id=1tc181wQGPzYPuULJTrhQQVr7V7wr4Tfm",
            "https://drive.google.com/uc?export=view&id=1uF4M7KglZNuQdjXEj1oUzKSlN0KoZi9y",
            "https://drive.google.com/uc?export=view&id=1uIzZBZHjMEK0ifKtPwEunQv4PhCizdmY",
            "https://drive.google.com/uc?export=view&id=1uEAeQgEgPq3vDx5J0qAGylWaEmTLI2iX",
            "https://drive.google.com/uc?export=view&id=1uPteg3e_q8_3DT4cBnjvMf9zO73jZ2M9",
            "https://drive.google.com/uc?export=view&id=1uKaw3nvaylX_U9Lus02kVsaEwvUcXvFh",
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
                "kesan": "Abangnya keren",
                "pesan": "Semangat bang, semoga makin sukses kedepannya",
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
                "kesan": "Abangnya keren baik juga",
                "pesan": "Semangat bang, sukses terus", 
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
                "kesan": "Kakaknya cantik dan berkarisma sekaliii",
                "pesan": "Sukses terus kedepannya kak", 
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
                "kesan": "Abangnya keren banget",
                "pesan": "Sukses terus kedepannya bang", 
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
                "kesan": "Abangnya keren, asik juga",
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
                "kesan": "Abangnya keren tapi pendiem",
                "pesan": "Sukses terus kedepannya bang", 
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
                "kesan": "Music taste kita sama kakk",
                "pesan": "Sukses terus kedepannya kak", 
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
                "kesan": "Kakaknya baik, ramah jugaa",
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
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semangat kuliahnya bang, sukses selalu", 
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
                "kesan": "Kakaknya keren bangett, baik jugaa",
                "pesan": "Sukses terus kakk, ayo main bareng ;)", 
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
                "kesan": "Kakaknya keren dan berwibawa",
                "pesan": "Semangat kuliahnya kak, sukses terus", 
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
                "pesan": "Semangat terus kak, sukses selalu", 
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
                "kesan": "Abangnya humble dan asik",
                "pesan": "Semangat kuliahnya bang, sukses terus", 
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
                "pesan": "Semangat kuliahnya kak, sukses selalu", 
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
                "kesan": "Abangnya ramah dan baik",
                "pesan": "Semangat kuliahnya bang, sukses terus", 
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
                "kesan": "Kakak keren bangettt, baik dan ramah jugaa",
                "pesan": "Semangat terus kakk, kapan kapan ayo ngobrol lagi", 
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
                "pesan": "Semangat kuliahnya bang, sukses terus", 
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
                "pesan": "Sukses selalu kak", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    PSDA()

elif menu == "Departemen MIKFES":

    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yWrblSM4YA_FMGiebvaOkj7vDDXC2pGO",
            "https://drive.google.com/uc?export=view&id=1z-gCLTQ0ajlnDhKbQgeMZi4X5k_NbK9T",
            "https://drive.google.com/uc?export=view&id=1yXcz1Ajxsm51gP2zTTDJLLJMcp3bSG0g",
            "https://drive.google.com/uc?export=view&id=1zMd1BP5tfQvhg8ngiHLX4uPWy0Ncshxi",
            "https://drive.google.com/uc?export=view&id=1yaQ8IvUZgqwhno4bmOURFBB7bC-k-AbA",
            "https://drive.google.com/uc?export=view&id=1yvCVrSqvsRDTNYkXmN_ooTX8qNBfUAF8",
            "https://drive.google.com/uc?export=view&id=1yXDp9nvcG4VkSSIR6iy99PEMsv_-ppGI",
            "https://drive.google.com/uc?export=view&id=1yfqYOVTkCMoNcF5lQsDaQa3ILjvuLQ3i",
            "https://drive.google.com/uc?export=view&id=1yhNC-M3YK0qtiuWStCdQGMJ9EP5k9O1c",
            "https://drive.google.com/uc?export=view&id=1yyytDf4VuGJzitKr_cUZu0uqKVe8ytPo",
            "https://drive.google.com/uc?export=view&id=1ycKcctg9wwdmQJ_D9cFs4wEfgnI4OjLi",
            "https://drive.google.com/uc?export=view&id=1yjRWUhcoX96nxTfTmZ7Q3X5p1YpY0uON",
            "https://drive.google.com/uc?export=view&id=1yiihgmaFiLr2pEPKHUUlcRIYpBSxKgHO",
            "https://drive.google.com/uc?export=view&id=1zOxvk7vaqTNfgdDeEIKGOyy649biUVAF", 
            "https://drive.google.com/uc?export=view&id=1zJ1HFx8JX8_2e3gThjS_SbVf1aX45bh4",
            "https://drive.google.com/uc?export=view&id=1zVcisGsPNB4gayPBVDS1Nx3UzgCFxz1N",
            "https://drive.google.com/uc?export=view&id=1z3rbKZ98fsL2fQSCYSv-Mm1gRWm4VRPr",
            "https://drive.google.com/uc?export=view&id=1zPmt6X8shDZZVb2H4QgoB8WZnJ-EwO_C",
            "https://drive.google.com/uc?export=view&id=1zMk_Aj2pTHI71wjIgMVRyH6XZa3lDBIH",
           
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
                "pesan": "Semangat kuliahnya bang, sukses terus",
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
                "pesan": "Semangat kuliahnya bang, sukses terus", 
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
                "pesan": "Sukses selalu bang", 
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
                "pesan": "Semangat kuliahnya bang, sukses terus", 
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
                "pesan": "Semangat kak semoga sukses selalu", 
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
                "pesan": "Semangat kuliahnya bang, sukses terus", 
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
                "pesan": "Sukses selalu kak", 
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
                "kesan": "Kakak keren banget, ramah juga",
                "pesan": "Semangat terus kak, sukses selalu kedepannya", 
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
                "kesan": "Kakaknya baik hati dan keren banget",
                "pesan": "Semangat kuliahnya kak, sukses terus", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya baik, cantik, dan keren banget",
                "pesan": "Semangat kuliahnya kak, sukses terus", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik",
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " 121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Abangnya keren",
                "pesan": "Sukses selalu bang, terus memberi motivasi kepada kami", 
                "jabatan" : "Kepala Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Aditya Rahman",
                "nim": " 122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abangnya keren",
                "pesan": "Semangat kuliahnya bang, sukses selalu", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Abangnya keren dan baik banget",
                "pesan": "Sukses selalu bang, semangat kuliahnya", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
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
                "pesan": "Semangat kuliahnya bang, sukses terus", 
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
                "pesan": "Semangat kuliahnya kak, sukses terus", 
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
                "pesan": "Semangat kuliahnya bang, sukses terus", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    mikfes()

elif menu == "Departemen_Eksternal":

    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vaCsxuvPBXxMtI_n0e-ruAqwH2XND9s9",
            "https://drive.google.com/uc?export=view&id=1ulVT7c8__bB8OqLYvOB7AZACsX80awbK",
            "https://drive.google.com/uc?export=view&id=1vTxd_6chk6RdcvGxazgNz-Ygr5-KgxVr",
            "https://drive.google.com/uc?export=view&id=1mKQWJ2MbItItlvpX61JGwk4RjK7CjOJZ",
            "https://drive.google.com/uc?export=view&id=1vpuMCV_YDxTEvA2Wkl6Z_8-U4V88HECH",
            "https://drive.google.com/uc?export=view&id=1vDQoxrJpcwK8R_wQkobb6HX2A0jdJSDm",
            "https://drive.google.com/uc?export=view&id=1v-oUYqLQ7-kQgatjyWBVwzv3c5u-aJEm",
            "https://drive.google.com/uc?export=view&id=1j-PCcvw7nCG9JeMU7DX_K8vKKEwEJdk5",
            "https://drive.google.com/uc?export=view&id=1vsBRfO1zxIHCCAbK1A0uTM5OGVPXieon",
            "https://drive.google.com/uc?export=view&id=1ujmRt9WVzqtKJ28W8hXrWmJvqyup9YaN",
            "https://drive.google.com/uc?export=view&id=1vhrfk3LfcPWk2IpxRMDwMdRcR0dUcUY0",
            "https://drive.google.com/uc?export=view&id=1gbu8wNNg-7G6IDlFZs3YQQMg4xGc6e_2",
            "https://drive.google.com/uc?export=view&id=1voQ7OkeYArdWMIti6v_DXoxTGSgDHo1r",
            "https://drive.google.com/uc?export=view&id=1usTaiArWmJ125PH1aIksQqzOOA0n3yPR",
            "https://drive.google.com/uc?export=view&id=1zb667RRswUktj6u5QTHg0X9qnNszrHGa",
            "https://drive.google.com/uc?export=view&id=1vjU0SlJWi3Hs9Yk79ap6EQleqNQp3Wom",
            "https://drive.google.com/uc?export=view&id=1zYwzlmYm4Xu68ufASzh8YeYr59MyubXn",
            "https://drive.google.com/uc?export=view&id=1bWItXALZxsCwgeaCccgwH22FLo-QJOgR",
            "https://drive.google.com/uc?export=view&id=1vPHcWF_yOQleEcIBskZoV7uDap4wd3Z1",
            "https://drive.google.com/uc?export=view&id=1ufqk9x5q6-puBUziktjcbY_231cYUyi-",
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
                "kesan": "Abangnya ramah, seru, baik",
                "pesan": "Semangat terus bangg",
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
                "kesan": "Kakaknya lucu plus humble",
                "pesan": "Semangat kuliahnya kak Dhitaa", 
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
                "pesan": "Semangat terus kuliahnya kaakk", 
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
                "kesan": "Abangnya baik, keren juga",
                "pesan": "Semangat terus kuliahnya bang", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": " @deaa.rsn",
                "kesan": "Kakak dea daplok kerennya cosval, baik banget terus lucu juga",
                "pesan": "Semangat terus kuliahnya kak dee, jangan kapok jadi daplok kami ya kak", 
                "jabatan" : "Staff Divisi Hubungan Luar",
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kak ester baik, ramah jugaa",
                "pesan": "Semangat kuliahnya kak Ester", 
                "jabatan" : "Staff Divisi Hubungan Luar",
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "surfing",
                "sosmed": " @nateee__15",
                "kesan": "Manis banget kakaknya, ramah juga, dan terlihat sibuk sekali ya kak",
                "pesan": "Semangat kuliah dan kesibukannya kak, sukses terus", 
                "jabatan" : "Staff Divisi Hubungan Luar", 
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
                "pesan": "Semangat kuliahnya kak, sukses teruss", 
                "jabatan" : "Staff Divisi Hubungan Luar", 
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main Sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Kak Mine baik banget, ramah dan seruu",
                "pesan": "Semangat kuliahnya kak, sukses terus kakk ", 
                "jabatan" : "Staff Divisi Hubungan Luar", 
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatra Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya baik, lucu, dan ramah",
                "pesan": "Semangat kuliahnya bang, sukses terus kedepannya", 
                "jabatan" : "Staff Divisi Hubungan Luar", 
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19 tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": " @yo_annamnk",
                "kesan": "Kakaknya lucu, ramah dan seru banget",
                "pesan": "Semangat kuliahnya kak, ayo ngobrol bareng lagi", 
                "jabatan" : "Staff Divisi Hubungan Luar", 
            },
            {
                "nama": " Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya keren, keliatan kalem dan baik juga",
                "pesan": "Semangat kuliahnya bang, semangat juga bikin portofolionya", 
                "jabatan" : " Kepala Divisi Pengabdian Masyarakat", 
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Abangnya baik",
                "pesan": "Semangat kuliahnya bang, sukses terus kedepannya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", 
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya baik dan ramah sekali",
                "pesan": "Semangat kuliahnya kak, sukses terus", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat",
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Quality Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya baik, ramah juga",
                "pesan": "Semangat kuliahnya kakak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", 
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatra Barat",
                "alamat": "WSukarame",
                "hobbi": "Nonton Youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semangat kuliahnya bang, sukses terus", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat",
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kakaknya baik, Keren juga, btw NIM kita sama kakkk",
                "pesan": "Semangat kuliahnya kak, sukses terus",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", 
            },
            {
                "nama": "Khaalishah Zuhrah Alyss Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semangat kuliahnya kak, sukses teruss", 
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
                "kesan": "Abangnya keren, baik, dan ramah",
                "pesan": "Semangat kuliahnya bang, sukses terus kedepannya", 
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
                "kesan": "Kakaknya lucu, baik, dan ramah jugaa",
                "pesan": "Semangat terus kuliahnya kak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
      ]
        display_images_with_data(gambar_urls, data_list)

    Departemen_Eksternal()

elif menu == "Departemen Internal":

    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TfZeVsGl6tYYLiKk6j-o-Bu0B67uTsXQ",
            "https://drive.google.com/uc?export=view&id=1TNDWES8HUssZ2J1n_7NAtE3zNDSchXEB",
            "https://drive.google.com/uc?export=view&id=1TBsCZDQEOSKg85o4jvYewsqGcI2GrOjU",
            "https://drive.google.com/uc?export=view&id=1TlzO6MMk3lhiqNuk5Dy0UiHL1cAWsaj7",
            "https://drive.google.com/uc?export=view&id=1T_5mzb-wxIfoI1WZMvSCkVCNsXuZ0nXN",
            "https://drive.google.com/uc?export=view&id=1TJihL7EtXR1uULPlJvgR8Uj_XkGNVilC",
            "https://drive.google.com/uc?export=view&id=1Tlernip1_gQZXd-7eMy6aYVMrzJLuwDs",
            "https://drive.google.com/uc?export=view&id=1T2OkqoGhBThxLDx4UU5hrQKo_R_Laals",
            "https://drive.google.com/uc?export=view&id=1T495J5k297WGhaazCCj0pAYGR0P-j71f",
            "https://drive.google.com/uc?export=view&id=1TSr6srR24Ijl9yq8rWJgZCws-GqszZAx",
            "https://drive.google.com/uc?export=view&id=1Tbb354jz2S8svTEm9Mceo902RyBUtXW3",
            "https://drive.google.com/uc?export=view&id=1TcRgQiKkjjOuvq6CzOhWtVqNU0pHEq6r",
            
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
                "kesan": "Keren banget bang Dimas, baik banget juga",
                "pesan": "Sukses terus kuliahnya bang",
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
                "kesan": "Baik sekali kakaknya ramah juga",
                "pesan": "Semangat kuliahnya kakak", 
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
                "kesan": "Abangnya lucu, ramah juga",
                "pesan": "Semangat kuliahnya bang, kasih rekomen dino yang bagus dong bangg, mau jugaa", 
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
                "pesan": "Semangat kuliah dan mancingnya kakk", 
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
                "kesan": "Kakaknya lucuu ramah juga, keren pokoknya",
                "pesan": "Sukses selalu kakk, semangat kuliahnya", 
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
                "kesan": "Abangnya keren, ramah juga",
                "pesan": "Sukses terus bang, sering sering cover lagunya bangg", 
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
                "kesan": "Keren banget abangnya",
                "pesan": "Sukses kuliahnya bang", 
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
                "kesan": "Abangnya keren, baik, dan ramahh",
                "pesan": "Sukses terus kedepannya bang, Semangattt", 
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
                "pesan": "Semangat kuliahnya bang", 
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
                "pesan": "Sukses terus kuliahnya kak", 
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
                "pesan": "Semangat kuliahnya kak, sukses selalu", 
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
                "kesan": "Abang daploknya cosval keren bangett, ramah juga",
                "pesan": "Semangat terus bang Rendi, sukses kuliahnya", 
                "jabatan" : "Staff Kerohanian", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    internal()

elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1a0Uorey9KO991gciyWFY6auEuhC_4RLK",
            "https://drive.google.com/uc?export=view&id=1aGBRFQL4e7x2TI3bx2E34j1BRFxpZK4D",
            "https://drive.google.com/uc?export=view&id=1aV9iluNmiynGUNRK_V6MzLxeDBCr4BXf",
            "https://drive.google.com/uc?export=view&id=1aFfCtSAmwoPvm02M9Lk6CjeKMPQSbOn5",
            "https://drive.google.com/uc?export=view&id=1_rhvnr-dR-AP7ZxXU6s_kXtk8qx-Cpam",
            "https://drive.google.com/uc?export=view&id=1_q2ho55NY5fH0MOCoFO4sEt_o04i6yqB",
            "https://drive.google.com/uc?export=view&id=1aWh40kMFYXg2f8iXyGDkHI8dBoMu8sEm",
            "https://drive.google.com/uc?export=view&id=1_x_YMI4rJKoit144ns5mmiUuXxOApetQ",
            "https://drive.google.com/uc?export=view&id=1_tTqfS1l5xeqyzGhidTQqYMtSx5aOlXy",
            "https://drive.google.com/uc?export=view&id=1a0Qg_Fljff8av3Y76azICXX5WHIaRfRI",
            
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
                "kesan": "Keren banget abangnya",
                "pesan": "Semangat terus bang, sukses kuliahnya",
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
                "kesan": "Kakaknya cantik, keren juga",
                "pesan": "Semangat terus kak, semoga lancar kuliahnya", 
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
                "kesan": "Kakaknya keren, lucu juga terus jago ngitung uang",
                "pesan": "Semangat kuliahnya kak", 
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
                "kesan": "Abangnya keren, brandingnya jagoo",
                "pesan": "Semangat bang sukses terus kedepannya", 
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
                "kesan": "Keren abangnya asik juga dan brandingnya keren sama seperti bang Danang",
                "pesan": "Semangat bang sukses terus kedepannya", 
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
                "kesan": "Abangnya keren, keliatan aktif kepanitiaan juga",
                "pesan": "Semangat bang kuliahnya, sukses terus", 
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
                "pesan": "Semangat kak kuliahnya, sukses terus", 
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
                "kesan": "Kakaknya keren banget",
                "pesan": "Semoga kerennya nular ya kak, sukses terus kak", 
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
                "pesan": "Semangat kuliahnya kak, sukses terus", 
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
                "kesan": "Abangnya keren dan kalem banget",
                "pesan": "Semangat bang kuliahnya, sukses terus", 
                "jabatan" : "Staff sponsor", # 1
            },
           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()

elif menu == "Departemen MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dEtDG2bb_aEJCWkjJOxzL7dI6L6ZaFwA",
            "https://drive.google.com/uc?export=view&id=1dKsSlxpvswpYAiMONtNmCmayZYQfMWzT",
            "https://drive.google.com/uc?export=view&id=1e-Vx_28BPJZ6ovfNQAAUwmaTXaSdFSKQ",
            "https://drive.google.com/uc?export=view&id=1dkzDPZbLAM0cDF38xJywcNkh4D5OIvcv",
            "https://drive.google.com/uc?export=view&id=1dsRp-s-x4sOAm-XKmO9viPqGCkHEKuEI",
            "https://drive.google.com/uc?export=view&id=1dUQGN63zQzuyvdhBtKRS11qRl_yhgg1j",
            "https://drive.google.com/uc?export=view&id=1dbdZGtj6JjB-jIdhpADtG9o6zRQQZmRU",
            "https://drive.google.com/uc?export=view&id=1dGTiPuzu7nE-lPiLuKTt5-bEQEljqcBg",
            "https://drive.google.com/uc?export=view&id=1drga09s0Sf1nXmhV3rhmvZLII7RSiHhx",
            "https://drive.google.com/uc?export=view&id=1dXBvSAlmplfz5TNu3uHXnTS_thCTOKs4",
            "https://drive.google.com/uc?export=view&id=1dNDFAUPBN5R08N6I12rTgaL3O0zdX-9E",
            "https://drive.google.com/uc?export=view&id=1ddkkpNoeazQlpmEjmmrtlgO4GgxUAHHh",
            "https://drive.google.com/uc?export=view&id=1dhcpQJcC_DPOQyq94I9oZIzt49c3JCBW",
            "https://drive.google.com/uc?export=view&id=1dwjnMYFhYZ7QBnUrIlH30pYgydo0oQhN",
            "https://drive.google.com/uc?export=view&id=1dfql2nF6u03F45hIHkPKCeu5gZuI4B5-",
            "https://drive.google.com/uc?export=view&id=1dxEgKxx5eaB7zJNcUF0DxgOy2xMIPloZ",
            "https://drive.google.com/uc?export=view&id=1datETYT3jx184AWR5tdonBFHh-T7aiMx",
            "https://drive.google.com/uc?export=view&id=1dYNsExh0DvlNY-12CZ3ACyheIyAdaZSS",
            "https://drive.google.com/uc?export=view&id=1dqP3OhGgBk2z7q5xs2_aggwIlEgyiktR",
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
                "kesan": "Abangnya asik, kece banget juga",
                "pesan": "Semangat kuliahnya bang, sukses terus",
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
                "kesan": "Manis bangett kakaknya, keren jugaa",
                "pesan": "Semangat terus kakakk, sukses kuliahnya", 
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
                "kesan": "Kakaknya baik, keren dan ramah juga",
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
                "pesan": "Semangat terus bang, sukses kuliahnya", 
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
                "kesan": "Abangnya keren, pasti portofolionya keren jugaa",
                "pesan": "Semangat kuliahnya bang, sukses selalu", 
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
                "kesan": "Kakaknya cantik banget, keren banget juga",
                "pesan": "Semangat kuliahnya kakk", 
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
                "kesan": "Kakaknya cantik, keren juga",
                "pesan": "Sukses terus kak", 
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
                "pesan": "Semangat kuliahnya kakak", 
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
                "kesan": "Kak cia lucu bangett keren jugaa",
                "pesan": "Semangan kuliahnya kak ciaa", 
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
                "kesan": "Kakaknya kerenn, ramah banget",
                "pesan": "Sukses terus kakk", 
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
                "pesan": "Semangat kuliahnya kak", 
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
                "pesan": "Semangat kak dan sukses selalu", 
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
                "kesan": "Abangnya baik dan keren juga",
                "pesan": "Boleh dong bang berbagi ilmu fotografinya", 
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
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semangat kuliahnya kak, sukses selalu", 
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
                "pesan": "Semangat bang, sukses selalu", 
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
                "kesan": "Abangnya keren banget dan sangat humble",
                "pesan": "Semangat kuliahnya bang, semoga isi linkedinnya nular bangg", 
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
                "kesan": "Kakaknya rajin dan ramah sekaliii",
                "pesan": "Semangat kuliahnya kak, sehat selalu", 
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
                "pesan": "Sukses terus kedepannya kak", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    medkraf()
