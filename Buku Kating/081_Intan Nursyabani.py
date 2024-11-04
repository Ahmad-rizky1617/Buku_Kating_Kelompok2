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
            st.write(f"jabatan: {data_list[i]['jabatan']}")
    st.write("Semua gambar telah dimuat!")


menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":

    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dQHbiGzXsxjbp_TguJNgfUNwDGx3JHRx",
            "https://drive.google.com/uc?export=view&id=1dGkdjR-B4Gx2r2J_IQfzsJpzJS2B9Iw5",
            "https://drive.google.com/uc?export=view&id=1dJ6438dvFzjRXr25KzO1lmxha8P4YSit",
            "https://drive.google.com/uc?export=view&id=1dOVQunnUCWK-DLOoIkwcMqIi70_gzwmu",
            "https://drive.google.com/uc?export=view&id=1dHmV6_bfmkavCuMYwf7V695ZC59GD1cB",
            "https://drive.google.com/uc?export=view&id=1dJspqeENS7eJioLC6jmakfEVc6EBK2UO",
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
                "kesan": "banyak wawasannya dan keren ",
                "pesan": "Sukses terus ya bang, makasih insightnya,",
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
                "kesan": "wah kakaknya dari pagaralam, sama dong",
                "pesan": "semangatt kak sukses terus",  
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
                "kesan": "cantik dan ramah kakaknya",
                "pesan": "semangat menjalani hidupnya kak",
                "jabatan" : "Bendahara umum",  # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": " 121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "keren dan asik abangnya",
                "pesan": "semangat kuliahnya bang", 
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
                "kesan": "baik dan ramah banget",
                "pesan": "semangat ya kak kuliahnya, semoga cita-citanya tercapai", 
                "jabatan" : "Sekretaris 1", # 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Baca",
                "sosmed": "@nadillaandr26",
                "kesan": "keren banget dan aura bendaharanya ",
                "pesan": "semangat kak, jangan pantang menyerah",  
                "jabatan" : "Bendahara 1", # 1
            },




        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YsYqLKVux0RmnPxZYAG6YbsAN0NMoPE1",
            "https://drive.google.com/uc?export=view&id=1Zjm7pbxsAfPPM20DZquOcEKItwlF9qIg",
            "https://drive.google.com/uc?export=view&id=1Yp3ixkRgSmDTHftHE24wyhtdDIOv3_m-",
            "https://drive.google.com/uc?export=view&id=1ZQTq9rjB7QXPNCD1NlMoIKGRCtT6elOn",
            "https://drive.google.com/uc?export=view&id=1Z2U3NJra7D_bJMxCGIYINZDCOzXQzbHW",
            "https://drive.google.com/uc?export=view&id=1YsO4rie16bT8whF7EhNHmc625siauKI1",
            "https://drive.google.com/uc?export=view&id=1Yq9_2hPoi7ghSnbVopFnIXZins_SB7Rq",
            "https://drive.google.com/uc?export=view&id=1ZHZ10ttXtBy4idifcA5IdFQ2d7VDqAlQ",
            "https://drive.google.com/uc?export=view&id=1a2_K6BqZ97eK6SndhruqF2I6mF3_GF6k",
            "https://drive.google.com/uc?export=view&id=1YyYb7gJShL6p7Q_uJlL9Mzu8JRjh1_S0",
            "https://drive.google.com/uc?export=view&id=1ZkZQWHZYa3uOVilfgX034vVf77bLLbuZ",
            "https://drive.google.com/uc?export=view&id=1ZjmDZJG89t782VjNTKNS8es0hKCrFQl4",
            "https://drive.google.com/uc?export=view&id=1Z-dzi2e0sh3MDZFSsgD2oNHvLsnPMA0w",
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
                "kesan": "Kakaknya lucu dan cantik banget pinter lagi",
                "pesan": "semangat kuliahnya kak,semoga cita-citanya tercapai",
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
                "kesan": "kakanya keren dan pinter juga penyampaiannya",
                "pesan": "Semangat kuliahnya kak, semoga makin rajin", 
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
                "kesan": "Ramah banget, baik, lucu",
                "pesan": "semangat kak, jangan menyerah", 
                "jabatan" : "Bendahara", # 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": " @anisadini10",
                "kesan": "Kakaknya asik dan ramah banget",
                "pesan": "semangat kuliahnya kak agar bisa membanggakan orangtua", 
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
                "kesan": "kakaknya ramah banget dan juga cantik",
                "pesan": "semangat ya kuliahnya, makinn sukses", 
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
                "kesan": "hobinya masya allah banget bang, keren",
                "pesan": "semangat kuliahnya kak, sukses jugaa", 
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
                "kesan": "masya allah sekali kak hobinya, kakaknya asik",
                "pesan": "selalu di baca kak al-waqiahnya, semangat terus!", 
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
                "kesan": "Abangnya juga rajin ibadah nih",
                "pesan": "semangat kuliahnya kak, semoga akademiknya lancar", 
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
                "kesan": "kakaknya ramah dan keren hobinya",
                "pesan": "Semangat kuliahnya, semoga semakin rajin baca al-qurannya", 
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
                "kesan": "Abangnya sangat ramah kelihatannya",
                "pesan": "semangat main kucingnya bang", 
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
                "kesan": "asik dan lucu banget kakaknya",
                "pesan": "semangat terus kak, semoga cepet ketemu sinyal gedung f nya kak", 
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
                "kesan": "kakaknya ramah dan baik banget",
                "pesan": "semangat kuliahnya kak! makin bahagia", 
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
                "kesan": "baik dan lucu abangnya",
                "pesan": "semangat terus bang! jangan patah semangat", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "Senator":

    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1P2wMXBexR0MUPDwc_Dw89cUMlKXZqp2F",
            "https://drive.google.com/uc?export=view&id=1P29uDWt0k_FGILGwtUyl0NB3K5y0zvLf",
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
                "kesan": "kakaknya keren dan menginspirasi karena wawasannya banyak",
                "pesan": "semangat terus kak",
                "jabatan": " Senator",
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kotabaru",
                "hobbi": " Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "publik speakingnya abangnya keren banget sih",
                "pesan": "semangat terus bang, lancar kuliahnya", 
                "jabatan": " Tim Senator",
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PkjEG44zQLQPS3YbDBPBOc3bQnEqrNeJ",
            "https://drive.google.com/uc?export=view&id=1Pb1dRYenoPF_0YJkDscimKJ_MRW0_HI5",
            "https://drive.google.com/uc?export=view&id=1QB9EzcnktdrdHk5ItenQDZjQ01QbN3e-",
            "https://drive.google.com/uc?export=view&id=1QHk789dDaR285B53GAxhDS5w7LLxlxYg",
            "https://drive.google.com/uc?export=view&id=1PQXPFsqxjtJl6aN_f-yZoKAYfWs9MGwz",
            "https://drive.google.com/uc?export=view&id=1Pn8eg5w3WRmvm6_vIgRjoEGqSarNvYc5",
            "https://drive.google.com/uc?export=view&id=1Q558qh-pt7crF0roVQdlmdHtscKHvb4x",
            "https://drive.google.com/uc?export=view&id=1PrbteSTCdtfirof6nmrme-hVwH4eZcX4",
            "https://drive.google.com/uc?export=view&id=1PsqUyC_DQmnseVzqss1bvelyQvnAM4IV",
            "https://drive.google.com/uc?export=view&id=1Q5IoFa91p0__pg4OsEcYhXeO0wyRffdq",
            "https://drive.google.com/uc?export=view&id=1QAn-t6Tn8WDG6xgdYzlBEPNU5gZ68UQN",
            "https://drive.google.com/uc?export=view&id=1PQKoh8qnUQLzIUJ2PG6alWZfvHwwrkrr",
            "https://drive.google.com/uc?export=view&id=1PVlnU51CLMUnd_hysfyKdFRCoNghy18P",
            "https://drive.google.com/uc?export=view&id=1PSk0VaKoqEqT032OEK07u6nrI0p8BiFY",
            "https://drive.google.com/uc?export=view&id=1PNLEovvmaUX4Gimo-5x9gpWOx1vee4hI",
            "https://drive.google.com/uc?export=view&id=1PMyD5rhbh05tR-F8MVvEmSNrBKyp25Fb",
            "https://drive.google.com/uc?export=view&id=1QQ7nFzlgwGw9O8HGQv4Kkfn4nF7pc0BN",
            "https://drive.google.com/uc?export=view&id=1PE9XjlbjVKOO0Zpq4oouGZEAyqHjy3oW",
            "https://drive.google.com/uc?export=view&id=1PJ24qk4roQF7u8SjF9qGSIl6FZCY7mnG",
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
                "kesan": "abangnya tegas dan keren banget bisa memotivasi banyak orang",
                "pesan": "Semangat mengejar cita-citanya bang",
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
                "kesan": "Asik dan cantik kakaknya, cara ngomongnya juga lucu",
                "pesan": "Semangat terus kak!sehat selalu", 
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
                "kesan": "humoris dan asik banget abangnya",
                "pesan": "Semangat terus bang, jangan lupa minum", 
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
                "kesan": "kakaknya berkharisma banget ",
                "pesan": "sehat selalu kak! semangat", 
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
                "kesan": "keren banget abangnya dalam memotivasi orang lain",
                "pesan": "Sehat selalu bang dan makin sukses", 
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
                "kesan": "abangnya keren dan peduli banget",
                "pesan": " sehat dan semangat terus ya bang", 
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
                "kesan": "pinter dan keren banget jago ngoding",
                "pesan": "semangat menuntut ilmunya bang, sehat selalu!", 
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
                "kesan": "asik dan cantik kakaknya",
                "pesan": "Semangat belajarnya kak, sehat selalu ya ", 
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
                "kesan": "cantik, ramah, dan keren kakaknya",
                "pesan": "semoga harapannya terkabul semua kak", 
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
                "kesan": "Abangnya baik ramah dan suka membantu",
                "pesan": "Semangat kuliahnya bang, sukses selalu ya", 
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
                "kesan": "kakaknya asik banget, sylenya boyish ",
                "pesan": "sehat terus kak, jangan kelelahan", 
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
                "kesan": "Kakaknya berwibawa dan kharismatik, keren",
                "pesan": "Semangat terus kak kuliahnya", 
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
                "kesan": "Kakaknya pinter dan inspiratif sekali",
                "pesan": "Terus memotivasi kami kak, semangat terus", 
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
                "kesan": "Abangnya humble dan asik juga",
                "pesan": "Semangat mengejar nilainya bang", 
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
                "kesan": "Kakaknya asik dan keren banget",
                "pesan": "Sukses selalu kak, semangat", 
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
                "kesan": "Abangnya ramah dan baik ",
                "pesan": "Semangat terus bang kuliahnya", 
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
                "kesan": "Kakaknya pasti sehat banget ya, ramah juga",
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
                "kesan": "Abangnya keren dan ramah",
                "pesan": "Sehat dan bahagia ya bang", 
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
                "kesan": "ramah, baik, dan inspiratif kakaknya",
                "pesan": "Sukses selalu, semangat!", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()
elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AmjM16_eVl1qty-qpQeBsUY49LsjKbhK",
            "https://drive.google.com/uc?export=view&id=1AyXNRk6IZxj-gIU8q-fTO3YXJn2Gg7NP",
            "https://drive.google.com/uc?export=view&id=1B4eLheFbhA4ruPVrDBlg18XlDm8g5nru",
            "https://drive.google.com/uc?export=view&id=1BfBlMNtO0dho_LgPxY0-jEq22bjyb2mq",
            "https://drive.google.com/uc?export=view&id=1BA7dmAstBfKRnoeJpBHkAGFQXxR_eAtq",
            "https://drive.google.com/uc?export=view&id=1B-jewURMfkZFdE_5pMNBgAQ_S7UyBnyd",
            "https://drive.google.com/uc?export=view&id=1BYE68XZEBrE1JGkP_-5d-J39UxrrXJFV",
            "https://drive.google.com/uc?export=view&id=1BOffgNHu9XJT1QmQSohU0lwEonq1iA5F",
            "https://drive.google.com/uc?export=view&id=1BtKZRqlUOdyy3pwYlOqf4YD1IUQib67H",
            "https://drive.google.com/uc?export=view&id=1B-jABB9FkUVrpeJNrIp3kg_MbRkCRSrA",
            "https://drive.google.com/uc?export=view&id=1B3swyCJ56-wLv03T1wDzLZoefMRfRLHu",
            "https://drive.google.com/uc?export=view&id=1B2A0ogX6R6BNlnRoqFURIs8UFT_FHWXD",
            "https://drive.google.com/uc?export=view&id=1AmLN6mAtCwT_x7U_wT4zd9axmHHkLY9O",
            "https://drive.google.com/uc?export=view&id=1BUy1UNIZ7JaFnUZ72WF6dhV2_xOJn684",
            "https://drive.google.com/uc?export=view&id=1BbP6L4fG3kQ7pOD4yzutPe21q1o2-fQs",
            "https://drive.google.com/uc?export=view&id=1AxdAyTSRlLDwt8dEPcWlF4UZllG2qQYP",
            "https://drive.google.com/uc?export=view&id=1BsAswkH4KNTo9L7M1yt0GApzQNuhxFGC",
            "https://drive.google.com/uc?export=view&id=1BdMv-Srt_XddhzPy9m9YZxaTBeWJ52vN",

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
                "kesan": "Ambisius dan pastinya pinter abangnya",
                "pesan": "semangat bang",
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
                "kesan": "Kakaknya baik dan ramah sekali ",
                "pesan": "Semangat kak!semoga sukses menjalani hidup", 
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
                "kesan": "hobbinya bagus bang melatih otak juga",
                "pesan": "Semangat terus bang, selalu olahraga bang biar sehat", 
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
                "kesan": "Baik dan ramah abangnya",
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
                "kesan": "Ramah dan suka menolong",
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
                "kesan": "Keren kakaknya, pinter juga keliatannya",
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
                "kesan": "abangnya keren dan jago ngoding nih kayaknya",
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
                "kesan": " ramah dan solutif abangnya",
                "pesan": "Semangat abang pj!selalu jadi orang baik bang", 
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
                "kesan": "Ramah dan baik banget kakaknya suka",
                "pesan": "Sukses selalu kak ya kak", 
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
                "kesan": "Keren kakaknya dan baik hati",
                "pesan": "Semangat selalu kakak", 
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
                "kesan": "kakaknya baik dan pinter juga",
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
                "kesan": "keren daa tidak sombong",
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
                "kesan": "ramah dan baik abangnya",
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
                "kesan": "abangnya humble dan suka menolong juga",
                "pesan": "Sukses selalu bang, jangan patang menyerah", 
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
                "kesan": "Keren banget dan pinter pastinya ",
                "pesan": "semangat terus bang", 
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
                "kesan": "Baik dan ramah banget kakaknya",
                "pesan": "terus semangat dan jaga kesehatan kak", 
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
                "kesan": "Baik dan selalu ramah abangnya",
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
                "kesan": "baik banget abangnya dan supportif juga",
                "pesan": "semangat terus bang! jangan lupa minum",
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
elif menu == "Departemen Eksternal":

    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kKYpuvasaPZ-KA2SyWkbhV1yrRAJLaLL",
            "https://drive.google.com/uc?export=view&id=1jrUlgTzJ4K_Ss0l8sDHADTCLrIdQr_Hm",
            "https://drive.google.com/uc?export=view&id=1kR4AoAW1PdQ-UxV3Ur8w9ASbVZHiQpjW",
            "https://drive.google.com/uc?export=view&id=1mAr7SH0O3Z7BVbPblqyK_-ptMG_yv6aj",
            "https://drive.google.com/uc?export=view&id=1kOSvVlUvc6tBs5BdKZIx-IPSwnvmInbS",
            "https://drive.google.com/uc?export=view&id=1kRePwe5QPFxwmc5ScXtJi0xoHfym18lT",
            "https://drive.google.com/uc?export=view&id=1SVaZP--zkBoNkQZbxx-pSrU79QyQb8WG",
            "https://drive.google.com/uc?export=view&id=1iymWqYUBHT-nehmfjXA0u9z0Bw-daCyW",
            "https://drive.google.com/uc?export=view&id=1kQ13Ko4HpPIcAqxbvMocyq5Bn8MHwtcb",
            "https://drive.google.com/uc?export=view&id=1kOf3G9twV2eG-63-vhqMyDG6-zS5sOjQ",
            "https://drive.google.com/uc?export=view&id=1SXsukP_lJRQAkrOCl9sii5q3Hd_Fb94t",
            "https://drive.google.com/uc?export=view&id=1P9ivC8ACYb2bDp6SIqvSv_a1XxlMrevg",
            "https://drive.google.com/uc?export=view&id=1jrE7yUuAcjG7LgftBo7KQDaVQ3ded3sf",
            "https://drive.google.com/uc?export=view&id=1PA3MUfJKruEBXZCBYMeHGbA0-hkD0SwL",
            "https://drive.google.com/uc?export=view&id=1dTPEOwDYGxIYXeK2DlpjlwQVLCatHqWG",
            "https://drive.google.com/uc?export=view&id=1k0iMyYLWsDuIouJW4cQTI32C2yki5wdA",
            "https://drive.google.com/uc?export=view&id=1b-06Tb7F_sOwzSZK24U_0ldXoAoNUIZ3",
            "https://drive.google.com/uc?export=view&id=1b0cPkvm14ikH03bCoRncORIfqVUKL0EX",
            "https://drive.google.com/uc?export=view&id=1jon-L2x3E67gvpf06xoPoBiGufac_djX",
            "https://drive.google.com/uc?export=view&id=1k-1YK4sanrLJAUVxjfRsotJdfM-2NaLJ",
            
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
                "kesan": "Abangnya baik dan selalu berbagi ilmu",
                "pesan": "Semakin sukses ya bang",
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
                "kesan": "keren dan aktif sih kakaknya",
                "pesan": "semangat selalu kak", 
                "jabatan" : "Sekretaris Departement", # 
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "asik banget dan lucu sih jokesnya masuk kak",
                "pesan": "sukses dan ceria terus kak", 
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
                "kesan": "Keren bang dan ramah juga",
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
                "kesan": "kak dea! daplok yang lucu, gemas, dan selalu supportif",
                "pesan": "Semangat terus ya kakk", 
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
                "kesan": "Asik banget dan lucu kakk, jaksel pride ya kak",
                "pesan": "Semangat terus kak", 
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
                "kesan": "aktif di organisasi an asik, wah kakaknya juga jaksel nih",
                "pesan": "Semangat ya kak", 
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
                "pesan": "bahagia selalu kak ", 
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
                "kesan": "Kakaknya baik dan unik",
                "pesan": "sukses terus kak semangat main sepak takrawnya ya", 
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
                "kesan": "Keren dan aktif juga abangnya keren",
                "pesan": "Jangan lupa istirahat dan minum ya bang", 
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
                "kesan": "Kakaknya asik dan keren",
                "pesan": "Sukses selalu, semangat belajar kuiahnya kak", 
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
                "kesan": "baik dan keren sih bikin porto hobinya",
                "pesan": "Selalu semangat bang, sukses", 
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
                "kesan": "Asik orangnya, hobinya juga unexpected banget",
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
                "kesan": "Kakaknya asik, semangat juga keliatannya",
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
                "kesan": "Baik dan ramah kakaknya",
                "pesan": "selalu sukses, bahagia dan jangan stress ya kak", 
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
                "kesan": "Keren dan baik hati abangnya",
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
                "kesan": "Baik dan ramah kakaknya",
                "pesan": "semangat terus ya kak", 
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
                "kesan": "Baik hati dan suka mengaji",
                "pesan": "Sukses selalu kakk, jangan stress kak", 
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
                "kesan": "humoris dan sangat memberi motivasi bang",
                "pesan": "Bahagia selalu bang, terus menolong orang bang", 
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
                "kesan": "baik banget dan asik juga",
                "pesan": "Semangat kak, jangan menyerah", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },

           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    eksternal()
elif menu == "Departemen Internal":

    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Xm998gAEVwmchKMxnGlXYGxxVOff4msD",
            "https://drive.google.com/uc?export=view&id=1YELdiY8fTDbUIONlcS1CZ4Y8XSAmkRWM",
            "https://drive.google.com/uc?export=view&id=1XruhCTm8JqIOsp7oEND-qzjyb9T4oelT",
            "https://drive.google.com/uc?export=view&id=1YFb2IkG2hl6NufCzRI52oM5RGOfaylxl",
            "https://drive.google.com/uc?export=view&id=1XxHNHoMi5ZHHLHQP16q1B3fyVRTw5AxM",
            "https://drive.google.com/uc?export=view&id=1XAOghvMihWfPELdWcb7JWmGeZK2QWkI-",
            "https://drive.google.com/uc?export=view&id=1XmZR2Gv2fpVz5GBF-kV0QfhwUXLvHtva",
            "https://drive.google.com/uc?export=view&id=1XsqEBgMfv75oV1-_02_GtnTZypkJf1NE",
            "https://drive.google.com/uc?export=view&id=1Y3rA8TmEsqjflzpUMrOlvBWK9209GZ5x",
            "https://drive.google.com/uc?export=view&id=1XsvriMQ4BxP-ql5aloUHEuW-z8xgLHBh",
            "https://drive.google.com/uc?export=view&id=1XygFn5tvPirMAv2wX5yNYejNEWMwwVfX",
            "https://drive.google.com/uc?export=view&id=1YBDl-l-j8cNNY3VViL1UqE3uSNMplQlF",
            
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
                "kesan": "Keren banget dan menginspirasi",
                "pesan": "Sukses selalu dan selalu optimis bang",
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
                "kesan": "Baik dan ramah kakaknya",
                "pesan": "selalu ramah sama setiap orang kak", 
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
                "kesan": "keren dan baik bang",
                "pesan": "semangat terus bang, jangan menyerah!", 
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
                "kesan": "kalem dan ramah kak",
                "pesan": " hobinya bermanfaat semua, sukses kak!", 
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
                "kesan": "baik dan ramah ",
                "pesan": "selalu optimis ya kak", 
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
                "kesan":"keren dan pinter bang",
                "pesan": "semangat terus belajarnya bang", 
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
                "kesan": "baik dan invormatif",
                "pesan": "semangat menjani harinya bang", 
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
                "kesan": "Keren dan kece abangnya",
                "pesan": "semoga menang terus bang main futsalnya", 
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
                "kesan": "baik dan ramah banget abangnya",
                "pesan": "selalu semangat dan jangan patah semangat bang!", 
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
                "kesan": "kalem dan ramah banget keliatannya",
                "pesan": "Bahagia selalu kak, jangan stress", 
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
                "kesan": "Kakaknya baik dan ramah banget",
                "pesan": "sehat selalu kak", 
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
                "kesan": "daplok yang supportif dan asik banget",
                "pesan": "Semangat ya bangg, kalau cape istirahat", 
                "jabatan" : "Staff Kerohanian", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    internal()
elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15dhTvL-0qDm4KUXCEKW5-EkuuZWYy04t",
            "https://drive.google.com/uc?export=view&id=15wpFXd5GTCj9QOGl76q0bbnL45_cOUFn",
            "https://drive.google.com/uc?export=view&id=15l28m9jZv2grW232Aif5brY__Baass7U",
            "https://drive.google.com/uc?export=view&id=15zeHTgYX1mT-u8-7ltlJD3F9kbzwbW2p",
            "https://drive.google.com/uc?export=view&id=15f1Mdht9fC6I0kbo7uWpeQf-rtlUTyWK",
            "https://drive.google.com/uc?export=view&id=15k0oDTepWcLzy0_jS8dLfYVER5ab65A-",
            "https://drive.google.com/uc?export=view&id=15w0hz2Tnk26Tso4aR3vp42KHBUc_qs-u",
            "https://drive.google.com/uc?export=view&id=1MVwlE2RUqWBRjHHmikEbsMajtub080Bp",
            "https://drive.google.com/uc?export=view&id=15eeTvkHeTJobOMgdUM6MHYCWxA3CDQlg",
            "https://drive.google.com/uc?export=view&id=15dYT5GR_tYEmKhyRmIjWZMEO5mHKwB5t",
            
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
                "kesan": "pasti relasinya dimana-mana",
                "pesan": "makin sukses dan semakin memotivasi bang",
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
                "kesan": "ramah dan keren banget",
                "pesan": "Semangat kak, semoga cita-citanya tercapai", 
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
                "kesan": "keahliannya sangat berguna ya kak",
                "pesan": "Semangat kak, semoga makin banyak uangnya", 
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
                "kesan": "pembawaannya asik dan jago banget marketingnya",
                "pesan": "semangat bang jualannya!stikernya", 
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
                "pesan": "Semangat bang, makin banyak duitnya", 
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
                "kesan": "keren dan berwibawa sih abangnya",
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
                "kesan": "Kakaknya kayaknya ramah dan baik banget",
                "pesan": "Semangat kak kuliahnya! terus jadi orang baik", 
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
                "kesan": "kakaknya keren dan berkharisma banget",
                "pesan": "Semoga makin sukses ya kak! semangat", 
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
                "kesan": "Kakaknya asik banget dan positif vibes",
                "pesan": "Semangat terus kak! jangan pantang menyerah", 
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
                "kesan": "Abangnya kalem dan ramah",
                "pesan": "Semangat terus bang kuliahnnya", 
                "jabatan" : "Staff sponsor", # 1
            },
           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()

