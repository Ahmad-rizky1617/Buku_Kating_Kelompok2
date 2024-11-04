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
            "https://drive.google.com/uc?export=view&id=1imW9VTZUMTCBBaEBm5XpTrhy2JeYRAJ6",
            "https://drive.google.com/uc?export=view&id=1iWPa8i2ngta1L4csT1nMCdtY7A2ohRiH",
            "https://drive.google.com/uc?export=view&id=1iYibd6MP-1vvGhSujlvjq9rdu-gM29_j",
            "https://drive.google.com/uc?export=view&id=1ihFkUXB_yvYXxoYL9X4zULdvEv2KuHqF",
            "https://drive.google.com/uc?export=view&id=1DuA73z2x9-AlvvC-l4XTGT8jlPHEUtWX",
            "https://drive.google.com/uc?export=view&id=1DyFiaISLItqLSMlD41jkr1rD3bQInX4y",
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
                "kesan": "abangnya keren banget",
                "pesan": "Semoga abang sehat selalu",
                "jabatan" : "Ketua himpunan",  
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya baik",
                "pesan": "semangat kuliahnya kak",  
                "jabatan" : " Sekretaris Umum" 
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Denger Musik",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya baik juga",
                "pesan": "tetap semangat kakak",
                "jabatan" : "Bendahara umum",  
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": " 121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@nadillaandr26",
                "kesan": "public speakingnya keren banget",
                "pesan": "tetap semangat kuliah bang", 
                "jabatan" : "Sekretaris Jendral", 
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh, Sumatra Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "bagus banget kah kak suara gitar bang pandra?",
                "pesan": "semangat kak kuliahnya", 
                "jabatan" : "Sekretaris 1", 
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "1214500030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Baca",
                "sosmed": "@nadillaandr26",
                "kesan": "bagus banget hobinya membaca kakak",
                "pesan": "semangat kak kuliahnya",  
                "jabatan" : "Bendahara 1", 
            },




        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ediVt-Hn_kdYLjX4SnVOLXfRH_V4N9-V",
            "https://drive.google.com/uc?export=view&id=1eHGPVl9H-QHcKKyQARsIY05jOwzKug1U",
            "https://drive.google.com/uc?export=view&id=1eNk9_ERN0agqDkL5EWjM2xKJx81spTTc",
            "https://drive.google.com/uc?export=view&id=1e6l5ec8k_P7zP4YoF-ixxjhWX9ToVDds",
            "https://drive.google.com/uc?export=view&id=1eMbc_kc1gAtMs3XnekNsDRPPgyCtBE_z",
            "https://drive.google.com/uc?export=view&id=1ehnEq3ti_RQPYNLCmKSouihyj_AymFL-",
            "https://drive.google.com/uc?export=view&id=1eM1keroHdMdID6cK4CFO5x_WPqHWqrMi",
            "https://drive.google.com/uc?export=view&id=1efq-Q-U5JRcO6d68KCwblNVLzm9LEBkv",
            "https://drive.google.com/uc?export=view&id=1eDpYixIH6vGgHZud-seCZmZQpfIh9dFb",
            "https://drive.google.com/uc?export=view&id=1eTnZ0OcSWZjR-Jy1hdFC5HXDqjZHATgO",
            "https://drive.google.com/uc?export=view&id=1ehbry5J9A6zD_CziD20s2PjyBSlxTQGy",
            "https://drive.google.com/uc?export=view&id=1e9TDKvPS9gFebpaQt14e0_WH7nf23H3j",
            "https://drive.google.com/uc?export=view&id=1eNk9_ERN0agqDkL5EWjM2xKJx81spTTc",
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
                "kesan": "Kakaknya ramah,dan baik",
                "pesan": "semangat kuliahnya kakak",
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
                "kesan": "masyaallah hobinya positif banget",
                "pesan": "Semangat kuliahnya kak", 
                "jabatan" : "Sekretaris", 
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "wlsbn0",
                "kesan": "suka filem apa tuh kak",
                "pesan": "semangat ya kak", 
                "jabatan" : "Bendahara", 
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450021",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": " @anisadini10",
                "kesan": "berarti kakaknya seneng baca ya",
                "pesan": "semangat kuliahnya kakak", 
                "jabatan" : "Kepala Komisi 1 Legislatif", 
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": " @dylebee",
                "kesan": "kak hobinya baca jurnal, waw aku sih udah ngantuk duluan kalo liat jurnal",
                "pesan": "semangat kuliahnya kak", 
                "jabatan" : "Kepala Komisi 2 Aspirasi dan Pengawasan", 
            },
            {
                "nama": "Muhammad Fachrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Sholat Malam",
                "sosmed": "@fhrul.pdf",
                "kesan": "masyaallah abangnya rajin sholat malam",
                "pesan": "semangat kuliahnya kak", 
                "jabatan" : "Kepala Komisi 3 Media Legislatif", 
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kalianda",
                "hobbi": "Membaca Al waqiah setiap magrib",
                "sosmed": " @ansftynn_",
                "kesan": "masyaallah kakaknya suka membaca al-qur'an",
                "pesan": "semangat kuliahnya kak, tetap baik hati kak", 
                "jabatan" : "Anggota Komisi 1 Legislatif", 
            },
            {
                "nama": "Feryadi Yulius ",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya hebat banget masih bisa sholat dhuha walaupun sitengah sibuknya kuliah",
                "pesan": "semangat kuliahnya kak", 
                "jabatan" : "Anggota Komisi 1 Legislatif", 
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-Qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "MasyaAllah hobbi kaknya positif banget",
                "pesan": "Semangat kuliahnya", 
                "jabatan" : "Anggota Komisi 1 Legislatif", 
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya seru karena memiliki hobbi yang sama dengan saya",
                "pesan": "Info manhua dan manwa yang bagus bang", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", 
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20 tahun",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": " @_.dheamelia",
                "kesan": "sepemikiran saya kak kenapa di gedung f nggak ada sinyal ya",
                "pesan": "semangat kuliahnya kak", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", 
            },
            {
                "nama": " Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "hobinya banyak dan sangat positif sekali abangnya",
                "pesan": "semangat kuliahnya kak", 
                "jabatan" : " Anggota Komisi 3 Legislatif", 
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Bilabong",
                "hobbi": "Cerita",
                "sosmed": "@jeremia_s_",
                "kesan": "aku pengen denger cerita dari kakak",
                "pesan": "semangat kuliahnya kak", 
                "jabatan" : " Anggota Komisi 3 Legislatif", 
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()
elif menu == "Senator":

    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WIu5lRkqMv-Ri5eFVuxJAjrWGBJuf0f4",
            "https://drive.google.com/uc?export=view&id=1uSR7WwjkEgw9hYfRtucWEyBXFhwyKIfs",
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "kakak keren banget bisa bisa kuliah sambil menjalankan kewajiban sebagai senator",
                "pesan": "semangat kuliahnya kak",
                "jabatan": "Senator"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20 tahun",
                "asal": "Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "abang hebat banget bisa naik ipknya walaupun sibuk",
                "pesan": "semangat kuliahnya bang",
                "jabatan": "Tim Senator"
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    senator()
    
elif menu == "Departemen PSDA":

    def departemen_psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14F0jkWpqwDhUpVAVvCrt2jBvPDUukg0U",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Axyxegto5FtFRGwNOMKKnfp76YKWVGU6",
            "https://drive.google.com/uc?export=view&id=1BUL10wbAHzo08mabLyl0cAofSNFVEq60",
            "https://drive.google.com/uc?export=view&id=1BJ9oPW8_WOQlyUPh0nVxw2Xnz_ZVWSKr",
            "https://drive.google.com/uc?export=view&id=1Az61SSfXhjVN-dMR1IfrrIAFY-84Lpzz",
            "https://drive.google.com/uc?export=view&id=1B4oR7QoBGGxiXFW6R9zjDn25Gz3zsIM-",
            "https://drive.google.com/uc?export=view&id=1B0hn31IfUxI246swWxEoU5u67yWJUdHI",
            "https://drive.google.com/uc?export=view&id=1B95mibc-Cf9DKM0NCgpQQzo9di37H8ih",
            "https://drive.google.com/uc?export=view&id=1B9vTWnV5j8Vw1-o51dRr9TbZKGg6V-PH",
            "https://drive.google.com/uc?export=view&id=1HbgqHBD6MulxFwghvNXn6cuc3BeJwk31",
            "https://drive.google.com/uc?export=view&id=1BOe1jIWtVYcDkQfzCq1A2nIMfTIsYC_L",
            "https://drive.google.com/uc?export=view&id=1BSzG-6-WAxIBKcOir3gm2LFWeVMuJaqE",
            "https://drive.google.com/uc?export=view&id=1B_H68_jNc0D0rR2gxYgXToxqFobMEfW_",
            "https://drive.google.com/uc?export=view&id=1BS86fgYOgexZLNtE1kl1ChLR0B_aaTQ6",
            "https://drive.google.com/uc?export=view&id=1BDTZLJGpCpS-pohM9T2NsVMfbD73zqjc",
            "https://drive.google.com/uc?export=view&id=1HeqjAdC1kKwQHaIWtfO5He2fgkFViAlz",
            "https://drive.google.com/uc?export=view&id=1BJ6IfopP5H0cx1nbHsJv68M7fv2qDPi-",
            "https://drive.google.com/uc?export=view&id=1BCjDCh6MxU0phW35Tz0SXEtvtYVoaYST",
            
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21 tahun",
                "asal": "Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "public speaking bang erikson keren banget",
                "pesan": "tetep semangat bang kuliahnya",
                "jabatan": "Kepala Departemen PSDA"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18 tahun",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "hobi kakanya bernafas?? sedikit membuat bingung",
                "pesan": "semangat kuliahnya kak",
                "jabatan": "Sekretaris Departemen PSDA"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21 Tahun",
                "asal": "Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "bagus sekali hobi adalah belajar",
                "pesan": "tetap semangat kuliah dan belajarnya",
                "jabatan": "Kepala Divisi Manajemen Minat dan Bakat"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19 Tahun",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "hobbi muter-muter dimana kak",
                "pesan": "semangat kulianya kak",
                "jabatan": "Kepala Divisi Kaderisasi"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21 Tahun",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya baikbanget suka menolong",
                "pesan": "semangat kuliahnya bang",
                "jabatan": "Kepala Divisi Olahraga dan Perlombaan"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19 Tahun",
                "asal": "Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abangnya asik banget siapa sangka tanggal lahirnya sama",
                "pesan": "tetap semangat bang ngaspraknya",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19 Tahun",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main Game",
                "sosmed": "@kemasverii",
                "kesan": "padahal kelihatan pintar tapi ternyata abangnya suka main game",
                "pesan": "semangat kuliahnya bang",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20 Tahun",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "kakaknya baik",
                "pesan": "semangat kuliahnya kakak",
                "jabatan": "Bendahara Divisi Manajemen Minat dan Bakat"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20 Tahun",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "waw nggak espec kakaknya suka baca webtoon",
                "pesan": "semangat kuliahnya kak",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21 Tahun",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "abangnya unik",
                "pesan": "semangat kuliahnya bang",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20 Tahun",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "waw kakaknya ternyata suka belajar",
                "pesan": "semangat kadernya kak",
                "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "kakaknya sangat prfesional bisa menyesuaikan tempat tergantung tempat",
                "pesan": "semangat kuliahnya kak",
                "jabatan": "Staff Divisi Kaderisasi"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20 Tahun",
                "asal": "Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "emang ternyata bukan saya doang yang nyari sinyal di gedung f",
                "pesan": "semangat kuliahnya kak",
                "jabatan": "Staff Divisi Kaderisasi"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19 Tahun",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "masih bingung kenapa ditanya minuman yang nggak di suka",
                "pesan": "semangat kuliahnya bang",
                "jabatan": "Staff Divisi Kaderisasi"
            },
            {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "122450041",
                "umur": "20 Tahun",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "kakaknya suka scroll tiktok nggak espek",
                "pesan": "semangat kuliahnya kak",
                "jabatan": "Staff Divisi Kaderisasi"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "hem abangnya belens banget hobbinya",
                "pesan": "semangat kuliahnya bang",
                "jabatan": "Staff Olahraga dan Perlombaan"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19 Tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "tidak terlihat seperti orang yang suka berenang kakaknya",
                "pesan": "semangat kuliahnya bang",
                "jabatan": "Staff Olahraga dan Perlombaan"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20 Tahun",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "abangnya emang terlihat seperti orang yang suka main game",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Olahraga dan Perlombaan"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21 Tahun",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "kakaknya suka memang terlihat suka membaca",
                "pesan": "semangat kuliahnya kak",
                "jabatan": "Staff Olahraga dan Perlombaan"
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    departemen_psda()
    
elif menu == "Departemen MIKFES":

    def departemen_mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f2vioqGzMV2eELraVYRG4WDa8u8oLPUN",
            "https://drive.google.com/uc?export=view&id=1e3CYzjKR-Rp0rg6Rkp_9Fn1EdEHq1_1h",
            "https://drive.google.com/uc?export=view&id=1eSv4965KK4shx4jCz00mGDFSEqhPhlWU",
            "https://drive.google.com/uc?export=view&id=1f-IMLxfbfr6A6cR_eQ7YH0EmsnT-oXWj",
            "https://drive.google.com/uc?export=view&id=1eWyxDNPGf-m5KmPqjhBkuhz-zRHtR1VA",
            "https://drive.google.com/uc?export=view&id=1e4EumDPOG49GAcDpQkqRshPGD6V6JhiQ",
            "https://drive.google.com/uc?export=view&id=1eoetaiLmlKVbdzhX2WnrOoIha3JO6mYg",
            "https://drive.google.com/uc?export=view&id=1e_-t93gbBAG_9Kv4LK-FFKWpujg0oOJw",
            "https://drive.google.com/uc?export=view&id=1ePm3jsggaIKZ4Ajb3l1bOxM6835z-EoI",
            "https://drive.google.com/uc?export=view&id=1eI_KzLxsbaFZaCP0sLYZnsiTjrpdxOGF",
            "https://drive.google.com/uc?export=view&id=1eHaOG0K72KoNkSKVTBd_c047eZR9_iYE",
            "https://drive.google.com/uc?export=view&id=1eAuSh096OSiRJxr_iDzM7zUxgD7-oglp",
            "https://drive.google.com/uc?export=view&id=1f4lNekAKjqsBlDBZFy-u0tk0YkZM4-Oi",
            "https://drive.google.com/uc?export=view&id=1eLJX09sfWQCE19nqR6ZOeVSdmRjS-xug",
            "https://drive.google.com/uc?export=view&id=1fALyDNM1_3-n2lRLG0CZlIxCl4SEaIUU",
            "https://drive.google.com/uc?export=view&id=1esAq7Gy-T7THtvjhAiaXrJPibayfMska",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21 Tahun",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "abangnya emang terlihat seperti suka olahraga",
                "pesan": "semangat olahraga dan kuliahnya",
                "jabatan": "Kepala Departement"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21 Tahun",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "siapa sangka kaknya suka memasak",
                "pesan": "semangat kuliahnya, semoga bisa menciptakan resep baru kak",
                "jabatan": "Sekretaris Departement"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "memang keren hobbinya olahraga",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Club dan Komunitas"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20 Tahun",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abangnya suka main game ternata",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Club dan Komunitas"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19 Tahun",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "hobbi kakaknya unik juga",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Club dan Komunitas"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "kakanya suka baca novel tentang apa?",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Club dan Komunitas"
            },      
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "hobi kakaknya agak membingungkan",
                "pesan": "semangat kuliahnya",
                "jabatan": "Kepala Divisi Pusat Inovasi dan Kajian Akademik"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "hobinya keren amat",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "film apa yang bisa di  tonton kak?",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "-",
                "sosmed": "@dindanababan_",
                "kesan": "kaknya baik",
                "pesan": "semangat kuliahnya kak",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20 Tahun",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "hobinya keren amat kak",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
            },      
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20 Tahun",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "waduh hebat sekali kakaknya suka meresume jurnal",
                "pesan": "semangat kuliahnya,dan kalo bisa ajari resume jurnal ya kak",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20 Tahun",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "hobi kakaknya sangat positif sekali",
                "pesan": "semangat kuliah,dan membaca kak",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "hobi kakaknya sangat positif sekali",
                "pesan": "semangat kuliah,dan membaca kak",
                "jabatan": "Kepala Divisi Survei dan Riset"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20 Tahun",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "kakaknya baik dan ramah",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Survei dan Riset"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20 Tahun",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "kereatif sekali kakaknya membuat konten",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Survei dan Riset"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20 Tahun",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "kaknya baik",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Survei dan Riset"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20 Tahun",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "kakanya ternyata suka main game",
                "pesan": "semangat kuliahnya",
                "jabatan": "Staff Divisi Survei dan Riset"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "hobinya agak unik",
                "pesan": "semangat kuliahnya, dan tepap berkembang kak",
                "jabatan": "Staff Divisi Survei dan Riset"
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    departemen_mikfes()
elif menu == "Departemen_Eksternal":

    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_yYTxhMlirQOV4XBFYJeKuLilwpAnC0i",
            "https://drive.google.com/uc?export=view&id=1_oNvNpQMzFIsvX1ul8UIeEjse_CiUmVp",
            "https://drive.google.com/uc?export=view&id=1m9akSWjlfAVov4Dva838nA6D7NRDmoRX",
            "https://drive.google.com/uc?export=view&id=1aE2NwsqvokVapwhE6qeDHWeUCShuCxgS",
            "https://drive.google.com/uc?export=view&id=1_sBLb6W-ZduOFXLm_YKafw-HYWSnXVjR",
            "https://drive.google.com/uc?export=view&id=1a6-IRDmSuvrF4rVeW2T-5cr1maEviR27",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1a0cZ_QsD4wrK1KtbeH_trSkJ8WbyvDZz",
            "https://drive.google.com/uc?export=view&id=1a3c_xHJed0uVIF2HDI3Dos_vsJ-1Tt8T",
            "https://drive.google.com/uc?export=view&id=1agumQWeTca-K--mSL7sI-DoN5DdbsDXV",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1__o6SLM68l4GYGHTPZ_ys-9CpX9cUgnD",
            "https://drive.google.com/uc?export=view&id=1_NwqBSi0sQjwkZJ_H0BWOaK0M1qPOnUS",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1_lYOgo-hJL5bmHE9BSrjrfgvTPjofbih",
            "https://drive.google.com/uc?export=view&id=1aPGJnbzbEF0uky3OApbPhk-v9McZirie",
            "https://drive.google.com/uc?export=view&id=1aHDk2vtm3RuKGaMlYjsL6aeJbPVahwF-",
            "https://drive.google.com/uc?export=view&id=1_lzcoDgZYjBRymwkC2nUhrcHus01zeT5",
            "https://drive.google.com/uc?export=view&id=1_mVt-S5kM06R1E5GwaEalc8tuTfIcVIc",
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
                "kesan": "Abangnya kocag, seru, baik",
                "pesan": "semangat kuliahnya bang, tetap jadi orang baik",
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
                "kesan": "Kakaknya humble",
                "pesan": "Semangat kuliahnya kak", 
                "jabatan" : "Sekretaris Departemen", 
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
                "pesan": "semangat ya kak, tetaplah tertawa sebelum tertawa itu dilarang", 
                "jabatan" : "Kepala Divisi Hubungan Luar", 
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
                "asal": "Sumatra Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": " @deaa.rsn",
                "kesan": "Kakaknya ramah, orangnya juga ",
                "pesan": "semangat ya kuliahnya jangan putus asa orang sibuk", 
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
                "kesan": "kakaknya pasti jago main golf",
                "pesan": "semangat kuliahnya kak, tetap pertahankan main golfnya", 
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
                "kesan": "Manis banget kakaknya, ramah juga",
                "pesan": "semangat kuliahnya kak, tetap baik hati kak", 
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
                "kesan": "Kakaknya bener-bener  banget!",
                "pesan": "semangat kuliahnya kak, semoga makin ", 
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
                "kesan": "MasyaAllah kak pertahankan hobbinya",
                "pesan": "Semangat kuliahnya, semoga semakin rajin mengerjakan tugas", 
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
                "kesan": "Abangnya baik, kalem, dan ramah",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari", 
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
                "kesan": "Kakaknya kelihatan aktif organisasi bangettt",
                "pesan": "semangat kak", 
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
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
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
                "pesan": "semangat kuliahnya bang, tetap pertahankan rajin sholat malamnya", 
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
                "kesan": "Kakaknya baik",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
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
                "kesan": "Kakaknya baik, dulu kakak asprak fisdas 1 aku juga",
                "pesan": "semangat kuliahnya kak ochaa", 
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
                "kesan": "Abangnya baik",
                "pesan": "semangat kuliahnya bang, tetap pertahankan rajin sholat malamnya", 
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
                "kesan": "kakaknya baik, aktif berorganisasi sekalii",
                "pesan": "semangat kuliahnya kak, tetap pertahankan aktifnya",
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
                "kesan": "kakaknya baik",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin mengajinya", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", 
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayth_",
                "kesan": "Abangnya baik",
                "pesan": "semangat kuliahnya bang", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", 
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": "kakaknya baik",
                "pesan": "semangat kuliahnya kak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", 
            },
      ]
        display_images_with_data(gambar_urls, data_list)

    Departemen_Eksternal()         

elif menu == "Departemen Internal":

    def departemen_internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UP90HFNN8_PISWGS1ThKBehfrgy4nAQE",
            "https://drive.google.com/uc?export=view&id=1U2Lw1_Zaq97ZlrJaI7e_Rf2t3EcVkpMt",
            "https://drive.google.com/uc?export=view&id=1TzLIvdQwDUcHGaSDm_x_PX9yuK5wvTsN",
            "https://drive.google.com/uc?export=view&id=1UU5y4_wd4E_E_Ii2kmDXJbOF12I4ohY-",
            "https://drive.google.com/uc?export=view&id=1U6Rx9f_w2qLhOby6PYU42hhcnffXCcsj",
            "https://drive.google.com/uc?export=view&id=1U-D8ETOA5uVbgS9mRQmDohZUlBrS7P06",
            "https://drive.google.com/uc?export=view&id=1UTm6LOhLtjWQ7coEE3c5L8clBT3XGamS",
            "https://drive.google.com/uc?export=view&id=1U-rja2EKdVIL3QkY1Xt6z5oRnWvH2-ku",
            "https://drive.google.com/uc?export=view&id=1Tq3yxqWRhNzgsPUiO2oqe18S9B3tH-6I",
            "https://drive.google.com/uc?export=view&id=1U4kzxZI4G5g4hCqPqTrTUobjsJgu581O",
            "https://drive.google.com/uc?export=view&id=1U8ROXCdm0ECN6AqS-OpUldO7Ys4qVswM",
            "https://drive.google.com/uc?export=view&id=1UCZizJesIcnxBkbHtz9ccA9xc_yrq0oq",
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
                "kesan": "sosok yang humoris dan menyenangkan.",
                "pesan": "Semoga terus semangat dan sukses dalam kuliah!",
                "jabatan": "Kepala Departemen Internal"
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "kakak yang sangat perhatian dan penyayang.",
                "pesan": "Teruslah berkarya dan jangan lupa istirahat!",
                "jabatan": "Sekretaris Departemen Internal"
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "orang yang sangat kreatif dan menyenangkan.",
                "pesan": "Semoga selalu menemukan dino-dino yang langka!",
                "jabatan": "Kadiv Keharmonisasian"
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Renita adalah teman yang sabar dan penuh inspirasi.",
                "pesan": "Semoga mendapatkan ikan besar di setiap memancing!",
                "jabatan": "Staff Keharmonisasian"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Salwa adalah teman yang selalu ceria dan menyenangkan.",
                "pesan": "Nonton film seru yuk di akhir pekan!",
                "jabatan": "Staff Keharmonisasian"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Rendra adalah sosok yang berbakat dan peka terhadap seni.",
                "pesan": "Terus berkarya dan semoga lagunya terkenal!",
                "jabatan": "Staff Keharmonisasian"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Kesan Yosia",
                "pesan": "Pesan Yosia",
                "jabatan": "Staff Keharmonisasian"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23 Tahun",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Kesan Ari",
                "pesan": "Pesan Ari",
                "jabatan": "Kepala Divisi Kerohanian"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Kesan Josua",
                "pesan": "Pesan Josua",
                "jabatan": "Staff Kerohanian"
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21 Tahun",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kesan Azizah",
                "pesan": "Pesan Azizah",
                "jabatan": "Staff Kerohanian"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20 Tahun",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kesan Meira",
                "pesan": "Pesan Meira",
                "jabatan": "Staff Kerohanian"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20 tahun",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Teman yang menyenangkan dan selalu bisa diandalkan.",
                "pesan": "Tetap semangat dalam berkuliah dan berkarya!",
                "jabatan": "Staff Kerohanian"
            },
             
        ]
        display_images_with_data(gambar_urls, data_list)

    departemen_internal()
