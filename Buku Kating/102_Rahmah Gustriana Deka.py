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
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KigidBoxqCQFKjbnCJaGhcBHQNAIkj_R",
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
            "https://drive.google.com/uc?export=view&id=1puMLChxw5ZN_UolemtLaX6WXV43YXFVf",#kak tri
            "https://drive.google.com/uc?export=view&id=1EZZY7_mYTeDu7ejDfmiBczsY9g_bYJQF",#kak anisa cahya
            "https://drive.google.com/uc?export=view&id=1zDPGFCASJrpKVu6gCCv97oQXbogUIlnN",#kak wulan
            "https://drive.google.com/uc?export=view&id=18oWdS293oxuuPOLGMy4OwZJZMVSpiLiy",#kak anisa dini
            "https://drive.google.com/uc?export=view&id=11S9NHIw4FgI84Nm64654L0_DiAGIQalw",#kak claudea
            "https://drive.google.com/uc?export=view&id=1G83Uaag3YP_jsW9Du1UlaeVbYIXRLh42",#bang fachrul
            "https://drive.google.com/uc?export=view&id=1jhGRJ6wzqLzJAgBlVVKYyZjojELxW5Z3",#kak annisa fitri
            "https://drive.google.com/uc?export=view&id=13nq9-0Df8jEDZ7hlTv1Syr2F71Cbi2Tq",#bang ferdyadi
            "https://drive.google.com/uc?export=view&id=19gEoEcv-5lHzR8h0FkJkd02_EUXkdABW",#kak renisha
            "https://drive.google.com/uc?export=view&id=1oyir-aqZkTlEXa5TBAxDFgcAyB7uGwXN",#bang mirzan
            "https://drive.google.com/uc?export=view&id=1ngQ1Nr0n1d_h3zFC-6JkzpLbb9NW1XQx",#kak dhea
            "https://drive.google.com/uc?export=view&id=1Qfessx7WHWYxM2K0SsaEpgzTJNgsXQU5", #kak berliana
            "https://drive.google.com/uc?export=view&id=1FDySwxCdXiRrsbOMV4WRMEo119fvKkDK", #bang jeremia

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
            "https://drive.google.com/uc?export=view&id=1HGAsOSY22pQaBtmXPraAbQ4E0QUw5w96",
            "https://drive.google.com/uc?export=view&id=1UP30Byp-tmJ4Gb7azZD57TywT_ZyeeXY",
            
            
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
            "https://drive.google.com/uc?export=view&id=1jOk5eg7cHMNty5aAHy5_RX3kJUYkC8y3", #bang econ
            "https://drive.google.com/uc?export=view&id=1SIdObS91eOt2qgmTL3sse0atWU6ADo8t",  #kak abeth
            "https://drive.google.com/uc?export=view&id=1PSLwDWF76U547JkgFDMOHeuUpGuLmSV3", #bang depan
            "https://drive.google.com/uc?export=view&id=1Na9LhIiGIkO5B83eN1bEn8LmKKS7-hvG", #kak afifah
            "https://drive.google.com/uc?export=view&id=1olxIySKgWUWPmI9fu78x0-OljsSJVlT4", #bang ateng
            "https://drive.google.com/uc?export=view&id=1LhzqsFQS4ipaIdET9GZyoBuIN_IBjmip",#bang jo
            "https://drive.google.com/uc?export=view&id=1mV5O0uRM53B3pTtXVeoxJWtKU-W8860O", #bang kemas
            "https://drive.google.com/uc?export=view&id=1D-77onOjipx_KBqm7JVf1RbZrql9G_gf", #kak presilia
            "https://drive.google.com/uc?export=view&id=1WKXxEkX_dZxOcYKq6HgbhbQm3tePZL_y", #kak rafa
            "https://drive.google.com/uc?export=view&id=1AcZPIZDEvzvCs8FARLqTA8d-te5KAe5J", #bang sahid
            "https://drive.google.com/uc?export=view&id=1IqmOni0CKT3g6nwlv5Xc_F6tPuzYTzNh", #kak vanesa
            "https://drive.google.com/uc?export=view&id=1bkJdXWNvNle2IfgPerr9zeraLjdfILky", #kak alya
            "https://drive.google.com/uc?export=view&id=1OOnSr2h7J8120ankpNAYblveMCEve7ji", #kak eksanty
            "https://drive.google.com/uc?export=view&id=1SkrZYHS2Mk9OqAHZYHI9avCHqhv7H7V2", #bang deri
            "https://drive.google.com/uc?export=view&id=1QHEl3exwVieS2hbR3J34w4cFvS4jC5s8", #kak okta
            "https://drive.google.com/uc?export=view&id=1ecJgGV6IwdzEqHTotH05rLP8o8fzEoWm", #bang gde mona
            "https://drive.google.com/uc?export=view&id=1lWUX3ztH71lE6jrIvJrzn50KQhQ5NF08", #kak jacline
            "https://drive.google.com/uc?export=view&id=1H8xkFLMvpISZ4dZTF2dnEYWYLxOLTOHm", #kak rafly
            "https://drive.google.com/uc?export=view&id=1lDZu2MxXZhuCuTOFa8pu-vg2AgJDSLhh", #kak dini
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
            "https://drive.google.com/uc?export=view&id=1UmUd0mR94j5-Yk5A3oje8FQ134Az76xB", #bang rafi
            "https://drive.google.com/uc?export=view&id=1UppJrbM-QZiNFEkWgzeA9QNptf5ziYT-", #kak annisa
            "https://drive.google.com/uc?export=view&id=1exRwLSf7mQ_IwGbMYu0ICMmGxOEenEoZ",#bang sahid
            "https://drive.google.com/uc?export=view&id=1lY8EbwujUHTfxUVXlEHV_maeI-AIKbHv", #bang fadhil
            "https://drive.google.com/uc?export=view&id=1k6MzzvdVduYP-IZuQrsTcf6PxJPlPTmi", #bang regi
            "https://drive.google.com/uc?export=view&id=1A7XgmzBJ-q-1sHNdXbjpv070RaLsaLP7", #kak dina
            "https://drive.google.com/uc?export=view&id=1VcDqEwP3ah4BDr42BY-gPRFsp3p1eq2C", #bang natanael
            "https://drive.google.com/uc?export=view&id=1e4Ify-Kutyz-gKaTo_HhmYaqBFSFWPDB", #bang anwar
            "https://drive.google.com/uc?export=view&id=1zRoUXH4geYCf5zkC30IjxmjUD_1JmMRo", #kak deva
            "https://drive.google.com/uc?export=view&id=1LcZHWbqB5Yk_BA7sZFAl0Lz9VVFlmGsp", #kak dinda
            "https://drive.google.com/uc?export=view&id=19TOvutB-6ujDkGFRG0gkyNBJPE-TRgP1", #kak marleta
            "https://drive.google.com/uc?export=view&id=1AbpdxGPwzAyQJmRcaJH4cSCG6O3gAV3B", #kak rut
            "https://drive.google.com/uc?export=view&id=10BCAefp5Rl9Cou1XKc8PorlpAth2n4kn", #bang abdurrahman
            "https://drive.google.com/uc?export=view&id=1dN4SQ3WUCOCTKmdU1L3lnCdhqSej4Qgc", #bang adit
            "https://drive.google.com/uc?export=view&id=1UBqpC1BVRFvWJECRmzomk_wsDYEQmqPM", #kak febiya
            "https://drive.google.com/uc?export=view&id=16KMv3K50DsNx0zsUi9ptw_QyhwPyWfvz", #bang syahrul
            "https://drive.google.com/uc?export=view&id=1fueiwXE1CYC0-ITSnhJCGSryyUnCLTo4", #bang randa
           
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
                "kesan": "Abang kalem yahorangnya?",
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
            "https://drive.google.com/uc?export=view&id=1ijGqxmuAeJlXNQAVJx4RBXaIVqJngBk-", #bang yogy
            "https://drive.google.com/uc?export=view&id=1a8-ywVBgDQOSqF8iiL3h5epumByVqt_D", #kak ramadhita
            "https://drive.google.com/uc?export=view&id=1R8JcrbGx68JFMzI_EoF9Spjfw6vn-aaa", #kak nazwa
            "https://drive.google.com/uc?export=view&id=1_N29FR9EEChVaZ_4oR8i0__CakKaSkgM", #kak dea
            "https://drive.google.com/uc?export=view&id=1wL8Zr_k4z3AO-TulVoJG97i1hfCvVB2_", #kak esteria
            "https://drive.google.com/uc?export=view&id=1T8vv-bDnO6EW7bPuKzo4md9WVIWvKdsQ", #kak natasya
            "https://drive.google.com/uc?export=view&id=1VdAxQJyipdNM6CjzlIIvfTw9sewOzzxv", #kak ratu
            "https://drive.google.com/uc?export=view&id=12_Gp5qnW1BaEip-GoG1NONBiisip8GXb", #bang tobias
            "https://drive.google.com/uc?export=view&id=19iSRZmio46e_yHMKTGcF4PWGu_bREEAt", #kak yohana
            "https://drive.google.com/uc?export=view&id=1rsUKVTpbfbs2JOiXEgXmA346KjHYLDQe", #bang rizky
            "https://drive.google.com/uc?export=view&id=17zMM0-_9psqGm894eTWSAyP5qspHuaC-", #bang arafi
            "https://drive.google.com/uc?export=view&id=191nGzUCKK0MIug4_6EvnedJG6w8pnymG", #kak asa
            "https://drive.google.com/uc?export=view&id=1tL4vKvbGnjGalOSyyK5xYoSMN03VYkuZ", #kak chalifia
            "https://drive.google.com/uc?export=view&id=1YadW3_teTcxYdxi-jEvejzOgRHQkZtNi", #bang irvan
            "https://drive.google.com/uc?export=view&id=1c-E7upJ5EWJB7gIFyU_cDjPDjnu4-CVw", #kak izza
            "https://drive.google.com/uc?export=view&id=1c-Uo6_8fTnxvqVU1H6-ifOi5hLQ18E69", #kak khalishah
            "https://drive.google.com/uc?export=view&id=1E7kTwgQFjx8w_MURAGh04pYud9qpcFNF", #bang raid
            "https://drive.google.com/uc?export=view&id=1nvgzoCt1UnvJKOlZDuOfBnWGIZIy7wR3", #kak tria
            
            
            
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
                "kesan": "Kakak vibesnya ceria banget",
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
                "kesan": "abang keknya tipe orang yang kalem ?",
                "pesan": "yow tetap semangat kuliahnya bangg", 
                "jabatan" : "Kepala Divisi Pengabdian Masyarakat", # 12
            },
             {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Hobinya sangat bermanfaat ya bang",
                "pesan": "Semangat bang, semoga sukses juga bertaninya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 13
            },
             {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ramah banget dan masyaallah suka banget liat cara berpakaian kakak",
                "pesan": "Tetap semangat kak menjalani hari-harinya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 14
            },
             {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakak asyik orangnya, cocok bgt di eksternal",
                "pesan": "Jangan cape jadai orang yang berbagi kebahagiaan ya kak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 15
            },
             {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Memang orang-orang eksternal ini asyik semua",
                "pesan": "Semangat bang jalani hari-harinya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 16
            },
             {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak asprak terbaikk, love sekebon deh buat kakak",
                "pesan": "Semangat trs ya kak di organisasi dan aspraknya heheh", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 17
            },
             {
                "nama": " Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kayak namanya, kakak masyaaallah sekali",
                "pesan": "Sukses selalu kak dunia akhiratnya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 18
            },
             {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Dari hobinya keknya abang ini semangat banget orangnya wkwk",
                "pesan": "Semangat aja deh bang semoga segala urusannya diperlancar", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 19
            },
             {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": " @tria_y062",
                "kesan": "positif vibes auranya",
                "pesan": "Semangat kak kuliahnya dan organisasinya ", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 20
            },

           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    eksternal()
