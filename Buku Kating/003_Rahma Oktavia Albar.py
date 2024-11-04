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
            st.write(f"Jabatan: {data_list[i]['jabatan']}")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gM3XwdLzI6lQ5Mvi8ixpMeJxWvLtjTR1",
            "https://drive.google.com/uc?export=view&id=1iDdUznI0pTbLoUhbCNm1YRBmCom7mdmb",
            "https://drive.google.com/uc?export=view&id=1gJFRhZKQwhznEG9HCsEOmhFPDIZV_R-2",
            "https://drive.google.com/uc?export=view&id=1gMcsr8CgmtOTYwylQvrFiE9VZZbAE1hH",
            "https://drive.google.com/uc?export=view&id=1gN0FCBuy1JW_-3vzWIdbmT58FCd8KM-J",
            "https://drive.google.com/uc?export=view&id=1gNhVYg8rcuJtwQuyRCa_4EtSgtc5IHnr",
        ]
        data_list =   [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Denger Musik",
                "sosmed": "@gumilangtkharisma",
                "kesan": "Public speaking abangnya keren",
                "pesan": "Semangat jadi Kahim bang",
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
                "kesan": "Kakaknya lucu banget",
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
                "kesan": "Kakaknya keren",
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
                "pesan": "semangat bang kuliahnya", 
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
                "kesan": "Kakaknya keren",
                "pesan": "sukses untuk perkuliahannya kak!", 
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
                "kesan": "Kakaknya pintar",
                "pesan": "semoga kakaknya selalu bahagia",  
                "jabatan" : "Bendahara 1", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_WvkQYhb6g10WXTr8BjT7Y-2cpRJgkLB",
            "https://drive.google.com/uc?export=view&id=1_H38EDfJcB0OieFBZoPm5JV0SDRmTuwU",
            "https://drive.google.com/uc?export=view&id=1_9jeW6TutB4TsYDl1NNPwvg1FuDUjjfJ",
            "https://drive.google.com/uc?export=view&id=1_TEv-1fzy35aDhrSAh381EttqcNQa1zw",
            "https://drive.google.com/uc?export=view&id=1_ObzRq3HvsPksRrthwTcdxXE98D1qa0_",
            "https://drive.google.com/uc?export=view&id=1_M7FiCiweLm7HM3GX1aSxh9G0FwD2cPz",
            "https://drive.google.com/uc?export=view&id=1_Y4-m0cl_bsvrcViv_njaiRZyZ50-hWq",
            "https://drive.google.com/uc?export=view&id=1_A00ioQJONePiv44kjvsXwbCZEUZtbjj",
            "https://drive.google.com/uc?export=view&id=1_j7u-DRindiugV92R4qsY_64gtn7NccR",
            "https://drive.google.com/uc?export=view&id=1_MqxQpc1jdFBlTctXHQV37LkCfbWj7Qk",
            "https://drive.google.com/uc?export=view&id=1_6XAumKRzJnyI4Wsjmaevu56tgshuOFc",
            "https://drive.google.com/uc?export=view&id=1_eNenuUr8gxiOfu14-s4AuFvPZ2FYWli",
            "https://drive.google.com/uc?export=view&id=1_JoMdQUrCDF_GpVgaFKf_NC4Vmt93Aha",
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
                "kesan": "Kak Tri bisa mengatur sikap ramah dan tegas di kondisi tertentu",
                "pesan": "Tetap jadi orang baik kakk Tri!",
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
                "kesan": "Kak Annisa ceria dan humble",
                "pesan": "Semangat kuliahnya juga sehat selalu kakak", 
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
                "kesan": "Senyum kak Wulan sangat cantik dan hangat",
                "pesan": "Semoga hari kak Wulan selalu menyenangkan dan penuh keberkahan", 
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
                "kesan": "Kakaknya positif vibes sekali dan penuh semangat",
                "pesan": "Jangan putus asa disetiap proses yang kakak jalani", 
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
                "kesan": "Kak Claudhea punya senyum yang cantik",
                "pesan": "Terus kejar apapun yang menjadi impian kakak", 
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
                "kesan": "Bang Fachrul terlihat tenang namun juga tegas",
                "pesan": "Jaga kesehatan dan tetap bekarya bang", 
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
                "kesan": "Kakaknya sangat berenergi, ramah",
                "pesan": "Selalu bangkit dan semangat dari jatuh bangunnya kehidupan yang kakak alami", 
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
                "kesan": "Abangnya humoris dan bisa menyebarkan keceriaan",
                "pesan": "Jangan pernah ragu dengan seluruh pilihan yang abang jalani", 
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
                "kesan": "Kak Renisha memiliki antusiasme yang tinggi",
                "pesan": "Selalu semangat di perkuliahan kak", 
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
                "kesan": "Abangnya baik",
                "pesan": "Sehat selalu bang", 
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
                "kesan": "Kakaknya selalu tersenyum, dan bersemangat",
                "pesan": "Semoga bahagia selalu kak", 
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
                "kesan": "Kakaknya asik sekali",
                "pesan": "Pertahankan ibadahnya kak, selalu semangat dalam menjalankan perkuliahan", 
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
                "kesan": "Abang Jeremi penuh energik, aktif, selalu excited dan fokus dalam mengerjakan apapun yang menjadi tanggung jawabnya",
                "pesan": "Jaga kesehatan dan tetap jadi seseorang yang selalu aktif dan bahagia, jangan lupa istirahat juga bang", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Senator":

    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TU0slUYvSBMdX4NL6oTCOcZ9LL0w_GHW",
            "https://drive.google.com/uc?export=view&id=1D6geIwOyjxqdMi6_PNtT8FyvOIZs08kR",
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "Kak Annisa bisa jadi humble dan tegas dimomen tertentu, publik speaking kakaknya keren",
                "pesan": "Jangan lupa bahagia kak",
                "jabatan" : "Senator", #1
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Bintang sangat tegas, bijaksana juga",
                "pesan": "Semangat kuliahnya bang", 
                "jabatan" : "Tim senator", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        senator()
elif menu == "Psda":

    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GAT54aX_Ju-CjEc6Qzwrm29C2Idh1IS6",
            "https://drive.google.com/uc?export=view&id=1L_TRm5K-izREME8g-MrA3WjkyHQbY204",
            "https://drive.google.com/uc?export=view&id=1MIEWmzamFbCxlaoAXXJYrqAOEH_DS8LU",
            "https://drive.google.com/uc?export=view&id=1McXdMtSbihHbknqKvTLZDZn-Gn6SX93Y",
            "https://drive.google.com/uc?export=view&id=1Lt09Ffsgx_O8gMtS32PVHl7LGo_hiw9q",
            "https://drive.google.com/uc?export=view&id=1MIGAchCP1li0K877oYBhVrSfn3IW6RSk",
            "https://drive.google.com/uc?export=view&id=1MNMUeDKfUoVUyqX2I07iWl5y5HBXDUMB",
            "https://drive.google.com/uc?export=view&id=1MEtDO3yTucJhqRI1_msfsmFphrqJnWM4",
            "https://drive.google.com/uc?export=view&id=1Mev-acFbcfViTBNUkz7W98pDo8gZL8h8",
            "https://drive.google.com/uc?export=view&id=1MOc-0TRzIfidryXL2NbbI-HRh5Gr1zCn",
            "https://drive.google.com/uc?export=view&id=1MG0QE1tVCIzoxvBZCX2Cy5nEMUvI1Bq2",
            "https://drive.google.com/uc?export=view&id=1LoI7FVcdR0JrBbFv1vmlI2IJsZw3g44a",
            "https://drive.google.com/uc?export=view&id=1M_GE0RXa_2LVNnddpp2p5OTCAt8YcKaj",
            "https://drive.google.com/uc?export=view&id=1MMGIOPTk0B4SrisbD7eNd5l8eS4ULp30",
            "https://drive.google.com/uc?export=view&id=1MOx407WVOMEzkVUmu3B79p4ZmjJ-FAd_",
            "https://drive.google.com/uc?export=view&id=1M1NV_KQphdDMMl4Xh-H1fbGEcTltg0vi",
            "https://drive.google.com/uc?export=view&id=1LzlGskXPAsT44gi3JHa2r209m8Wigv8y",
            "https://drive.google.com/uc?export=view&id=1Lzdx6HVlkBQsk4myGQ4Kl-dY6raeI4lz",
            "https://drive.google.com/uc?export=view&id=1MC006cQ8O6BW8GoP6NC337wOtHySKt7o",
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Bang Ericson memiliki public speaking yang bagus",
                "pesan": "Sehat selalu bang",
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
                "kesan": "Kak Elisabeth sangat ceria",
                "pesan": "Bahagia selalu kak, kejar semua impian kakak", 
                "jabatan" : "Sekretaris Departemen PSDA", # 1
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal": "Riau",
                "alamat": "Pulau Damar ",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Bang Deyvan humble",
                "pesan": "Selalu semangat ditengah jatuh bangunnya kehidupan bang", 
                "jabatan" : "Kepala Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter-muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak afifah baik namun juga berwibawa",
                "pesan": "Jaga kesehatan kak, selalu bersemangat mengejar tujuan kakak", 
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
                "kesan": "Bang Farhan sangat bijak dan mengayomi sekali",
                "pesan": "Semangat kuliahnya bang, jangan lupa istirahat sejenak", 
                "jabatan" : "Kepala Divisi Olahraga dan Perlombaan", # 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Johannes sangat tangguh, dan tegas",
                "pesan": "Jaga kesehatan bang, jangan lupa apresiasi diri sendiri", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main Game",
                "sosmed": "@kemasverii",
                "kesan": "Bang Kemas sangat pintar", 
                "Pesan" : "Selalu optimis dalam mengejar impian bang",
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "Nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "Kak Presilia sangat ceria dan cantik", 
                "Pesan" : "Sehat selalu ya kak",
                "jabatan" : "Bendahara Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kak Rafa humble", 
                "Pesan" : "Jangan lupa apresiasi diri sendiri kak",
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "Nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Bang Sahid keren sekali", 
                "Pesan" : "Semangat menjalani semester 5 bang",
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kak Vanessa keren, karismatik jugaa", 
                "Pesan" : "Selalu bahagia ya kak",
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "Kakaknya tegas dan humble", 
                "Pesan" : "Sehat selalu kak Allya",
                "jabatan" : " Staff Divisi Kaderisasi", # 1
            },
            {
                "Nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty cantik, humble.", 
                "Pesan" : "Selalu bahagia kak, teruslah mengejar impian kakak",
                "jabatan" : " Staff Divisi Kaderisasi", # 1
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Abangnya humoris dan juga tegas sekali dibeberapa kondisi", 
                "Pesan" : "Semangat bang mengejar tujuan abang",
                "jabatan" : " Staff Divisi Kaderisasi", # 1
            },
            {
                "Nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "122450041 ",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "Kakaknya sangat ceria", 
                "Pesan" : "Semangat kak kuliahnya, jangan patah smangat",
                "jabatan" : " Staff Divisi Kaderisasi", # 1
            },
            {
                "Nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "  Abangnya keren sekali", 
                "Pesan" : "Semangat bang dengan tugas kuliahnya",
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
            {
                "Nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kak Jaclin sangat baik, ramah", 
                "Pesan" : "Semangat kak kuliahnya, terus kejar impian",
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Bang Rafly tegas namun juga baik", 
                "Pesan" : "Sehat selalu bang, jangan patah semangat",
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_ ",
                "kesan": "Kakaknya cantik, positif vibes sekali",
                "pesan": "Selalu semangat dengan segala impian kakak", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ]

        display_images_with_data(gambar_urls, data_list)
        psda()
elif menu == "Departemen Mikfess":

    def mikfess():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aSFy_3pzZS6nP8N2V-ocp8YBJfXsS_E2",
            "https://drive.google.com/uc?export=view&id=1aJRYRxJ9dVCzs9N_vK6MS_h9LA03witC",
            "https://drive.google.com/uc?export=view&id=1aTM907qRsSpPYQ7K16Wk57v6akObW4TL",
            "https://drive.google.com/uc?export=view&id=1_ya6pouMdrphXeL98NCfVETZzMuuf_FH",
            "https://drive.google.com/uc?export=view&id=1aSzWchZNKUyAMlesIloH_W2Yvm-_n8g8",
            "https://drive.google.com/uc?export=view&id=1a9Mh5rW_ZK7945GDdX9lDyFnJFI5uof2",
            "https://drive.google.com/uc?export=view&id=1aGDhnSzjZrSqNWowRl2gfBaU94IIqghP",
            "https://drive.google.com/uc?export=view&id=1_rx4wmBHmWMyWMpOquAZYn9bzX4UaPRg",
            "https://drive.google.com/uc?export=view&id=1_sMyyg8TdkrL_buQm2EDuR6BRU0rOSrv",
            "https://drive.google.com/uc?export=view&id=1_ydCtVTp1zA-QEBoDvc_ugTYEnO0prqi",
            "https://drive.google.com/uc?export=view&id=1_rkCeUqShrzvxeYb61fh2EffijivtRWX",
            "https://drive.google.com/uc?export=view&id=1a4ygP_3lxyA9gYae17XSsYZXEyNB6q3J",
            "https://drive.google.com/uc?export=view&id=1aA4e5iX_naP2TEuU5h4YIKSFWkca5NfP",
            "https://drive.google.com/uc?export=view&id=1aAqqV1wZ3eZRGLsbY_i0cqOz01OHJF7u",
            "https://drive.google.com/uc?export=view&id=1a-9c1QMNyyc05Hk6YHVNCyGEO4vc1enZ",
            "https://drive.google.com/uc?export=view&id=1_wYJjhXkmD1BRppzhVGcVAc50ErSHqsh",
            "https://drive.google.com/uc?export=view&id=1a3LrJP9FFVt-Uyn1fEXZZjHfSH6o5O4d",
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
                "kesan": "Abangnya keren",
                "pesan": "Jaga kesehatan bang",
                "jabatan" : "Kepala Departement", #1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakaknya baik",
                "pesan": "Selalu semangat kak dalam kuliah", 
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
                "kesan": "Abangnya keren sekali",
                "pesan": "Selalu semangat bang dalam menjalani kehidupan ", 
                "jabatan" : "Staff Divisi Club dan Komunitas", # 1
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung ",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya energik",
                "pesan": "Selalu sehat dan bahagia", 
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
                "kesan": "Abangnya sangat pintar dan humble",
                "pesan": "Selalu sehat bang dan jangn lupa untuk selalu bersemangat", 
                "jabatan" : "Staff Divisi Club dan Komunitas", # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakaknya cantik sekali",
                "pesan": "Selalu happy kak", 
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
                "kesan": "Abangnya sangat keren dan penuh semangat",
                "pesan": "Sukses kuliahnya bang", 
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
                "kesan": "Abangnya pintar dan sangat mengayomi",
                "pesan": "Sukses kuliahnya bang, jangan lupa istirahat", 
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
                "kesan": "Kak Deva sangat ramah",
                "pesan": "Jangan lupa bahagia kak", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "",
                "sosmed": "@dindanababan_",
                "kesan": "Kak Dinda sungguh ceria",
                "pesan": "Selalu bahagia setiap harinya kak", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Marleta sangat cantik, baik",
                "pesan": "Selalu penuh semangat kak menjalani hari", 
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
                "kesan": "Kakaknya baik, cantik, selalu penuh energik",
                "pesan": "Sehat selalu kak", 
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
                "kesan": "Kakaknya humble",
                "pesan": "Selalu bahagia kak", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Abangnya berwibawa dan penuh semangat",
                "pesan": "Sukses selalu diperkuliahan bang", 
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
                "kesan": "Abangnya sangat bersemangat",
                "pesan": "Sehat dan selalu bahagia bang", 
                "jabatan" : " Staff Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Abangnya pintar sekali",
                "pesan": "Selalu semangat dengan jatuh bangunnya kehidupan", 
                "jabatan" : " Staff Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya sangat cantik",
                "pesan": "Selalu semangat dalam menggapai impian", 
                "jabatan" : " Staff Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Selalu happy seperti namanya",
                "pesan": "Semangat selalu dalam mengejar impian", 
                "jabatan" : " Staff Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya ramah, baik,sangat bersemangat dan pintar sekali.",
                "pesan": "Semangat selalu dalam mengejar impian bang Randaaa", 
                "jabatan" : " Staff Divisi Survei dan Riset", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        mikfess()
elif menu == "Departemen Eksternal":

    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZmDZ2d3cLQisw2bx7F3atV9DbykcPK9X",
            "https://drive.google.com/uc?export=view&id=1ZibGy4V7E8U0-6TcELvO6AvvylxbZQXn",
            "https://drive.google.com/uc?export=view&id=1Zyearsh4z7fw4ISHJSXqj0z51IBJ48cR",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1ZtFcuR2TPuPTy8wTr1KXVDrLsYU-GYpc",
            "https://drive.google.com/uc?export=view&id=1ZuxwqcVoDA7uYopXp8N4Q-S2V03YiaKN",
            "https://drive.google.com/uc?export=view&id=1ZkbN7bWqS4K30ERFfJJhDUdIkRaqgxJG",
            "https://drive.google.com/uc?export=view&id=1_14bmoJ3o_usodYfjrK3GVwsSaT7WNp-",
            "https://drive.google.com/uc?export=view&id=1ZoOOQitq33kbFXM-Wj5otJjWlmlz-Tuc",
            "https://drive.google.com/uc?export=view&id=1gihhpSzqENUfkTkOr7NmOfkzShZwfEcM",
            "https://drive.google.com/uc?export=view&id=1Zcc2P2C7mfB619IUsBpF0_7znYYxAkHs",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1ZjvEZUqeg1mVERxQNoY3auTj_hgU24wT",
            "https://drive.google.com/uc?export=view&id=1bmScgDFtlNSZGd6OaJeGTsWzSZYAkXIs",
            "https://drive.google.com/uc?export=view&id=1bsc3jfLVW1AIFq7Gn6zuW62XwBfrB7ef",
            "https://drive.google.com/uc?export=view&id=1ZguPyTQDiOXnKbrBc5C6o3X6-Vn0UiMY",
            "https://drive.google.com/uc?export=view&id=1ZX6LAKveRdlrUJQjkYhxsGGPMROiCAyl",
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
                "kesan": "Abangnya keren",
                "pesan": "Jangan lupa bahagia banggg",
                "jabatan" : "Kepala Departement", #1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakaknya sangat ceria",
                "pesan": "Sukses selalu kak", 
                "jabatan" : "Sekretaris Departement", # 1
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri ",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya sangat humble",
                "pesan": "Sukses selalu kak dalam perkuliahan", 
                "jabatan" : " Kepala Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abangnya baik sekali",
                "pesan": "Sukses selalu kuliahnya di semester 5 ini bang", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea cantik,ceria, sangat mengayomi",
                "pesan": "Sukses selalu kuliahnya di semester 5 ya kak, jaga kesehatan", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": " 122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kak esteria sangat lemah lembut",
                "pesan": "Jangan lupa istirahat kak",
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": " 122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15 ",
                "kesan": "Kak Natasya senyumnya manis sekali",
                "pesan": "Jangan lupa selalu bersyukur di setiap harinya kakk",
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Novelia Adinda",
                "nim": " 122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya sangat ceria",
                "pesan": "Selalu semangat dalam semua impian kakak",
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": " 122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya positif vibes",
                "pesan": "Selalu semangat kuliah kak",
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Tobias David Manogari",
                "nim": " 122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya tegas namun juga peduli",
                "pesan": "Selalu semangat kuliah bangg, jangan lupa istirahat sejenak",
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Yohana Manik",
                "nim": " 122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Humble bangett",
                "pesan": "Selalu semangat dengan jatuh bangunnya kehidupan",
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": " 121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya keren",
                "pesan": "Selalu bahagia dengan pilihan abang",
                "jabatan" : "Kepala Divisi Pengabdian Masyarakat", # 1
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi ",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana ",
                "kesan": "Abangnya keren dan bijaksana",
                "pesan": "Selalu bahagia dengan pilihan abang",
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
                "kesan": "Kak Uyi sangat keren dan cantik",
                "pesan": "Selalu bahagia kakkkk",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat ", # 1
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": " Q Time",
                "sosmed": "@chlfawww ",
                "kesan": "Kakak cantik",
                "pesan": "Selalu bahagia kakkkk",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat ", # 1
            },
            {
                "nama": " Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya keren",
                "pesan": "Selalu bahagia bang",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat ", # 1
            },
            {
                "nama": " Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": " Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "kakaknya cantik",
                "pesan": "Selalu bahagia kak",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat ", # 1
            },
            {
                "nama": " Khaalishah Zuhrah Alyaa Vanefi",
                "nim": " 122450034 ",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": " Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "kakaknya cantik sekalii",
                "pesan": "Selalu bahagia kak",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat ", # 1
            },
            {
                "nama": " Raid Muhammad Naufal",
                "nim": " 122450027 ",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Abangnya humbble",
                "pesan": "Selalu bahagia bang",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat ", # 1
            },
            {
                "nama": "Tria Yunanni",
                "nim": " 122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya keren",
                "pesan": "Selalu bahagia kakk",
                "jabatan" : "Staff Divisi Pengabdian Masyarakat ", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        eksternal()
elif menu == "Departemen Internal":

    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VTilddP5YaygZixOReB07LLiAN57k7_2", #bang dimas
            "https://drive.google.com/uc?export=view&id=1UUnrbewmv-rJodP8HEEmRT4Bcb26Abho", #kak chaterine
            "https://drive.google.com/uc?export=view&id=1UpnM5ow3JbKrurcIWrBZive75yzn4R3I", #bang akbar
            "https://drive.google.com/uc?export=view&id=1VMV8Mx-3c8Zd6VemlcYdDS_6GagKlH3l", #kak renta
            "https://drive.google.com/uc?export=view&id=1VPu8h-lU7a9FpF_B-wHeKMk_afWIOdSV", #kak salwa
            "https://drive.google.com/uc?export=view&id=1Uw4Qw2TmFp1GrUArTXQ9ULombL_aGFjp", #bang rendra
            "https://drive.google.com/uc?export=view&id=1VVwMFdiogGwROcIla02GtvYrr2I2Yzyy", #bang yosia
            "https://drive.google.com/uc?export=view&id=1UouphWS-qshzrnhaqLMVlwlc1FMiqTpT", #bang ari
            "https://drive.google.com/uc?export=view&id=1V_I1b-8lFWKbst2GUL897MlN_VF9D5hq", #bang joshua
            "https://drive.google.com/uc?export=view&id=1VN89GV2NTVoT5Y2HN6-oexnQAEHQyz7j", #kak azizah
            "https://drive.google.com/uc?export=view&id=1VQHeNGqEO84e9HcQonYcC0t80s3DZuaU", #kak meira
            "https://drive.google.com/uc?export=view&id=1VTdFTvDVx44UW9Gr1j4LxPhrFnu-xtZS", #bang rendi
            
            
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
                "kesan": "Public speakingnya keren",
                "pesan": "Semangat gapai impian bang",
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
                "kesan": "kakaknya humble",
                "pesan": "Semangat kuliahnya bang", 
                "jabatan" : "Sekretaris Departemen Internal", # 2
            },
            {
                "nama": "Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Abangnya asik",
                "pesan": "Semangat bang kuliahnya", 
                "jabatan" : "Kepala Divisi Keharmonisasian", # 3
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakak humble",
                "pesan": "Jangan lupa istirahat kak", 
                "jabatan" : "Staff Keharmonisasian", # 4
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakak cantik sekali",
                "pesan": "Semangat kak kuliahnya", 
                "jabatan" : "Staff Keharmonisasian", # 5
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abangnya humble",
                "pesan": "Jangan berhenti menjadi orang baik bang", 
                "jabatan" : "Staff Keharmonisasian", # 6
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Abangnya sangat keren",
                "pesan": "Jangan lupa bahagia kak", 
                "jabatan" : "Staff Keharmonisasian", # 7
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abangnya tenang, kalem",
                "pesan": "Semangat bang semoga baik dunia dan akhiratnya", 
                "jabatan" : "Kepala Divisi Kerohanian", # 8
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Abang tenang namun asik",
                "pesan": "Semangat bang kuliahnya", 
                "jabatan" : "Staff Kerohanian", # 9
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": " kakaknya keren sekali",
                "pesan": "Semangat menjadi orang baik bang", 
                "jabatan" : "Staff Kerohanian", # 10
            },
             {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meiralsty_",
                "kesan": "Kakak sangat tenang",
                "pesan": "Semangat terus yah kak ", 
                "jabatan" : "Staff Kerohanian", # 11
            },
             {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Abangnya humble,baik, mengayomi, tidak pernah marah",
                "pesan": "Semangat menjadi daplok bang, jangan pernah lelah dengan kami bang", 
                "jabatan" : "Staff Kerohanian", # 12
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    internal()
elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1a_fc261uHsqyZwx-Xp5kB-hlhdIaT8P0", #bang andrian
            "https://drive.google.com/uc?export=view&id=", #kak adisty
            "https://drive.google.com/uc?export=view&id=", #kak nabila
            "https://drive.google.com/uc?export=view&id=", #bang danang
            "https://drive.google.com/uc?export=view&id=", #bang farel
            "https://drive.google.com/uc?export=view&id=", #bang ahmad
            "https://drive.google.com/uc?export=view&id=", #kak tessa
            "https://drive.google.com/uc?export=view&id=", #kak nabilah
            "https://drive.google.com/uc?export=view&id=", #kak elia
            "https://drive.google.com/uc?export=view&id=", #bang dhafin
            
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
                "kesan": "Bang Andrian sangat inspiratif, bisa tenang dan tegas diberbagai kondisi",
                "pesan": "Jangan terlalu keras pada diri sendiri dan jaga kesehatan bang",
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
                "kesan": "Kakak ramah orangnya",
                "pesan": "Semangat kak, semoga lancar kegiatan kuliah dan di SSDnya", 
                "jabatan" : "Sekretaris Departemen SSD", # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kece abiezz bener-bener calon pengusaha",
                "pesan": "Semangat kak kegiatan KWU nya", 
                "jabatan" : "Kepala Divisi KWU", # 3
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Abang asyik banget, cocok di KWU",
                "pesan": "Semangat bang ikut lombanya ", 
                "jabatan" : "Staff KWU", # 4
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": " 122450110",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Ga espect kalo abang di divisi KWU hehe soalnya jadi kapo suporteran",
                "pesan": "Jangan berkurang ya bang semangatnya buat KWU ataupun suporteran hehe", 
                "jabatan" : "Staff KWU", # 5
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukitting",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang pendiem dan kalem ",
                "pesan": "Semangat bang kuliahnyaa", 
                "jabatan" : "Staff KWU", # 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak orangnya ramah adan ceria ",
                "pesan": "Semangat kak kuliah dan organisasinya", 
                "jabatan" : "Staff KWU", # 7
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kece abiezz jadi kadiv sponshorhip",
                "pesan": "Semangat kak, terutama buat nyariin sponsor buat acara HMSD kita", 
                "jabatan" : "Kepala Divisi Sponsorship", # 8
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kakak orangnya seru keknya",
                "pesan": "Semangat kak menjalani kegiatannya", 
                "jabatan" : "Staff sponsor", # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": " Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang kalem yah?",
                "pesan": "Woop semangatt bang kuliahnya", 
                "jabatan" : "Staff sponsor", # 10
            },
           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()