elif menu == "Departemen SSD":

    def departemen_ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c7eNUlfXtEao8O3ZH9ze35OeTROJthjt",
            "https://drive.google.com/uc?export=view&id=1coEEYwMqtDNY8fNBAWsvs4HUfyNx-tTq",
            "https://drive.google.com/uc?export=view&id=1ciZgOReys8jzYwqyWeGGejFkcFviAenf",
            "https://drive.google.com/uc?export=view&id=1c9F6dTAyDeagxBNGXXp9vkvBFhNdHajj",
            "https://drive.google.com/uc?export=view&id=1bpno9NUtS9FD3Q35b2uoEqt248yv6rH9",
            "https://drive.google.com/uc?export=view&id=1cEy37tk7YQH1FfjKpxeqSj2Kohk7DXD3",
            "https://drive.google.com/uc?export=view&id=1cazkML-yJhkqs3ifXa173Oj6eCpV9K4Y",
            "https://drive.google.com/uc?export=view&id=1bqkLNVmEJOwaITmtC3LuBnJgArpRENtM",
            "https://drive.google.com/uc?export=view&id=1bqt07Rw1hRnchFqo0k-7gr5MKMcti7kM",
            "https://drive.google.com/uc?export=view&id=1c6Aq8N-wxW10_1THqGM00vAjydxU3tNx",
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumbangaol",
                "nim": "121450090",
                "umur": "21 Tahun",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Kesan Andrian di sini",
                "pesan": "Pesan Andrian di sini",
                "jabatan": "Kepala Departemen SSD"
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23 Tahun",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Kesan Adisty di sini",
                "pesan": "Pesan Adisty di sini",
                "jabatan": "Sekretaris Departemen SSD"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21 Tahun",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kesan Nabila di sini",
                "pesan": "Pesan Nabila di sini",
                "jabatan": "Kepala Divisi KWU"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Kesan Danang di sini",
                "pesan": "Pesan Danang di sini",
                "jabatan": "Staff KWU"
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20 Tahun",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Kesan Farel di sini.",
                "pesan": "Pesan untuk Farel.",
                "jabatan": "staff KWU"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20 Tahun",
                "asal": "Bukittingi",
                "alamat": "Airan 1",
                "hobbi": "badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Kesan Ahmad di sini.",
                "pesan": "Pesan untuk Ahmad.",
                "jabatan": "staff KWU"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20 Tahun",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kesan Tessa di sini.",
                "pesan": "Pesan untuk Tessa.",
                "jabatan": "staff KWU"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20 Tahun",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kesan Nabilah di sini.",
                "pesan": "Pesan untuk Nabilah.",
                "jabatan": "Kepala Divisi Sponsor"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20 Tahun",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kesan Elia di sini.",
                "pesan": "Pesan untuk Elia.",
                "jabatan": "staff sponsor"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kesan Dhafin di sini.",
                "pesan": "Pesan untuk Dhafin.",
                "jabatan": "staff sponsor"
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    departemen_ssd()
    
elif menu == "MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HHnAwI-Oym0WK5cF5mn7qWGh01rtecq-",
            "https://drive.google.com/uc?export=view&id=1M6qqCq_dSKUgqfUldD-TjHe3YSJ5y1ZP",
            "https://drive.google.com/uc?export=view&id=18-IVJxUTRlPfoIs0FyNJSBMjhBDWwc2O",
            "https://drive.google.com/uc?export=view&id=1BI0hACtGIDQ6-iquGUxINQSGMzchr1l4",
            "https://drive.google.com/uc?export=view&id=1ZoBGxeIjiamgfVAuMA9WEJzcUNp3a66I",
            "https://drive.google.com/uc?export=view&id=1bj_iEJn9y3UOn2luMF0kBO98n6WgMmek",
            "https://drive.google.com/uc?export=view&id=1WLQXDQAEzmiz2eOsr1f7hrNMOk1pabOM",
            "https://drive.google.com/uc?export=view&id=1oeNykB_dvw8XSp6ipWWfRR5QfQfxObKL",
            "https://drive.google.com/uc?export=view&id=1X7S2jxY170QqMW-TBPacAuZHJGns2yJp",
            "https://drive.google.com/uc?export=view&id=1PP-L9tYGpF3RrbRmxTRelxVR82aT-xjN",
            "https://drive.google.com/uc?export=view&id=13j5yjEna2IjP51NImm0i0iccql8rfpkT",
            "https://drive.google.com/uc?export=view&id=1yIRiDvvNrI7SFua5TQf6XQIqP9ZP996D",
            "https://drive.google.com/uc?export=view&id=1AvFTVf4KdzLSOtrD6ycHawydzh76eNMA",
            "https://drive.google.com/uc?export=view&id=14JewrP8NmURihe-_i5IfsMgTr53V2-v3",
            "https://drive.google.com/uc?export=view&id=1J7BLMT0vl1dE0wieHD399Co1BLDAxjo9",
            "https://drive.google.com/uc?export=view&id=1LX4NkKNCLMf4Zh-KLyBC0TPaji8PYUQA",
            "https://drive.google.com/uc?export=view&id=1wkMcj8038z1xhx63QvhH73buJhHDLNLv",
            "https://drive.google.com/uc?export=view&id=1T4cO-DVNf1sHJiKmUBUZzHsAMm7sTz8Y",
            "https://drive.google.com/uc?export=view&id=1zq18qVQJ6hEAw9eez3z-PDS1QhduCJTD",
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
                "kesan": "",
                "pesan": "",
                "jabatan" : "Kepala Departemen MedKraf", #1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Sekretaris", 
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Kepala Divisi Media & Konten", 
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": " 121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": " @dino_kiper",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Kepala Divisi PDD", 
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Kepala Divisi Visual Desain", 
            },
            {
                "nama": "Cintya  Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Suka banget sama outfit kakak, cocok banget di divisi media & konten",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Media & Konten", 
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " 122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Media & Konten", 
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Media & Konten", 
            },
            {
                "nama": "Patricia Leondra Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Media & Konten", 
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Media & Konten", 
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Media & Konten", 
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "",
                "sosmed": "@dwiratnn_",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi PDD", 
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "",
                "pesan": "Ramahh banget kak Dheaa", 
                "jabatan" : "Anggota Divisi PDD", 
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
                "jabatan" : "Anggota Divisi PDD", 
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Visual Desain", 
            },
             {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Visual Desain", 
            },
             {
                "nama": "Hermawan Manurung ",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani) ",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Visual Desain", 
            },
             {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi Visual Desain", 
            },
             {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Anggota Divisi PDD", 
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
