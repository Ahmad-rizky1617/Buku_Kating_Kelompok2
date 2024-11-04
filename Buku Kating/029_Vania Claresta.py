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
            "Departemen Medkraf"
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
                "pesan":"semangat kuliahnya bang semoga bisa magang di telkom juga kek abg",
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
                "pesan":"semoga sukses dalam meraih cita-cita nya bang semangat ngasprak alpro bg",
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
                "pesan":"kakaknya cantik dan baik, terima kasih untuk ilmu nya kak",
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
                "kesan": "Kakak ini ramah dan cepat respon asik banget",  
                "pesan":"Semoga segala impian tercapai, ayo kita cerita cerita lagi kak",
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
                "kesan": "Kakak ini baik dan lembut",  
                "pesan":"Semoga kakak sukses dalam studinya dan semangat ngasprak strukdat ya kak",
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
            "https://drive.google.com/uc?export=view&id=1S7Qu4n_ydXrbDdOqpEAGI6F3UsxmUjVQ",
            "https://drive.google.com/uc?export=view&id=1S2cFo5n-_6C326oF9yZ0xM8qsbuzYiIZ",
            "https://drive.google.com/uc?export=view&id=1RoD9Rw3Cx3TX177hJ0oS4n-w7YToaQuH",
            "https://drive.google.com/uc?export=view&id=1RxceoRKV4MwZlwBAp00KIfrolT5QmSx8",
            "https://drive.google.com/uc?export=view&id=1S94CLhb6mpVKNdt7c-xKL5LKdqIxsXYi",
            "https://drive.google.com/uc?export=view&id=1RzVDxd9Q93M25RNnKeAIYbvvTPiFZhAZ",
            "https://drive.google.com/uc?export=view&id=1Rsdgrq5kM0MMzanD2yqwJvYiodAx-LcY",
            "https://drive.google.com/uc?export=view&id=1RrZe4tf6WNvyX5vUT1OjLdX95Odix7Jp",
            "https://drive.google.com/uc?export=view&id=1S7CgABU38B-TIQPWAsTEe81Xw73UcXTO",#done
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
                "pesan":"semangat ngasprak alpro terima kasih sudah banyak membantu codingan alpro kalau error kak",
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
                "pesan":"baik sekali hobinya kak",
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
                "pesan":"suka film drakor ga kak",
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
                "pesan":"jaya terus kak",
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
                "kesan": "Kakak ini baik dan asik",  
                "pesan":"kak hobinya keren banget suka baca jurnal, semoga nular kak",
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
                "pesan":"keren nya hobinya bang",
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
                "pesan":"semangat kuliah kak, untuk hobinya dilanjutkan terus ya kak",
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
                "pesan":"semangat dan sukses dalam studinya bang terus lanjutkan hobinya bg",
                "jabatan": "Anggota Komisi 1 Legislatif"# 8
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini baik dan cepat respon",  
                "pesan":"semangat terus kuliahnya kak keren sekali hobinya kak",
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
                "pesan":"semangat terus kuliahnya dan sukses selalu bang jaga kesehatan selalu bg",
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
                "kesan": "Kakak ini baik dan unik juga lucu",  
                "pesan":"semangat nyari sinyal kak meskipun di gedung f sinyal nya suka hilang-hilang",
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
                "pesan":"ajarin ngoding kak",
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
                "pesan":"suka cerita apa tu bang",
                "jabatan": "Anggota Komisi 3 Legislatif"# 13
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eHMKKfc3HEC4YYmAy0cqyWYYVcAcbm82",
            "https://drive.google.com/uc?export=view&id=1eJ-YHTxATDoZiK-3Fa3VSJ6IpSe-wQro",#done
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
                "pesan":"tips bisa mahir public speaking donk kak",
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
                "pesan":"bahagia terus bg",
                "jabatan": "Anggota"# 2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eAKSz7fEbxr75ZaIoE1YPnVrvWAlIafl",#ericson
            "https://drive.google.com/uc?export=view&id=1eCDWwhsnMaWBMIC3J5hVnLLWhE5AfVHM",#elisabeth
            "https://drive.google.com/uc?export=view&id=1e8QC5AevsnwgYZ9YtMauDldeL_DUJPSS",#devyan
            "https://drive.google.com/uc?export=view&id=1dx2Dmex5iVknJGvvBv3uqtpiYfk5mrBU",#nisrina
            "https://drive.google.com/uc?export=view&id=1dukQJSdF3XE4vOhb-xJsNHf_X4u44t5d",#farhan
            "https://drive.google.com/uc?export=view&id=1e4cBSVFFtC4UrXYg29_uVzctvjfOJWTD",#johannes
            "https://drive.google.com/uc?export=view&id=1e5smFs5u-Tj_QdMZzgY58DTRQYsjEqsJ",#kemas
            "https://drive.google.com/uc?export=view&id=1eDg4pn-niJYB_WLLsAQkaTEvuSYMBtjf",#presilia
            "https://drive.google.com/uc?export=view&id=1e6ptt4598kunbZiPfH96ATZtZT-3vV4k",#aqila
            "https://drive.google.com/uc?export=view&id=1e9rafcPgvsGfAkHm_6kX7UqLZn6c_aDq",#sahid
            "https://drive.google.com/uc?export=view&id=1e9nF12SqfWkfmJr4BmY7dpltctmCKg82",#vanessa
            "https://drive.google.com/uc?export=view&id=1e2IHglu3uJupRCt-4O-7ZOX2ZGhiYs3R",#allya
            "https://drive.google.com/uc?export=view&id=1dwRJPkb3FuOVm7FWT4GR3JSmkuNjJ8AP",#eksanty
            "https://drive.google.com/uc?export=view&id=1e3NbsCOgNY96sTKwQ1a5fdMUcnTUgOQf",#deri
            "https://drive.google.com/uc?export=view&id=1dzxswbds0pWbFTv1tDTsl-aLojP1MLVk",#okta
            "https://drive.google.com/uc?export=view&id=1dtsmuDiQ5RbczV2V4ObVezERI9i_lRNp",#gede
            "https://drive.google.com/uc?export=view&id=1dq_DZOiSBxbukrrJRTsKoXHnNM2cgz9V",#jaclin
            "https://drive.google.com/uc?export=view&id=1ds14HDz8aoU0VhmssBm4oJtIMT351GWF",#rafly
            "https://drive.google.com/uc?export=view&id=1dpzqhX8beEBns20PpspZJ2ntIdF9p2o6",# andini done
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan berwibawa",  
                "pesan":"semangat terus sampai akhir bang",
                "jabatan": "Kepala Departemen PSDA"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini asik dan semangat",  
                "pesan":"jaga kesehatan kak",
                "jabatan": "Sekretaris"# 2
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Ternyata kita satu kampung halaman ya bg",  
                "pesan":"semangat skripsi bang",
                "jabatan": "Kepala Divisi Manajemen Minat dan Bakat"# 3
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": " 122450033",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter-muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini cantik",  
                "pesan":"hobinya unik kak",
                "jabatan": "Kepala Divisi Kaderisasi"# 4
            },
            {
                "nama":"M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@dmfarhan.ath",
                "kesan": "Abangnya baik dan asik saat wawancara",  
                "pesan":"keren sekali hobinya bang",
                "jabatan": "Kepala Divisi Olahraga dan Perlombaan"# 5
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@jonanneskrisjnnn",
                "kesan": "Abang ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya bang dan sukses ngaspraknya",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"# 6
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main game",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini baik dan pinter ngoding",  
                "pesan":"semangat terus upgrade skillnya bang",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"# 7
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "Kakak ini baik dan sangat sopan",  
                "pesan":"semangat untuk hobinya kak",
                "jabatan": "Bendahara Divisi Manajemen Minat dan Bakat"# 8
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqila",
                "kesan": "Kakak ini baik dan lembut dan kita satu asal provinsi ya kak",  
                "pesan":"infokan judul webtoon yang menarik kak",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"# 9
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Abang ini baik dan ramah",  
                "pesan":"semangat kuliah bg jaga kesehatan",
                "jabatan": "Staff Divisi Manjemen Minat dan Bakat"# 10
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "perum Kropri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes_",
                "kesan": "Kakak ini baik dan cepat respon",  
                "pesan":"semangat terus kuliahnya kak dan lancar skripsinya",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"# 11
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini cepat bersosialisasi",  
                "pesan":"ayo nongs bareng kak",
                "jabatan": "Staff Divisi Kaderisasi"# 12
            },
            {
                "nama": " Eksanty Febriana Sukma Islamiaty",             
                "nim": "122450001",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Natar ",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini baik dan asprak saya dulu waktu fisdas tpb",  
                "pesan":"semangat nyari sinyal nya kak",
                "jabatan": "Staff Divisi Kaderisasi"# 13
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": " 122450051",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Abang ini baik dan lucu",  
                "pesan":"abangnya cocok jadi pemateri soalnya asik dan ga ngebosenin",
                "jabatan": "Staff Divisi Kaderisasi"# 14
            },
            {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": " 122450041 ",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "Kakak ini baik dan lucu",  
                "pesan":"semangat kuliah dan scroll tiktoknya kak jaga kesehatan selalu",
                "jabatan": "Staff Divisi Kaderisasi"# 15
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya ",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abangnya keren",  
                "pesan":"semangat skripsi bang, keren hobinya suka membaca",
                "jabatan": "Staff Divisi Olahraga dan Perlombaan"# 16
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":" Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakak ini baik dan lembut",  
                "pesan":"semangat terus kuliahnya kakak cantik",
                "jabatan": "Staff Divisi Olahraga dan Perlombaan"# 17
            },
            {
                "nama": "Rafly Prabu Darmawan",             
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini baik",  
                "pesan":"semangat bang bahagia selalu ya",
                "jabatan": "Staff Divisi Olahraga dan Perlombaan"# 18
            },
            {
                "nama": "Syalaisha Andini Putriansyah",             
                "nim": " 122450111",
                "umur": "21",
                "asal":" Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_ ",
                "kesan": "Kakak ini baik",  
                "pesan":"hobinya keren kak",
                "jabatan": "Staff Divisi Olahraga dan Perlombaan"# 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()
    
elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZDq6PegKOKfIyuTqUsw-ZuFForvUwsJK",#rafi
            "https://drive.google.com/uc?export=view&id=1ZfoVtTExFEUbGyF4KPMDBKL6c5nLYm-_",#annisa
            "https://drive.google.com/uc?export=view&id=1ZGczZDXcbZIGZYpTDhSaJS7DkN4aMXGv",#ahmad sahidin
            "https://drive.google.com/uc?export=view&id=1a_sViNswtHfe8C5Ebb3_7ONT3NlonYyK",#fadhil
            "https://drive.google.com/uc?export=view&id=1ZGqMm2UEgLZ_2eicn8bMzR7Bxv1TwQwA",#regi
            "https://drive.google.com/uc?export=view&id=1Z_7yttFRd_8W0kaJrS6vsnc39XXZS5XM",#syalaisa
            "https://drive.google.com/uc?export=view&id=1ZGFRGnb7rLHYDt_8RyEA7_JqyNLlsl-F",#natanael
            "https://drive.google.com/uc?export=view&id=1ZJU5wHRbvXHLgtGhGbNNN-NADMmJUNfi",#anwar
            "https://drive.google.com/uc?export=view&id=1ZPBG32VWclujSmE2xQvikkOe5Hhgz0FJ",#kk deva
            "https://drive.google.com/uc?export=view&id=1Zc_CoHYeRUCgnshC5qQrWnvtdgE0rQM_", #dinda
            "https://drive.google.com/uc?export=view&id=1ZKbHau1vC9D1NyPSgC0xmkYck4aZAeDK",#marleta
            "https://drive.google.com/uc?export=view&id=1ZV57ERBiROHEDyaoWWMBMwE1ylCSsesw",#rut
            "https://drive.google.com/uc?export=view&id=1ZT8JfzNIsjVg2ps1kM_k-NwlsWL4X0Ti",#puspa
            "https://drive.google.com/uc?export=view&id=1ZguFj_0cfUNiWU4qxRmnP6Jhth7uxkcd",#abdurrahman
            "https://drive.google.com/uc?export=view&id=1ZnmycaXLGATlfQIzjx1T9E6jVLGaJCpf",#adit
            "https://drive.google.com/uc?export=view&id=1Zra0p0OeXfmsMXB9eG0nNUnXaB0Mh4eA",#eggi
            "https://drive.google.com/uc?export=view&id=1ZglQLyq6J1cbI_VqC1_YZ895vtbI2tqd",#febiya
            "https://drive.google.com/uc?export=view&id=1ZrK5tMsAMCpAndI3s8_xMsUCax2228_7",#syahrul
            "https://drive.google.com/uc?export=view&id=1ZkUsVx42cSKCiBh7RJwuRTH49mRBBtyA",#randa done
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "Abangnya tegas dan antusias dalam menyemangati kami",  
                "pesan":"semangat olahraga nya bang",
                "jabatan": "Kepala Departemen MIKFES"# 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak ini lembut dan cantik",  
                "pesan":"waw pasti masakan kk nya enak semua",
                "jabatan": "Sekretaris Departemen MIKFES"# 2
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang ini baik",  
                "pesan":"semangat dan sukses terus bang,semangat juga olaharaganya bg",
                "jabatan": "Staff Divisi Club dan Komunitas"# 3
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": " 122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung ",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya baik",  
                "pesan":"semangat terus kuliahnya bang dan jaya selalu",
                "jabatan": "Staff Divisi Club dan Komunitas"# 4
            },
            {
                "nama":"Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya baik dan keren banget jadi duta",  
                "pesan":"semangat terus kuliahnya bang, cocok bg jadi duta doa terbaik buat abg",
                "jabatan": "Staff Divisi Club dan Komunitas"# 5
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": " 122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gg Yudhistira ",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak nya lembut dan ramah",  
                "pesan":"semangat terus kuliahnya kak dan tetap bahagia terus",
                "jabatan": "Staff Divisi Club dan Komunitas"# 6
            },
            {
                "nama": " Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kemiling ",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": " @natanaeloks",
                "kesan": "Abang ini baik dan inspiratif",  
                "pesan":"semangat terus kuliahnya bang dan sukses untuk inspirasi selanjutnya",
                "jabatan": "Kepala Divisi Pusat Inovasi dan Kajian Akademik"# 7
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Korpri ",
                "hobbi": " ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abang ini baik dan jago matematika",  
                "pesan":"semangat jadi mentor tugas kelompok kami ya bg, makin jago matematikanya bang",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"# 8
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": " @anjaniiidev",
                "kesan": "Kakak ini baik dan lembut",  
                "pesan":"rekomendasi film yang bagus kak",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"# 9
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":" Medan",
                "alamat": "Jl. Lapas",
                "hobbi": " ",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya baik dan cute",  
                "pesan":"semangat terus kuliahnya dan sukses selalu kak",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"# 10
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":" Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini baik dan cantik",  
                "pesan":"semangat terus kuliahnya kak suka liatin jurnal apa kak",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"# 11
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":" Batam, Kep.Riau",
                "alamat": " Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini suka senyum dan pinter, keren hobinya resume jurnal",  
                "pesan":"semangat terus kuliahnya kak,semangat juga ngasprak alpronya kak",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"# 12
            },
            {
                "nama": " Syadza Puspadari Azhar",             
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": " Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini baik dan suka bantuin pas praktikum",  
                "pesan":"semangat dan sukses terus kuliahnya kak, semangat ngasprak kak",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"# 13
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " 121450128",
                "umur": "23",
                "asal":"Bandar Lampung",
                "alamat":  "Perumnas Way Kandis ",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Abang ini baik",  
                "pesan":"semangat terus kuliahnya bang, suka baca apa tu bg",
                "jabatan": "Kepala Divisi Survei dan Riset"# 14
            },
            {
                "nama": "Aditya Rahman",
                "nim": " 122450113",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abang ini baik, jago jadi pemateri",  
                "pesan":"semangat terus kuliahnya dan sukses selalu bang semangat ngoding bg",
                "jabatan": "Staff Divisi Survei dan Riset"# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr ",
                "kesan": "Abangnya baik",  
                "pesan":"semangat terus kuliahnya bang dan sukses untuk semua yang sedang dikerjakan semangat ngoding bg",
                "jabatan": "Staff Divisi Survei dan Riset"# 16
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":" Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama ",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini baik dan lembut",  
                "pesan":"semangat terus kuliahnya kakak cantik, rekomendasi k-drama yang bikin baper kak",
                "jabatan": "Staff Divisi Survei dan Riset"# 17
            },
            {
                "nama": "Happy Syahrul Ramadhan",             
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abang ini baik",  
                "pesan":"semangat dan sukses terus kuliahnya bang",
                "jabatan": "Staff Divisi Survei dan Riset"# 18
            },
            {
                "nama": "Randa Andriana Putra",             
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abang ini baik dan pinter ADS",  
                "pesan":"semangat dan sukses terus kuliahnya kak, semangat juga untuk ngasprak ADS bang",
                "jabatan": "Staff Divisi Survei dan Riset"# 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

    
elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_9BVd38ynoY4Uk_OQG9a2AWNYAhk2tbj",
            "https://drive.google.com/uc?export=view&id=1_0CP9eInfa0uJmoXiBRVVQ7WxqaGa1Q0",
            "https://drive.google.com/uc?export=view&id=1_PjP5UXSVDVhKpdPsRkgkmot8dO_it2m",
            "https://drive.google.com/uc?export=view&id=1mOqy2mC2EB2QbuoONoPZtlJbMjWyWRT4",#bg bastian
            "https://drive.google.com/uc?export=view&id=1_Aktn-WwiJqAaHVMxSBSxhxW4EkZCICi",
            "https://drive.google.com/uc?export=view&id=1_TdGNBjl8HkS7ecvnCbz84J15HLp44PD",
            "https://drive.google.com/uc?export=view&id=1_XYAOnrsUaGXRqcJPeYgSC9t_b_MjWP4",
            "https://drive.google.com/uc?export=view&id=1jEIhIMHTH0cAoVuHc7YiOdtamNZzIqIY",
            "https://drive.google.com/uc?export=view&id=1_Jad5CkpBXOHeW2U-VGCaYkgttj-kC_a",
            "https://drive.google.com/uc?export=view&id=1_BmoF3tSUytKbONighfbRkVp53KfvOVX",
            "https://drive.google.com/uc?export=view&id=1_W5kajaZXZ1wfM0RWLzPkd_uavQyJmTb",
            "https://drive.google.com/uc?export=view&id=1gmeOk87rjxSzsLXuwtpJhTKgwrUktecu",
            "https://drive.google.com/uc?export=view&id=1ZzMXgSbkh4vZNlSQqxkwzDg_LPdT9IBu",
            "https://drive.google.com/uc?export=view&id=1Zv7FJMpF5LbmTMijr5GgwGhMLXanRuy9",
            "https://drive.google.com/uc?export=view&id=1_5Iy-DfSRHRy_wuJN1y_Yemnvyhqrc4q",
            "https://drive.google.com/uc?export=view&id=1_ZxKf7LX2Z3ugzSrXRpqmbs-BmZkWKfI",
            "https://drive.google.com/uc?export=view&id=1c5mAzOQa8BmP1vbTj7ICQu2gJ41h-R-V",
            "https://drive.google.com/uc?export=view&id=1Zz9XDNRl8DZNey4s3wjn9M6pJ-J-f8Wr",
            "https://drive.google.com/uc?export=view&id=1Zx6_J4ATHIKCZXnRNdBbs_48NiinEI10",#done
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":" Tangerang",
                "alamat": "Jatimulyo ",
                "hobbi": "BAB setiap jam 7 pagi",
                "sosmed": "@yogyst",
                "kesan": "Abangnya baik dan fast respon",  
                "pesan":"semangat terus bg doa terbaik untuk abang",
                "jabatan": "Kepala Departemen Eksternal"# 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakak nya cantik",  
                "pesan":"semangat kuliahnya kak, suka jalan-jalan kemana kak",
                "jabatan": "Sekretaris Departemen Eksternal"# 2
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Kochpri ",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak ini baik dan asik waktu wawancara",  
                "pesan":"semangat dan sukses terus kak, ajarin main golf kak",
                "jabatan": "Kepala Divisi Hubungan Luar"# 3
            },
            {
                "nama": "Bastian Heskia Silaban ",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abangnya baik keren banget hobinya menggambar",  
                "pesan":"semangat terus kuliahnya bang dan jaya selalu",
                "jabatan": "Staff Divisi Hubungan Luar"# 4
            },
            {
                "nama":"Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":" Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak daplok terkcheee",  
                "pesan":"semangat semester 5 nya kak de, sabar terus dalam membimbing kelompok cosval",
                "jabatan": "Staff Divisi Hubungan Luar"# 5
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "  122450025",
                "umur": "19",
                "asal":" Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": " Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kakak nya asik banget karena ketawa terus",  
                "pesan":"semangat terus kuliahnya kak dan tetap bahagia terus, ajak main golf ya kak kapan-kapan",
                "jabatan": "Staff Divisi Hubungan Luar"# 6
            },
            {
                "nama": " Natasya Ega Lina",
                "nim": " 122450024",
                "umur": "19",
                "asal":" Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": " @nateee__15 ",
                "kesan": "Kakak ini baik",  
                "pesan":"semangat terus kuliahnya kak, doa terbaik untuk kk",
                "jabatan": "Staff Divisi Hubungan Luar"# 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":" Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": " Tidur",
                "sosmed": "@nvliaadinda ",
                "kesan": "Kakak ini cantik dan asik",  
                "pesan":"bahagia terus kak dan hobi kita sama kak",
                "jabatan": "Staff Divisi Hubungan Luar"# 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova ",
                "nim": "122450106",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": " @jasminednva",
                "kesan": "Kakak ini baik dan lembut serta aktif dalam merespon juga cantik",  
                "pesan":"semangat terus kuliahnya kak, terkesan dengan hobinya kak, upgrade terus hobinya kak",
                "jabatan": "Staff Divisi Hubungan Luar"# 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya baik",  
                "pesan":"semangat terus kuliahnya dan sukses ngsaprak ADS bang, semangat jogging bang",
                "jabatan": "Staff Divisi Hubungan Luar"# 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal":"Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakak ini baik dan cantik",  
                "pesan":"semangat terus kuliahnya kak dan sukses untuk semua yang sedang dikerjakan, waw ajarin main bowling donk kak",
                "jabatan": "Staff Divisi Hubungan Luar"# 11
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":" Bekasi",
                "alamat": "TVRI ",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abang ini baik dan lembut",  
                "pesan":"semangat terus kuliahnya bang dan jangan cepat menyerah",
                "jabatan": "Kepala Divisi Pengabdian Masyrakat"# 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",             
                "nim": "122450002",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Way Huwi ",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana ",
                "kesan": "Abang ini baik",  
                "pesan":"semangat dan sukses terus kuliahnya bang, bang suka bertani dimana",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"# 13
            },
            {
                "nama": "Asa Do’a Uyi",
                "nim": " 122450005",
                "umur": "20",
                "asal":" Muara Enim",
                "alamat":  "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini baik",  
                "pesan":"semangat terus kuliahnya bang tetap semangat kak selaras dengan hobinya",
                "jabatan": "Staf Divisi Pengabdian Masyarakat"# 14
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik",  
                "pesan":"semangat terus kuliahnya bang dan sukses untuk semua yang sedang dikerjakan",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"# 15
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":" Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Senang bisa kenal dengan kakak",  
                "pesan":"semangat terus kuliahnya kak, semangat menginspirasi orang banyak dengan keaktifan kakak",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"# 16
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",             
                "nim": " 122450034 ",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": " Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak ini baikb dan",  
                "pesan":"semoga sukses dan jangan lupa berbagi ilmu dengan kami kak",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"# 17
            },
            {
                "nama": "Raid Muhammad Naufal",             
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Abang ini baik dan ramah",  
                "pesan":"semangat dan sukses terus kuliahnya bang, semangat dan jangan lupa berbagi ilmu bang",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"# 18
            },
            {
                "nama": "Tria Yunanni",             
                "nim": "122450062",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat dan sukses terus kuliahnya kak, semoga sukses untuk yangs sedang dikerjakan",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"# 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
    
elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1agOP3gpQqoqwZCBL0BqrSUq9ABodSPnS",#dimas
            "https://drive.google.com/uc?export=view&id=1axRqybH-aZaXfU5Xo2KVXnq2iVu4diM-",#catherine
            "https://drive.google.com/uc?export=view&id=1aqM1TviO4qZf_xQ9r3Npu6PxwMpBIu0_",#akbar
            "https://drive.google.com/uc?export=view&id=1az6MU0wbsdzfB_vP8AzT4A_1zKwU5jx5",#renita
            "https://drive.google.com/uc?export=view&id=1b0etQER_z7XzKpPUggeVU_TCh2znp6OW",#salwa
            "https://drive.google.com/uc?export=view&id=1ad5ib85uV0IsmfT0HnY2HKkAkI37MQYb",#rendra
            "https://drive.google.com/uc?export=view&id=1amX5AWsrblaP5CRmJWDrq5yzUgnKeR5g",#yosia
            "https://drive.google.com/uc?export=view&id=1asTWkM_U4CdehMbK9rRoqiDh0sfmu_aM",#ari
            "https://drive.google.com/uc?export=view&id=1asxKQj_8b1R1B-mkjEC0_Y0w1lmCYAi9",#josua
            "https://drive.google.com/uc?export=view&id=1azLpM9spcdLLxqd1OT8W9qGwnmyphMtF",#azizah
            "https://drive.google.com/uc?export=view&id=1bH4Q3F4MFnlH5woz2xaVHKYck5iU2dUm",#meira
            "https://drive.google.com/uc?export=view&id=1bId9GY1BdQjBha5-gUpzOSDzPOaLsnYH",#rendi done
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":" Tangerang selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "menunggu ayam jantan bertelur ",
                "sosmed": "@dimzrky_ ",
                "kesan": "Abangnya baik, fast respon, suka menyemangati dan inspiratif",  
                "pesan":"semangat terus bg, terima kasih untuk cerita inspirasinya, lancar luncur skripsinya bang",
                "jabatan": "Kepala Departemen Internal"# 1
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakak nya cantik dan anggun",  
                "pesan":"semangat kuliahnya kak semoga skripsinya lancar",
                "jabatan": "Sekretaris Departemen Internal"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Abang ini baik dan asik",  
                "pesan":"semangat dan sukses terus bang",
                "jabatan": "Kepala Divisi Keharmonisasian"# 3
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakaknya baik dan cute",  
                "pesan":"semangat terus kuliahnya kak dan jangan menyerah, semangat memancing kak",
                "jabatan": "Staff Divisi Keharmonisasian"# 4
            },
            {
                "nama":"Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan ",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694 ",
                "kesan": "Kakak ini baik dan lembut",  
                "pesan":"semangat kuliah dan semoga segala impian tercapai, suka nonton apa tu kak",
                "jabatan": "Staff Divisi Keharmonisasian"# 5
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":" Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abangnya nya asik dan hobinya keren",  
                "pesan":"semangat kuliah bang, infokan lagunya bang manatau kita bisa duet",
                "jabatan": "Staff Divisi Keharmonisasian"# 6
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Abangnya baik dan ramah",  
                "pesan":"semangat terus kuliahnya bang sukses selalu, semangat juga nungguin ayam betina berkokok ya bg",
                "jabatan": "Staff Divisi Keharmonisasian"# 7
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":" Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17 ",
                "kesan": "Abang ini baik dan asik",  
                "pesan":"bahagia terus bang, lancar kuliahnya bang keren bg hobinya jago futsal",
                "jabatan": "Kepala Divisi Kerohanian"# 8
            },
            {
                "nama": "Josua Panggabean ",
                "nim": " 122450061",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": " @josuapanggabean_",
                "kesan": "Kakak ini baik dan suka mengajarkan kalau codingan strukdat saya error",  
                "pesan":"semangat terus kuliahnya bang dan terima kasih untuk ilmunya semangat ngasprak strukdat ya bang",
                "jabatan": "Staff Divisi Kerohanian"# 9
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":" Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat terus kuliahnya kak, hati hati bawa kendaraan ya kak",
                "jabatan": "Staff Divisi Kerohanian"# 10
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":" Pesawaran ",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_ ",
                "kesan": "Kakak ini baik dan cantik",  
                "pesan":"semangat terus kuliahnya kak dan sukses untuk semua yang sedang dikerjakan, suka nonton apa tu kak",
                "jabatan": "Staff Divisi Kerohanian"# 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang ",
                "hobbi": "Berenang di Laut",
                "sosmed": " @rexander",
                "kesan": "Abang ini baik setia nungguin kelompok cosval kalau lagi kerja kelompok",  
                "pesan":"semangat semester 5 bg ren, kenapa ga bernang di kolam renang bg",
                "jabatan": "Staff Divisi Divisi Kerohanian"# 12
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
    
elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bLnUzRxt67Q78FR1u3i7O2QGrDwK8FEy",#andrian
            "https://drive.google.com/uc?export=view&id=1bTKepx_Xxw9Qy8TaY9RSfCt-D1ymdfHb",#adisty
            "https://drive.google.com/uc?export=view&id=1bbFMqoTeFNtdK1ZsrgAjhq_bd9qhaeRL",#nabila
            "https://drive.google.com/uc?export=view&id=1bP35JHNBGYEkkc_1DeUIn_rGx0TgojJ2",#danang
            "https://drive.google.com/uc?export=view&id=1bQWq4FWTK9g9_eZ4dj1t96R4n4Qb2Ec6",#farel
            "https://drive.google.com/uc?export=view&id=1bmSiZv1S3u1Z5-S5uDjgoGMrHl4P62Oq",#ahmad
            "https://drive.google.com/uc?export=view&id=1bZavJjxS_W9sAZLk3_rbBd5mvk_cAC5S",#tessa
            "https://drive.google.com/uc?export=view&id=1bOQF0SS03qIEkOJfpOlks0rhFtf963hK",#nabilah
            "https://drive.google.com/uc?export=view&id=1bn76jsgkqxerbn11WPnb_4NDG-puxqpV",#elia
            "https://drive.google.com/uc?export=view&id=1bmwsww7nVHUpROTwL7oPwp0fANq6btC4",#dhafin done
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumbangaol",
                "nim": "121450090",
                "umur": "21",
                "asal":" Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abangnya baik, dan cekatan sepertinya serta keren dalam berbisnis",  
                "pesan":"semangat terus bg, semangat mencari duit, jangan lupa berbagi ilmu ya bang",
                "jabatan": "Kepala Departemen SSD"# 1
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23",
                "asal":"Metro",
                "alamat": "Sukarame ",
                "hobbi": "nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak nya cantik dan baik",  
                "pesan":"semangat kuliahnya kak, rekemondasi film yang bagus kak",
                "jabatan": "Sekretaris Departemen SSD"# 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kakak ini baik dan asik",  
                "pesan":"semangat dan sukses terus kak, pasti suka hitung uang yang merah kan kk",
                "jabatan": "Kepala Divisi KWU"# 3
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": " 122450085",
                "umur": "21",
                "asal":" Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya keren jago promosi",  
                "pesan":"semangat terus kuliahnya bang dan jangan menyerah,ajari ilmu promosi suatu barang bg",
                "jabatan": "Staff Divisi KWU"# 4
            },
            {
                "nama":"Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Abang ini baik",  
                "pesan":"semangat kuliah dan semoga segala impian tercapai, pasti abgnya multitalent",
                "jabatan": "Staff Divisi KWU"# 5
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittingi",
                "alamat": "Airan 1 ",
                "hobbi": "badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abangnya baik dan keren",  
                "pesan":"semangat kuliah bang semangat main badminton bg",
                "jabatan": "Staff Divisi KWU"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": " 122450040",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya baik dan ramah",  
                "pesan":"semangat terus kuliahnya kak sukses selalu,suka nulis jurnal atau cerita kak",
                "jabatan": "Staff Divisi KWU"# 7
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":" Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak ini baik dan keren ",  
                "pesan":"bahagia terus kak, lancar kuliahnya kak, hobi kita sama kak",
                "jabatan": "Kepala Divisi Sponsor"# 8
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": " 122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": " @meylanielia",
                "kesan": "Kakak ini baik juga asik karena suka ketawa terus waktu waktu wawancara",  
                "pesan":"semangat terus kuliahnya kak dan bahagia terus ya kak,ayo main musik bareng kak",
                "jabatan": "Staff Divisi Sponsorship"# 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Nangka",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya baik",  
                "pesan":"semangat terus kuliahnya bang, semangat olahraga bg dhafin",
                "jabatan": "Staff Divisi Sponsorship"# 10
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
    
elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1blOf3tY9iyGXPDca8xW20BDEmjoGDP_A",#wahyu
            "https://drive.google.com/uc?export=view&id=1beDrHdXq-7P4OKQ-MVgTGQ_I6XDUIA9R",#elok
            "https://drive.google.com/uc?export=view&id=1bWPFB9_emzwZDzqGhXYbx82HPy_ft88r",#3
            "https://drive.google.com/uc?export=view&id=1bZbliVI_v6BeTp1gl3jxGCiWttzCl9Eo",#4
            "https://drive.google.com/uc?export=view&id=1bZ690ca3mUqtjexumKPt3Taz_txemLof",#5
            "https://drive.google.com/uc?export=view&id=1bd6R-9fySzykFepSho5ASffZ0OdI4A5e",#6
            "https://drive.google.com/uc?export=view&id=1bQgJWdovgTEGeSqPWoCLu69QD4AR0zCp",#7
            "https://drive.google.com/uc?export=view&id=1bJwsRUEaxerRUoxFxWgy8vUe1P_hSLb7",#8
            "https://drive.google.com/uc?export=view&id=1bW-qI6PeONeeJkJO0hRFAreJ8vwJPMYM",#patricia
            "https://drive.google.com/uc?export=view&id=1bbHzYhQka0mC7dSMqsUkUfs59byXB5ym",#10
            "https://drive.google.com/uc?export=view&id=1biFKje3WWkK8x32VlXfWVPrTz_aGD8i4",#11
            "https://drive.google.com/uc?export=view&id=1b_FeCbO4YqbarmYWvwAmIWoVxTZrrBHr",#12
            "https://drive.google.com/uc?export=view&id=1bK7v8-YmQO4OclnF6X0TqRq97YO78ZUW",#13
            "https://drive.google.com/uc?export=view&id=1bJ1eZVOYP1q58a6ET_4FyRoJbC1J--Xi",#14
            "https://drive.google.com/uc?export=view&id=1bZSzBP5poh0MgXY-a6TFVNXnDVwrIhO4",#15
            "https://drive.google.com/uc?export=view&id=1bLjMw3qxCf9N7lFVbDZ2NU4yhghCYNe2",#16
            "https://drive.google.com/uc?export=view&id=1bPVxXeAcYR66jxThC37-cLmB3AA_CluG",#17
            "https://drive.google.com/uc?export=view&id=1bR5vNp5XoxTKpnAKoyir6OseGL5qu-i3",#18
            "https://drive.google.com/uc?export=view&id=1baDN2eQlJURqnVWY92_qLMaL7vSHmUdx",#19done
        
        ]   
        data_list = [
            {
                "nama": " Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal":" Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "",
                "kesan": "Abangnya baik",  
                "pesan":"semangat terus bg jaya selalu bang lancar skripsi ya bg",
                "jabatan": "Kepala Departemen Medkraf"# 1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakak nya cantik dan baik",  
                "pesan":"semangat kuliahnya kak semangat juga ngasprak ADS kak",
                "jabatan": "Sekretaris Departemen Medkraf"# 2
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakak ini baik dan asik",  
                "pesan":"semangat dan sukses terus kak dan semangat nugas nya kak",
                "jabatan": "Kepala Divisi Media dan Konten"# 3
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":" Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abangnya keren",  
                "pesan":"semangat terus kuliahnya bang dan jangan menyerah semoga cepat dapat hobinya bg",
                "jabatan": "Kepala Divisi PDD "# 4
            },
            {
                "nama":"Muhammad Arsal Ranjana Putra ",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Abang ini baik",  
                "pesan":"semangat kuliah dan semoga segala impian tercapai ajarin ngoding bg",
                "jabatan": "Kepala Divisi Visual Desain"# 5
            },
            {
                "nama": "Cintya  Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakaknya nya baik dan cantik",  
                "pesan":"semangat kuliah kak dan sukses selalu ya, semangat ngegym juga kak",
                "jabatan": "Staff Divisi Media dan Kreatif"# 6
            },
            {
                "nama": "Eka Fidiya Putri ",
                "nim": " 122450045",
                "umur": "20",
                "asal":"Natar, lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakaknya baik dan ramah, public speakingnya juga bagus",  
                "pesan":"semangat terus kuliahnya kak sukses selalu, keren kk waktu jadi MC pplk 2023 kemarin kak",
                "jabatan": "Staff Divisi Media dan Kreatif"# 7
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":" Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakak ini baik dan cantik",  
                "pesan":"bahagia terus kak, lancar kuliahnya kak, suka baca apa tu kak",
                "jabatan": "Staff Divisi Media dan Kreatif"# 8
            },
            {
                "nama": "Patricia Leondra Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":" Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak ini baik juga cantik dan lembut",  
                "pesan":"semangat terus kuliahnya kak dan bahagia terus ya kak, rekomendasi film yang bagus kak",
                "jabatan": "Staff Divisi Media dan Kreatif"# 9
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame ",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakaknya baik dan asik banget",  
                "pesan":"semangat terus kuliahnya kak dan semangat baca ngoding kak",
                "jabatan": "Staff Divisi Media dan Konten"# 10
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah  ",
                "nim": "122450020",
                "umur": "20",
                "asal":" Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya baik juga cepat respon",  
                "pesan":"semangat terus bg jaya selalu kak,ayo duet bareng kak",
                "jabatan": "Staff Divisi Media dan Konten"# 11
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak nya cantik dan baik",  
                "pesan":"semangat kuliahnya kak keren banget hobinya kak",
                "jabatan": "Staff Divisi PDD"# 12
            },
            {
                "nama": "Gymnastiar Al Khoarizmy ",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": " Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Abang nya baik dan asik",  
                "pesan":"semangat dan sukses terus bang, jaga kesehatan ya bg",
                "jabatan": "Staff Divisi PDD"# 13
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kakaknya baik dan lembut",  
                "pesan":"semangat terus kuliahnya kak dan jangan menyerah terus bahagia kak",
                "jabatan": "Staff Divisi PDD "# 14
            },
            { 
                "nama":"Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": " ",
                "asal":"Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakak ini baik",  
                "pesan":"semangat kuliah dan semoga segala impian tercapai, sekali-kali baca yg happy ending kak",
                "jabatan": "Staff Divisi PDD"#15
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Kakaknya nya baik dan cantik",  
                "pesan":"semangat kuliah kak dan sukses selalu ya, semangat upgrade skill nya ya bg",
                "jabatan": "Staff Divisi Visual dan Desain"#16
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangnya baik dan ramah",  
                "pesan":"semangat terus kuliahnya bang sukses selalu jangan lupa belajar bg",
                "jabatan": "Staff Divisi Visual Desain"# 17
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "LinkedIn nya bagus banget bang, abangnya juga lucu dan asik ",  
                "pesan":"bahagia terus bang, lancar kuliahnya bang, jangan lupa berbagi ilmu ya bang",
                "jabatan": "Staff Divisi Visual Desain"# 18
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakak ini baik juga cantik dan lembut",  
                "pesan":"semangat terus kuliahnya kak dan bahagia terus ya kak semangat ngerjain tugas kak",
                "jabatan": "Staff Divisi Visual Desain"# 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan
