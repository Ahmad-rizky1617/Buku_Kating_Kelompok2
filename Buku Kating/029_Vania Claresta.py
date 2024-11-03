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
            "https://drive.google.com/uc?export=view&id=1naWWiP0QDQMfR1dcNG4lRYjp6geiVJ6p",
            "https://drive.google.com/uc?export=view&id=1ndWyt4pk5eOAfz9TeNXmi3emBX93415z",
            "https://drive.google.com/uc?export=view&id=1nlDjitisHsSbyIgnUMwsBI_Fgd75HC5h",
            "https://drive.google.com/uc?export=view&id=1nbAPhEAhw-s-zzPB1QGWzEF2_QtcEIof",
            "https://drive.google.com/uc?export=view&id=1nfU24R4eqmPFzbsD3H7L5lJYcQ6g9os9",
            "https://drive.google.com/uc?export=view&id=1nmJNyKD1wAvub_8BtHG1R8tD76U_5uDW",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Denger musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abangnya asik dan cepat respon",  
                "pesan":"semangat kuliahnya bang",
                "jabatan": "Ketua Himpunan"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abangnya baik dan cepat respon",  
                "pesan":"semoga sukses dalam merai cita-cita nya bang",
                "jabatan": "Sekretaris Jendral"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini ramah",  
                "pesan":"Semoga kakak sukses dalam studinya",
                "jabatan": "Sekretaris Umum"# 1
            },
            {
                "nama": "Hartiti Fadillah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Denger musik",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini ramah dan lembut",  
                "pesan":"Semoga kakak sukses dalam studinya dan skripsinya",
                "jabatan": "Bendahara Umum"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini ramah dan cepat respon",  
                "pesan":"Semoga segala impian tercapai",
                "jabatan": "Sekretaris 1"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Baca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak ini ramah",  
                "pesan":"Semoga kakak sukses dalam studinya",
                "jabatan": "Bendahara 1"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Rqj-2KnpYZ9bQiWDWMrozXo7d4AWe-Xl",
            "https://drive.google.com/uc?export=view&id=1RnUnQQuRisUZPd0BJlVLrbnuuhsiRvMe",
            "https://drive.google.com/uc?export=view&id=1RzJdAyrHJJnydZfTI9HWSsZ1evgV2s2R",
            "https://drive.google.com/uc?export=view&id=1RreIhlSFkApDy6CW4Sk5vKrVMnW9XQhb",
            "https://drive.google.com/uc?export=view&id=1RoD9Rw3Cx3TX177hJ0oS4n-w7YToaQuH",
            "https://drive.google.com/uc?export=view&id=1RxceoRKV4MwZlwBAp00KIfrolT5QmSx8",
            "https://drive.google.com/uc?export=view&id=1Rsdgrq5kM0MMzanD2yqwJvYiodAx-LcY",
            "https://drive.google.com/uc?export=view&id=1S94CLhb6mpVKNdt7c-xKL5LKdqIxsXYi",
            "https://drive.google.com/uc?export=view&id=1S7Qu4n_ydXrbDdOqpEAGI6F3UsxmUjVQ",
            "https://drive.google.com/uc?export=view&id=1Rsdgrq5kM0MMzanD2yqwJvYiodAx-LcY",
            "https://drive.google.com/uc?export=view&id=1S2cFo5n-_6C326oF9yZ0xM8qsbuzYiIZ",
            "https://drive.google.com/uc?export=view&id=1RrZe4tf6WNvyX5vUT1OjLdX95Odix7Jp",
            "https://drive.google.com/uc?export=view&id=1S7CgABU38B-TIQPWAsTEe81Xw73UcXTO",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Tanya sama gpt",
                "sosmed": "@trimurniaa",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat dan sukses untuk segala yang sedang diusahakan",
                "jabatan": "Ketua Badan Legislatif"# 1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Puasa Senin Kamis",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat kuliahnya kak",
                "jabatan": "Sekretaris"# 2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kak",
                "jabatan": "Bendahara"# 3
            },
            {
                "nama": "Annisa Dini Amalia",
                "nim": "121450021",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kak dan sukses terus",
                "jabatan": "Kepala Komisi 1 Legislatif"# 4
            },
            {
                "nama":"Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kak",
                "jabatan": "Kepala Komisi 2 Aspirasi dan Pengawasan"# 5
            },
            {
                "nama": "Muhammad Fachrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Sholat malam",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya bang dan sukses",
                "jabatan": "Kepala Komisi 3 Media"# 6
            },
            {
                "nama": "Annisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kalianda",
                "hobbi": "Membaca Al Waqiah setiap magrib",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini baik dan cepat respon",  
                "pesan":"semangat terus kuliahnya kak",
                "jabatan": "Anggota Komisi 1 Legislatif"# 7
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini baik dan cepat respon",  
                "pesan":"semangat dan sukses dalam studinya bang",
                "jabatan": "Anggota Komisi 1 Legislatif"# 8
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Bca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini baik dan cepat respon",  
                "pesan":"semangat terus kuliahnya kak",
                "jabatan": "Anggota Komisi 1 Legislatif"# 9
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya dan sukses selalu bang",
                "jabatan": "Anggota Komisi 2 Aspirasi"# 10
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Organ Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung f",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini baik dan cepat respon",  
                "pesan":"semangat terus kuliahnya kak dan sukses",
                "jabatan": "Anggota Komisi 2 Aspirasi"# 11
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca buku, ngoding, ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini baik dan lembut",  
                "pesan":"semangat terus kuliahnya kak",
                "jabatan": "Anggota Komisi 3 Legislatif"# 12
            },
            {
                "nama": "Jeremia Susanto",             
                "nim": "122450022",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Bilabong",
                "hobbi": "Cerita",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini baik dan cepat respon",  
                "pesan":"semangat terus kuliahnya kak",
                "jabatan": "Anggota Komisi 3 Legislatif"# 13
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bixTwe-6hUKxS8PEGnXBvKyEzHqjkQyA",
            "https://drive.google.com/uc?export=view&id=1Leuaq-2dIhVZo4q1BGGGLyjCiPQfPRYk",    
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lamoung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "Kakak ini baik dan public speaking nya keren",  
                "pesan":"sukses terus kak",
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
                "kesan": "Abang ini baik",  
                "pesan":"Semangat kuliahnya bang",
                "jabatan": "Anggota"# 2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
# Tambahkan menu lainnya sesuai kebutuhan
