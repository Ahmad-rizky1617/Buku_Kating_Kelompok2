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
            "https://drive.google.com/uc?export=view&id=1kRpF8CfSwZiOvSbRqOIP0fIWiEl9ZWen",
            "https://drive.google.com/uc?export=view&id=1kN0fl9r_uNuCDkokO6q5pkoR95vAphCw",
            "https://drive.google.com/uc?export=view&id=1kIFH0l5XTEpKWS5wIFFo7mg4HJzKdNUU",
            "https://drive.google.com/uc?export=view&id=1kN5q9qiun2iS-jtTCgS6QldJ889mgckA",
            "https://drive.google.com/uc?export=view&id=1kMvwpLYe01bmYXAttBfQRrcB1SuBM52w",
            "https://drive.google.com/uc?export=view&id=1kIFH0l5XTEpKWS5wIFFo7mg4HJzKdNUU",
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
                "kesan": "Abangnya baik dan cerdas",  
                "pesan":"semangat kuliahnya ya bang",
                "jabatan" : "Ketua himpunan", # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": " 121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@nadillaandr26",
                "kesan": "Abangnya asik",
                "pesan": "semangat kuliahnya", 
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
                "kesan": "Kakaknya kayak kpopers",
                "pesan": "semangat kuliahnya ya kak",  
                "jabatan" : "Sekretaris Umum" # 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Denger Musik",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya asik deh",
                "pesan": "semangat kakak",
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
                "kesan": "Kakaknya ramah",
                "pesan": "semangat dan sukses ya kak", 
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
                "kesan": "Kakaknya keren abiez",
                "pesan": "semangat dan bahagia terus kak",  
                "jabatan" : "Bendahara 1", # 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jbhwT84UPmSagSU9HTinfDWB8hBA_bDH",
            "https://drive.google.com/uc?export=view&id=1kE-RchHZqQjDPX91GbcBQ03Ab9jjuEh9",
            "https://drive.google.com/uc?export=view&id=1k56lyGCYHUvdI2UvicQbFmEaKde_Rie9",
            "https://drive.google.com/uc?export=view&id=1jkJzDcDdXE_KO9iVfD6Hq_kw_YAIrlL0",
            "https://drive.google.com/uc?export=view&id=1jnnr1n63euFqrtKjshcur3r1-2RZRZPV",
            "https://drive.google.com/uc?export=view&id=1jqNuly9F4NVjEHy0Xi9KvL9X29EoJugD",
            "https://drive.google.com/uc?export=view&id=1jSMTOVkf7JvSzEFaALzONg0mx1QkwcaK",
            "https://drive.google.com/uc?export=view&id=1jsLgElW-F014LjUdcbWl_cc0-jxm-psa",
            "https://drive.google.com/uc?export=view&id=1jWsAs5zdBxEbx2rhY-TKxMospp-3e8xW",
            "https://drive.google.com/uc?export=view&id=1k-GcNhvG1LQziWTfHds-EWJYiD_wOVWs",
            "https://drive.google.com/uc?export=view&id=1k83p1FsuTHwsApsPGeqNdbWRX2RazYX_",
            "https://drive.google.com/uc?export=view&id=1j_NbBX0hXdC9f6H98GAE1kz4y6VaorUp",
            "https://drive.google.com/uc?export=view&id=1jx7z_Lv0GvKYldlcD_FK_M4JRdXzn5PB",
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
                "kesan": "Kakaknya cantik deh kak",
                "pesan": "semangat terus",
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
                "kesan": "Kakaknya asik",
                "pesan": "Semangat dan keren terus ya kak ", 
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
                "kesan": "Kakaknya keren deh",
                "pesan": "semangat kak", 
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
                "kesan": "Kakaknya manis banget",
                "pesan": "semangat tetep cantik ya kak", 
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
                "kesan": "Cantik banget kak hidungnya mancung banget",
                "pesan": "semangat terus kak", 
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
                "kesan": "Abangnya ramah abiez",
                "pesan": "semangat kuliahnya ya bang", 
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
                "kesan": "kakak ini ramah sekali",
                "pesan": "semangat terus kak", 
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
                "kesan": "Abangnya ramah banget nih",
                "pesan": "semangat dan bahagia terus bang", 
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
                "kesan": "kakaknya lucu dan asik banget",
                "pesan": "Semangat kak tetep asik ya", 
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
                "kesan": "Abangnya asik",
                "pesan": "Semangat terus bang", 
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
                "kesan": "Kakaknya cantik dan manis banget",
                "pesan": "Terus bahagia dan semangat ya kak", 
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
                "kesan": "Kakaknya paling lucu",
                "pesan": "semangat terus ya kakak", 
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
                "kesan": "Abang paling ramah",
                "pesan": "Bang jere paling keren, semangat terus bang", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lEL1z8cU13x_iHlSHGcDddOyJN2hYdOV",
            "https://drive.google.com/uc?export=view&id=1hnD6mV8B7wqfu15nPYi-u1I809PIetgO",    
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "Kakaknya keren banget public speakingnya",  
                "pesan":"sukses terus dan tetep keren ya kak",
                "jabatan": "Senator"# 1
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "121450093",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini keren dan cerdas",  
                "pesan":"Semangat kuliahnya ya bang tetep jadi keren",
                "jabatan": "Anggota"# 2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":

    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vDL7tbrMs2iPIKrCu2GrIxBteP8C03ft",
            "https://drive.google.com/uc?export=view&id=1NP_Eo9IDIsLOvEeCTMEp6vFQ4bgV1sF1",
            "https://drive.google.com/uc?export=view&id=1XDfqmuRiYZhczjozW5LqzzQyM6wNBqeS",
            "https://drive.google.com/uc?export=view&id=1pPclJZprsQ5l5aauJKpmoL36HeTb-bho",
            "https://drive.google.com/uc?export=view&id=1oypyuKM2-IrAC-K66EFjI9x9dLfD43bn",
            "https://drive.google.com/uc?export=view&id=1ZkBH-AqfxbFldfL--mHJwuBrnBuycVME",
            "https://drive.google.com/uc?export=view&id=1ImoiOhDxlHh4NXSGWY8z5rUaE_AUMU8s",
            "https://drive.google.com/uc?export=view&id=12jgrEdED6ID3t_q0c9tX6M38dlV_KrBm",
            "https://drive.google.com/uc?export=view&id=1Yri2Jupqb8eHb5VFHkwLY9n8qXBYcL6f",
            "https://drive.google.com/uc?export=view&id=1SQY3y77q9mkwASCSoJqk1LXfb1n2HjRK",
            "https://drive.google.com/uc?export=view&id=1Y4yLuhDRDRBkP6Qwa7vhTpR1Mwtle6jb",
            "https://drive.google.com/uc?export=view&id=1ozuP1Y90ugRYuqT2pEkBe7rIjDI6kJqN",
            "https://drive.google.com/uc?export=view&id=1pMdHjQlNOwdOP4DduFj4ADkgwLUYWs9K",
            "https://drive.google.com/uc?export=view&id=1pMVU9a7jVkWqJCnWT7isp_rFMzPifvMw",
            "https://drive.google.com/uc?export=view&id=1p3KDXQU1Exy6DY8MT6dURexPKZnQAhIa",
            "https://drive.google.com/uc?export=view&id=1oyipoqRx5gIGKW0nlA11dyIx6ViT8GRX",
            "https://drive.google.com/uc?export=view&id=1oy2Too6IFE8ZbvZgKqCoE68o2g2sP12D",
            "https://drive.google.com/uc?export=view&id=1ouiI9wSE4WEuOGz4zy5SMr8mkf85FMHn",
            "https://drive.google.com/uc?export=view&id=1ip40diJIUtWRXLpn8ACxFw05B2Gg6yjZ",
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
                "kesan": "Abangnya ramah banget",
                "pesan": "Semangat bang tetep keren ya",
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
                "kesan": "Kakaknya lucu dan asik",
                "pesan": "Semangat kuliahnya kakak", 
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
                "kesan": "Abangnya jago olahraga nih keliatan",
                "pesan": "Semangat ya bang", 
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
                "kesan": "Kakaknya manis",
                "pesan": "Semangat kak dan terus bahagia ya kak", 
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
                "kesan": "Abangnya keren dan ramah",
                "pesan": "Terus semangat bang", 
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
                "kesan": "Abangnya asik",
                "pesan": "Semangat dan asik terus bang", 
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
                "kesan": "Abangnya ramah abiez dan pinter banget",
                "pesan": "Semangat ya bang dan terus bahagia", 
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
                "kesan": "Sama-sama dari bekasi kak hehehe",
                "pesan": "Semangat belajarnya kak", 
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
                "kesan": "Keren kakaknya",
                "pesan": "Semangat terus ya", 
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
                "kesan": "Abangnya ramah dan keren nih",
                "pesan": "Semangat kuliahnya dan bahagia selalu bang", 
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
                "kesan": "Kakak cantik banget",
                "pesan": "Semangat dan jaga kesehatan terus ya kak", 
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
                "kesan": "Kakaknya tegas",
                "pesan": "Semangat kuliahnya ya kak", 
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
                "kesan": "Kakaknya baik dan cantik",
                "pesan": "Semangat ya kak kuliahnya dan tetep lancar serta sukes", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450011",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Abangnya ramah",
                "pesan": "Semangat ya bang tetep maju", 
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
                "kesan": "Kakaknya cantik dan manis",
                "pesan": "Semangat sukses terus ya kak", 
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
                "kesan": "Abangnya ramah dan sama nih dari bekasi",
                "pesan": "Semangat ya bang", 
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
                "kesan": "Kakaknya manis",
                "pesan": "Semangat kakak", 
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
                "kesan": "Abangnya ramah nih",
                "pesan": "Semangat dan bahagia terus ya bang", 
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
                "kesan": "Kakaknya ramah dan baik hati",
                "pesan": "Semangat sukses terus kak", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    PSDA()

