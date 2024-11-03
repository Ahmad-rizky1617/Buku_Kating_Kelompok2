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
            "Medkraf",
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
            "https://drive.google.com/uc?export=view&id=1KigidBoxqCQFKjbnCJaGhcBHQNAIkj_R_",
            "https://drive.google.com/uc?export=view&id=1javxwN58k5pP9s13dkCY0Kb0_SX1UUoR",
            "https://drive.google.com/uc?export=view&id=1ZQmloglh13t3bISyQ9tnB4CsmfbXnY1t",
            "https://drive.google.com/uc?export=view&id=10oFD_etmz-IrXNHmDN4ocZOep67IBfCC",
            "https://drive.google.com/uc?export=view&id=1DDMkd8mhdVTGGgLsnoqwIcz7xnx0UDYz",
            "https://drive.google.com/uc?export=view&id=1swTSXxL-bbX_Xy17tjlAobTKwS2YrKS2",
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
                "kesan": "abang keren dan asik banget orangnya",
                "pesan": "Semangat bang kuliahnya",
                "jabatan" : "Ketua himpunan",  # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": " 121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abang lucu bikin ketawa mulu",
                "pesan": "semangat bang kuliahnya,", 
                "jabatan" : "Sekretaris Jendral", # 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "kakak juga asyik orangnya",
                "pesan": "pokoknya semangat kak",  
                "jabatan" : " Sekretaris Umum" # 3
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Denger Musik",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak kayaknya orangnya pendiam dan suka ngitungin uang ",
                "pesan": "semangat terus kak kuliah dan ngurusin keuangan",
                "jabatan" : "Bendahara umum",  # 4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh, Sumatra Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak keliatannya rajin orangnya",
                "pesan": "semangat kak menjalanihari-harinya", 
                "jabatan" : "Sekretaris 1", # 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "1214500030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Baca",
                "sosmed": "@nadillaandr26",
                "kesan": "kakak keliatan rajin dan pintar",
                "pesan": "semangat kak kuliahnya, sukses selalu",  
                "jabatan" : "Bendahara 1", # 6
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1puMLChxw5ZN_UolemtLaX6WXV43YXFVf",
            "https://drive.google.com/uc?export=view&id=1EZZY7_mYTeDu7ejDfmiBczsY9g_bYJQF",
            "https://drive.google.com/uc?export=view&id=1zDPGFCASJrpKVu6gCCv97oQXbogUIlnN",
            "https://drive.google.com/uc?export=view&id=18oWdS293oxuuPOLGMy4OwZJZMVSpiLiy",
            "https://drive.google.com/uc?export=view&id=11S9NHIw4FgI84Nm64654L0_DiAGIQalw",
            "https://drive.google.com/uc?export=view&id=1G83Uaag3YP_jsW9Du1UlaeVbYIXRLh42",
            "https://drive.google.com/uc?export=view&id=1jhGRJ6wzqLzJAgBlVVKYyZjojELxW5Z3",
            "https://drive.google.com/uc?export=view&id=13nq9-0Df8jEDZ7hlTv1Syr2F71Cbi2Tq",
            "https://drive.google.com/uc?export=view&id=19gEoEcv-5lHzR8h0FkJkd02_EUXkdABW",
            "https://drive.google.com/uc?export=view&id=1oyir-aqZkTlEXa5TBAxDFgcAyB7uGwXN",
            "https://drive.google.com/uc?export=view&id=1ngQ1Nr0n1d_h3zFC-6JkzpLbb9NW1XQx",
            "https://drive.google.com/uc?export=view&id=1Qfessx7WHWYxM2K0SsaEpgzTJNgsXQU5",
            "https://drive.google.com/uc?export=view&id=1FDySwxCdXiRrsbOMV4WRMEo119fvKkDK",

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
                "kesan": "Kakak keren banget,ramah, asyik dan baik",
                "pesan": "semangat kak kuliah dan organisasinya",
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
                "kesan": "Masyaallah kakak",
                "pesan": "Cuma bisa bilang semangat ke kakak", 
                "jabatan" : "Sekretaris", # 2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "wlsbn0",
                "kesan": "kakak orangnya ramah",
                "pesan": "semangat ya kak", 
                "jabatan" : "Bendahara", # 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450021",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": " @anisadini10",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "semangat terus kuliahnya kakak", 
                "jabatan" : "Kepala Komisi 1 Legislatif", # 4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": " @dylebee",
                "kesan": "keren banget kak hobinya",
                "pesan": "semangat ya kak kuliahnnya apalagi pp", 
                "jabatan" : "Kepala Komisi 2 Aspirasi dan Pengawasan", # 5
            },
            {
                "nama": "Muhammad Fachrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Sholat Malam",
                "sosmed": "@fhrul.pdf",
                "kesan": "Masyaallah sekali abang ini rajin solat malam",
                "pesan": "tetep rajin solat malamnya yah bang", 
                "jabatan" : "Kepala Komisi 3 Media Legislatif", # 6
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kalianda",
                "hobbi": "Membaca Al waqiah setiap magrib",
                "sosmed": " @ansftynn_",
                "kesan": "Manis dan asyik kakak",
                "pesan": "semangat kak kuliahnya, terus hobinya ditambah kak bacaan  surahnya", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 7
            },
            {
                "nama": "Feryadi Yulius ",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "keliatan humoris bang",
                "pesan": "semangat kuliahnya bang, ditambah lagi solat sunahnya", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 8
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-Qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "MasyaAllah  hobinya",
                "pesan": "Semangat kuliahnya, semoga selain cumlaude jadi hafidz quran juga", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 9
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya baik, kalem",
                "pesan": "Semangat kuliahnya bang", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", # 10
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20 tahun",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": " @_.dheamelia",
                "kesan": "Kakak orangnya organisasi banget",
                "pesan": "Semangat kak buat nyari sinyal di gedung f nya", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", # 11
            },
            {
                "nama": " Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Masyaallah kak definisi seimbang dunia akhirat",
                "pesan": "semangat kuliahnya kak, ibadahnya semoga ga kendor", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 12
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Bilabong",
                "hobbi": "Cerita",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang keren banget, dan baik suka ngasih motivasi",
                "pesan": "semangat bang kuliahnya, semoga lulus dengan hasil terbaik", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 13
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()
elif menu == "Senator":

    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id"
            "https://drive.google.com/uc?export=view&id",
            
            
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
                "kesan": "Prinsip hidup kakak keren banget ",
                "pesan": "Semangat kakak, semoga dipermudah urusannya",
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
                "kesan": "Publik speaking abang keren bangett",
                "pesan": "Semangat bang, semoga cepet lulus", 
                "jabatan" : "Tim Senator", # 2
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    senator()
elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "Publik speaking abang bagus banget, abang juga suka memotivasi lagi",
                "pesan": "Semangat kuliahnya bang",
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
                "kesan": "Kakak orangnya seru dan lucu abis, jadi pencair suasana",
                "pesan": "jangan pernah cape jadi orang asyik ya kak", 
                "jabatan" : "Sekretaris Departemen PSDA", # 2
            },
            {
                "nama": "Deyvan Loxefal ",
                "nim": "121450148",
                "umur": "21",
                "asal": "Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang orangnya lucu abiezz",
                "pesan": "Semangat bang kuliahnya, ayukk biar cepat lulus", 
                "jabatan" : "Kepala Divisi Manjakat", # 3
            },
            {
                "nama": " Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Suka banget sama kakak, bisa tegas dan juga asyik ",
                "pesan": "Semangat kak kuliahnya, semoga sukses", 
                "jabatan" : "Kepala Divisi Kaderisasi", # 4
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Suka banget sama cara abang memotivasi kita dengan berbagi pengalamannya",
                "pesan": "Semangat kuliahnya bang, dan semoga dipermudah segala urusan di Divisi ini", 
                "jabatan" : "Kepala Divisi Olahraga dan Perlombaan", # 5
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "JL. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abang powerfull banget, kaya gapunya capek",
                "pesan": "Terus semangat yah bang, biar kita praktikum dan suporterannya juga semangat", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 6
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main game",
                "sosmed": "@kemasverii",
                "kesan": "abang kece banget jago ngoding",
                "pesan": "Semangat bang, makasi banyak tutornya ", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 7
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan":"Kakak keren banget",
                "pesan": "Semangat kak kuliahnya, semoga dapet hasil yang terbaik ", 
                "jabatan" : "Bendahara Divisi Manajemen Minat dan Bakat", # 8
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak orangnya asyik",
                "pesan": "Semangat kak kuliah dan organisasinya", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 9
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Abang keliatannya ramah",
                "pesan": "Semangat bangg", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 10
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kakk keren banget main basketnya",
                "pesan": "semangat selalu kakk", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 11
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak keren banget, bisa se tegas itu",
                "pesan": "Semangat kak kuliahnya, semoga sukses selalu", 
                "jabatan" : "Staff Divisi Kaderisasi", # 12
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": " 122450001",
                "umur": "20",
                "asal": " Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak baik, tegas juga",
                "pesan": "Tetap semangat yah kak", 
                "jabatan" : "Staff Divisi Kaderisasi", # 13
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Abang orangnya baik",
                "pesan": "Semangat bang kuliah dan kaderin kitanya", 
                "jabatan" : "Staff Divisi Kaderisasi", # 14
            },
            {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "1224500418",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "Wah ternyata sama-sama orang lamtim",
                "pesan": "jangan menyerah ya kak", 
                "jabatan" : "Staff Divisi Kaderisasi", # 15
            },
            {
                "nama": "Gede Moena",
                "nim": " 121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang keliatannya agak pendiam yah",
                "pesan": "semangat terus yah bang", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 16
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": " Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakak orangnya baik",
                "pesan": "Semangat kak menjalani hari-harinya", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 17
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang keliatannya baik dan ramah",
                "pesan": "Kuliahnya yang semangat yah bang", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 18
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Masyaallah kak hobinya",
                "pesan": "semangat kak kuliahnya", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    PSDA()
elif menu == "Departemen MIKFES":

    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
           
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
                "kesan": "Abang keren, kelihatan orang akademik banget hehe",
                "pesan": "Semangat bang akademik dan organisasinya",
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
                "kesan": "Kakak orangnya baik dan ramah",
                "pesan": "Semangat kak jadi sekretarisnya", 
                "jabatan" : "Sekretaris Departemen", # 2
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang juga keren",
                "pesan": "Semangat bang di CK nya", 
                "jabatan" : " Staff Divisi Club dan Komunitas", # 3
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abang baik dan ramah",
                "pesan": "Semoga lancar segala urusannya bang", 
                "jabatan" : "Staff Divisi Club dan Komunitas", # 4
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame ",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "abang keliatannya ramah dan seru",
                "pesan": "Always semangat ya bang", 
                "jabatan" : "Staff Divisi Club dan Komuitas", # 5
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak keren abiezz",
                "pesan": "Semangat kak kuliahnyaa", 
                "jabatan" : "Staff Divisi Club dan Komunitas", # 6
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "abang keknya sepuh akademik nih hehe",
                "pesan": "Semangat terus bang, rajin belajar", 
                "jabatan" : "Kepala Divisi Pusat Inovasi dan Kajian Akademik", # 7
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Keknya abang humoris dan asyik, sepuh mtk nih",
                "pesan": "Semangat yah bantuin kita ngerjain tugas kader", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 8
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak orangnya baik",
                "pesan": "Semangat kak di PIKA nya", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 9
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "-",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak agak pendiem yah keknya",
                "pesan": "Semangat kuliah dan kepengurusan di PIKA", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 10
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurna",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak orangnya ramah dah positif vibes banget",
                "pesan": "Semangat terus kak", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 11
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya ",
                "pesan": "Bahagia terus ya kakak", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 12
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " 121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Suhu Figma nih keknya abang",
                "pesan": "Semangat terus bang bimbing kami magang di SNR nya", 
                "jabatan" : "Kepala Divisi Survei dan Riset", # 13
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Suhu Figma nih keknya abang",
                "pesan": "Semangat terus bang bimbing kami magang di SNR nya", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 14
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak yang baik dan cantik",
                "pesan": "Semangat kak bimbing kami di SNR", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 15
            },
             {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abang keknya seru nih orangnya",
                "pesan": "Semangat bangg", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 16
            },
             {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Keren abiezz bang",
                "pesan": "Semangat bang mengejar akademiknya", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 17
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    mikfes()
elif menu == "Departemen Eksternal":

    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            
            
            
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
                "kesan": "Suka banget sama public speakingnya abang",
                "pesan": "Semoga diperlancar bang segala urusannya",
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
                "kesan": "Kakak keren banget",
                "pesan": "Tetap semangat menjalani hari-hari kuliah kak", 
                "jabatan" : "Sekretaris Departement", # 2
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Suka banget sama kakak, ketawanya sangatt mencairkan suasana",
                "pesan": "Jangan cape ketawa ya kak heheh", 
                "jabatan" : "Kepala Divisi Hubungan Luar", # 3
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Wow hobi kit sama bang",
                "pesan": "Semangat bang kuliahnya!", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak daplokku yang cantik, baik dan sabar seluas samudra",
                "pesan": "Semangat kak kuliahnya dan jangan pernah cape sama kelakuan anakmu ini yah", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 5
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kakak orangnya asyik",
                "pesan": "Semangat kakak,tetep bahagia terus ya", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 6
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Kakak sepuh coding ini kayaknya",
                "pesan": "Semangat terus kakk", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Seperti kakak-kakak hublu lainnya, kakak juga ga kalah asyik dan positif vibes orangnya",
                "pesan": "Semangat terus kak dalam menyebarkan kebahagiaan", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Wow anti mainstream hobinya",
                "pesan": "Semangat kak kuliah dan organisasinya", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang yang selalu enerjik kalau suporteran",
                "pesan": "Gasss bang, makin ditambah lagi semangatnya kalo mimpin suporteran", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 10
            },
             {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakak agak kalem?",
                "pesan": "Sukses selalu kak di dalam hal apapun", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 11
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