elif menu == "Departemen Internal":

    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YN2H4doscOexjLxjH33kEdWf4CbfZUUC", #bang dimas
            "https://drive.google.com/uc?export=view&id=1Ycprcpt0FXpzwoKRqwYwm15KcWzaPzMS", #kak chaterine
            "https://drive.google.com/uc?export=view&id=1YTG4aZbQn4gx_I4-EbSAx0M8oIeUUTlj", #bang akbar
            "https://drive.google.com/uc?export=view&id=1YnEyIer1F_Dxs0_pVKA743fh6zW66buY", #kak renita
            "https://drive.google.com/uc?export=view&id=1YZLsc_QuBQwFR1fbyDWHDXrtJ2nd1now", #kak salwa
            "https://drive.google.com/uc?export=view&id=1YFyOrsuzXcgXsg-44pDOhQqEuvEhcBP1", #bang rendra
            "https://drive.google.com/uc?export=view&id=1YRwqSoeyComW_P9YdvhJYYwccN9A-KKt", #bang yosia
            "https://drive.google.com/uc?export=view&id=1YUWxcM0geFAnJ45LHW595s2QrP1OTEw7", #bang ari
            "https://drive.google.com/uc?export=view&id=1YcRaCk9jY1VxncJktwhXlkLPcdYrwo5H", #bang joshua
            "https://drive.google.com/uc?export=view&id=1YW1ChJV5If6Gm1fVSFNChP6Z-NY4qn7i", #kak azizah
            "https://drive.google.com/uc?export=view&id=1YZWBIzACVA0xk3pZeNghFRh_w0S5zjKu", #kak meira
            "https://drive.google.com/uc?export=view&id=1Y_NeC6HKTHcp8mWHTZFFiSFmUFiqPcKA", #bang rendi
            
            
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
                "kesan": "Suka banget sama abang, dibalik orang yang humoris ternyata keren banget kepemimpinannya",
                "pesan": "Semangat bang, akademiknya jangan dilupain yah",
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
                "kesan": "Kakak asyik juga orangnya",
                "pesan": "Tetap semangat kak akademik dan non akademiknya", 
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
                "kesan": "Hobinya out of the box bang",
                "pesan": "Semangat bang menambah Dino nya hehe", 
                "jabatan" : "Kepala Divisi Keharmonisasian", # 3
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakak lucu orangnya",
                "pesan": "ajakin aku mancing dong kak hehe", 
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
                "kesan": "Masyaallah kaya namanya kak",
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
                "kesan": "Abang orangnya asyik banget, bisa bikin orang ketawa ",
                "pesan": "Bang jangan cape jadi orang yang humoris yah", 
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
                "kesan": "Humoris abiez nih abang orangnya",
                "pesan": "Lanjutkan bang, buat orang lain jadi tertawa", 
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
                "kesan": "Masyaallah abang keliatannya kalem dan sangat agamis, cocok banget di kerohanian",
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
                "kesan": "Abang diem-diem tapi lucu orangnya ",
                "pesan": "Semangat bang, apalagi buat pj MSS RB heheh", 
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
                "kesan": " kalem kakaknya",
                "pesan": "Semangat kak menjalani hari-harinya", 
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
                "kesan": "Kakak juga kalem, cocok banget di kerohanian",
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
                "kesan": "Memang daplok paling baik sih, fix",
                "pesan": "Semangat terus abangkuhh, semoga semuanya dipermudah", 
                "jabatan" : "Staff Kerohanian", # 12
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    internal()
elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1b7--nNF7jieTX_ex6v_WMNkIDOl9-mSj", #bang andrian
            "https://drive.google.com/uc?export=view&id=1au7Q2eT7dKiTpdQBkDbHd6MsTyoB_0jF", #kak adisty
            "https://drive.google.com/uc?export=view&id=1bLiACMZqniCGWr_1lLC4mmTJm7I5-hsb", #kak nabila
            "https://drive.google.com/uc?export=view&id=1b1Z_v1VdTDfehVT7Q-dtEyq8n_Q7n8R4", #bang danang
            "https://drive.google.com/uc?export=view&id=1bGNuu5hs4b6NVA-ThDHu5IIjwl3H6uwb", #bang farel
            "https://drive.google.com/uc?export=view&id=1bIfvr75NcA2v8LUojnOHnhOC82qXvOhx", #bang ahmad
            "https://drive.google.com/uc?export=view&id=1bJgE3IIARnCWAV6bbF7aU7TpKALfldBa", #kak tessa
            "https://drive.google.com/uc?export=view&id=1b0bkl1F7g8xjzXV4G7wS2RD9FdX_TfUI", #kak nabilah
            "https://drive.google.com/uc?export=view&id=1b01v2USQAoLCeu5YsIcfmOToJNb8Ltkv", #kak elia
            "https://drive.google.com/uc?export=view&id=1avpZQn0PvHvdsLuJnOLCLN558PfpKFcD", #bang dhafin
            
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
                "kesan": "Keren banget bang, calon pengusaha ini",
                "pesan": "Semangat terus bang kuliah sama usahanya",
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
            "https://drive.google.com/uc?export=view&id=1Ff0f8gaqYnRjgmScq52IoLpQ1hoOq_OX", #bang wahyu
            "https://drive.google.com/uc?export=view&id=1SH0gLOWKKJ6Mxlm-Xzt08kRiBdLqa2nJ", #kak elok
            "https://drive.google.com/uc?export=view&id=1xNCiT2jSiJt8_34fbND4T11U38-f96dB", #kak arsyiah
            "https://drive.google.com/uc?export=view&id=14r_7uEgUfjGtGi65dL8VhEWwNRTBkdU1", #bang kaisar
            "https://drive.google.com/uc?export=view&id=1wk76U8Ln3iyuqmDlKC_WDKu2Vt10bp6O", #bang arsal
            "https://drive.google.com/uc?export=view&id=1URGLLwBrN98iYr2bYKdyR4yKkZKLt0NU", #kak cintya
            "https://drive.google.com/uc?export=view&id=1kXZnQQ-LB1IruGmrCa-7JtuhvIkMFnJ2", #kak eka
            "https://drive.google.com/uc?export=view&id=11zDizN1t31QxpQ_wextoFJ33i0dZQ8Fv", #kak najla
            "https://drive.google.com/uc?export=view&id=17lohyDjfoXOSoewCA1OS9-OiNDKz6WvP", #kak patricia
            "https://drive.google.com/uc?export=view&id=1nNx6s4u3yp8Y9sOospGlyJebzOMvA6Xj", #kak rahma
            "https://drive.google.com/uc?export=view&id=15LQYCuZdbVPHJxSlagC4Y5TBAopO1JKu", #kak try
            "https://drive.google.com/uc?export=view&id=1XIOXhuuaEuyjf6u3OJ6AI5Sf1MWxzLBC", #kak dwy
            "https://drive.google.com/uc?export=view&id=1_Beg14KeRAJf1ftxZw-EHeAsFU_nuCYX", #bang gymnastiar
            "https://drive.google.com/uc?export=view&id=1S1gfHHQZEH6bCP-6PWE6SVHvFp_y27_J", #kak nasywa
            "https://drive.google.com/uc?export=view&id=1oF5wW97bslezpc57jA0aj1AV2AZr4ESG", #bang abid
            "https://drive.google.com/uc?export=view&id=1w2tJZD9-Hc47nXGy7MS0UHXFBrKp97_e", #bang akmal
            "https://drive.google.com/uc?export=view&id=1yXJJwEfOE5khuqyE8YquTWnpnhaA6tPd", #bang hermawan
            "https://drive.google.com/uc?export=view&id=1Mu-JFgI_jMQe-GL0lm7_up3LOBReJIbb", #kak khusnun
            "https://drive.google.com/uc?export=view&id=1EtIFr9JEhvwpmfqrPAG5UIlG1z6GIYh8", #kak priska
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
                "kesan": "Keren banget bang orang jauh",
                "pesan": "Semangat kuliahnya dan kegiatan di Medkrafnya",
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
                "kesan": "keren banget kak hobinya editing",
                "pesan": "Semangat terus deh kak berkaryanya", 
                "jabatan" : "Sekretaris", # 2
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kak hobi kita sama hehehe",
                "pesan": "Semangat kak mengemban tugasnya", 
                "jabatan" : "Kepala Divisi Media & Konten", # 3
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": " 121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": " @dino_kiper",
                "kesan": "Abang orangya asyik dan lucu",
                "pesan": "Semangat bang kuliahnya, dan kabarin kalo dah dapet hobinya xixi", 
                "jabatan" : "Kepala Divisi PDD", # 4
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Kecee gada obat hobi ngoding+kadiv Visual Desain",
                "pesan": "Semangat bang ngodingnya", 
                "jabatan" : "Kepala Divisi Visual Desain", # 5
            },
            {
                "nama": "Cintya  Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Gaya kakak dah cocok banget sebagai Divisi media & konten",
                "pesan": "Semangat kak kuliahnya, dan semangat juga buat kontennya hihi", 
                "jabatan" : "Anggota Divisi Media & Konten", # 6
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " 122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakak kayanya tipe orang yang suka banget berorganisasi",
                "pesan": "Semangat dan jangan lupa istirahat di tengah kesibukannya ya kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 7
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Hobinya sangat bermanfaat sekali",
                "pesan": "Semangat terus kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 8
            },
            {
                "nama": "Patricia Leondra Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "suka banget sama kaka, ceria dan ramah banget",
                "pesan": "Tetap semangat yah ka, terus ceria dan ramah selalu", 
                "jabatan" : "Anggota Divisi Media & Konten", # 9
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kece parah hobinya, sepuh coding nih ya kak?",
                "pesan": "Semangat kak kuliahnya", 
                "jabatan" : "Anggota Divisi Media & Konten", # 10
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Dari hobinya kayaknya kakak orangnya asyik",
                "pesan": "Semangat kakk", 
                "jabatan" : "Anggota Divisi Media & Konten", # 11
            },
            {
            "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak keliatan kalem hehe ",
                "pesan": "Semangat terus kak kegiatan di PDD nya", 
                "jabatan" : "Anggota Divisi PDD", # 12
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Keliatan suhunya hehe",
                "pesan": "semangat terus kak menjalankan kegiatannya", 
                "jabatan" : "Anggota Divisi PDD", # 13
            },
            {
                "nama": "Nasywa Nur Afifah ",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "kakak baik dan ramah",
                "pesan": "Semangat kak kuliahnyaa", 
                "jabatan" : "Anggota Divisi PDD", # 14
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abang seru nih keknya orangnya",
                "pesan": "Semangat terus yah bang", 
                "jabatan" : "Anggota Divisi Visual Desain", # 15
            },
             {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Sangat terlihat kalo abang sepuh coding hehe",
                "pesan": "Semangat terus bang", 
                "jabatan" : "Anggota Divisi Visual Desain", # 16
            },
             {
                "nama": "Hermawan Manurung ",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani) ",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang asprak yang sangat baik dan rajin",
                "pesan": "Jangan cape ya bang ngasprak kami", 
                "jabatan" : "Anggota Divisi Visual Desain", # 17
            },
             {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Sudah terlihat kalo kakak sangat rajin dan pintar",
                "pesan": "Semangat dan jaga kesehatan kak", 
                "jabatan" : "Anggota Divisi Visual Desain", # 18
            },
             {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakak orangnya ramah",
                "pesan": "Jangan kebanyakan nangis yah kak hehe", 
                "jabatan" : "Anggota Divisi PDD", # 19
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    medkraf()