elif menu == "Departemen MIKFES":

    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nO4Mu3X9TTLNQsdfjIZQS8-YlU5sY2K3",
            "https://drive.google.com/uc?export=view&id=1mSUftl6iIKPD9aS2WIcbTH2r9oZ0zRhN",
            "https://drive.google.com/uc?export=view&id=1nBhacmujXU3VEmZHTKI5J-UW_C9NUZiZ",
            "https://drive.google.com/uc?export=view&id=1nH0qwf9Z1ciVVM1uZ9GtNBoNKKMgco5y",
            "https://drive.google.com/uc?export=view&id=1nSsU3x6EYvy5kYIfMZssaBYO3dyz7m2D",
            "https://drive.google.com/uc?export=view&id=1mV5cBKrcbYnPK2T8mg_QVi8x3GG8PIuf",
            "https://drive.google.com/uc?export=view&id=1nGOHAJmIcLfDlJlD4YhSQ83as0hOLXFW",
            "https://drive.google.com/uc?export=view&id=1n_Cglxvp8YCLMCOQw3desWEqX43-k7sD",
            "https://drive.google.com/uc?export=view&id=1mpsls947viarKMXdkbHIrZsiDsjNdBC-",
            "https://drive.google.com/uc?export=view&id=1njEcuyTUJZzuI_grMa1g8m5alxrTpxrZ",
            "https://drive.google.com/uc?export=view&id=1nUiKjp7y3BiqGzBBMtQzyBZnyGCrqxuj",
            "https://drive.google.com/uc?export=view&id=1ndkt4GCMSZSWXEvEqWi73KQGqenJFXu3",
            "https://drive.google.com/uc?export=view&id=1nNyEhX8Ef1PtQxu-NVFH9d5-yakN_-qv",
            "https://drive.google.com/uc?export=view&id=1my1-YHJcu6Sv-zeb9XhbcuDq5Z-fVN4A",
            "https://drive.google.com/uc?export=view&id=1mrpbJV6suUfYrEpq_Rb_cCG0Ik6hbCb9", 
            "https://drive.google.com/uc?export=view&id=1mPeXCdFLew7aTSdm2xYnZGfz1r6zdYGL",
            "https://drive.google.com/uc?export=view&id=1n3A9GvCUAUkQXpuzWAT0ppcYJSh4KeP8",
            "https://drive.google.com/uc?export=view&id=1nJ9g-xG-kuasz2n5hMbE9d6te2oAfj-w",
           
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
                "kesan": "Abangnya pinter",
                "pesan": "Semangat dan jaga kesehatan",
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
                "kesan": "Kakaknya cantik",
                "pesan": "Semangat ya kakak", 
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
                "kesan": "Abangnya ramah",
                "pesan": "Semangat ya bang kuliahnya", 
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
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semangat dan bahagia terus ya bang", 
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
                "kesan": "Abangnya keren",
                "pesan": "Semangat dan tetep keren ya bang", 
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
                "kesan": "Kakanya ramah banget",
                "pesan": "Semangat ya kak tetep ramah ya", 
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
                "kesan": "Abangnya cerdas",
                "pesan": "Semangat dan lancar semnua ya bang", 
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
                "kesan": "Abang pj aku nih baik dan ramah",
                "pesan": "Semangat terus sukses ya bang", 
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
                "kesan": "Kakaknya cantik dan ramah",
                "pesan": "Sukses kak lancar terus kuliahnya", 
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
                "kesan": "Keren kakaknya cantik",
                "pesan": "Semangat terus ya kak dan tetep bahagia", 
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
                "kesan": "Kakaknya pinter dan asik",
                "pesan": "Semangat terus ya kak", 
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
                "kesan": "Kakaknya cantik",
                "pesan": "Semangat kak tetep keren ya", 
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
                "kesan": "Abang ini ramah dan keren",
                "pesan": "Semangat sukses dan tetap bahagia ya bang", 
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
                "kesan": "Abangnya pinter dan ramah",
                "pesan": "Sukses selalu ya bang", 
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
                "kesan": "Abangnya asik",
                "pesan": "Selalu asik ya bang", 
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
                "kesan": "Baik kakaknya",
                "pesan": "Selalu ramah ya kak suskes terus", 
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
                "kesan": "Baik abangnya",
                "pesan": "Selalu happy ya bang", 
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
                "kesan": "Abangnya pinter",
                "pesan": "Keren dan semangat terus ya bang", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    mikfes()

elif menu == "Departemen Eksternal":

    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kfW6dnmF5q-LveDLL33oWsWV7ojMBl9_",
            "https://drive.google.com/uc?export=view&id=1kstRHnsYbQ-D-z6sxaUM6meVPv243tqM",
            "https://drive.google.com/uc?export=view&id=1lC5Mt0CmbE9JM8gvt2QlDN_FdPSkoxyj",
            "https://drive.google.com/uc?export=view&id=1mJ1Xh2V3tnz-kZDaWrOab1g1CdrcV2c0",
            "https://drive.google.com/uc?export=view&id=1l3H9V0BBOaxyfFjWZbeABIVaebQ_oPrI",
            "https://drive.google.com/uc?export=view&id=1kjqQ7RKZZ_gkisqbiQEuqhcW8VqU4SmX",
            "https://drive.google.com/uc?export=view&id=1kiM6Y3OSvyM1fZ_z9Y0wF3EvGso2bZfU",
            "https://drive.google.com/uc?export=view&id=1izHzeMUKNSpxnyV5o2vmdvWiakf9mX_1",
            "https://drive.google.com/uc?export=view&id=1l8GnZbOS70hEzH-TLrtRKnurmUHnbSva",
            "https://drive.google.com/uc?export=view&id=1krp556z__VUCzlriLcddBXjSHbsW5Npy",
            "https://drive.google.com/uc?export=view&id=1kfUKdU-pM55CH1SH7PwIEYOziHYQbe",
            "https://drive.google.com/uc?export=view&id=1g_z72t1RlZp5FM2MEb417YKFxfiPLhMu",
            "https://drive.google.com/uc?export=view&id=1l2SL1IPFvOgkMWD6t4AGa8KkwIxOgNeD",
            "https://drive.google.com/uc?export=view&id=1keRM9SexL00nFWnJa5EDkKwnUkpgRiRt",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1kxSRDYmlWFn1dzhgdZjopQXmlxJEZEqU",
            "https://drive.google.com/uc?export=view&id=1krCeY-b_MpgV4LvTYKHkk4tA_hAIuiA2",
            "https://drive.google.com/uc?export=view&id=1bIZJgWnRzoKJVkewLkBRq5kIRUJ7b65M",
            "https://drive.google.com/uc?export=view&id=1kTuuhLsEMbUDkHKqsltabTXSVCqr6x4U",
            "https://drive.google.com/uc?export=view&id=1kZ5LRMaFKikyApm22_HE4Cnh_1-17Sk_",
            
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
                "kesan": "Abangnya ramah dan keren",
                "pesan": "Semangat terus ya bang",
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
                "kesan": "Kakaknya cantik",
                "pesan": "Semangat dan bahagia terus ya kak", 
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
                "kesan": "Kakaknya lucu banget",
                "pesan": "Bahagia dan keren terus ya kak", 
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
                "kesan": "Keren hobi abangnya",
                "pesan": "Semangat terus dan bahagia ya bang", 
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
                "kesan": "Kakak daplok aku yang keren dan cantik baik sekali",
                "pesan": "Semangat selalu kakak", 
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
                "kesan": "Kakaknya cantik dan lucu banget",
                "pesan": "Semangat terus kakak cantik", 
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
                "kesan": "Kakaknya semarga sama aku",
                "pesan": "Semangat kak lancar semuanya ya kak", 
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
                "kesan": "Kakaknya cantik",
                "pesan": "Bahagia terus ya dan lancar kuliahnya kak", 
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
                "kesan": "Kakaknya manis sekali",
                "pesan": "Lancar semua dan jaga kesehatan ya kak", 
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
                "kesan": "Abangnya baik",
                "pesan": "Semangat ya bang", 
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
                "kesan": "Kakaknya tegas dan asik",
                "pesan": "Sukses selalu kak lancar semuanya", 
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
                "kesan": "Abangnya ramah",
                "pesan": "Tetap keren dan bahagia ya bang", 
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
                "kesan": "Asik dan ramah banget abangnya",
                "pesan": "Tetap ramah ya bang semangat dan lancar semuanya", 
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
                "kesan": "Kakaknya ramah sekali",
                "pesan": "Semangat terus ya kak", 
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
                "kesan": "Kakaknya cantik sekali",
                "pesan": "Tetap semangat ya kak", 
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
                "kesan": "Abangnya keren",
                "pesan": "Bahagia terus ya bang", 
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
                "kesan": "Kakak izza paling keren dan ramah banget",
                "pesan": "Semangat terus dan lancar semuanya ya kak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Baik banget kakaknya",
                "pesan": "Lancar semuanya ya kak", 
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
                "kesan": "Abangnya ramah",
                "pesan": "Semangat dan jaga kesehatan ya bang", 
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
                "kesan": "Kakaknya manis",
                "pesan": "Semangat ya kak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },

           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    eksternal()

