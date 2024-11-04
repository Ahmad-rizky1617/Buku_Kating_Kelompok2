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
            st.write("  ")
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
            "https://drive.google.com/uc?export=view&id=",
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
                "nim": "122450033",
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
            }
            {
                "Nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg"
                "kesan": "Kak Presilia sangat ceria dan cantik", 
                "Pesan" : "Sehat selalu ya kak",
                "jabatan" : "Bendahara Divisi Manajemen Minat dan Bakat", # 1
            }
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla"
                "kesan": "Kak Rafa humble", 
                "Pesan" : "Jangan lupa apresiasi diri sendiri kak",
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            }
            {
                "Nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana"
                "kesan": "Bang Sahid keren sekali", 
                "Pesan" : "Semangat menjalani semester 5 bang",
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            }
            {
                "Nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__"
                "kesan": "Kak Vanessa keren, karismatik jugaa", 
                "Pesan" : "Selalu bahagia ya kak",
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            }
            {
                "Nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__"
                "kesan": "Kak Vanessa keren, karismatik jugaa", 
                "Pesan" : "Selalu bahagia ya kak",
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            }
            {
                "Nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_"
                "kesan": "Kakaknya tegas dan humble", 
                "Pesan" : "Sehat selalu kak Allya",
                "jabatan" : " Staff Divisi Kaderisasi", # 1
            }
            {
                "Nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana"
                "kesan": "Kak Eksanty cantik, humble.", 
                "Pesan" : "Selalu bahagia kak, teruslah mengejar impian kakak",
                "jabatan" : " Staff Divisi Kaderisasi", # 1
            }
            {
                "Nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_"
                "kesan": "Abangnya humoris dan juga tegas sekali dibeberapa kondisi", 
                "Pesan" : "Semangat bang mengejar tujuan abang",
                "jabatan" : " Staff Divisi Kaderisasi", # 1
            }
            {
                "Nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "122450041 ",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda"
                "kesan": "Kakaknya sangat ceria", 
                "Pesan" : "Semangat kak kuliahnya, jangan patah smangat",
                "jabatan" : " Staff Divisi Kaderisasi", # 1
            }
            {
                "Nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa"
                "kesan": "  Abangnya keren sekali", 
                "Pesan" : "Semangat bang dengan tugas kuliahnya",
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            }
            {
                "Nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_"
                "kesan": "Kak Jaclin sangat baik, ramah", 
                "Pesan" : "Semangat kak kuliahnya, terus kejar impian",
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            }
            {
                "Nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd"
                "kesan": "Bang Rafly tegas namun juga baik", 
                "Pesan" : "Sehat selalu bang, jangan patah semangat",
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            }
        ]

        display_images_with_data(gambar_urls, data_list)
        psda()
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
                "jabatan" : "Anggota Divisi PDD", # 1
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

    medkraf()  

# Tambahkan menu lainnya sesuai kebutuhan