elif menu == "MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15cGzGOexgGS4uZmlG6xmS_T99jrKIYg5",#1
            "https://drive.google.com/uc?export=view&id=15PIqaPobXgvG3soQGeRz_lZYDPa--9zO",#2
            "https://drive.google.com/uc?export=view&id=15Tp7XOP5sIUJTcIU8csP6Z-XsyWl3T-4",#3
            "https://drive.google.com/uc?export=view&id=15DOiMB_gdMxxuhHwVpicRUL-Oz-uCOuG",#4
            "https://drive.google.com/uc?export=view&id=15Uke_mXgLpyu6m8-605qUMmCiKvO68WQ",#5
            "https://drive.google.com/uc?export=view&id=14lZMRwGUsRdRrdML86YE1B2wW2zp6CPp",#6
            "https://drive.google.com/uc?export=view&id=15IT91svYjQaCaRfeo31lRi-kQv29alCn",#7
            "https://drive.google.com/uc?export=view&id=15RXiSQSA53Ecs2OYLombYJq6MXFiiYkC",#8
            "https://drive.google.com/uc?export=view&id=14nE1W3HSxAGCyMDJG8PcRHYzviap_-Lb",#9
            "https://drive.google.com/uc?export=view&id=15Npx6xB5roGQi3395quA2Tor1wZ9k0V5",#9
            "https://drive.google.com/uc?export=view&id=15PRBXYr87h4cbUi1BW3Zuxe8lZXQEtUw",#10
            "https://drive.google.com/uc?export=view&id=1562UOjbMtor5K-gZ5WzxxV51D0rW3aVq",#11
            "https://drive.google.com/uc?export=view&id=1539TMLrhNhj_1-u6WufaUE4jU6UHtfG4",#12
            "https://drive.google.com/uc?export=view&id=14z3-auN29QIHGHkq7x1S0PkLNNK3XTTJ",#13
            "https://drive.google.com/uc?export=view&id=14px3za3ESTTNTr8ODJCjJuxfViXlx7Mx",#14
            "https://drive.google.com/uc?export=view&id=14si5mrjZOV9vH4PQB5yPSRKloLaRY06m",#15
            "https://drive.google.com/uc?export=view&id=14o02oqINW8kzo3QML2q6rH9koiqUi-Ut",#16
            "https://drive.google.com/uc?export=view&id=15N3ywqqAsjpTXBwP1wwa_K7o92nChHtS",#17
            "https://drive.google.com/uc?export=view&id=157mZ2MSuP1CgUsGKJiklmBLs9mjJkUKB",#18
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
                "kesan": "abangnya kharismatik dan tegas",
                "pesan": "Semangat terus bang kuliahnya!",
                "jabatan" : "Kepala departemen",  
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "manis dan ramah banget",
                "pesan": "Semangat ya kak! semoga makin sukses", 
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
                "kesan": "Kakaknya ramah dan baik banget",
                "pesan": "semangat kak jangan stress kuliahnya", 
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
                "kesan": "Abangnya ramah dan talkactive",
                "pesan": " sehat terus bang", 
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
                "kesan": " kelihatannya pinter dan jago banget",
                "pesan": " semangat ngodingnya bang", 
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
                "kesan": "keren dan stylish banget",
                "pesan": "semangat kuliahnya kak!", 
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
                "kesan": "pasti orangnya sibuk banget ya kak",
                "pesan": "Jangan lupa minum dan istirahat kak", 
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
                "kesan": "kpopers ya kak?",
                "pesan": "semangat terus kak kuliah dan ngejalanin hobinya", 
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
                "kesan": "ramah dan lucu kakaknya",
                "pesan": "semangat kak, jangan stress kuliahnya", 
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
                "kesan": "Keren sih kak hobinya",
                "pesan": " semangat terus kak kuliahnya, ayo ngoding bareng", 
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
                "kesan": "keren dan Baik banget kakaknya",
                "pesan": "semangat kak buat kontennya ", 
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
                "kesan": "Kakaknya baik hati dan ramah ",
                "pesan": "Semangat kak, selalu ramah dimanapun itu", 
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
                "kesan": "Baik dan ramah abangnya",
                "pesan": "improv terus skill pddnya bang!semangat", 
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
                "pesan": "terus jadi diri yang positif ya Kak, sukses selalu!", 
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
                "pesan": "Tetap semangat ngodingnya bang", 
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
                "pesan": "Semangat bang, tetep jaga kesehatan dan terus berkarya.", 
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
                "pesan": "Tetap semangat ya, Kak! jaga kesehatan juga", 
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
                "pesan": "Tetep positif dan bahagia, Kak! ", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    medkraf()


    

    



# Tambahkan menu lainnya sesuai kebutuhan