elif menu == "Departemen Internal":

    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lTtqkA_k6tmyp57Ha0comD6m8uHAUniI",
            "https://drive.google.com/uc?export=view&id=1lvaqTKmKtiBofIX-ivLAqeagBEpn6WqL",
            "https://drive.google.com/uc?export=view&id=1lemPpKiFq32KTkZz4A3TOOvm7wyiaNXA",
            "https://drive.google.com/uc?export=view&id=1oqm-UHpFzKt-UVhLmOSU8ZMcsXuYlG1-",
            "https://drive.google.com/uc?export=view&id=1m03wsLcxfkmb44WBs6-Sko1o9yUhscXy",
            "https://drive.google.com/uc?export=view&id=1lVQAAyWpc-WgSu6fIDQcuj4loqxtfyJ6",
            "https://drive.google.com/uc?export=view&id=1laxdZVz_MwRLjHDRRxnt4lNVNj5adf3g",
            "https://drive.google.com/uc?export=view&id=1ljKBMIvy5YXTcN2cW_-kS2KKtxO2IZXw",
            "https://drive.google.com/uc?export=view&id=1llMORI34UKeLZA2RtpC7tcuVT4mMb3_M",
            "https://drive.google.com/uc?export=view&id=1lwg4C9V4YTOzjrX_aCHLMKj0TAeGI6dz",
            "https://drive.google.com/uc?export=view&id=1m3Tjyrd1m1PES7UOYl6uLqba8rHfvGgn",
            "https://drive.google.com/uc?export=view&id=1m7aNAoBBQYjQFB050M1IsUEHyixJgf9h",
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
                "kesan": "Abangnya keren dan asik banget",
                "pesan": "Semangat dan terus bahagia ya bang",
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
                "kesan": "Cantik sekali kakaknya",
                "pesan": "Semangat dan maju terus kakak", 
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
                "kesan": "Ramah abangnya",
                "pesan": "Tetep semangat dan asik bang", 
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
                "kesan": "Kakaknya ramah sekali",
                "pesan": "Semangat dan jaga kesehatan terus ya kak", 
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
                "kesan": "Baik dan cantik kakaknya",
                "pesan": "Sukses dan semangat terus ya kak", 
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
                "kesan": "Abangnya pinter sama-sama dari bekasi",
                "pesan": "Semangat dan maju terus ya bang", 
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
                "kesan": "Abangnya asik",
                "pesan": "Semangat dan bahagia terus ya bang", 
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
                "kesan": "Abangnya baik",
                "pesan": "Semangat bang lancar kuliahnya", 
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
                "kesan": "Abangnya ramah dan asik",
                "pesan": "Tetap semangat dan bahagia ya bang", 
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
                "kesan": "Kakaknya kalem dan baik",
                "pesan": "Semangat dan tetap bahagia ya kak", 
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
                "kesan": "Kakaknya cantik dan manis",
                "pesan": "Semangat dan jaga kesehatan ya kak", 
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
                "kesan": "Abang ini sangat ramah dan baik hati serta tidak sombong dan sangat asik",
                "pesan": "Semangat ya bang dan jangan lupa bahagia", 
                "jabatan" : "Staff Kerohanian", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    internal()


elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1abJZkzXAN7P5AIZWwbjlNoBPHhqERFc8",
            "https://drive.google.com/uc?export=view&id=1du-JtPmQmUudgHGjKFvzD5rd1AUktI1K",
            "https://drive.google.com/uc?export=view&id=1dwj_ORcA-uYhLOkuFK9Q-CZsv2whWAYd",
            "https://drive.google.com/uc?export=view&id=1e5lsEqkmG6eZdlJ2TmG-IpnoEyQkLGFp",
            "https://drive.google.com/uc?export=view&id=1dvl778LqNsuGG6Wx8rELg4WtNvfJX4lD",
            "https://drive.google.com/uc?export=view&id=1e2fAS9gxvigzAzpqQK5vmTpv04gxU_Ao",
            "https://drive.google.com/uc?export=view&id=1dw9c0VlZlXlRBaSGctWeNg9wOXK_Qqia",
            "https://drive.google.com/uc?export=view&id=1asuGZzmO0mVjxgdD6urKw6F8yZpFU2OV",
            "https://drive.google.com/uc?export=view&id=1akv2kNTpT5Eg4P_JH9QueM36i5Ej5DYi",
            "https://drive.google.com/uc?export=view&id=1alzhewMMQKzSwm9J6HUqwus9McqC9ddx",
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
                "kesan": "Abangnya semarga sama aku dan ramah banget abangnya",
                "pesan": "Semangat dan lancar semuanya ya bang",
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
                "kesan": "Kakaknya cantik",
                "pesan": "Semangat terus kakak", 
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
                "kesan": "Kakaknya ramah nih",
                "pesan": "Semangat kak happy terus ya", 
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
                "kesan": "Abangnya keren",
                "pesan": "Semangat dan tetep keren ya bang", 
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
                "kesan": "Abangnya ramah dan keren",
                "pesan": "Semangat dan tetep keren bang", 
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
                "kesan": "Abangnya baik",
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
                "kesan": "Kakaknya humble",
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
                "kesan": "Keren kakaknya",
                "pesan": "Semangat kakak", 
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
                "kesan": "Kakaknya manis banget",
                "pesan": "Semangat kuliahnya ya kak", 
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
                "kesan": "Abangnya ramah dan baik",
                "pesan": "Semangat bang kuliahnya", 
                "jabatan" : "Staff sponsor", # 1
            },
           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()