elif menu == "MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oh3rDMGc-FmZ6g6KIp0N0lQhWg4S-_vl",
            "https://drive.google.com/uc?export=view&id=1ohhXu_O0ZsmtEDcZuyXsIPzOVfhUINbg",
            "https://drive.google.com/uc?export=view&id=1nfbPMTBlk31QAsZEgGw4BOCRO5jOHBJw",
            "https://drive.google.com/uc?export=view&id=1oUmDqaqPfFF6DlEbDA8BrinmsKpPgg0y",
            "https://drive.google.com/uc?export=view&id=1oUfxKbxxO8gEWIhWitosFaW9Ht3HnyWN",
            "https://drive.google.com/uc?export=view&id=1o3DoJheLzXOTjHkEPwJgmAjBWOP4dNLA",
            "https://drive.google.com/uc?export=view&id=1ntDX8m0AGL6-v3mx9Z2Suo1Nj6Q-JVo6",
            "https://drive.google.com/uc?export=view&id=1oYK6pwRARYDXmri1kRuiYwi0Uo4mnqKx",
            "https://drive.google.com/uc?export=view&id=1nyl0idv655ClY4u5NYghM0EoHlFiP6KM",
            "https://drive.google.com/uc?export=view&id=1oANg7paizXX7kpefyttrzIMqsVPZ5x8l",
            "https://drive.google.com/uc?export=view&id=1o1p05c7u17bHOarPtwtLaEqXufKiTTsE",
            "https://drive.google.com/uc?export=view&id=1nf-lga1sA0RwcKf5jyMuoWOTfbcQZYK0",
            "https://drive.google.com/uc?export=view&id=1od-PJsRYHaTR_Em3BfgvR0R9ycVAvXei",
            "https://drive.google.com/uc?export=view&id=1on7DBFm_OIm3OmPg6Vq4uZe-FzG11HoL",
            "https://drive.google.com/uc?export=view&id=1o_Yb7EAIGWydkYC98WicgO_EY0-S504k",
            "https://drive.google.com/uc?export=view&id=1o3Rh_ouOlpp67DWr95ekyyxT8_SS7L3K",
            "https://drive.google.com/uc?export=view&id=1oqFNc-c6q4BLIbwt4Eb3ZC43aOlZ4zKH",
            "https://drive.google.com/uc?export=view&id=1okxI73otukgCTBq-C-S2xpW7lFEa7nAj",
            "https://drive.google.com/uc?export=view&id=1naUo-YoZtOk3gdqBKK3Harg_CvuOrZgb",
          
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
                "kesan": "abangnya punya sikap kepemimpinan yang baik, abangnya bisa serius dan ramah di kondisi yang diperlukan",
                "pesan": "Sehat selalu bang",
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
                "kesan": "Kak Elok sangat baik, beliau bisa jadi seseorang yang tenang dan menebarkan aura positif",
                "pesan": "Jangan lelah menjadi orang baik kak, kakak luar biasa dengan segala usaha kakak untuk menggapai mimpi", 
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
                "kesan": "Kakak penuh keberanian dan sangat inspiratif",
                "pesan": "semangatt selalu kak kadiv media & konten, teruslah bekarya kak, jangan putus semangat dengan apapun yang dikejar", 
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
                "kesan": "Abangnya tegas, bisa jadi ramah juga",
                "pesan": "Sehat selalu bang Kaisar, dan jangan biarkan kegagalan menghentikan abang", 
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
                "kesan": "Abangnya sangat sabar dan telaten dalam mengajarkan sesuatu, memancarkan aura ketenangan juga",
                "pesan": "semangat bang kuliah, ngasprak, dan segala kegiatan abang, namun jangan lupa untuk beristirahat sejenak", 
                "jabatan" : "Kepala Divisi Visual Desain", # 1
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakaknya sangat cantik, percaya diri, dan ceria",
                "pesan": "Semangat ngonten kakak, jangan lupa untuk apresiasi diri sendiri setelah melakukan segala kegiatan kakak", 
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
                "kesan": "Kak Eka selalu punya cara unik dan asik dalam berkomunikasi",
                "pesan": "Bahagia selalu kak, jangan takut untuk mencoba hal baru", 
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
                "kesan": "Kakaknya punya aura tegas namun sangat ramah dalam berbicara",
                "pesan": "Bahagia selalu kak, teruslah bersinar dengan semua impian kakak", 
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
                "kesan": "Cantik banget kakaknya seperti namanya, kak Patricia punya senyum yang bisa menular ke orang lain",
                "pesan": "Sukses selalu kak, teruslah menjadi seseorang yang percaya diri", 
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
                "kesan": "Kak Rahma sangat ceria, dan humble dengan semua orang",
                "pesan": "Nama depan kita sama kak, sehat sehat ya kak, kakak hebat dengan segala kreativitas kakak", 
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
                "kesan": "Kakaknya sangat komunikatif",
                "pesan": "Jangan menyerah dalam hal apapun, teruslah bersemangat dalam mengejar impian", 
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
                "kesan": "Kakaknya asik, positif vibes",
                "pesan": "Selalu semangat dalam mengejar mimpi kak", 
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
                "kesan": "Bang Gymnastiar keren, apalagi jika berfoto sambil memegang tutup kamera seperti digambar, sangat mencerminkan anggota PDD",
                "pesan": "Semangat dan optimis terus dengan segala impian abang", 
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
                "kesan": "Kakaknya punya semangat yang sangat besar, antusiasme juga",
                "pesan": "semangat kuliahnya kak, semoga hidup kakak selalu penuh kebaikan dan keberkahan", 
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
                "kesan": "Abangnya sangat humble",
                "pesan": "Selalu bahagia Bang Abit, teruslah membuat hidup abang lebih bewarna", 
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
                "kesan": "Bang Akmal bisa bersikap tenang dan energik dikondisi tertentu",
                "pesan": "Sehat selalu bang Akmal, jangan pernah ragu dengan pilihan abang", 
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
                "kesan": "Keren abangnya kayak linkedln abangnya",
                "pesan": "Sukses selalu bang, teruslah melangkah lebih jauh untuk menggapai impian abang", 
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
                "kesan": "Kakaknya inspiratif dan penuh semangat",
                "pesan": "Happy terus ya kak, semangat dengan segala kreativitas baru", 
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
                "kesan": "Kakaknya cantik, sangat antusias dengan berbagai hal",
                "pesan": "Selalu semangat dengan segala impian kakak, jangan mudah menyerah kakak", 
                "jabatan" : "Staff Divisi PDD", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