elif menu == "Departemen MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mETsT3hX9aJrpdrhu1xJUIBLjJPCorm8",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1mRv-tfqR4D3DhqXkD5UOUyvo8YyED-c9",
            "https://drive.google.com/uc?export=view&id=1mNjjesVChJVL0g13YEAxqbCQ9eSVNLlp",
            "https://drive.google.com/uc?export=view&id=1mPgThfRSz-ctuXql44X7cqnxArucqZQu",
            "https://drive.google.com/uc?export=view&id=1mW0lCeCQBJZAyC4VBUDXAw4TOAgS5D3H",
            "https://drive.google.com/uc?export=view&id=1md-wGX1dYr9GmfgpaarzX_QuGt_5x7s4",
            "https://drive.google.com/uc?export=view&id=1mqYIVl2ecidcn9mw67vjxRlnavl-R74K",
            "https://drive.google.com/uc?export=view&id=1mSZeB3PIiHO2BqZ8PMhaOP2n60hMcdlA",
            "https://drive.google.com/uc?export=view&id=1mXAmPuSs7sKrWiWGdyFhM3r8rf-1gn-O",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1mKLVCWjH8hJLH57Kc866PIokqGMXpycW",
            "https://drive.google.com/uc?export=view&id=1mJIvmGuxOm6FaBDioHMloXZFU0I6BEfG",
            "https://drive.google.com/uc?export=view&id=1mQmM71DvQ6Gz3TodGoUx0kiAma31qKQN",
            "https://drive.google.com/uc?export=view&id=1mo6ysG1t5jGgFZQ-X6cEoChM1WcrfuGh",
            "https://drive.google.com/uc?export=view&id=1me-F-_xZNKpollfWbBWtUvKmfuzupGGR",
            "https://drive.google.com/uc?export=view&id=1mGSQrPt1sGMlqIY5NKUeOYdZHzkrPq3g",
            "https://drive.google.com/uc?export=view&id=1mXX0JDoDgXpZeh02p-UtRosOW-PG5qVu",
            "https://drive.google.com/uc?export=view&id=1mPFGs-Og_d2d-fXF4LEW1u4tpCkHCCvo",
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
                "kesan": "Abangnya baik",
                "pesan": "Semangat ya bang",
                "jabatan" : "Kepala Departemen Media Kreatif ", #1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakaknya cantik banget",
                "pesan": "Semangat ya kak", 
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
                "kesan": "Kakaknya cantik",
                "pesan": "Semangat dan bahagia terus ya kak", 
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
                "kesan": "Abangnya ramah banget",
                "pesan": "Semangat terus bang", 
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
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semangat terus bang", 
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
                "kesan": "Suka banget sama style kakak",
                "pesan": "Semangat ya kak", 
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
                "kesan": "Kakaknya lucu",
                "pesan": "Semangat dan bahagia terus kak", 
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
                "kesan": "Kakak kakak kpopers",
                "pesan": "Semangat bahagia terus ya kak", 
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
                "kesan": "Kakaknya cantik poll dan ramah banget",
                "pesan": "Semangat kak cya", 
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
                "kesan": "Kakaknya lucu",
                "pesan": "Semangat kak maju terus", 
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
                "kesan": "Kakanya cantik dan NIM kita sama",
                "pesan": "Semangtat ya kak kuliahnya sukses terus", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {   "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakaknya kalem banget",
                "pesan": "Semangat kak", 
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
                "kesan": "Abangnya asik",
                "pesan": "Semangat bang", 
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
                "kesan": "Kakaknya ramah banget",
                "pesan": "semangat kuliahnya kak", 
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
                "kesan": "Abangnya baik",
                "pesan": "Sukses terus bang", 
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
                "kesan": "Ramah banget abangnya",
                "pesan": "Semangat ya bang", 
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
                "kesan": "Abangnya baik",
                "pesan": "Semangat terus bang", 
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
                "kesan": "Kakaknya cantik",
                "pesan": "Semangat kak", 
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
                "kesan": "Kakaknya ramah",
                "pesan": "Semangat terus kuliahnya ya kak", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


    

# Tambahkan menu lainnya sesuai kebutuhan